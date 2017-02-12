events = {}
event_name = []
class Calendar(object):
  def __init__(self):
    pass
    
  def add_event(self):
    self.event_name = input("Enter event name")
    self.event_venue = input("Enter event venue")
    self.event_date = input("Enter event date")
    events[self.event_name] = [self.event_venue, self.event_date]
    event_name.append(self.event_name)
    
  def view_all(self):
    print("===========View All Events==============")
    for event in events.keys():
      print("%s %s" %(event,events[event]))
      
  def view_last_event(self):
    print("===========View Last Event==============")
    len_of_event_name = len(event_name)
    print(event_name[len_of_event_name-1])
    
    
angela = Calendar()
angela.add_event()
malyun = Calendar()
malyun.add_event()
malyun.view_all()
angela.view_last_event()