call ..\vars.bat

call ..\DOCXToWeb.bat xevious.docx > xevious.docx.inc.html
call ..\CodeToWeb.bat cpu1.txt "Xevious - CPU1" > cpu1.txt.html
call ..\CodeToWeb.bat cpu2.txt "Xevious - CPU2" > cpu2.txt.html
call ..\CodeToWeb.bat cpu3.txt "Xevious - CPU3" > cpu3.txt.html

call ..\WebDeploy