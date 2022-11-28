from collections import defaultdict
import json
import requests
from Shedule import Shedule


class Route:
    def __init__(self, schedule: Shedule):
        self.route_dict = defaultdict(list)
        self.schedule = schedule

    def route_create(self, transport, station_a, station_b):
        self.url_info = requests.get(
            f"https://api.tomtom.com/routing/1/calculateRoute/{station_a.x},{station_a.y}:{station_b.x},{station_b.y}/json?key=ia1LDxd6nw6VlbbyIjdMPAd01h0aiA9g").text
        self.route_info = json.loads(self.url_info)