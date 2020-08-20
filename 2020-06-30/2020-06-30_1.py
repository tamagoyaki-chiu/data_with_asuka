import mywindows3
import wx
import codecs
class myframe1(mywindows3.MyFrame1):
	img=["2.jpg","1.jfif"]
	i=0
	def myclick( self, event ):
		# w2=myframe2(None)
		# w2.Show()
		# self.Hide()
		# self.m_panel1.Hide()
		# self.m_panel2.Show()
		# f=codecs.open("2.jpg","rb")
		# m=wx.Image(f, wx.BITMAP_TYPE_JPEG)
		# b=wx.Bitmap(m)
		# self.m_bitmap1.SetBitmap(b)
		# self.m_bitmap1.SetBitmap(wx.Bitmap(wx.Image(codecs.open("2.jpg","rb"), wx.BITMAP_TYPE_JPEG)))
		r=wx.FileSelector(
			"測試",
			wildcard="圖片|*.jpg",
			flags=wx.FD_OPEN
		)
		print(r)

	def mytimer( self, event ):
		# wx.MessageBox("xxx")
		f=codecs.open(self.img[self.i%2],"rb")
		m=wx.Image(f, wx.BITMAP_TYPE_JPEG)
		b=wx.Bitmap(m)
		self.m_bitmap1.SetBitmap(b)
		self.i+=1

class myframe2(mywindows3.MyFrame2):
	def myclick( self, event ):
		w1=myframe1(None)
		w1.Show()
		self.Hide()

a=wx.App()
w1=myframe1(None)
w1.Show()
w1.m_timer1.Start(3000)
# w2=myframe2(None)
# w2.Show()
a.MainLoop()
