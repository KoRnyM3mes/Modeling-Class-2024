import maya.cmds as cmd

def Group():
    selectedObjs = cmd.ls(selection = True)
    for i in range(len(selectedObjs)):
        cmd.group(selectedObjs, name = (selectedObjs[i] + "_Grp"))

Group()