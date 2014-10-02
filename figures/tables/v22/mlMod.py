import os
files = [
"mlTables_0b_ge2j.tex",
"mlTables_0b_ge4j.tex",
"mlTables_1b_ge2j.tex",
"mlTables_1b_ge4j.tex",
"mlTables_1b_le3j.tex",
"mlTables_2b_ge2j.tex",
"mlTables_2b_ge4j.tex",
"mlTables_2b_le3j.tex",
"mlTables_0b_le3j.tex",]

for file in files:
    cmd1 = "sed -i 's/\\\documentclass/%\\\documentclass/' "
    cmd2 = r"sed -i 's/\\begin{doc/%\\begin{doc/' "
    cmd3 = "sed -i 's/\\\end{doc/%\\\end{doc/' "
    cmdList = [cmd1,cmd2,cmd3]
    for cmd in cmdList:
        print cmd + file
        os.system(cmd + file)
