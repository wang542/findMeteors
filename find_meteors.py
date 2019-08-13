import math
import requests


def calc_dist(lat1, lon1, lat2, lon2):
    lat1 = math.radians(lat1)
    lon1 = math.radians(lon1)
    lat2 = math.radians(lat2)
    lon2 = math.radians(lon2)

    h=math.sin((lat2-lat1)/2) **2+\
        math.cos(lat1) * math.cos(lat2)