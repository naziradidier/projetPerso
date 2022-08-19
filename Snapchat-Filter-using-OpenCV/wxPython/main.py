import wx
app = wx.App()
window = wx.Frame(None, title="wx python Frame", size=(600, 400))
panel = wx.Panel(window)
label = wx.StaticText(panel, label="hello word", pos=(300, 20))
button = wx.Button(panel, label="exit", pos=(300, 300))
window.Show(True)
app.MainLoop()


