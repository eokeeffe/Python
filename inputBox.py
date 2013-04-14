#input box in wxpython

import wx

class bucky(wx.Frame):
	def __init__(self,parent,id):
		wx.Frame.__init__(self,parent,id,'Frame aka window',size=(300,200))
		panel = wx.Panel(self)
	
		box = wx.TextEntryDialog(None,"Please enter Artist Name","Find Top 50 Albums","Name")
		if box.ShowModal()==wx.ID_OK:
			answer=box.GetValue()
			
		box2= wx.MessageBox(answer)
		
app=wx.PySimpleApp()
frame=bucky(parent = None,id = -1)
app.MainLoop()