import string


class IDMgr:

    def __init__(self):
        self._used_ids = []

    def add_id(self, text):

        text = text.lower()
        text = text.replace(' ', '-')

        tt = ''
        for t in text:
            if t in string.ascii_letters or t in '0123456789-':
                tt += t
        text = tt

        if text in self._used_ids:
            i = 1
            while True:
                g = text + str(i)
                if not g in self._used_ids:
                    text = g
                    break
                i += 1

        self._used_ids.append(text)
        return text
