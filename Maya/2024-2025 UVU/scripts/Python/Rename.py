import maya.cmds as cmd

def Rename(name=str):
    sels = cmd.ls(selection = True)
    if len(sels) == 0:
       return
    hashNum = name.count('#')
    nameParts = name.rpartition('#')
    namePartsL = list(nameParts)
    namePartsL[0] = namePartsL[0].replace('#','')

    i = 1
    for sel in sels:
      iStr = str(i).zfill(hashNum)
      i += 1
      newName = f'{namePartsL[0]}{iStr}{namePartsL[2]}'
      cmd.rename(sel, newName) 

Rename('leg_###_jnt')