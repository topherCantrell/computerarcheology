import string
import traceback

from web.text_line import TextLine

from web.make_web_error import MakeWebError


class MarkupToHTML:

    def __init__(self):
        self.headers = []
        self.raw_mode = None

    @staticmethod
    def read_text_lines(fileName):
        ret = []
        with open(fileName) as f:
            raw = f.readlines()

        num = 1
        for r in raw:
            if r[-1] == '\n':
                ret.append(TextLine(r[0:-1], fileName, num))
            else:
                ret.append(TextLine(r, fileName, num))
            num += 1

        return ret

    @staticmethod
    def entize_string(s):
        ret = ""
        # Eventually we want to escape stretches of text.
        for c in s:
            if c == '<':
                ret = ret + "&lt;"
            elif c == '>':
                ret = ret + "&gt;"
            elif c == '&':
                ret = ret + "&amp;"
            else:
                ret = ret + c
        return ret

    def make_header_link(self, text):
        ret = ""
        for t in text:
            if t in string.ascii_letters or t in string.digits:
                ret = ret + t
        if len(ret) == 0:
            ret = "header"
        if ret in self.headers:
            ret = ret + str(len(self.headers))
        self.headers.append(ret)
        return ret

    def mark_down_headers(self, proc, page_nav):

        #     text        lid   id
        # == This is it == it #thisIt

        # Count the leading "=". This is the
        # header number.
        i = 0
        while(proc[i] == '='):
            i = i + 1

        # Find the end of the text
        j = proc.index('=', i)

        text = proc[i:j].strip()
        alt_text = proc[j + i:].strip()

        # The link ID might be explicitly given
        if '#' in alt_text:
            x = alt_text.index('#')
            lid = alt_text[x + 1:].strip()
            alt_text = alt_text[0:x].strip()
        else:
            lid = self.make_header_link(text)

        # There might be alternate text just for the navigation pane
        if alt_text == "":
            alt_text = text

        h = '<h%d id="%s" class="siteTarget">%s</h%d>'
        t = h % (i, lid, text, i)

        page_nav.append({'level': i, 'text': alt_text, 'link': lid})
        return t

    def mark_down_braces(self, proc):
        p1 = '<a href="%s">%s</a>'
        p2 = '<img src="%s">%s</img>'
        # print proc
        while "[" in proc:
            i = proc.index("[")
            ii = i
            j = proc.index("]", i)

            tmp = p1
            if proc[i + 1] == '!':
                tmp = p2
                ii = i + 1
            if " " in proc[i:j]:
                k = proc.index(" ", i)
                proc = proc[0:i] + tmp % (proc[ii + 1:k].strip(), proc[k + 1:j].strip()) + proc[j + 1:]
            else:
                proc = proc[0:i] + tmp % (proc[ii + 1:j].strip(), "") + proc[j + 1:]
        return proc

    def mark_down_start_raw(self, proc, body_lines):
        if proc.startswith("{{{code"):
            self.raw_mode = "pre"
            body_lines.append('<pre class="codePreStyle">')
            self.raw_mode = "pre"
            return

        if proc.startswith("{{{html"):
            self.raw_mode = "html"
            return

        body_lines.append("<pre>")
        self.raw_mode = "pre"

    def mark_down_continue_raw(self, proc, body_lines):
        if proc.startswith("}}}"):
            if self.raw_mode == "pre":
                body_lines.append("</pre>")
            return True

        body_lines.append(proc + "\n")
        return False

    def mark_down_start_bullets(self, proc):
        return '<ul><li>' + proc[1:].strip() + '</li>'

    def mark_down_continue_bullets(self, proc):
        return '<li>' + proc[1:].strip() + '</li>'

    def mark_down_end_bullets(self, body_lines):
        body_lines.append('</ul>')

    def mark_down_start_table(self, proc):
        hdrs = proc.split("||")[1:-1]
        if hdrs[0].startswith("="):
            hdrs[0] = hdrs[0][1:].strip()
            s = '<table class="table table-condensed"><thead><tr>'
            for h in hdrs:
                s = s + '<th>' + h.strip() + '</th>'
            s = s + '</tr></thead>'
        else:
            s = '<table class="table table-condensed"><tr>'
            for h in hdrs:
                s = s + '<td>' + h.strip() + '</td>'
            s = s + '</tr>'
        return s

    def mark_down_continue_table(self, proc):
        cells = proc.split("||")[1:-1]
        s = '<tr>'
        for c in cells:
            s = s + '<td>' + c.strip() + '</td>'
        s = s + '</tr>'
        return s

    def mark_down_end_table(self, body_lines):
        body_lines.append("</table>")

    def mark_down_non_string(self, obj, body_lines, page_nav):
        # print "WHAT THE HECK IS THIS "+str(obj)
        pass

    def mark_down(self, raw, fills, page_nav):
        self.raw_mode = None
        self.headers = []

        mode = "none"

        bodyLines = []  # List of lines for the body
        for line in raw:
            try:

                if not isinstance(line, TextLine):
                    self.mark_down_non_string(line, bodyLines, page_nav)
                    continue

                proc = line.text.strip()

                # In raw mode, we don't process any markup at all
                if mode == "raw":
                    nm = self.mark_down_continue_raw(line.text, bodyLines)
                    if nm:
                        mode = "none"
                    continue

                # This is how you get into raw mode
                if proc.startswith("{{{"):
                    self.mark_down_start_raw(line.text, bodyLines)
                    mode = "raw"
                    continue

                # -- Markup Processing --

                proc = MarkupToHTML.entize_string(proc)

                # Handle defines
                if proc.startswith("%%"):
                    i = proc.index(" ")
                    fills[proc[2:i]] = proc[i + 1:].strip()
                    continue

                # Handle line breaks
                proc = proc.replace("[[br]]", "<br>")

                # Handle paragraph breaks
                if proc == "":
                    proc = '<p />'

                # Handle quick headers
                if proc.startswith("="):
                    proc = self.mark_down_headers(proc, page_nav)

                # Handle quick links
                if "[" in proc:
                    # print "::" + proc + "::"
                    proc = self.mark_down_braces(proc)

                # If we are making a list of bullets
                if mode == "bullets":
                    if proc.startswith("*"):
                        proc = self.mark_down_continue_bullets(proc)
                    else:
                        self.mark_down_end_bullets(bodyLines)
                        mode = "none"
                else:
                    if proc.startswith("*"):
                        proc = self.mark_down_start_bullets(proc)
                        mode = "bullets"
                        bodyLines.append(proc)
                        continue

                # If we are making a table
                if mode == "table":
                    if proc.startswith("||"):
                        proc = self.mark_down_continue_table(proc)
                    else:
                        self.mark_down_end_table(bodyLines)
                        mode = "none"
                else:
                    if proc.startswith("||"):
                        proc = self.mark_down_start_table(proc)
                        mode = "table"
                        bodyLines.append(proc)
                        continue

                # If we get here we have a line to add
                bodyLines.append(proc + " ")
            except Exception:
                print ("Error on line " + str(line.lineNumber) + " in file '" + line.fileName + "'")
                traceback.print_exc()

        # All done
        return bodyLines

    def make_page_nav(self, page_nav):
        if len(page_nav) < 1:
            return ""

        # Normalize for pages that start at "2"
        tlev = page_nav[0]["level"]
        if tlev != 1:
            tlev = tlev - 1
            for p in page_nav:
                p["level"] = p["level"] - tlev

        pret = [{'level': 0}]
        self._make_page_nav_recurse(pret, 1, 0, page_nav)

        # pprint.pprint(pret)

        lines = []
        self._make_page_nav_html_recurse(pret[0]['sub'], lines)
        return "".join(lines)

    def _make_page_nav_html_recurse(self, cur, lines):
        for c in cur:
            cl = "n"
            if c["level"] == 1:
                cl = "1"
            # li = '<li class="sn%s"><a class="sna" onclick="pageScrollTo(\'%s\');return false;">%s</a>'
            li = '<li class="sn%s"><a class="sna" href="#%s">%s</a>'
            li = li % (cl, c["link"], c["text"])
            lines.append(li)
            if 'sub' in c:
                lines.append('<ul>')
                self._make_page_nav_html_recurse(c['sub'], lines)
                lines.append('</ul>')
            lines.append('</li>')

    def _make_page_nav_recurse(self, parent, lev, pos, page_nav):
        ret = []
        while True:
            if pos == len(page_nav) or page_nav[pos]["level"] < lev:
                parent[len(parent) - 1]["sub"] = ret
                return pos
            if page_nav[pos]["level"] == lev:
                ret.append(page_nav[pos])
                pos = pos + 1
                continue
            if page_nav[pos]["level"] != (lev + 1):
                raise Exception("Missing header level")
            pos = self._make_page_nav_recurse(ret, lev + 1, pos, page_nav)

    def translate(self, root_dir, in_name, out_name, bread_crumbs, site_tree, title, raw=None):

        template = "<!-- %%BODY%% -->"  # Default (body-only) template

        fills = {"template": "master.template", "title": title}  # Fill-ins dictionary (with defaults)
        page_nav = []

        # Read the markup (if it wasn't passed in)
        if raw is None:
            raw = MarkupToHTML.read_text_lines(in_name)

        # Process the mark down on the content
        body_lines = self.mark_down(raw, fills, page_nav)

        # Page template
        if "template" in fills:
            with open(root_dir + fills["template"]) as f:
                template = f.read()

        im = ""
        if "image" in fills:
            im = '<img src="' + fills["image"] + '" height="90" style="PADDING-LEFT: 40px"/>'

        # To a single string
        body = "".join(body_lines)
        # body = "TESTING"

        pageTree = self.make_page_nav(page_nav)

        if fills["title"] is None:
            raise MakeWebError("'%%title' must be given", in_name)

        # Substitute pieces into the template
        oput = template.replace("<!-- %%TITLE%% -->", fills["title"])
        oput = oput.replace("<!-- %%CONTENT_TITLE%% -->", fills["title"])
        oput = oput.replace("<!-- %%BREAD_CRUMBS%% -->", bread_crumbs)
        oput = oput.replace("<!-- %%PAGE_TREE%% -->", pageTree)
        oput = oput.replace("<!-- %%SITE_TREE%% -->", site_tree)
        oput = oput.replace("<!-- %%CONTENT%% -->", body)
        oput = oput.replace("<!-- %%IMAGE%% -->", im)

        # Remove any un-filled parts of the template
        while("<!-- %%") in oput:
            i = oput.index("<!-- %%")
            j = oput.index("-->", i)
            oput = oput[0:i] + oput[j + 3:]

        # Write the HTML
        with open(out_name, 'w') as f:
            f.write(oput)
