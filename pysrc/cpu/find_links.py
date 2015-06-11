
class FindLinks(object):

    def add_comment(self, original, commentPos):
        """
        Add a blank comment to the code line
        """
        original = original[:-1]  # Strip line feed
        while len(original) < commentPos:
            original = original + " "
        original = original + ";\n"
        return original

    def print_ram_hits(self):
        self.ram_hits.sort()
        for r in self.ram_hits:
            print "|| " + r + "     ||                  || ||"

    def add_spec(self, r, s, last_comment_pos):

        if ";" not in r:
            r = self.add_comment(r, last_comment_pos)

        # In case we are replacing an existing ... strip out the existing
        i = r.index(";")
        if r[i + 1:].strip().startswith("{"):
            j = r.index("}", i)
            r = r[0:i] + " " + r[j + 1:]

        r = r[0:i + 1] + s + " " + r[i + 1:].strip()

        return r + "\n"
