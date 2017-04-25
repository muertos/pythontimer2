import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from time import strftime, gmtime, sleep

class MyWindow(Gtk.Window):
	
	def __init__(self):
		Gtk.Window.__init__(self, title="Hello World")

		self.box = Gtk.Box(spacing=6)
		self.add(self.box)

		self.starttimer = Gtk.Button(label="Start")
		self.starttimer.connect("clicked", self.counttime)
		self.starttimer.connect("delete-event", Gtk.main_quit)
		self.box.pack_start(self.starttimer, True, True, 0)

		self.stoptimer = Gtk.Button(label="Stop")
		self.stoptimer.connect("clicked", self.stoptime)
		self.box.pack_start(self.stoptimer, True, True, 0)
	
	def counttime(self, widget):
		max_seconds = 10
		count = 0
		curr = sec_count = int(strftime("%S", gmtime()))
		while count < max_seconds:
			sec_count = int(strftime("%S", gmtime()))
			if sec_count != curr:
				count = count + 1
				curr = sec_count
				print "."

	def stoptime(self, widget):
		print("Timer stopped")


win = MyWindow()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()
