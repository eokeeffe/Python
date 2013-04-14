#!/usr/bin/python

# simple clicker gui , just press the button :)

import wx
import random

APP_SIZE_X = 300
APP_SIZE_Y = 200

class MyButtons(wx.Dialog):
	count = 0
	number = 'Number of Clicks so far:'
	text = None
	def __init__(self, parent, id, title):
		wx.Dialog.__init__(self, parent, id, title, size=(APP_SIZE_X, APP_SIZE_Y))
		
		wx.Button(self, 1, 'Close', (50, 130))
		wx.Button(self, 2, 'Click', (150, 130), (110, -1))
		
		self.text = wx.StaticText(self, -1, style=wx.ALIGN_CENTRE)
		self.text.SetLabel(self.number+str(self.count))
		
		self.Bind(wx.EVT_BUTTON, self.OnClose, id=1)
		self.Bind(wx.EVT_BUTTON, self.Click, id=2)
		
		self.Centre()
		self.ShowModal()
		self.Destroy()
		
	def OnClose(self, event):
		self.Close(True)
		
	def Click(self, event):
		self.count = self.count + 1
		self.text.SetLabel(self.number+str(self.count))
		

app = wx.App(0)
MyButtons(None, -1, 'click.py')
app.MainLoop()