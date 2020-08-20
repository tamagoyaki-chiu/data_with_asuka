# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.combo
import wx.aui
import wx.html
import wx.richtext
import wx.adv
import wx.grid

###########################################################################
## Class MyFrame1
###########################################################################

class MyFrame1 ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 433,444 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		fgSizer1 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer1.SetFlexibleDirection( wx.BOTH )
		fgSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )


		self.SetSizer( fgSizer1 )
		self.Layout()
		self.m_statusBar1 = self.CreateStatusBar( 1, wx.STB_SIZEGRIP, wx.ID_ANY )
		self.m_menubar1 = wx.MenuBar( 0 )
		self.m_menu1 = wx.Menu()
		self.m_menubar1.Append( self.m_menu1, u"檔案" )

		self.m_menu2 = wx.Menu()
		self.m_menuItem1 = wx.MenuItem( self.m_menu2, wx.ID_ANY, u"測試", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu2.Append( self.m_menuItem1 )
		self.m_menuItem1.Enable( False )

		self.m_menu2.AppendSeparator()

		self.m_menuItem2 = wx.MenuItem( self.m_menu2, wx.ID_ANY, u"MyMenuItem", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu2.Append( self.m_menuItem2 )

		self.m_menu11 = wx.Menu()
		self.m_menuItem3 = wx.MenuItem( self.m_menu11, wx.ID_ANY, u"MyMenuItem", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu11.Append( self.m_menuItem3 )

		self.m_menu2.AppendSubMenu( self.m_menu11, u"測試1" )

		self.m_menubar1.Append( self.m_menu2, u"編輯" )

		self.SetMenuBar( self.m_menubar1 )

		self.m_toolBar1 = self.CreateToolBar( wx.TB_HORIZONTAL, wx.ID_ANY )
		self.m_tool1 = self.m_toolBar1.AddLabelTool( wx.ID_ANY, u"tool", wx.Bitmap( u"windmill_gardening_icon_146734.ico", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None )

		self.m_toolBar1.Realize()


		self.Centre( wx.BOTH )

	def __del__( self ):
		pass


###########################################################################
## Class MyFrame2
###########################################################################

class MyFrame2 ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		self.m_notebook1 = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_panel5 = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		gSizer1 = wx.GridSizer( 0, 2, 0, 0 )

		self.m_textCtrl1 = wx.TextCtrl( self.m_panel5, wx.ID_ANY, u"aaa", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_textCtrl1.SetMaxLength( 5 )
		gSizer1.Add( self.m_textCtrl1, 0, wx.ALL, 5 )

		self.m_textCtrl2 = wx.TextCtrl( self.m_panel5, wx.ID_ANY, u"aaa\nbbb\nccc", wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE )
		gSizer1.Add( self.m_textCtrl2, 0, wx.ALL, 5 )

		self.m_bitmap1 = wx.StaticBitmap( self.m_panel5, wx.ID_ANY, wx.Bitmap( u"windmill_gardening_icon_146734.ico", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.m_bitmap1, 0, wx.ALL, 5 )


		self.m_panel5.SetSizer( gSizer1 )
		self.m_panel5.Layout()
		gSizer1.Fit( self.m_panel5 )
		self.m_notebook1.AddPage( self.m_panel5, u"a page", False )
		self.m_panel6 = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer3 = wx.BoxSizer( wx.VERTICAL )

		m_comboBox1Choices = [ u"aaa", u"bbb", u"ccc" ]
		self.m_comboBox1 = wx.ComboBox( self.m_panel6, wx.ID_ANY, u"a", wx.DefaultPosition, wx.DefaultSize, m_comboBox1Choices, 0 )
		bSizer3.Add( self.m_comboBox1, 0, wx.ALL, 5 )

		self.m_bcomboBox1 = wx.combo.BitmapComboBox( self.m_panel6, wx.ID_ANY, u"Combo!", wx.DefaultPosition, wx.DefaultSize, "", 0 )
		bSizer3.Add( self.m_bcomboBox1, 0, wx.ALL, 5 )

		m_choice2Choices = [ u"aaa", u"bbb" ]
		self.m_choice2 = wx.Choice( self.m_panel6, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice2Choices, 0 )
		self.m_choice2.SetSelection( 0 )
		bSizer3.Add( self.m_choice2, 0, wx.ALL, 5 )

		m_listBox1Choices = [ u"aaa", u"bbb", u"ccc" ]
		self.m_listBox1 = wx.ListBox( self.m_panel6, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_listBox1Choices, 0 )
		bSizer3.Add( self.m_listBox1, 0, wx.ALL, 5 )


		self.m_panel6.SetSizer( bSizer3 )
		self.m_panel6.Layout()
		bSizer3.Fit( self.m_panel6 )
		self.m_notebook1.AddPage( self.m_panel6, u"a page", False )
		self.m_panel7 = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		gSizer2 = wx.GridSizer( 0, 2, 0, 0 )

		self.m_checkBox1 = wx.CheckBox( self.m_panel7, wx.ID_ANY, u"Check Me!", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_checkBox1.SetValue(True)
		gSizer2.Add( self.m_checkBox1, 0, wx.ALL, 5 )

		self.m_checkBox2 = wx.CheckBox( self.m_panel7, wx.ID_ANY, u"Check Me!", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer2.Add( self.m_checkBox2, 0, wx.ALL, 5 )

		m_radioBox2Choices = [ u"Radio Button", u"aaa", u"bbb" ]
		self.m_radioBox2 = wx.RadioBox( self.m_panel7, wx.ID_ANY, u"wxRadioBox", wx.DefaultPosition, wx.DefaultSize, m_radioBox2Choices, 1, wx.RA_SPECIFY_COLS )
		self.m_radioBox2.SetSelection( 1 )
		gSizer2.Add( self.m_radioBox2, 0, wx.ALL, 5 )


		self.m_panel7.SetSizer( gSizer2 )
		self.m_panel7.Layout()
		gSizer2.Fit( self.m_panel7 )
		self.m_notebook1.AddPage( self.m_panel7, u"a page", True )
		self.m_scrolledWindow2 = wx.ScrolledWindow( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.HSCROLL|wx.VSCROLL )
		self.m_scrolledWindow2.SetScrollRate( 5, 5 )
		gSizer3 = wx.GridSizer( 0, 2, 0, 0 )

		self.m_panel10 = wx.Panel( self.m_scrolledWindow2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer4 = wx.BoxSizer( wx.VERTICAL )

		self.m_radioBtn6 = wx.RadioButton( self.m_panel10, wx.ID_ANY, u"RadioBtn", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer4.Add( self.m_radioBtn6, 0, wx.ALL, 5 )

		self.m_radioBtn7 = wx.RadioButton( self.m_panel10, wx.ID_ANY, u"RadioBtn", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer4.Add( self.m_radioBtn7, 0, wx.ALL, 5 )

		self.m_radioBtn8 = wx.RadioButton( self.m_panel10, wx.ID_ANY, u"RadioBtn", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer4.Add( self.m_radioBtn8, 0, wx.ALL, 5 )


		self.m_panel10.SetSizer( bSizer4 )
		self.m_panel10.Layout()
		bSizer4.Fit( self.m_panel10 )
		gSizer3.Add( self.m_panel10, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_panel111 = wx.Panel( self.m_scrolledWindow2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer5 = wx.BoxSizer( wx.VERTICAL )

		self.m_radioBtn9 = wx.RadioButton( self.m_panel111, wx.ID_ANY, u"RadioBtn", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer5.Add( self.m_radioBtn9, 0, wx.ALL, 5 )

		self.m_radioBtn10 = wx.RadioButton( self.m_panel111, wx.ID_ANY, u"RadioBtn", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer5.Add( self.m_radioBtn10, 0, wx.ALL, 5 )

		self.m_staticline1 = wx.StaticLine( self.m_panel111, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer5.Add( self.m_staticline1, 0, wx.EXPAND |wx.ALL, 5 )


		self.m_panel111.SetSizer( bSizer5 )
		self.m_panel111.Layout()
		bSizer5.Fit( self.m_panel111 )
		gSizer3.Add( self.m_panel111, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_slider1 = wx.Slider( self.m_scrolledWindow2, wx.ID_ANY, 100, 0, 1000, wx.DefaultPosition, wx.DefaultSize, wx.SL_HORIZONTAL )
		gSizer3.Add( self.m_slider1, 0, wx.ALL, 5 )

		self.m_gauge1 = wx.Gauge( self.m_scrolledWindow2, wx.ID_ANY, 100, wx.DefaultPosition, wx.DefaultSize, wx.GA_HORIZONTAL )
		self.m_gauge1.SetValue( 80 )
		gSizer3.Add( self.m_gauge1, 0, wx.ALL, 5 )


		self.m_scrolledWindow2.SetSizer( gSizer3 )
		self.m_scrolledWindow2.Layout()
		gSizer3.Fit( self.m_scrolledWindow2 )
		self.m_notebook1.AddPage( self.m_scrolledWindow2, u"a page", False )

		bSizer1.Add( self.m_notebook1, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_auinotebook1 = wx.aui.AuiNotebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.aui.AUI_NB_DEFAULT_STYLE )
		self.m_panel11 = wx.Panel( self.m_auinotebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_auinotebook1.AddPage( self.m_panel11, u"a page", False, wx.NullBitmap )
		self.m_panel12 = wx.Panel( self.m_auinotebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_auinotebook1.AddPage( self.m_panel12, u"a page", True, wx.NullBitmap )
		self.m_panel13 = wx.Panel( self.m_auinotebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_auinotebook1.AddPage( self.m_panel13, u"a page", False, wx.NullBitmap )

		bSizer1.Add( self.m_auinotebook1, 1, wx.EXPAND |wx.ALL, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()

		self.Centre( wx.BOTH )

	def __del__( self ):
		pass


###########################################################################
## Class MyFrame3
###########################################################################

class MyFrame3 ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,463 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer2 = wx.BoxSizer( wx.VERTICAL )

		self.m_listbook1 = wx.Listbook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LB_DEFAULT )
		self.m_scrolledWindow3 = wx.ScrolledWindow( self.m_listbook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.HSCROLL|wx.VSCROLL )
		self.m_scrolledWindow3.SetScrollRate( 5, 5 )
		gSizer4 = wx.GridSizer( 0, 2, 0, 0 )

		self.m_htmlWin2 = wx.html.HtmlWindow( self.m_scrolledWindow3, wx.ID_ANY, wx.DefaultPosition, wx.Size( 100,100 ), wx.html.HW_SCROLLBAR_AUTO )
		gSizer4.Add( self.m_htmlWin2, 0, wx.ALL, 5 )

		self.m_richText1 = wx.richtext.RichTextCtrl( self.m_scrolledWindow3, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0|wx.VSCROLL|wx.HSCROLL|wx.NO_BORDER|wx.WANTS_CHARS )
		gSizer4.Add( self.m_richText1, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_toggleBtn1 = wx.ToggleButton( self.m_scrolledWindow3, wx.ID_ANY, u"Toggle me!", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer4.Add( self.m_toggleBtn1, 0, wx.ALL, 5 )

		self.m_searchCtrl2 = wx.SearchCtrl( self.m_scrolledWindow3, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_searchCtrl2.ShowSearchButton( True )
		self.m_searchCtrl2.ShowCancelButton( False )
		gSizer4.Add( self.m_searchCtrl2, 0, wx.ALL, 5 )

		self.m_colourPicker1 = wx.ColourPickerCtrl( self.m_scrolledWindow3, wx.ID_ANY, wx.BLACK, wx.DefaultPosition, wx.DefaultSize, wx.CLRP_DEFAULT_STYLE )
		gSizer4.Add( self.m_colourPicker1, 0, wx.ALL, 5 )

		self.m_fontPicker1 = wx.FontPickerCtrl( self.m_scrolledWindow3, wx.ID_ANY, wx.NullFont, wx.DefaultPosition, wx.DefaultSize, wx.FNTP_DEFAULT_STYLE )
		self.m_fontPicker1.SetMaxPointSize( 100 )
		gSizer4.Add( self.m_fontPicker1, 0, wx.ALL, 5 )

		self.m_filePicker1 = wx.FilePickerCtrl( self.m_scrolledWindow3, wx.ID_ANY, u"D:\\python\\mywindows.py", u"Select a file", u"*.*", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE )
		gSizer4.Add( self.m_filePicker1, 0, wx.ALL, 5 )

		self.m_dirPicker1 = wx.DirPickerCtrl( self.m_scrolledWindow3, wx.ID_ANY, u"D:\\python", u"Select a folder", wx.DefaultPosition, wx.DefaultSize, wx.DIRP_DEFAULT_STYLE )
		gSizer4.Add( self.m_dirPicker1, 0, wx.ALL, 5 )

		self.m_datePicker1 = wx.adv.DatePickerCtrl( self.m_scrolledWindow3, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.DefaultSize, wx.adv.DP_DEFAULT )
		gSizer4.Add( self.m_datePicker1, 0, wx.ALL, 5 )

		self.m_calendar1 = wx.adv.CalendarCtrl( self.m_scrolledWindow3, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.DefaultSize, wx.adv.CAL_SHOW_HOLIDAYS )
		gSizer4.Add( self.m_calendar1, 0, wx.ALL, 5 )


		self.m_scrolledWindow3.SetSizer( gSizer4 )
		self.m_scrolledWindow3.Layout()
		gSizer4.Fit( self.m_scrolledWindow3 )
		self.m_listbook1.AddPage( self.m_scrolledWindow3, u"a page", False )
		self.m_scrolledWindow4 = wx.ScrolledWindow( self.m_listbook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.HSCROLL|wx.VSCROLL )
		self.m_scrolledWindow4.SetScrollRate( 5, 5 )
		gSizer5 = wx.GridSizer( 0, 2, 0, 0 )

		self.m_scrollBar1 = wx.ScrollBar( self.m_scrolledWindow4, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.SB_HORIZONTAL )
		gSizer5.Add( self.m_scrollBar1, 0, wx.ALL, 5 )

		self.m_spinCtrl1 = wx.SpinCtrl( self.m_scrolledWindow4, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 10, 2 )
		gSizer5.Add( self.m_spinCtrl1, 0, wx.ALL, 5 )

		self.m_spinCtrlDouble2 = wx.SpinCtrlDouble( self.m_scrolledWindow4, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 100, 4.000000, 1 )
		self.m_spinCtrlDouble2.SetDigits( 0 )
		gSizer5.Add( self.m_spinCtrlDouble2, 0, wx.ALL, 5 )

		self.m_spinBtn1 = wx.SpinButton( self.m_scrolledWindow4, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer5.Add( self.m_spinBtn1, 0, wx.ALL, 5 )

		self.m_hyperlink1 = wx.adv.HyperlinkCtrl( self.m_scrolledWindow4, wx.ID_ANY, u"xxx", u"http://teaching.bo-yuan.net/", wx.DefaultPosition, wx.DefaultSize, wx.adv.HL_DEFAULT_STYLE )
		gSizer5.Add( self.m_hyperlink1, 0, wx.ALL, 5 )

		self.m_genericDirCtrl2 = wx.GenericDirCtrl( self.m_scrolledWindow4, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.DIRCTRL_3D_INTERNAL|wx.SUNKEN_BORDER, wx.EmptyString, 0 )

		self.m_genericDirCtrl2.ShowHidden( False )
		gSizer5.Add( self.m_genericDirCtrl2, 1, wx.EXPAND |wx.ALL, 5 )


		self.m_scrolledWindow4.SetSizer( gSizer5 )
		self.m_scrolledWindow4.Layout()
		gSizer5.Fit( self.m_scrolledWindow4 )
		self.m_listbook1.AddPage( self.m_scrolledWindow4, u"a page", False )
		self.m_scrolledWindow5 = wx.ScrolledWindow( self.m_listbook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.HSCROLL|wx.VSCROLL )
		self.m_scrolledWindow5.SetScrollRate( 5, 5 )
		gSizer6 = wx.GridSizer( 0, 2, 0, 0 )

		self.m_treeCtrl1 = wx.TreeCtrl( self.m_scrolledWindow5, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TR_DEFAULT_STYLE )
		gSizer6.Add( self.m_treeCtrl1, 0, wx.ALL, 5 )

		self.m_grid1 = wx.grid.Grid( self.m_scrolledWindow5, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

		# Grid
		self.m_grid1.CreateGrid( 5, 5 )
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
		gSizer6.Add( self.m_grid1, 0, wx.ALL, 5 )

		m_checkList2Choices = [u"aaa", u"bbb", u"ccc"]
		self.m_checkList2 = wx.CheckListBox( self.m_scrolledWindow5, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_checkList2Choices, 0 )
		gSizer6.Add( self.m_checkList2, 0, wx.ALL, 5 )


		self.m_scrolledWindow5.SetSizer( gSizer6 )
		self.m_scrolledWindow5.Layout()
		gSizer6.Fit( self.m_scrolledWindow5 )
		self.m_listbook1.AddPage( self.m_scrolledWindow5, u"a page", True )

		bSizer2.Add( self.m_listbook1, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_choicebook1 = wx.Choicebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.CHB_DEFAULT )
		self.m_panel8 = wx.Panel( self.m_choicebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_choicebook1.AddPage( self.m_panel8, u"a page", True )
		self.m_panel9 = wx.Panel( self.m_choicebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_choicebook1.AddPage( self.m_panel9, u"a page", False )
		self.m_panel10 = wx.Panel( self.m_choicebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_choicebook1.AddPage( self.m_panel10, u"a page", False )
		bSizer2.Add( self.m_choicebook1, 1, wx.EXPAND |wx.ALL, 5 )


		self.SetSizer( bSizer2 )
		self.Layout()
		self.m_timer1 = wx.Timer()
		self.m_timer1.SetOwner( self, wx.ID_ANY )

		self.Centre( wx.BOTH )

	def __del__( self ):
		pass


