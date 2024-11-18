import maya.cmds as cmd

def Grouper():
    selectedObjs = cmd.ls(selection = True)
    for obj in selectedObjs:
        trans = cmd.xform(obj, q=True, ws=True, t=True)
        rot = cmd.xform(obj, q=True, ws=True, ro=True)
        cmd.xform(obj, os=True, t=[0, 0, 0], ro=[0, 0, 0])
        grps = cmd.group(obj, name = (obj + "_Grp"))
        cmd.xform(grps, ws=True, t=[trans[0], trans[1], trans[2]], ro=[rot[0], rot[1], rot[2]])
Grouper()