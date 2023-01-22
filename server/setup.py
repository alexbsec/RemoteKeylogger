import subprocess

with open("run-commands.txt", "r") as cmd:
    cmds = cmd.readlines()
    for c in cmds:
        subprocess.run(c.split(" "))
