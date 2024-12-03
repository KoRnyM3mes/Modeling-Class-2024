import maya.cmds as cmd

def Color(color=int):
    sels = cmd.ls(selection = True)
    shapes = cmd.listRelatives(sels, shapes=True)

    for shape in shapes:
        cmd.setAttr(f"{shape}.overrideEnabled", 1)
        cmd.setAttr(f"{shape}.overrideColor", color)

Color(1)