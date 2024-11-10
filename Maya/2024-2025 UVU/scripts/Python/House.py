import maya.cmds as cmd

cmd.polyCube( w=5.5, h=5.5, d=5.5, name="house")
cmd.move(0, 2.75, 0)

cmd.polyCube(w=7, h=1.5, d= 7, sz=3, cuv=4, ch=1, name="Roof")
cmd.move (0, 6.25, 0)
cmd.select ('Roof.e[2:3]')
cmd.move(0, 1.5, 0, r=True)

cmd.polyCylinder (r=.5, h=2, sx=20, name="chimney")
cmd.move (2, 8.4, 2)
cmd.polyBevel3 ('chimney.e[20:39]')