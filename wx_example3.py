try:
        import wx
        import os
except ImportError:
        raise ImportError,"The wxPython module is required to run this program"
class MessageDialog(wx.Dialog):
        def __init__(self, parent, id, title):
                wx.Dialog.__init__(self, parent, id, "Ayuda", size=(300, 300))
                #textoayuda=wx.TextCtrl(self, label='Ayuda:')
                texto1='''The program is divided into three stages.'''
                texto2='''\n\nFirst stage, selecting the measurements file. \nSecond stage, selecting or creating the destination file. \nThird, executing the program by pressing the Parse File button.'''
                texto3='''\n\nYou can use the file-directory tree browsers to select the measurements file, and the directory where you want to create the destination file, if it is not created yet.)'''
                sizer=wx.GridBagSizer()
                st1=wx.StaticText(self, -1, texto1, style=wx.ALIGN_LEFT)
                st2=wx.StaticText(self, -1, texto2, style=wx.ALIGN_LEFT)
                st3=wx.StaticText(self, -1, texto3, style=wx.ALIGN_LEFT)
                sizer.Add(st1, pos=(0,0), flag=wx.EXPAND|wx.TOP|wx.BOTTOM, border=15)
                sizer.Add(st2, pos=(4,0), flag=wx.EXPAND|wx.TOP|wx.BOTTOM, border=15)
                sizer.Add(st3, pos=(8,0), flag=wx.EXPAND|wx.TOP|wx.BOTTOM, border=15)
                button4=wx.Button(self, label='Ok')
                sizer.Add(button4,pos=(12,4), flag=wx.BOTTOM|wx.EXPAND)
                self.Centre()
                self.Show(True)
                self.Bind(wx.EVT_BUTTON, self.CloseHelp)
                self.SetSizer(sizer)
        def CloseHelp(self, event):
                self.Destroy()
class Main(wx.Frame):
        def __init__(self, parent, id, title):
                wx.Frame.__init__(self, parent, id, title, size=(1100,600))
                self.parent=parent
                self.initialize()
                self.Centre()
                self.Show(True)
        def initialize(self):
                sizer=wx.GridBagSizer()
                text1=wx.StaticText(self, label='Measurements File:')
                sizer.Add(text1, pos=(0,1), flag=wx.TOP|wx.LEFT|wx.BOTTOM, border=10)
                self.entry=wx.TextCtrl(self,-1,value=u"File path and name... Pick it down there.")
                sizer.Add(self.entry,(1,1),(1,30),wx.EXPAND)
                self.dir=wx.GenericDirCtrl(self, -1, dir='/home')
                sizer.Add(self.dir,(3,1),(20,30),wx.EXPAND)
                text2=wx.StaticText(self, label='Destination File:')
                sizer.Add(text2, pos=(0,40), flag=wx.TOP|wx.LEFT|wx.BOTTOM, border=10)
                self.entry2=wx.TextCtrl(self,-1,value=u"File path and name... Pick a file or create a new one after choosing the directory.")
                sizer.Add(self.entry2,(1,38),(1,34),wx.EXPAND)
                self.dir2=wx.GenericDirCtrl(self, -1, dir='/home')
                sizer.Add(self.dir2,(3,38),(20,34),wx.EXPAND)
                #Botones
                button1=wx.Button(self, label='Parse File')
                sizer.Add(button1,(26,31),(1,6), flag=wx.BOTTOM, border=6)
                button2=wx.Button(self, label='Cancel')
                sizer.Add(button2,(26,24),(1,4), flag=wx.BOTTOM, border=4)
                button3=wx.Button(self, label='Help')
                sizer.Add(button3,(26,39),(1,4), flag=wx.BOTTOM, border=4)
                #self.SetSizerAndFit(sizer)
                self.SetSizer(sizer)
                #Eventos
                self.Bind(wx.EVT_BUTTON, self.Cerrar, id=button2.GetId())
                self.Bind(wx.EVT_BUTTON, self.OnHelp, id=button3.GetId())
                self.Bind(wx.EVT_BUTTON, self.Parser, id=button1.GetId())
                #These are the problematic events:
				self.Bind(wx.EVT_TREE_ITEM_ACTIVATED, self.OnActivated, id=self.dir.GetId())
                self.Bind(wx.EVT_TREE_ITEM_ACTIVATED, self.OnActivated2, id=self.dir2.GetId())
                self.Bind(wx.EVT_TREE_SEL_CHANGED, self.OnActivated, id=self.dir.GetId())
                self.Bind(wx.EVT_TREE_SEL_CHANGED, self.OnActivated2, id=self.dir2.GetId())
        def Cerrar(self, event):
                self.Close()
        def Parser(self, event):
                os.system("/home/alex/programas/parser.py")
        def OnHelp(self, event):
                dlg=MessageDialog(None, -1, "")
                dlg.ShowModal()
        def OnActivated(self, event):#This is the problematic def…
                origen=self.dir.GetPath()
                TextCtrlValue(self.entry, origen)
                #self.entry.SetValue(origen)
                #origen.Destroy()
                origen=os.listdir(self.dir.GetPath())
                origen=self.GetItemText(event.GetItem(self.dir))
                SetValue(self.entry, origen)
                event.Skip()
        def OnActivated2(self, event):#Ignore this one. Same as OnActivated.
                destino=os.listdir(self.dir.GetPath())
                destino=self.GetItemText(event.GetItem())
                #SetValue(self.entry2, destino)
                event.Skip()
if __name__=="__main__":
        app=wx.App()
        frame=Main(None,-1,"Parser Interface...")
        #MessageDialog(None,-1,"Diálogo de ayuda...")
        app.MainLoop() 