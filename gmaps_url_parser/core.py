#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re


def parse(url):
    coords = {}
    coords_re = re.compile(r'place/(.+)/@(.+),(.+),(.+)/')
    coords['latitude'] = float(coords_re.search(url).group(2))
    coords['longitude'] = float(coords_re.search(url).group(3))
    coords['place'] = coords_re.search(url).group(1).replace('+', ' ')
    type_string = coords_re.search(url).group(4)
    if type_string.endswith('m'):
        coords['maptype'] = 'earth'
        coords['zoom_level'] = type_string.strip('m')
    elif type_string.endswith('z'):
        coords['maptype'] = 'map'
        coords['zoom_level'] = type_string.strip('z')
    return coords
