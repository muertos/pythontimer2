import gi, threading, time
gi.require_version('Gtk','3.0')
from gi.repository import Gtk
from time import strftime, gmtime, sleep

class Worker(threading.Thread):
    timerIsRunning = False
    quit = False
    
    def run(self):
        print "entered worker.run"
        time.sleep(1)
        while not self.quit:
            print self.timerIsRunning
            if self.timerIsRunning:
                print "timer is running"
                max_seconds = 10
                count = 0
                curr = sec_count = int(strftime("%S", gmtime()))
                while self.timerIsRunning:
                    sec_count = int(strftime("%S", gmtime()))
                    if sec_count != curr:
                        count = count + 1
                        if count > max_seconds:
                            timerIsRunning = False
                            break
                        curr = sec_count
                        print "."
                    
            else:
                print "timer should not be running"
                print self.timerIsRunning
                time.sleep(1)

#    def starttimer(self, widget):
#        timerIsRunning = True

#    def stoptimer(self, widget):
#        timerIsRunning = False

class Window(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="thread testing")
        self.worker = Worker() 
        #self.worker.run()
        self.worker.start() #explore what this does

        def command(arg):
            self.worker.timerIsRunning = arg

        self.box = Gtk.Box(spacing=6)
        self.add(self.box)
        self.button1 = Gtk.Button(label="button1")
        self.button2 = Gtk.Button(label="button2")
        self.box.pack_start(self.button1, True, True, 0)
        self.box.pack_start(self.button2, True, True, 0)
        self.button1.connect("clicked", lambda _b: command(True))
        self.button2.connect("clicked", lambda _b: command(False))


win = Window()
win.connect("delete-event", Gtk.main_quit)
win.show_all() # why tho
Gtk.main()
