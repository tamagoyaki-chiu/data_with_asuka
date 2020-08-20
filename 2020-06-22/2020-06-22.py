import time
import os

# print("A")
# time.sleep(3)
# print("B")

# for i in range(0,10,1):
# 	os.system("cls")
# 	if i>=0 and i<=3:
# 		print("您好")
# 	elif i>=4 and i<=7:
# 		print("哈囉~哈囉~")
# 	else:
# 		print("哈哈哈")
# 	time.sleep(2)

# print(time.time())
# time.sleep(2)
# print(time.time())
# while True:
# 	os.system("cls")
# 	print(time.strftime("%Y-%m-%d %H:%M:%S"))
# 	time.sleep(1)
import prettytable

# t=prettytable.PrettyTable(["Id","Title"], encoding="utf8")
# t.align["Title"]="r"
# t.add_row([1,"AAA"])
# t.add_row([2,"BBB"])
# t.add_row([3,"CCC"])
# print(t)

import colorama

# colorama.init(True)

# print("ABC")
# print(colorama.Fore.GREEN+colorama.Style.BRIGHT+"ABC")
# print(colorama.Back.RED+"ABC")

import mywindows2
import wx
import codecs
class myframe1(mywindows2.MyFrame1):
	def myclick( self, event ):
		# self.SetTitle("標題文字")
		# wx.MessageBox("ABC")
		self.m_grid1.AppendCols(3)
		self.m_grid1.SetColLabelValue(0, "標題名稱")
		self.m_grid1.AppendRows(3)
		self.m_grid1.SetRowLabelValue(1, "ABC")
		self.m_grid1.SetSize(500,200)
		self.m_grid1.SetCellValue(1, 2, "123")
		print(self.m_grid1.GetSize())

	def myclick2( self, event ):
		# wx.Exit()
		# self.m_staticText1.SetLabel("ABC")
		# wx.MessageBox(self.m_staticText1.GetLabel())
		# self.m_choice1.SetSelection(2)
		r=self.m_filePicker1.GetPath()
		wx.MessageBox(r)
		with codecs.open(r,"r","utf8") as f:
			self.m_textCtrl1.SetValue(f.read())
			
	def myclick3( self, event ):
		# wx.MessageBox(self.m_textCtrl1.GetValue())
		# self.m_gauge1.SetValue(self.m_gauge1.GetValue()+10)
		# wx.MessageBox(str(self.m_choice1.GetCurrentSelection()))
		wx.MessageBox(self.m_hyperlink1.GetURL())
	def myclick4( self, event ):
		# self.m_choice1.Append(self.m_textCtrl1.GetValue())
		pass

a=wx.App() #建立變數
w=myframe1(None)
w.Show()
a.MainLoop() #讓視窗持續顯示
