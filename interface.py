# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class mainFramee
###########################################################################

class mainFramee ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Sistem Coffie Toffie", pos = wx.DefaultPosition, size = wx.Size( 573,484 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		mainSizer = wx.BoxSizer( wx.VERTICAL )

		self.m_notebook1 = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Home = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.Home.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVECAPTION ) )

		bSizer6 = wx.BoxSizer( wx.VERTICAL )


		bSizer6.Add( ( 0, 0), 1, 0, 5 )

		self.m_staticText6 = wx.StaticText( self.Home, wx.ID_ANY, u"Selamat Datang di Coffie Toffie", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText6.Wrap( -1 )

		self.m_staticText6.SetFont( wx.Font( 20, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Britannic Bold" ) )

		bSizer6.Add( self.m_staticText6, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer6.Add( ( 0, 0), 1, 0, 5 )


		self.Home.SetSizer( bSizer6 )
		self.Home.Layout()
		bSizer6.Fit( self.Home )
		self.m_notebook1.AddPage( self.Home, u"Home", False )
		self.Menu = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.Menu.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVECAPTION ) )

		bSizer51 = wx.BoxSizer( wx.VERTICAL )

		self.m_notebook = wx.Notebook( self.Menu, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Food = wx.Panel( self.m_notebook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer52 = wx.BoxSizer( wx.VERTICAL )

		self.mainPanel1 = wx.Panel( self.Food, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer31 = wx.BoxSizer( wx.VERTICAL )

		bSizer41 = wx.BoxSizer( wx.HORIZONTAL )


		bSizer41.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.limitData1 = wx.SpinCtrl( self.mainPanel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS|wx.SP_WRAP, 1, 100000, 10 )
		self.limitData1.SetMinSize( wx.Size( 70,-1 ) )

		bSizer41.Add( self.limitData1, 0, wx.ALL, 5 )

		self.btnAddDataFood = wx.Button( self.mainPanel1, wx.ID_ANY, u"Tambah Data", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer41.Add( self.btnAddDataFood, 0, wx.ALL, 5 )

		self.btnGetFood = wx.Button( self.mainPanel1, wx.ID_ANY, u"Menu Makanan", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer41.Add( self.btnGetFood, 0, wx.ALL, 5 )

		self.btnEditFood = wx.Button( self.mainPanel1, wx.ID_ANY, u"Edit", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer41.Add( self.btnEditFood, 0, wx.ALL, 5 )

		self.btnDeleteFood = wx.Button( self.mainPanel1, wx.ID_ANY, u"Delete", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer41.Add( self.btnDeleteFood, 0, wx.ALL, 5 )


		bSizer41.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer31.Add( bSizer41, 0, wx.EXPAND, 5 )

		fgSizer21 = wx.FlexGridSizer( 0, 2, 1, 5 )
		fgSizer21.SetFlexibleDirection( wx.HORIZONTAL )
		fgSizer21.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_ALL )

		self.listCtrlFood = wx.ListCtrl( self.mainPanel1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_AUTOARRANGE|wx.LC_REPORT )
		self.listCtrlFood.SetMinSize( wx.Size( 540,380 ) )

		fgSizer21.Add( self.listCtrlFood, 0, wx.ALL, 5 )


		bSizer31.Add( fgSizer21, 0, wx.EXPAND, 5 )


		self.mainPanel1.SetSizer( bSizer31 )
		self.mainPanel1.Layout()
		bSizer31.Fit( self.mainPanel1 )
		bSizer52.Add( self.mainPanel1, 1, wx.EXPAND |wx.ALL, 5 )


		self.Food.SetSizer( bSizer52 )
		self.Food.Layout()
		bSizer52.Fit( self.Food )
		self.m_notebook.AddPage( self.Food, u"Food", False )
		self.Drink = wx.Panel( self.m_notebook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer521 = wx.BoxSizer( wx.VERTICAL )

		self.mainPanel11 = wx.Panel( self.Drink, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer311 = wx.BoxSizer( wx.VERTICAL )

		bSizer411 = wx.BoxSizer( wx.HORIZONTAL )


		bSizer411.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.limitData = wx.SpinCtrl( self.mainPanel11, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS|wx.SP_WRAP, 1, 100000, 10 )
		self.limitData.SetMinSize( wx.Size( 70,-1 ) )

		bSizer411.Add( self.limitData, 0, wx.ALL, 5 )

		self.btnAddDataDrink = wx.Button( self.mainPanel11, wx.ID_ANY, u"Tambah Data", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer411.Add( self.btnAddDataDrink, 0, wx.ALL, 5 )

		self.btnGetDrink = wx.Button( self.mainPanel11, wx.ID_ANY, u"Menu Minuman", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer411.Add( self.btnGetDrink, 0, wx.ALL, 5 )

		self.btnEditDrink = wx.Button( self.mainPanel11, wx.ID_ANY, u"Edit", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer411.Add( self.btnEditDrink, 0, wx.ALL, 5 )

		self.btnDeleteDrink = wx.Button( self.mainPanel11, wx.ID_ANY, u"Delete", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer411.Add( self.btnDeleteDrink, 0, wx.ALL, 5 )


		bSizer411.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer311.Add( bSizer411, 0, wx.EXPAND, 5 )

		fgSizer211 = wx.FlexGridSizer( 0, 2, 1, 5 )
		fgSizer211.SetFlexibleDirection( wx.HORIZONTAL )
		fgSizer211.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_ALL )

		self.listCtrlDrink = wx.ListCtrl( self.mainPanel11, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_AUTOARRANGE|wx.LC_REPORT )
		self.listCtrlDrink.SetMinSize( wx.Size( 540,380 ) )

		fgSizer211.Add( self.listCtrlDrink, 0, wx.ALL, 5 )


		bSizer311.Add( fgSizer211, 0, wx.EXPAND, 5 )


		self.mainPanel11.SetSizer( bSizer311 )
		self.mainPanel11.Layout()
		bSizer311.Fit( self.mainPanel11 )
		bSizer521.Add( self.mainPanel11, 1, wx.EXPAND |wx.ALL, 5 )


		self.Drink.SetSizer( bSizer521 )
		self.Drink.Layout()
		bSizer521.Fit( self.Drink )
		self.m_notebook.AddPage( self.Drink, u"Drink", True )
		self.Snack = wx.Panel( self.m_notebook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer522 = wx.BoxSizer( wx.VERTICAL )

		self.mainPanel12 = wx.Panel( self.Snack, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer312 = wx.BoxSizer( wx.VERTICAL )

		bSizer412 = wx.BoxSizer( wx.HORIZONTAL )


		bSizer412.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.limitData = wx.SpinCtrl( self.mainPanel12, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS|wx.SP_WRAP, 1, 100000, 10 )
		self.limitData.SetMinSize( wx.Size( 70,-1 ) )

		bSizer412.Add( self.limitData, 0, wx.ALL, 5 )

		self.btnAddDataSnack = wx.Button( self.mainPanel12, wx.ID_ANY, u"Tambah Data", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer412.Add( self.btnAddDataSnack, 0, wx.ALL, 5 )

		self.btnGetSnack = wx.Button( self.mainPanel12, wx.ID_ANY, u"Menu Snack", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer412.Add( self.btnGetSnack, 0, wx.ALL, 5 )

		self.btnEditSnack = wx.Button( self.mainPanel12, wx.ID_ANY, u"Edit", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer412.Add( self.btnEditSnack, 0, wx.ALL, 5 )

		self.btnDeleteSnack = wx.Button( self.mainPanel12, wx.ID_ANY, u"Delete", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer412.Add( self.btnDeleteSnack, 0, wx.ALL, 5 )


		bSizer412.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer312.Add( bSizer412, 0, wx.EXPAND, 5 )

		fgSizer212 = wx.FlexGridSizer( 0, 2, 1, 5 )
		fgSizer212.SetFlexibleDirection( wx.HORIZONTAL )
		fgSizer212.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_ALL )

		self.listCtrlSnack = wx.ListCtrl( self.mainPanel12, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_AUTOARRANGE|wx.LC_REPORT )
		self.listCtrlSnack.SetMinSize( wx.Size( 540,380 ) )

		fgSizer212.Add( self.listCtrlSnack, 0, wx.ALL, 5 )


		bSizer312.Add( fgSizer212, 0, wx.EXPAND, 5 )


		self.mainPanel12.SetSizer( bSizer312 )
		self.mainPanel12.Layout()
		bSizer312.Fit( self.mainPanel12 )
		bSizer522.Add( self.mainPanel12, 1, wx.EXPAND |wx.ALL, 5 )


		self.Snack.SetSizer( bSizer522 )
		self.Snack.Layout()
		bSizer522.Fit( self.Snack )
		self.m_notebook.AddPage( self.Snack, u"Snack", False )

		bSizer51.Add( self.m_notebook, 1, wx.EXPAND |wx.ALL, 5 )


		self.Menu.SetSizer( bSizer51 )
		self.Menu.Layout()
		bSizer51.Fit( self.Menu )
		self.m_notebook1.AddPage( self.Menu, u"Menu", True )
		self.DaftarTransaksi = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.DaftarTransaksi.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVECAPTION ) )

		bSizer5 = wx.BoxSizer( wx.VERTICAL )

		self.mainPanel = wx.Panel( self.DaftarTransaksi, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer3 = wx.BoxSizer( wx.VERTICAL )

		bSizer4 = wx.BoxSizer( wx.HORIZONTAL )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.limitData = wx.SpinCtrl( self.mainPanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS|wx.SP_WRAP, 1, 100000, 10 )
		self.limitData.SetMinSize( wx.Size( 70,-1 ) )

		bSizer4.Add( self.limitData, 0, wx.ALL, 5 )

		self.btnAddDataTransaksi = wx.Button( self.mainPanel, wx.ID_ANY, u"Tambah Data", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer4.Add( self.btnAddDataTransaksi, 0, wx.ALL, 5 )

		self.btnGetTransaksi = wx.Button( self.mainPanel, wx.ID_ANY, u"Riwayat Transaksi", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer4.Add( self.btnGetTransaksi, 0, wx.ALL, 5 )

		self.btnEditTransaksi = wx.Button( self.mainPanel, wx.ID_ANY, u"Edit", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer4.Add( self.btnEditTransaksi, 0, wx.ALL, 5 )

		self.btnDeleteTransaksi = wx.Button( self.mainPanel, wx.ID_ANY, u"Delete", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer4.Add( self.btnDeleteTransaksi, 0, wx.ALL, 5 )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer3.Add( bSizer4, 0, wx.EXPAND, 5 )

		fgSizer2 = wx.FlexGridSizer( 0, 2, 1, 5 )
		fgSizer2.SetFlexibleDirection( wx.HORIZONTAL )
		fgSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_ALL )

		self.listCtrlTransaksi = wx.ListCtrl( self.mainPanel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_AUTOARRANGE|wx.LC_REPORT )
		self.listCtrlTransaksi.SetMinSize( wx.Size( 540,380 ) )

		fgSizer2.Add( self.listCtrlTransaksi, 0, wx.ALL, 5 )


		bSizer3.Add( fgSizer2, 0, wx.EXPAND, 5 )


		self.mainPanel.SetSizer( bSizer3 )
		self.mainPanel.Layout()
		bSizer3.Fit( self.mainPanel )
		bSizer5.Add( self.mainPanel, 1, wx.EXPAND |wx.ALL, 5 )


		self.DaftarTransaksi.SetSizer( bSizer5 )
		self.DaftarTransaksi.Layout()
		bSizer5.Fit( self.DaftarTransaksi )
		self.m_notebook1.AddPage( self.DaftarTransaksi, u"Daftar Transaksi", False )
		self.About = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.About.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVECAPTION ) )

		bSizer16 = wx.BoxSizer( wx.VERTICAL )


		bSizer16.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_staticText15 = wx.StaticText( self.About, wx.ID_ANY, u"Hubungi Kami", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText15.Wrap( -1 )

		self.m_staticText15.SetFont( wx.Font( 36, wx.FONTFAMILY_DECORATIVE, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Bauhaus 93" ) )

		bSizer16.Add( self.m_staticText15, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_staticText16 = wx.StaticText( self.About, wx.ID_ANY, u"IG : @Coffie_Toffie", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText16.Wrap( -1 )

		self.m_staticText16.SetFont( wx.Font( 20, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Berlin Sans FB" ) )

		bSizer16.Add( self.m_staticText16, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_staticText17 = wx.StaticText( self.About, wx.ID_ANY, u"Jl. Sumater, Jember", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText17.Wrap( -1 )

		self.m_staticText17.SetFont( wx.Font( 20, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Berlin Sans FB" ) )

		bSizer16.Add( self.m_staticText17, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_staticText18 = wx.StaticText( self.About, wx.ID_ANY, u"Buka Tiap Hari dari 19.00", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText18.Wrap( -1 )

		self.m_staticText18.SetFont( wx.Font( 22, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Berlin Sans FB" ) )

		bSizer16.Add( self.m_staticText18, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_staticText19 = wx.StaticText( self.About, wx.ID_ANY, u"Tutup : 00.00", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText19.Wrap( -1 )

		self.m_staticText19.SetFont( wx.Font( 22, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Berlin Sans FB" ) )

		bSizer16.Add( self.m_staticText19, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer16.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer16.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		self.About.SetSizer( bSizer16 )
		self.About.Layout()
		bSizer16.Fit( self.About )
		self.m_notebook1.AddPage( self.About, u"About", False )

		mainSizer.Add( self.m_notebook1, 1, wx.EXPAND |wx.ALL, 5 )


		self.SetSizer( mainSizer )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.btnAddDataFood.Bind( wx.EVT_BUTTON, self.handleBtnAddDataFood )
		self.btnGetFood.Bind( wx.EVT_BUTTON, self.handleBtnGetFood )
		self.btnEditFood.Bind( wx.EVT_BUTTON, self.handleBtnEditFood )
		self.btnDeleteFood.Bind( wx.EVT_BUTTON, self.handleBtnDeleteFood )
		self.listCtrlFood.Bind( wx.EVT_LIST_ITEM_SELECTED, self.handleSelectedItemFood )
		self.btnAddDataDrink.Bind( wx.EVT_BUTTON, self.handleBtnAddDataDrink )
		self.btnGetDrink.Bind( wx.EVT_BUTTON, self.handleBtnGetDrink )
		self.btnEditDrink.Bind( wx.EVT_BUTTON, self.handleBtnEditDrink )
		self.btnDeleteDrink.Bind( wx.EVT_BUTTON, self.handleBtnDeleteDrink )
		self.listCtrlDrink.Bind( wx.EVT_LIST_ITEM_SELECTED, self.handleSelectedItemDrink )
		self.btnAddDataSnack.Bind( wx.EVT_BUTTON, self.handleBtnAddDataSnack )
		self.btnGetSnack.Bind( wx.EVT_BUTTON, self.handleBtnGetSnack )
		self.btnEditSnack.Bind( wx.EVT_BUTTON, self.handleBtnEditSnack )
		self.btnDeleteSnack.Bind( wx.EVT_BUTTON, self.handleBtnDeleteSnack )
		self.listCtrlSnack.Bind( wx.EVT_LIST_ITEM_SELECTED, self.handleSelectedItemSnack )
		self.btnAddDataTransaksi.Bind( wx.EVT_BUTTON, self.handleBtnAddDataTransaksi )
		self.btnGetTransaksi.Bind( wx.EVT_BUTTON, self.handleBtnGetTransaksi )
		self.btnEditTransaksi.Bind( wx.EVT_BUTTON, self.handleBtnEditTransaksi )
		self.btnDeleteTransaksi.Bind( wx.EVT_BUTTON, self.handleBtnDeleteTransaksi )
		self.listCtrlTransaksi.Bind( wx.EVT_LIST_ITEM_SELECTED, self.handleSelectedItemTransaksi )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def handleBtnAddDataFood( self, event ):
		event.Skip()

	def handleBtnGetFood( self, event ):
		event.Skip()

	def handleBtnEditFood( self, event ):
		event.Skip()

	def handleBtnDeleteFood( self, event ):
		event.Skip()

	def handleSelectedItemFood( self, event ):
		event.Skip()

	def handleBtnAddDataDrink( self, event ):
		event.Skip()

	def handleBtnGetDrink( self, event ):
		event.Skip()

	def handleBtnEditDrink( self, event ):
		event.Skip()

	def handleBtnDeleteDrink( self, event ):
		event.Skip()

	def handleSelectedItemDrink( self, event ):
		event.Skip()

	def handleBtnAddDataSnack( self, event ):
		event.Skip()

	def handleBtnGetSnack( self, event ):
		event.Skip()

	def handleBtnEditSnack( self, event ):
		event.Skip()

	def handleBtnDeleteSnack( self, event ):
		event.Skip()

	def handleSelectedItemSnack( self, event ):
		event.Skip()

	def handleBtnAddDataTransaksi( self, event ):
		event.Skip()

	def handleBtnGetTransaksi( self, event ):
		event.Skip()

	def handleBtnEditTransaksi( self, event ):
		event.Skip()

	def handleBtnDeleteTransaksi( self, event ):
		event.Skip()

	def handleSelectedItemTransaksi( self, event ):
		event.Skip()


###########################################################################
## Class createTransaksiFrame
###########################################################################

class createTransaksiFrame ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Data Transaksi", pos = wx.DefaultPosition, size = wx.Size( 432,364 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )

		gSizer2 = wx.GridSizer( 5, 2, 1, 15 )

		self.labelName = wx.StaticText( self, wx.ID_ANY, u"Nama Menu", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelName.Wrap( -1 )

		gSizer2.Add( self.labelName, 0, wx.ALL, 5 )

		self.textCtrlNamaMenu = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer2.Add( self.textCtrlNamaMenu, 1, wx.ALL, 5 )

		self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"Jumlah", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )

		gSizer2.Add( self.m_staticText3, 0, wx.ALL, 5 )

		self.textCtrlJumlah = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer2.Add( self.textCtrlJumlah, 1, wx.ALL, 5 )

		self.m_staticText4 = wx.StaticText( self, wx.ID_ANY, u"Harga", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4.Wrap( -1 )

		gSizer2.Add( self.m_staticText4, 0, wx.ALL, 5 )

		self.textCtrlHarga = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer2.Add( self.textCtrlHarga, 1, wx.ALL, 5 )

		self.m_staticText4 = wx.StaticText( self, wx.ID_ANY, u"Total", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4.Wrap( -1 )

		gSizer2.Add( self.m_staticText4, 0, wx.ALL, 5 )

		self.textCtrlTotal = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer2.Add( self.textCtrlTotal, 0, wx.ALL, 5 )


		gSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.btnSave = wx.Button( self, wx.ID_ANY, u"Save", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer2.Add( self.btnSave, 0, wx.ALL, 5 )


		self.SetSizer( gSizer2 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.btnSave.Bind( wx.EVT_BUTTON, self.handleBtnSave )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def handleBtnSave( self, event ):
		event.Skip()


###########################################################################
## Class createMakananFrame
###########################################################################

class createMakananFrame ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Data Makanan", pos = wx.DefaultPosition, size = wx.Size( 432,364 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )

		gSizer2 = wx.GridSizer( 5, 2, 1, 15 )

		self.labelName = wx.StaticText( self, wx.ID_ANY, u"Nama Makanan", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelName.Wrap( -1 )

		gSizer2.Add( self.labelName, 0, wx.ALL, 5 )

		self.textCtrlNamaMakanan = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer2.Add( self.textCtrlNamaMakanan, 1, wx.ALL, 5 )

		self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"Stock", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )

		gSizer2.Add( self.m_staticText3, 0, wx.ALL, 5 )

		self.textCtrlStock = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer2.Add( self.textCtrlStock, 1, wx.ALL, 5 )

		self.m_staticText41 = wx.StaticText( self, wx.ID_ANY, u"Harga", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText41.Wrap( -1 )

		gSizer2.Add( self.m_staticText41, 0, wx.ALL, 5 )

		self.textCtrlHargaMakanan = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer2.Add( self.textCtrlHargaMakanan, 1, wx.ALL, 5 )


		gSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.btnSave = wx.Button( self, wx.ID_ANY, u"Save", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer2.Add( self.btnSave, 0, wx.ALL, 5 )


		self.SetSizer( gSizer2 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.btnSave.Bind( wx.EVT_BUTTON, self.handleBtnSaveMakanan )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def handleBtnSaveMakanan( self, event ):
		event.Skip()


###########################################################################
## Class createMinumanFrame
###########################################################################

class createMinumanFrame ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Data Minuman", pos = wx.DefaultPosition, size = wx.Size( 432,364 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )

		gSizer2 = wx.GridSizer( 5, 2, 1, 15 )

		self.labelName = wx.StaticText( self, wx.ID_ANY, u"Nama Minuman", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelName.Wrap( -1 )

		gSizer2.Add( self.labelName, 0, wx.ALL, 5 )

		self.textCtrlNamaMinuman = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer2.Add( self.textCtrlNamaMinuman, 1, wx.ALL, 5 )

		self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"Stock", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )

		gSizer2.Add( self.m_staticText3, 0, wx.ALL, 5 )

		self.textCtrlStock = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer2.Add( self.textCtrlStock, 1, wx.ALL, 5 )

		self.m_staticText41 = wx.StaticText( self, wx.ID_ANY, u"Harga", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText41.Wrap( -1 )

		gSizer2.Add( self.m_staticText41, 0, wx.ALL, 5 )

		self.textCtrlHargaMinuman = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer2.Add( self.textCtrlHargaMinuman, 1, wx.ALL, 5 )


		gSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.btnSave = wx.Button( self, wx.ID_ANY, u"Save", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer2.Add( self.btnSave, 0, wx.ALL, 5 )


		self.SetSizer( gSizer2 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.btnSave.Bind( wx.EVT_BUTTON, self.handleBtnSaveMinuman )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def handleBtnSaveMinuman( self, event ):
		event.Skip()


###########################################################################
## Class createSnackFrame
###########################################################################

class createSnackFrame ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Data Snack", pos = wx.DefaultPosition, size = wx.Size( 432,364 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )

		gSizer2 = wx.GridSizer( 5, 2, 1, 15 )

		self.labelName = wx.StaticText( self, wx.ID_ANY, u"Nama Snack", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelName.Wrap( -1 )

		gSizer2.Add( self.labelName, 0, wx.ALL, 5 )

		self.textCtrlNamaSnack = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer2.Add( self.textCtrlNamaSnack, 1, wx.ALL, 5 )

		self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"Stock", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )

		gSizer2.Add( self.m_staticText3, 0, wx.ALL, 5 )

		self.textCtrlStock = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer2.Add( self.textCtrlStock, 1, wx.ALL, 5 )

		self.m_staticText41 = wx.StaticText( self, wx.ID_ANY, u"Harga", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText41.Wrap( -1 )

		gSizer2.Add( self.m_staticText41, 0, wx.ALL, 5 )

		self.textCtrlHargaSnack = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer2.Add( self.textCtrlHargaSnack, 1, wx.ALL, 5 )


		gSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.btnSave = wx.Button( self, wx.ID_ANY, u"Save", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer2.Add( self.btnSave, 0, wx.ALL, 5 )


		self.SetSizer( gSizer2 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.btnSave.Bind( wx.EVT_BUTTON, self.handleBtnSaveSnack )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def handleBtnSaveSnack( self, event ):
		event.Skip()


