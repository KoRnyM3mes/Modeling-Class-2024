import maya.cmds as cmd

def Group(ctrls):
    for ctrl in ctrls:
        trans = cmd.xform(ctrl, q=True, ws=True, t=True)
        rot = cmd.xform(ctrl, q=True, ws=True, ro=True)
        cmd.xform(ctrl, os=True, t=[0, 0, 0], ro=[0, 0, 0])
        grps = cmd.group(ctrl, name = (ctrl + "_Grp"))
        cmd.xform(grps, ws=True,  t=[trans[0], trans[1], trans[2]], ro=[rot[0], rot[1], rot[2]])   

def ControlMaker():
    selectedObjs = cmd.ls(selection = True)
    ctrlList= []
    for obj in selectedObjs:
        rot = cmd.xform(obj, q=True, ws=True, ro=True)
        trans = cmd.xform(obj, q=True, ws=True, t=True)
        if '_' in obj:
            nameLs = obj.rpartition('_')
            ctrlName = (nameLs[0] + "_Ctrl")
        else:
            ctrlName = (obj + "_Ctrl")
        ctrlList.append(ctrlName)
        ctrl = cmd.circle(name = ctrlName)
        cmd.xform(ctrl, t=[trans[0], trans[1], trans[2]], ro=[rot[0], rot[1], (rot[2])])
    Group(ctrlList)


ControlMaker()