from code_line import CodeLine
from find_links import FindLinks

# CODE_SPACE = (0x0000, 0x17FF)
# RAM_SPACE = (0x4000, 0x43FF)

# Z80 specifics
CODE_OPS = ["JP", "JR", "CALL", "DJNZ", "DJZ"]

# All memory fetches are ($....)
# Things like "LD  HL,$4040" where $4040 is the address of a known memory location


class FindLinksZ80(FindLinks):

    def process(self, raw, do_ram):
        # Process the file line by line
        last_comment_pos = 0
        newLines = []
        candidates = []
        self.ram_hits = []
        for r in raw:

            t = r.strip()

            # Keep comment lines as-is
            if t.startswith(";"):
                newLines.append(r)
                continue

            # Keep blank lines as-is
            if t == "":
                newLines.append(r)
                continue

            # Must be code. Parse that.
            c = CodeLine()
            c.parse(r)

            # Keep up with the comment spacing from line to line in case we
            # need to add a blank comment
            if c.comment:
                last_comment_pos = c.originalCommentPos

            # Ignore any existing specs (comment this out if you want to overwrite)
            if c.comment and c.comment[1:].strip().startswith("{"):
                newLines.append(r)
                continue

            # Only process lines that are opcodes
            if not c.opcode:
                newLines.append(r)
                continue

            #
            # CPU specifics here
            #

            # Good old Z80 -- memory references are in parens
            if "($" in c.opcode:

                # INs and OUTs come from port space
                if c.opcode.startswith("OUT ") or c.opcode.startswith("IN "):
                    newLines.append(r)
                    continue

                i = c.opcode.index("($") + 2
                j = c.opcode.index(")", i)
                v = c.opcode[i:j]
                if v not in self.ram_hits:
                    self.ram_hits.append(v)

                # This must be a RAM reference
                if do_ram:
                    r = self.add_spec(r, "{-}", last_comment_pos)
                newLines.append(r)
                continue

            if "$" in c.opcode:
                i = c.opcode.index("$")

                wrds = c.opcode.split(" ")
                if wrds[0] in CODE_OPS:
                    # This must be a code reference
                    r = self.add_spec(r, "{}", last_comment_pos)
                    newLines.append(r)
                    continue

                # Numeric but not code
                cand = c.opcode[0:i]
                if cand not in candidates:
                    candidates.append(cand)

            # This doesn't need any fixing
            newLines.append(r)

        # These are numeric constants we did not process
        # for c in candidates:
        #    print c

        return newLines
