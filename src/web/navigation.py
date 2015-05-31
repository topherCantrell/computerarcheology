
def _make_crumb(link, nav, active):

    if active:
        return '<li class="active"><strong>' + nav + '</strong></li>'
    else:
        return '<li><a href="' + link + '">' + nav + '</a></li>'


def get_bread_crumbs(nodes):

    nodes = nodes[1:]
    active_node = None

    if "nav" not in nodes[-1]:
        nodes = nodes[:-1]

    if len(nodes) > 0:
        crumbs = _make_crumb("/", "Home", False)
    else:
        crumbs = _make_crumb("/", "Home", True)

    for x in xrange(len(nodes)):
        link = "/"
        for y in xrange(x + 1):
            if "dir" in nodes[y]:
                link = link + nodes[y]["dir"] + "/"
        node = nodes[x]
        active = False
        if x == (len(nodes) - 1):
            active_node = node
            active = True
        nav = None
        if "nav" in node:
            nav = node["nav"]
        else:
            nav = node["dir"]
        crumbs = crumbs + _make_crumb(link, nav, active)

    return crumbs, active_node


def _get_site_nav_html(link, nav, level, active, leaf=True, opened=True):
    #            snn
    # <li class="sn1"><span class="sna"><strong>NAV</strong></span></li>
    # <li class="sn1"><a class="sna">NAV</a></li>
    cl = "snn"
    if level == 0:
        cl = "sn1"
    if not leaf:
        if opened:
            cl = cl + " collapsed expanded"
        else:
            cl = cl + " collapsed"
    if active:
        return '<li class="' + cl + '"><span class="sna"><strong>' + nav + '</strong></span>'
    else:
        return '<li class="' + cl + '"><a class="sna" href="' + link + '">' + nav + '</a>'


def _get_site_nav_recurse(node, nodes, link, level, active_node):
    ret = ""
    ents = node["entries"]
    for ent in ents:
        active = False
        if ent == active_node:
            active = True
        opened = False
        if ent in nodes:
            opened = True
        if "dir" in ent:
            if "nav" in ent:
                leaf = False
                if "leaf" in ent and ent["leaf"]:
                    leaf = True
                ret = ret + _get_site_nav_html(link + ent["dir"] + "/", ent["nav"], level, active, leaf, opened)
                if opened:
                    ret = ret + '<ul>'
                else:
                    ret = ret + '<ul hidden>'
                ret = ret + _get_site_nav_recurse(ent, nodes, link + ent["dir"] + "/", level + 1, active_node)
                ret = ret + "</ul></li>"
        elif "nav" in ent:
            ret = ret + _get_site_nav_html(link + ent["out"], ent["nav"], level, active, True, opened)
            ret = ret + "</li>"

    return ret


def get_site_nav(desc, nodes, active_node):

    if len(nodes) < 3:
        a = _get_site_nav_html("/", "Home", 0, True) + "<p></li>"
    else:
        a = _get_site_nav_html("/", "Home", 0, False) + "<p></li>"

    ret = a + _get_site_nav_recurse(desc, nodes, "/", 0, active_node)

    return ret
