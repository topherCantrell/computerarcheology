# Computer Archeology



## OLD (refactoring)

This repository contains the content and tools to generate my [Computer Archeology](http://computerarcheology.com) website.

It also contains the archeology tools (disassemblers, assemblers, formatters, etc).

The "art" directory contains images for the READMEs here. 

The "content" directory contains the raw files that make up the Computer Archeology website. This is the meat of the project.

The "oldjavasrc" directory contains assemblers and disassemblers and various older tools that need translating to Python.

The "pysrc" directory contains the Python source files. You should run command line tools with this as your current working directory.

Once you have cloned the project open a command line to the "pysrc" directory. 

```
python make_web.py
```

This command creates a "deploy" directory. This is a local copy of the webserver root directory.

```
python development_server.py
```

This command starts a local web server. Point your browser to "localhost:8080".

All of the content is in github markdown. The process is described in [markdownstyle.md](markdwonstyle.md).

# TODO

My web server should watch this repo and automatically reploy when changes are made.
