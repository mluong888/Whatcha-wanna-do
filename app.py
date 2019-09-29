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
# def eb_api_query():
    argument = {}
    # argument["location.address"]="San Francisco"
    # argument["location.within"]="10mi"
    # # argument["price"]="free"
    # argument["start_date.range_start"] = "2019-09-29T00:00:00"
    # # argument["sort_by"] = "date"
    # argument["expand"] = "venue"
    # argument["categories"] = "102"

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
    pp = pprint.PrettyPrinter(indent=4)
    # pp.pprint(event["events"][0])
    if event == None:
        print("didnt work")
        return;
    limit = min(10, len(event["events"]))
    # print(len(event))
    first_event = event["events"][0:limit]
    print(len(first_event))
    lst = []
    for e in first_event:
        # pp.pprint(e)
        dict = {}
        dict["name"] = e["name"]["text"]
        dict["url"] = e["url"]
        dict["description"] = e["description"]["text"]
        # print(type(dict["date"]))
        dict["date"] = (e["start"]["local"])[0:10]
        dict["start_time"] = (e["start"]["local"])[11:19]
        dict["end_time"] = e["end"]["local"][11:19]
        # dict["location"] = e["venue"]["address"]["address_1"]
        # dict["city"] = e["venue"]["address"]["city"]
        dict["image"] = e["logo"]["original"]["url"]
        # print(e["logo"]["original"]["url"])
        lst.append(dict)
        # return dict
    # print(location)
    # print(lst)
    return lst
# print(eb_api_query())
