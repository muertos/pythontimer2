import gi, threading, logging, time
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from time import strftime, gmtime, sleep

class Worker(threading.Thread):
	close = False
	enable_timer = False

        def counttime(self, widget):
            enable_timer = True
            max_seconds = 10
            count = 0
            curr = sec_count = int(strftime("%S", gmtime()))
            while enable_timer == True:
                sec_count = int(strftime("%S", gmtime()))
                if sec_count != curr:
                    count = count + 1
                    curr = sec_count
                    print "."
                if count == max_seconds:
                    enable_timer = False

        def stoptime(self, widget): #this still needs work and is not being called while counttime is running, until after counttime finishes
            print "Time stopped"
            enable_timer = False

            
        def run(self):
            while not self.close:
                if self.enable_timer:
                    logging.warn("Timer started..")
                    counttime()
                else:
                    time.sleep(0.1)

class Window(Gtk.Window):

#need to implement worker class in this to actually make this work
    def __init__(self):
        super(Window, self).__init__()
        self.worker = Worker()
        self.worker.start()
        Gtk.Window.__init__(self, title="Timer") #is this needed?
	self.box = Gtk.Box(spacing=6)
        self.add(self.box)
                
        self.starttimer = Gtk.Button(label="Start")
        self.starttimer.connect("clicked", self.worker.counttime)
        self.box.pack_start(self.starttimer, True, True, 0)

        self.stoptimer = Gtk.Button(label="Stop")
        self.stoptimer.connect("clicked", self.worker.stoptime)
        self.box.pack_start(self.stoptimer, True, True, 0)


if __name__ == "__main__":
    main = Window()
    try:
        main.connect("delete-event", Gtk.main_quit)
        main.show_all()
        Gtk.main()
    finally:
        main.worker.close = True
        main.worker.join()
