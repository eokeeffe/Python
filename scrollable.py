import  wx
import  wx.lib.scrolledpanel as scrolled

class TestPanel(scrolled.ScrolledPanel):
    def __init__(self, parent):
        scrolled.ScrolledPanel.__init__(self, parent, -1)
        name = raw_input("Please enter the filename to read")
        fh = open(name,'r')
        text = fh.read()
        fh.close()
        vbox = wx.BoxSizer(wx.VERTICAL)
        desc = wx.StaticText(self, -1,text)
        desc.SetForegroundColour("Blue")
        vbox.Add(desc, 0, wx.ALIGN_LEFT|wx.ALL, 5)

        self.SetSizer(vbox)
        self.SetAutoLayout(1)
        self.SetupScrolling()


		
app = wx.App(0)
frame = wx.Frame(None, wx.ID_ANY)
fa = TestPanel(frame)
frame.Show()
app.MainLoop()