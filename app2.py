import ticketpy
import pprint

tm_client = ticketpy.ApiClient('DhfuZsulCs5UNronw8pNCf6GEVc7GIPY')
pp = pprint.PrettyPrinter(indent=4)
def tm_api(*args):
    # print(args)
    argument = {}
    argument["city"] = args[0]
    argument["startDateTime"] = args[1]+"T00:00:00Z"
    # argument["endDateTime"] = args[1][:8]+str(int(args[1][8:10])+1) + args[1][10:]+"T00:00:00Z"
    argument["radius"] = args[2]
    argument["keyword"] = args[3]
    pages = tm_client.events.find(**argument)
# def tm_api():
#     argument = {}
#     argument["keyword"] = "hip hop"
#     argument["city"] = "San Francisco"
#     argument["radius"] = "10"
#     argument["startDateTime"] = "2019-11-03T10:00:00Z"
#     argument["endDateTime"] = "2019-11-04T23:59:00Z"
#     pages = tm_client.events.find(**argument)


    lst = []
    for page in pages:
        for event in page:
            if len(lst) == 10:
                break;
            dict = {}
            dict["name"] = event.json["name"]
            dict["url"] = event.json["url"]
            dict["date"] = event.json["dates"]["start"]["localDate"]
            dict["start_time"] = event.json["dates"]["start"]["localTime"]

            dict["image"] = event.json["images"][0]["url"]

            end = (int(event.json["dates"]["start"]["localTime"][0:2])+3)%24
            if end < 10:
                endStr = "0"+str(end)
            else:
                endStr = str(end)
            dict["end_time"] = endStr + dict["start_time"][2:]

            # print(event.json["_embedded"]["venues"][0]["address"])
            dict["venue_name"] = event.json["_embedded"]["venues"][0]["name"]
            dict["address"] = event.json["_embedded"]["venues"][0]["address"]["line1"]
            # print(dict["end_time"])

            # print(event.json)
            # pp.pprint(event.json[])
            # e = event.json["_embedded"]["attractions"][0]
            # pp.pprint(event.json["_embedded"]["venues"][0]["name"])
            # pp.pprint(event.json["dates"]["start"]["localDate"])
            # pp.pprint(event.json["dates"]["start"]["localTime"])
            # pp.pprint(event.json["dates"]["start"])
            # pp.pprint(event.json)
            # pp.pprint(event.json["name"])
            # pp.pprint(event.json["url"])
            # pp.pprint(event.json["images"][0]["url"])
            # pp.pprint(event.json.keys())
            # print(event.json)
            lst.append(dict)
    return lst
        # object_methods = [method_name for method_name in dir(event)
        #           if callable(getattr(event, method_name))]
        # print(object_methods)
# print(tm_api())
