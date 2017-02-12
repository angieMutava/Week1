my_event = {}
event_list = []
class calendarApp(object):

	
	#Title message
	def title(self):
		print ('-' * 10)
		print ("Calendar App.")
	#Get user choice 
	def get_user_choice(self):
		print ('-' * 10)
		print ("Choose an Option Below:\n")
		print ('[1] Add an Event')
		print ('[2] See All Events')
		print ('[3] View last Event\n')

		

	#Add an event
	def add_event(self):
	  print ('-' * 10)
	  
	  choice = input( "Enter your Choice. \n")
	  if choice == '1':
	    self.mm = int(input('Enter Month: \n'))
	    self.yy = int(input('Enter Year: \n'))
	    self.dd = int(input('Enter Day: \n'))
	    self.my_cal = calendar.month(self.yy, self.mm)
	    print (self.my_cal)
	    self.event = input(" Add Event: \n")
	    
	    print("Event added on  %s/%s/%s is %s"%(self.dd, self.mm, self.yy,self.event))
	    #events = event.title()
	    my_event[self.my_cal]=self.event
	    
  
  #See all events	
	def see_all(self):
	
		for event in my_event.values():
			event_list.append(event)
		for event in event_list:
		  print(event)

		
	#view last event	
	def view_last_event(self):
	  
	  print(event_list[len(event_list)-1])
	  

angela = calendarApp()
malyun = calendarApp()
rose = calendarApp()
angela.title()
angela.get_user_choice()
angela.add_event()
malyun.get_user_choice()
malyun.add_event()
rose.get_user_choice()
rose.add_event()
rose.see_all()
rose.view_last_event()
