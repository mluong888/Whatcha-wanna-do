from eventbrite import Eventbrite
import pprint

eventbrite = Eventbrite("P7YQTPVH6UWEJMN24ZV4")
user = eventbrite.get_user()
# print(user['ID'])
#print(user["id"])

args = {}
args["location.address"]="San Francisco"
args["location.within"]="10mi"
args["price"]="free"
args["start_date.range_start"] = "2019-06-22T00:00:00"
args["sort_by"] = "date"
event = eventbrite.event_search(**args)
#event = eventbrite.event_search(price="free", sort_by="date")
#start_date.range_start = "2019-06-22T00:00:00"
# print(user['ID'])
#print(event==None)
pp = pprint.PrettyPrinter(indent=4)
# pp.pprint(event["events"][0])
first_event = event["events"][0]
print("name: " + first_event["name"]["text"] + "\n")
print("url: " + first_event["url"]+ "\n")
print("description: " + first_event["description"]["text"]+ "\n")
print("start time: " + first_event["start"]["local"]+ "\n")
print("end time: " + first_event["end"]["local"]+ "\n")
loc = first_event["venue_id"]
print("location_id: " + first_event["venue_id"]+ "\n")


location = eventbrite.venue_id(venue_id=loc)
print(location["address"])
