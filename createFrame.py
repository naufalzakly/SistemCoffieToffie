"""Subclass of mainFrame, which is generated by wxFormBuilder."""

import wx
import interface
import datetime
from models import transaksi

# Implementing mainFrame
class createFrameTransaksii( interface.createTransaksiFrame ):
    def __init__( self ):
        interface.createTransaksiFrame.__init__(self, parent=None)
        self.transaksiModel = transaksi.Transaksi()
        self.id = None

    def setId(self, id):
        self.id = id

    def setNamaMenu(self, nama_menu):
        self.textCtrlNamaMenu.SetValue(nama_menu)

    def setJumlah(self, jumlah):
        self.textCtrlJumlah.SetValue(str(int))

    def setHarga(self, harga):
        self.textCtrlHarga.SetValue(str(int))

    def setTotal(self, total):
        self.textCtrlTotal.SetValue(str(int))

    def handleBtnSave(self, event):
        nama_menu = self.textCtrlNamaMenu.GetValue().strip()
        jumlah = self.textCtrlJumlah.GetValue().strip()
        harga = self.textCtrlHarga.GetValue().strip()
        total = self.textCtrlTotal.GetValue().strip()

        try:
            if self.id == None:
                result = self.transaksiModel.insert(values=[nama_menu, jumlah, harga, total], columns=['nama_menu', 'jumlah', 'harga', 'total'])
            else:
                result = self.transaksiModel.update(colValues={'nama_menu': nama_menu, 'jumlah': jumlah, 'harga': harga, 'total': total}, identifierValue=self.id)

        except Exception as err:
            wx.MessageDialog(None, str(err), 'An error occured.', style=wx.OK | wx.ICON_ERROR).ShowModal()

        finally:
            if self.id == None:
                wx.MessageDialog(None, 'New transaksi successfully added.', 'Success', style=wx.OK | wx.ICON_INFORMATION).ShowModal()
            else:
                wx.MessageDialog(None, 'Transaksi data has been updated.', 'Update Success', style=wx.OK | wx.ICON_INFORMATION).ShowModal()