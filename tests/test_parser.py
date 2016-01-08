#!/usr/bin/env python
# -*- coding: utf-8 -*-

from gmaps_url_parser import parse


def test_parser():
    url = "https://www.google.com/maps/place/Bou+Saada,+Algeria/@35.2131065,4.1479717,10106m/data=!3m1!1e3!4m2!3m1!1s0x128bb3c644644ec3:0x7f746dd09dad9a9f"
    coords = {'place': 'Bou Saada, Algeria', 'longitude': 4.1479717, 'latitude': 35.2131065}
    c = parse(url)
    assert c['longitude'] == coords['longitude']
    assert c['latitude'] == coords['latitude']
    assert c['place'] == coords['place']
