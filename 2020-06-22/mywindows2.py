# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.grid

###########################################################################
## Class MyFrame1
###########################################################################

class MyFrame1 ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"XXX", pos = wx.DefaultPosition, size = wx.Size( 596,466 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		gSizer1 = wx.GridSizer( 0, 2, 0, 0 )

		self.m_button1 = wx.Button( self, wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.m_button1, 0, wx.ALL, 5 )

		self.m_textCtrl1 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		gSizer1.Add( self.m_textCtrl1, 0, wx.ALL, 5 )

		self.m_button2 = wx.Button( self, wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.m_button2, 0, wx.ALL, 5 )

		self.m_button3 = wx.Button( self, wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.m_button3, 0, wx.ALL, 5 )

		self.m_grid1 = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

		# Grid
		self.m_grid1.CreateGrid( 1, 1 )
		self.m_grid1.EnableEditing( True )
		self.m_grid1.EnableGridLines( True )
		self.m_grid1.EnableDragGridSize( False )
		self.m_grid1.SetMargins( 0, 0 )

		# Columns
		self.m_grid1.EnableDragColMove( False )
		self.m_grid1.EnableDragColSize( True )
		self.m_grid1.SetColLabelSize( 30 )
		self.m_grid1.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.m_grid1.EnableDragRowSize( True )
		self.m_grid1.SetRowLabelSize( 80 )
		self.m_grid1.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance

		# Cell Defaults
		self.m_grid1.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		gSizer1.Add( self.m_grid1, 0, wx.ALL, 5 )


		self.SetSizer( gSizer1 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_button1.Bind( wx.EVT_BUTTON, self.myclick )
		self.m_button2.Bind( wx.EVT_BUTTON, self.myclick2 )
		self.m_button3.Bind( wx.EVT_BUTTON, self.myclick3 )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def myclick( self, event ):
		event.Skip()

	def myclick2( self, event ):
		event.Skip()

	def myclick3( self, event ):
		event.Skip()


