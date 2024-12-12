import maya.cmds as cmd
import Recolor

class RecolorUI():
    def __init__(self):
        self.mWindow = 'rcWindow'

    def create(self):
        self.delete()

        self.mWindow = cmd.window(self.mWindow,
                                  title = 'Recolor Tool',
                                  widthHeight = (500,200),
                                  resizeToFitChildren=True)
        mColumn = cmd.columnLayout(parent=self.mWindow, adjustableColumn=True)

        cmd.textField(parent=mColumn, font='boldLabelFont', editable=False, text='Use the slider to select a color')
        self.colorSlider = cmd.intSlider(parent=mColumn, min=0, max=31, dragCommand=self.updateColorDisp)
        self.colorDisplay = cmd.canvas(parent=mColumn, rgbValue = (0, 0, 0))
        cmd.button(parent=mColumn, label='Change color', command = lambda *args: self.RC_CMD())

        cmd.showWindow(self.mWindow)


    def updateColorDisp(self, sliderNum):
        if sliderNum == 0:
            cmd.canvas(self.colorDisplay, edit=True, rgbValue=(.471,.471,.471))
        elif sliderNum == 1:
            cmd.canvas(self.colorDisplay, edit=True, rgbValue=(0,0,0))
        elif sliderNum == 2:
            cmd.canvas(self.colorDisplay, edit=True, rgbValue=(.251,.251,.251))
        elif sliderNum == 3:
            cmd.canvas(self.colorDisplay, edit=True, rgbValue=(.6,.6,.6))
        elif sliderNum == 4:
            cmd.canvas(self.colorDisplay, edit=True, rgbValue=(.608,0,.157))
        elif sliderNum == 5:
            cmd.canvas(self.colorDisplay, edit=True, rgbValue=(0,.015,.376))
        elif sliderNum == 6:
            cmd.canvas(self.colorDisplay, edit=True, rgbValue=(0,0,1))
        elif sliderNum == 7:
            cmd.canvas(self.colorDisplay, edit=True, rgbValue=(0,.274,.098))
        elif sliderNum == 8:
            cmd.canvas(self.colorDisplay, edit=True, rgbValue=(.149,0,.263))
        elif sliderNum == 9:
            cmd.canvas(self.colorDisplay, edit=True, rgbValue=(.784,0,.784))
        elif sliderNum == 10:
            cmd.canvas(self.colorDisplay, edit=True, rgbValue=(.535,.283,.200))
        elif sliderNum == 11:
            cmd.canvas(self.colorDisplay, edit=True, rgbValue=(.246,.137,.121))
        elif sliderNum == 12:
            cmd.canvas(self.colorDisplay, edit=True, rgbValue=(.591,.153,0))
        elif sliderNum == 13:
            cmd.canvas(self.colorDisplay, edit=True, rgbValue=(.997,.011,0))
        elif sliderNum == 14:
            cmd.canvas(self.colorDisplay, edit=True, rgbValue=(0,1,.061))
        elif sliderNum == 15:
            cmd.canvas(self.colorDisplay, edit=True, rgbValue=(0,.255,.6))
        elif sliderNum == 16:
            cmd.canvas(self.colorDisplay, edit=True, rgbValue=(1,1,1))
        elif sliderNum == 17:
            cmd.canvas(self.colorDisplay, edit=True, rgbValue=(.927,.941,0))
        elif sliderNum == 18:
            cmd.canvas(self.colorDisplay, edit=True, rgbValue=(.392,.863,1))
        elif sliderNum == 19:
            cmd.canvas(self.colorDisplay, edit=True, rgbValue=(.263,1,.639))
        elif sliderNum == 20:
            cmd.canvas(self.colorDisplay, edit=True, rgbValue=(1,.69,.69))
        elif sliderNum == 21:
            cmd.canvas(self.colorDisplay, edit=True, rgbValue=(.89,.675,.474))
        elif sliderNum == 22:
            cmd.canvas(self.colorDisplay, edit=True, rgbValue=(.996,1,.547))
        elif sliderNum == 23:
            cmd.canvas(self.colorDisplay, edit=True, rgbValue=(0,.6,.329))
        elif sliderNum == 24:
            cmd.canvas(self.colorDisplay, edit=True, rgbValue=(.849,.570,.427))
        elif sliderNum == 25:
            cmd.canvas(self.colorDisplay, edit=True, rgbValue=(.878,.784,.306))
        elif sliderNum == 26:
            cmd.canvas(self.colorDisplay, edit=True, rgbValue=(.635,.812,.278))
        elif sliderNum == 27:
            cmd.canvas(self.colorDisplay, edit=True, rgbValue=(.231,.757,.580))
        elif sliderNum == 28:
            cmd.canvas(self.colorDisplay, edit=True, rgbValue=(.255,.820,.725))
        elif sliderNum == 29:
            cmd.canvas(self.colorDisplay, edit=True, rgbValue=(.227,.616,.808))
        elif sliderNum == 30:
            cmd.canvas(self.colorDisplay, edit=True, rgbValue=(.612,.420,.808))
        else:
            cmd.canvas(self.colorDisplay, edit=True, rgbValue=(.808,.349,.655))

    def RC_CMD(self):
        index = cmd.intSlider(self.colorSlider, q=True, value=True)

        Recolor.Color(index)
        

    def delete(self):
        if (cmd.window(self.mWindow, exists=True)):
            cmd.deleteUI(self.mWindow)