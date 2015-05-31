import json
import os
import shutil

import web.navigation
import web.markup_to_html

from web.make_web_error import MakeWebError


def process_entry_code(e, dep, cont):
    raise Exception("TODO")


def process_entry_address(e, dep, cont):
    raise Exception("TODO")


def process_entry_mark(nodes, dep, cont):

    e = nodes[-1]

    nav = None
    if "nav" in e and e["nav"] is not "":
        nav = e["nav"]

    bread_crumbs, active_node = web.navigation.get_bread_crumbs(nodes)
    site_nav = web.navigation.get_site_nav(desc, nodes, active_node)

    mu = web.markup_to_html.MarkupToHTML()

    mu.translate(content_root,
                 cont + e["mark"],
                 dep + e["out"],
                 bread_crumbs,
                 site_nav,
                 nav)


def process_entry_copy(e, dep, cont):
    fname = e["copy"]
    shutil.copy(cont + fname, dep + fname)


def process_entry_copy_dir(e, dep, cont):
    fname = e["copyDir"]
    os.makedirs(dep + fname)
    for f in os.listdir(cont + fname):
        if os.path.isfile(cont + fname + "/" + f):
            shutil.copy(cont + fname + "/" + f, dep + fname + "/" + f)


def process_entries(nodes, dep, cont):

    ents = nodes[-1]["entries"]

    for e in ents:
        if "mark" in e:
            process_entry_mark(nodes + [e], dep, cont)
        elif "copy" in e:
            process_entry_copy(e, dep, cont)
        elif "copyDir" in e:
            process_entry_copy_dir(e, dep, cont)
        elif "dir" in e:
            directory = e["dir"]
            os.makedirs(dep + directory)
            process_entries(nodes + [e], dep + directory + "/", cont + directory + "/")
        else:
            raise Exception("Unknown deployment entry:" + str(e))


with open('site.js') as data_file:
    desc = json.load(data_file)

content_root = desc["content_root"]
deploy_root = desc["deploy_root"]

if os.path.exists(deploy_root):
    shutil.rmtree(deploy_root)

os.makedirs(deploy_root)

try:

    process_entries([desc], deploy_root, content_root)

except MakeWebError, e:

    if e.line:
        print "ERROR: " + e.message + " in " + e.fname + " at line " + str(e.line)
    else:
        print "ERROR: " + e.message + " in " + e.fname
