from eventbrite import Eventbrite
from tok import secret
import pprint

token = secret()
eventbrite = Eventbrite(token)
user = eventbrite.get_user()
# print(user['ID'])
#print(user["id"])
#def eb_api_query(*args):
def eb_api_query(*args):
    argument = {}
    # argument["location.address"]="San Francisco"
    # argument["location.within"]="10mi"
    # argument["price"]="free"
    # argument["start_date.range_start"] = "2019-07-05T00:00:00"
    # argument["sort_by"] = "date"
    # argument["expand"] = "venue"
    # argument["categories"] = "101"
    argument["location.address"]=args[0]
    argument["location.within"]=args[2]
    pr = args[3]
    if pr != "meh":
        argument["price"]=args[3]
    argument["start_date.range_start"] = args[1]+"T00:00:00"
    argument["sort_by"] = "date"
    argument["expand"] = "venue"
    argument["categories"] = args[4]
    event = eventbrite.event_search(**argument)
    # print(event)
    #event = eventbrite.event_search(price="free", sort_by="date")
    #start_date.range_start = "2019-06-22T00:00:00"
    # print(user['ID'])
    #print(event==None)
    pp = pprint.PrettyPrinter(indent=4)
    # pp.pprint(event["events"][0])
    if event == None:
        print("didnt work")
        return;
    limit = min(5, len(event))
    first_event = event["events"][0:limit]
    lst = []
    for e in first_event:
        dict = {}
        dict["name"] = e["name"]["text"]
        dict["url"] = e["url"]
        dict["description"] = e["description"]["text"]
        # print(type(dict["date"]))
        dict["date"] = (e["start"]["local"])[0:10]
        dict["start_time"] = (e["start"]["local"])[11:19]
        dict["end_time"] = e["end"]["local"][11:19]
        dict["location"] = e["venue"]["address"]["address_1"]
        dict["city"] = e["venue"]["address"]["city"]
        lst.append(dict)
        # return dict
    # print("name: " + first_event["name"]["text"] + "\n")
    # print("url: " + first_event["url"]+ "\n")
    # print("description: " + first_event["description"]["text"]+ "\n")
    # print("start time: " + first_event["start"]["local"]+ "\n")
    # print("end time: " + first_event["end"]["local"]+ "\n")
    # print("location: " + first_event["venue"]["address"]["address_1"] + "\n")
    # print("city: " + first_event["venue"]["address"]["city"] + "\n")
    # # print("location_2: " + first_event["venue"]["address"]["address_2"] + "\n")
    # print("location_id: " + first_event["venue_id"]+ "\n")
    # eventzzzz = eventbrite.event_search(**args, venue_id = loc)
    # pp.pprint(first_event)
    # object_methods = [method_name for method_name in dir(eventbrite)
    #               if callable(getattr(eventbrite, method_name))]
    # print(object_methods)
    # location = eventbrite.get(id=loc)
    # print(location)
    # print(lst[0])
    return lst
# print(eb_api_query())
