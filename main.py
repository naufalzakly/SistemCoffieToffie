import wx
from mainFrame import mainFrame

class MainApp(wx.App):
    def OnInit(self):
        self.frame = mainFrame(None)
        self.frame.Show(True)
        self.SetTopWindow(self.frame)
        return True

if __name__ == '__main__':
    app = MainApp()
    app.MainLoop()
