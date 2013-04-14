import wx
import wx.lib.agw.customtreectrl as CT

class MainWindow(wx.Frame):
    def __init__(self, *args, **kwargs):
        wx.Frame.__init__(self, *args, **kwargs)

        self.panel = wx.Panel(self)
        self.dir = CT.CustomTreeCtrl(self.panel, size=(100, -1), 
                                     style=wx.SUNKEN_BORDER,
                                     agwStyle=CT.TR_FULL_ROW_HIGHLIGHT | CT.TR_HIDE_ROOT | CT.TR_NO_LINES | CT.TR_ROW_LINES)           

        root = self.dir.AddRoot("The Root Item")
        child = self.dir.AppendItem(root, "Test")
        child = self.dir.AppendItem(child, "Test 2")
        child = self.dir.AppendItem(child, "Test 3")
        child = self.dir.AppendItem(root, "Test 4")

        self.dir.ExpandAll()

        self.sizer = wx.BoxSizer()
        self.sizer.Add(self.dir, proportion=1, flag=wx.EXPAND)

        self.border = wx.BoxSizer()
        self.border.Add(self.sizer, 1, wx.ALL | wx.EXPAND, 5)

        self.panel.SetSizerAndFit(self.border)  
        self.Show()


app = wx.App(False)
win = MainWindow(None, size=(200, 300))
app.MainLoop()
