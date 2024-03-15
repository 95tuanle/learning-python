import json
import urllib.request


def print_results(data):
    the_json = json.loads(data)

    if "title" in the_json["metadata"]:
        print(the_json["metadata"]["title"])

    count = the_json["metadata"]["count"]
    print(str(count) + " events recorded")

    for i in the_json["features"]:
        print(i["properties"]["place"])
    print("--------------\n")

    for i in the_json["features"]:
        if i["properties"]["mag"] >= 4.0:
            print("%2.1f" % i["properties"]["mag"], i["properties"]["place"])
    print("--------------\n")

    for i in the_json["features"]:
        if i["properties"]["felt"] is not None:
            print("%2.1f" % i["properties"]["mag"], i["properties"]["place"],
                  " reported " + str(i["properties"]["felt"]) + " times")


def main():
    url_data = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.geojson"
    web_url = urllib.request.urlopen(url_data)
    print("Result code: " + str(web_url.getcode()))
    if web_url.getcode() == 200:
        data = web_url.read()
        print_results(data)
    else:
        print("Received an error from server, cannot retrieve results " + str(web_url.getcode()))


if __name__ == "__main__":
    main()
