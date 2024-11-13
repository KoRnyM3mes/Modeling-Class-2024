import maya.cmds as cmd

def Grouper():
    selectedObjs = cmd.ls(selection = True)
    for i in range(len(selectedObjs)):
        trans = cmd.xform(selectedObjs[i], q=True, ws=True, t=True)
        rot = cmd.xform(selectedObjs[i], q=True, ws=True, ro=True)
        cmd.xform(selectedObjs[i], os=True, t=[0, 0, 0], ro=[0, 0, 0])
        grps = cmd.group(selectedObjs[i], name = (selectedObjs[i] + "_Grp"))
        cmd.xform(grps, ws=True, t=[trans[0], trans[1], trans[2]], ro=[rot[0], rot[1], rot[2]])
Grouper()