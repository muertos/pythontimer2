#3/21/2017
#Simple stopwatch cuz I can and need it so QA doesn't hate me
#one day this will have a GUI

from time import strftime, gmtime, sleep

max_seconds = input("seconds: ");
count = 0

curr = sec_count = int(strftime("%S", gmtime()))

while count < max_seconds:
	sec_count = int(strftime("%S", gmtime()))
	if sec_count != curr:
		count = count + 1
		curr = sec_count
		print "."

print "%d seconds have elapsed" % count
