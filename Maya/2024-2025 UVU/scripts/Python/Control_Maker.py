import maya.cmds as cmd

def Group(ctrls):
    for i in range(len(ctrls)):
        rot = cmd.xform(ctrls[i], q=True, ws=True, ro=True)
        grps = cmd.group(ctrls[i], name = (ctrls[i] + "_Grp"))
        cmd.xform(grps, ws=True, ro=[rot[0], rot[1], rot[2]])
        cmd.xform(ctrls[i], os=True, ro=[0, 0, 0])   

def controlMaker():
    selectedObjs = cmd.ls(selection = True)
    ctrlList= []
    for i in range(len(selectedObjs)):
        rot = cmd.xform(selectedObjs[i], q=True, ws=True, ro=True)
        trans = cmd.xform(selectedObjs[i], q=True, ws=True, t=True)
        if '_' in selectedObjs[i]:
            nameLs = selectedObjs[i].rpartition('_')
            ctrlName = (nameLs[0] + "_Ctrl")
        else:
            ctrlName = (selectedObjs[i] + "_Ctrl")
        ctrlList.append(ctrlName)
        ctrl = cmd.circle(name = ctrlName)
        cmd.xform(ctrl, t=[trans[0], trans[1], trans[2]], ro=[rot[0], rot[1], (rot[2] + 90)])
    Group(ctrlList)


controlMaker()