#!/usr/bin/python

# dragdrop.py

import os
import wx

class MyTextDropTarget(wx.TextDropTarget):
    def __init__(self, object):
        wx.TextDropTarget.__init__(self)
        self.object = object

    def OnDropText(self, x, y, data):
        self.object.InsertStringItem(0, data)


class DragDrop(wx.Frame):
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title, size=(650, 500))
        panel = wx.Panel(self,-1,style=wx.BORDER)

       
        #self.dir = wx.GenericDirCtrl(splitter1, -1, dir='/home/', style=wx.DIRCTRL_DIR_ONLY)
        self.lc1 = wx.ListCtrl(panel, -1, size=(100,100),pos=(0,0),style=wx.LC_LIST)
        self.lc2 = wx.ListCtrl(panel, -1, size=(100,100),pos=(200,0),style=wx.LC_LIST)

        dt = MyTextDropTarget(self.lc2)
        self.lc2.SetDropTarget(dt)
        self.Bind(wx.EVT_LIST_BEGIN_DRAG, self.OnDragInit, id=self.lc1.GetId())
        #self.Bind(wx.EVT_LIST_BEGIN_DRAG, self.OnDragInit2, id=self.lc2.GetId())
        self.Bind(wx.EVT_DROP_FILES,self.OnDrop, id=self.lc2.GetId())        
        #tree = self.dir.GetTreeCtrl()

        #splitter2.SplitHorizontally(self.lc1, self.lc2)
        #splitter1.SplitVertically(self.lc2, splitter2)

        #self.Bind(wx.EVT_TREE_SEL_CHANGED, self.OnSelect, id=tree.GetId())

        self.OnSelect(0)
        self.Centre()
        self.Show(True)

    def OnSelect(self, event):
        #list = os.listdir(self.dir.GetPath())
        self.lc1.ClearAll()
        self.lc2.ClearAll()
        list=['ciao','sono','fabio']
        for i in range(len(list)):
            self.lc1.InsertStringItem(0, list[i])

    def OnDrop(self,evt):
        print 'OnDrop'
    def OnDragInit(self, event):
        print 'OnDragInit'
        text = self.lc1.GetItemText(event.GetIndex())
        tdo = wx.TextDataObject(text)
        tds = wx.DropSource(self.lc1)
        tds.SetData(tdo)
        tds.DoDragDrop(True)
        #try:
        #    self.lc2.GetItemText(event.GetIndex())
        #except:pass
        #    self.lc1.DeleteItem(event.GetIndex())

    def OnDragInit2(self, event):
        print 'OnDragInit2'
        text = self.lc2.GetItemText(event.GetIndex())
        tdo = wx.TextDataObject(text)
        tds = wx.DropSource(self.lc2)
        tds.SetData(tdo)
        tds.DoDragDrop(True)
        self.lc2.DeleteItem(event.GetIndex())


app = wx.App()
DragDrop(None, -1, 'dragdrop.py')
app.MainLoop()
