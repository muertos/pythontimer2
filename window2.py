import gi, threading, logging, time
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from time import strftime, gmtime, sleep

class Worker(threading.Thread):
	close = False
	enable_timer = False

        def run(self, enable_timer):
            max_seconds = 10
            count = 0
            curr = sec_count = int(strftime("%S", gmtime()))
            while not self.close:
                if enable_timer:
                    sec_count = int(strftime("%S", gmtime()))
                    if sec_count != curr:
                        count = count + 1
                        curr = sec_count
                        print "."
                    if count == max_seconds:
                        enable_timer = False
                else:
                    time.sleep(0.1)

        #def stoptime(self, widget): #this still needs work and is not being called while counttime is running, until after counttime finishes
        #    print "Time stopped"
        #    enable_timer = False

            
        #def run(self):
        #    while not self.close:
        #        if self.enable_timer:
        #            logging.warn("Timer started..")
        #            self.counttime()
        #        else:
        #            time.sleep(0.1)

class Window(Gtk.Window):
    def __init__(self):
        super(Window, self).__init__()
        self.worker = Worker()
        self.worker.start()
        Gtk.Window.__init__(self, title="Timer") #is this needed?
	self.box = Gtk.Box(spacing=6)
        self.add(self.box)
        self.starttimer = Gtk.Button(label="Start")
        self.stoptimer = Gtk.Button(label="Stop")
        self.box.pack_start(self.starttimer, True, True, 0)
        self.box.pack_start(self.stoptimer, True, True, 0)
                
        def command(arg):
            self.worker.enable_timer = arg

        self.starttimer.connect("clicked", lambda _b: command(True))
        self.stoptimer.connect("clicked", lambda _b: command(False))

if __name__ == "__main__":
    main = Window()
    try:
        main.connect("delete-event", Gtk.main_quit)
        main.show_all()
        Gtk.main()
    finally:
        main.worker.close = True
        main.worker.join()
