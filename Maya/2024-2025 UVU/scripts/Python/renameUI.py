import maya.cmds as cmd
import Rename

class RenameUI():
    def __init__(self):
        self.mWindow = 'rnWindow'

    def create(self):
        self.delete()

        self.mWindow = cmd.window(self.mWindow,
                                  title = 'Sequential Renamer Tool',
                                  widthHeight = (500,200),
                                  resizeToFitChildren=True)
        mColumn = cmd.columnLayout(parent=self.mWindow, adjustableColumn=True)

        self.nameField = cmd.textField(parent=mColumn, font='boldLabelFont',  placeholderText='Name_##_NodeType')
        cmd.button(parent=mColumn, label='Rename selected', command = lambda *args: self.RN_CMD())

        cmd.showWindow(self.mWindow)

    def RN_CMD(self):
        name = cmd.textField(self.nameField, q=True, text=True)

        Rename.Rename(name)
    
    def delete(self):
        if (cmd.window(self.mWindow, exists=True)):
            cmd.deleteUI(self.mWindow)