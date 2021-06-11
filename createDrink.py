import wx
import interface
import datetime
from models import drinkk

# Implementing mainFrame
class createFrameDrink( interface.createMinumanFrame ):
    def __init__( self ):
        interface.createMinumanFrame.__init__(self, parent=None)
        self.drinkModel = drinkk.Drink()
        self.id = None

    def setId(self, id):
        self.id = id

    def setNamaMinuman(self, nama_minuman):
        self.textCtrlNamaMinuman.SetValue(nama_minuman)

    def setStock(self, stock_minuman):
        self.textCtrlStock.SetValue(str(int))

    def setHarga(self, harga_minuman):
        self.textCtrlHargaMinuman.SetValue(str(int))


    def handleBtnSaveMinuman(self, event):
        nama_minuman = self.textCtrlNamaMinuman.GetValue().strip()
        stock_minuman = self.textCtrlStock.GetValue().strip()
        harga_minuman = self.textCtrlHargaMinuman.GetValue().strip()

        try:
            if self.id == None:
                result = self.drinkModel.insert(values=[nama_minuman, stock_minuman, harga_minuman], columns=['nama_minuman', 'stock_minuman', 'harga_minuman'])
            else:
                result = self.drinkModel.update(colValues={'nama_minuman': nama_minuman, 'stock_minuman': stock_minuman, 'harga_minuman': harga_minuman, }, identifierValue=self.id)

        except Exception as err:
            wx.MessageDialog(None, str(err), 'An error occured.', style=wx.OK | wx.ICON_ERROR).ShowModal()

        finally:
            if self.id == None:
                wx.MessageDialog(None, 'New drink successfully added.', 'Success', style=wx.OK | wx.ICON_INFORMATION).ShowModal()
            else:
                wx.MessageDialog(None, 'Drink data has been updated.', 'Update Success', style=wx.OK | wx.ICON_INFORMATION).ShowModal()