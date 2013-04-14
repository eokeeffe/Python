#!/usr/bin/python

# fonts.py

import wx

class MyFrame(wx.Frame):
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title, wx.DefaultPosition, wx.Size(325, 320))

        panel = wx.Panel(self, -1)
        fh = open('Daft-punk.txt','r')
        text1 = fh.read()
        fh.close()
        font1 = wx.Font(10, wx.NORMAL, wx.ITALIC, wx.NORMAL)
        font2 = wx.Font(10, wx.ROMAN, wx.NORMAL, wx.NORMAL)
        font3 = wx.Font(10, wx.MODERN, wx.NORMAL, wx.BOLD)
        lyrics1 = wx.StaticText(panel, -1, text1,(30,15), style=wx.ALIGN_CENTRE)
        lyrics1.SetFont(font1)
        self.Center()

class MyApp(wx.App):
    def OnInit(self):
        frame = MyFrame(None, -1, 'fonts.py')
        frame.Show(True)
        self.SetTopWindow(frame)
        return True

app = MyApp(0)
app.MainLoop()