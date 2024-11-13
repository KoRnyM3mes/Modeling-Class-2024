import maya.cmds as cmd

def Group():
    selectedObjs = cmd.ls(selection = True)
    for i in range(len(selectedObjs)):
        rot = cmd.xform(selectedObjs[i], q=True, ws=True, ro=True)
        grps = cmd.group(selectedObjs[i], name = (selectedObjs[i] + "_Grp"))
        cmd.xform(grps, ws=True, ro=[rot[0], rot[1], rot[2]])
        cmd.xform(selectedObjs[i], os=True, ro=[0, 0, 0])
Group()