
import wx
import wx.grid
import interface
from models import transaksi
from models import foodd
from models import snackk
from models import drinkk
from models import dbsqlite
from createFrame import createFrameTransaksii
from createFood import createFrameFood
from createSnack import  createFrameSnack
from createDrink import createFrameDrink

# Implementing mainFrame Transaksi
class mainFrame( interface.mainFramee ):
	def __init__( self, parent ):
		interface.mainFramee.__init__( self, parent )
		self.TransaksiModel = transaksi.Transaksi()
		self.FoodModel = foodd.Food()
		self.DrinkModel = drinkk.Drink()
		self.SnackModel = snackk.Snack()
		self.selectedSnack = None
		self.selectedFood = None
		self.selectedDrink = None
		self.selectedTransaksi = None
		self.columns = ['ID', 'Nama Menu', 'Jumlah', 'Harga', 'Total']
		self.columnsFood = ['ID', 'Nama Makanan', 'Stock', 'Harga']
		self.columnsDrink = ['ID', 'Nama Minuman', 'Stock', 'Harga']
		self.columnsSnack = ['ID', 'Nama Snack', 'Stock', 'Harga']
		self.initColumnsTransaksi()
		self.initColumnsFood()
		self.initColumnsDrink()
		self.initColumnsSnack()
		# self.btnEdit.Disable()
		# self.btnDelete.Disable()
		self.limitData.SetValue(100)

	def clearListTransaksi(self):
		self.listCtrlTransaksi.ClearAll()
		self.initColumnsTransaksi()
		
	def clearListFood(self):
		self.listCtrlFood.ClearAll()
		self.initColumnsFood()

	def clearListDrink(self):
		self.listCtrlDrink.ClearAll()
		self.initColumnsDrink()
	
	def clearListSnack(self):
		self.listCtrlSnack.ClearAll()
		self.initColumnsSnack()

	def initColumnsSnack(self):
		for index, col in enumerate(self.columnsSnack):
			self.listCtrlSnack.InsertColumn(index, col)

	def initColumnsDrink(self):
		for index, col in enumerate(self.columnsDrink):
			self.listCtrlDrink.InsertColumn(index, col)

	def initColumnsFood(self):
		for index, col in enumerate(self.columnsFood):
			self.listCtrlFood.InsertColumn(index, col)
	
	def initColumnsTransaksi(self):
		for index, col in enumerate(self.columns):
			self.listCtrlTransaksi.InsertColumn(index, col)
	
	def handleBtnGetTransaksi( self, event ):
		self.clearListTransaksi()
		transaksii = self.TransaksiModel.get(orderByColumn='id', orderByDirection='ASC')
		for rowIndex, row in enumerate(transaksii):
			self.listCtrlTransaksi.InsertItem(rowIndex, row[0])
			for columnIndex, col in enumerate(self.columns):
				self.listCtrlTransaksi.SetItem(rowIndex, columnIndex, str(row[columnIndex]))
	
	def handleBtnGetFood( self, event ):
		self.clearListFood()
		food = self.FoodModel.get(orderByColumn='id', orderByDirection='ASC')
		for rowIndex, row in enumerate(food):
			self.listCtrlFood.InsertItem(rowIndex, row[0])
			for columnIndex, col in enumerate(self.columnsFood):
				self.listCtrlFood.SetItem(rowIndex, columnIndex, str(row[columnIndex]))
	
	def handleBtnGetDrink( self, event ):
		self.clearListDrink()
		drink = self.DrinkModel.get(orderByColumn='id', orderByDirection='ASC')
		for rowIndex, row in enumerate(drink):
			self.listCtrlDrink.InsertItem(rowIndex, row[0])
			for columnIndex, col in enumerate(self.columnsDrink):
				self.listCtrlDrink.SetItem(rowIndex, columnIndex, str(row[columnIndex]))
	
	def handleBtnGetSnack( self, event ):
		self.clearListSnack()
		snack = self.SnackModel.get(orderByColumn='id', orderByDirection='ASC')
		for rowIndex, row in enumerate(snack):
			self.listCtrlSnack.InsertItem(rowIndex, row[0])
			for columnIndex, col in enumerate(self.columnsSnack):
				self.listCtrlSnack.SetItem(rowIndex, columnIndex, str(row[columnIndex]))


	def handleSelectedItemTransaksi(self, event):
		selectedId = event.GetItem().GetText()
		if not selectedId: return

		self.selectedTransaksi = selectedId
		self.btnEditTransaksi.Enable()
		self.btnDeleteTransaksi.Enable()


	def handleSelectedItemFood(self, event):
		selectedId = event.GetItem().GetText()
		if not selectedId: return

		self.selectedFood = selectedId
		self.btnEditFood.Enable()
		self.btnDeleteFood.Enable()

	def handleSelectedItemDrink(self, event):
		selectedId = event.GetItem().GetText()
		if not selectedId: return

		self.selectedDrink = selectedId
		self.btnEditDrink.Enable()
		self.btnDeleteDrink.Enable()
	
	def handleSelectedItemSnack(self, event):
		selectedId = event.GetItem().GetText()
		if not selectedId: return

		self.selectedSnack = selectedId
		self.btnEditSnack.Enable()
		self.btnDeleteSnack.Enable()

	def handleBtnDeleteTransaksi(self, event):
		if self.selectedTransaksi == None: return

		r = wx.MessageDialog(None, 'This data will be deleted permanently.', 'Are you sure', style=wx.ICON_WARNING | wx.YES_NO | wx.NO_DEFAULT).ShowModal()

		if r == wx.ID_YES:
			self.TransaksiModel.delete(self.selectedTransaksi)
			wx.MessageDialog(None, 'Transaksi has been deleted.', 'Delete Success', style=wx.OK | wx.ICON_INFORMATION).ShowModal()

	def handleBtnDeleteFood(self, event):
		if self.selectedFood == None: return

		r = wx.MessageDialog(None, 'This data will be deleted permanently.', 'Are you sure', style=wx.ICON_WARNING | wx.YES_NO | wx.NO_DEFAULT).ShowModal()

		if r == wx.ID_YES:
			self.FoodModel.delete(self.selectedFood)
			wx.MessageDialog(None, 'Food has been deleted.', 'Delete Success', style=wx.OK | wx.ICON_INFORMATION).ShowModal()

	def handleBtnDeleteDrink(self, event):
		if self.selectedDrink == None: return

		r = wx.MessageDialog(None, 'This data will be deleted permanently.', 'Are you sure', style=wx.ICON_WARNING | wx.YES_NO | wx.NO_DEFAULT).ShowModal()

		if r == wx.ID_YES:
			self.DrinkModel.delete(self.selectedDrink)
			wx.MessageDialog(None, 'Drink has been deleted.', 'Delete Success', style=wx.OK | wx.ICON_INFORMATION).ShowModal()

	def handleBtnDeleteSnack(self, event):
		if self.selectedSnack == None: return

		r = wx.MessageDialog(None, 'This data will be deleted permanently.', 'Are you sure', style=wx.ICON_WARNING | wx.YES_NO | wx.NO_DEFAULT).ShowModal()

		if r == wx.ID_YES:
			self.SnackModel.delete(self.selectedSnack)
			wx.MessageDialog(None, 'Snack has been deleted.', 'Delete Success', style=wx.OK | wx.ICON_INFORMATION).ShowModal()

	def handleBtnEditTransaksi(self, event):
		if self.selectedTransaksi == None: return

		transaksi = self.TransaksiModel.find(self.selectedTransaksi)
		frame = createFrameTransaksii()
		frame.setNamaMenu(transaksi[1])
		frame.setJumlah(transaksi[2])
		frame.setHarga(transaksi[3])
		frame.setTotal(transaksi[4])
		frame.setId(self.selectedTransaksi)
		frame.Show()
	
	def handleBtnEditFood(self, event):
		if self.selectedFood == None: return

		Food = self.FoodModel.find(self.selectedFood)
		frame = createFrameFood()
		frame.setNamaMakanan(Food[1])
		frame.setStock(Food[2])
		frame.setHarga(Food[3])
		frame.setId(self.selectedFood)
		frame.Show()
	
	def handleBtnEditDrink(self, event):
		if self.selectedDrink == None: return

		Drink = self.DrinkModel.find(self.selectedDrink)
		frame = createFrameDrink()
		frame.setNamaMinuman(Drink[1])
		frame.setStock(Drink[2])
		frame.setHarga(Drink[3])
		frame.setId(self.selectedDrink)
		frame.Show()

	def handleBtnEditSnack(self, event):
		if self.selectedSnack == None: return

		Snack = self.SnackModel.find(self.selectedSnack)
		frame = createFrameSnack()
		frame.setNamaSnack(Snack[1])
		frame.setStock(Snack[2])
		frame.setHarga(Snack[3])
		frame.setId(self.selectedSnack)
		frame.Show()

	def handleBtnAddDataTransaksi(self, event):
		frame = createFrameTransaksii()
		frame.Show()
	
	def handleBtnAddDataFood(self, event):
		frame = createFrameFood()
		frame.Show()
	
	def handleBtnAddDataDrink(self, event):
		frame = createFrameDrink()
		frame.Show()
	
	def handleBtnAddDataSnack(self, event):
		frame = createFrameSnack()
		frame.Show()

