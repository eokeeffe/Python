import  wx
import  wx.lib.scrolledpanel as scrolled
import string

class TestPanel(scrolled.ScrolledPanel):
	def __init__(self, parent):
		scrolled.ScrolledPanel.__init__(self, parent, -1)
		
		self.textbox = wx.TextCtrl(self, -1, "",wx.DefaultPosition, wx.DefaultSize,wx.TE_MULTILINE)
		#create the input dialog box
		box = wx.TextEntryDialog(None,"Please enter Artist Name","Find Top 50 Albums","Name")
		#check if the box was correctly executed
		if box.ShowModal()==wx.ID_OK:
			answer=box.GetValue()
		#open the file for reading 
		filehandle = open(answer,'r')
		#read the file
		text = filehandle.read()
		#get the dimensions for the scroll box
		vbox = wx.BoxSizer(wx.VERTICAL)
		desc = wx.StaticText(self, -1,text)
		desc.SetForegroundColour("Blue")
		vbox.Add(desc, 0, wx.ALIGN_LEFT|wx.ALL, 5)
		#set the sizes and layout and show it
		self.SetSizer(vbox)
		self.SetAutoLayout(1)
		self.SetupScrolling()
		
app = wx.App(0)
frame = wx.Frame(None, wx.ID_ANY)
fa = TestPanel(frame)
frame.Show()
app.MainLoop()