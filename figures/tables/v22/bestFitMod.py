import os
files = ["ensemble_2012pf_RQcdZero_fZinvAll_0b_le3j-1hp_300toys_bySelection.tex",
         "ensemble_2012pf_RQcdZero_fZinvAll_0b_ge4j-1hp_300toys_bySelection.tex",
         "ensemble_2012pf_RQcdZero_fZinvAll_1b_le3j-1hp_300toys_bySelection.tex",
         "ensemble_2012pf_RQcdZero_fZinvAll_1b_ge4j-1hp_300toys_bySelection.tex",
         "ensemble_2012pf_RQcdZero_fZinvAll_2b_le3j-1h_300toys_bySelection.tex",
         "ensemble_2012pf_RQcdZero_fZinvAll_2b_ge4j-1h_300toys_bySelection.tex"]

for file in files:
    cmd1 = "sed -i 's/\\\documentclass/%\\\documentclass/' "
    cmd2 = "sed -i 's/\\\def/%\\\def/' "
    cmd3 = "sed -i 's/\\\end{doc/%\\\end{doc/' "
    cmd4 = "sed -i 's/\\\use/%\\\use/' "
    cmd5 = r"sed -i 's/\\begin{doc/%\\begin{doc/' "
    cmd6 = r"sed -i 's/\\new/%\\new/' "

    cmdList = [cmd1,cmd2,cmd3,cmd4,cmd5,cmd6]
    for cmd in cmdList:
        os.system(cmd + file)
