# -*- coding: utf-8 -*-
"""
Read GPS coordinates from exif as decimal degrees
This works, at least on GoPro Hero8 images
"""

import exifread


def readLatLon(fileName):    
    photo = open(fileName,'rb')
    tags = exifread.process_file(photo)
    latTag = tags.get('GPS GPSLatitude')
    latTagRef = tags.get('GPS GPSLatitudeRef')
    latitudeDeg = float((latTag.values[0].num / latTag.values[0].den))
    latitudeMin = float((latTag.values[1].num / latTag.values[1].den))
    latitudeSec = float((latTag.values[2].num / latTag.values[2].den))
    latitude = latitudeDeg + (latitudeMin / 60) + (latitudeSec / 3600)
    if latTagRef.values == 'S':
        latitude = -latitude
    
    lonTag = tags.get('GPS GPSLongitude')
    lonTagRef = tags.get('GPS GPSLongitudeRef')
    longitudeDeg = float(lonTag.values[0].num / lonTag.values[0].den)
    longitudeMin = float(lonTag.values[1].num / lonTag.values[1].den)
    longitudeSec = float(lonTag.values[2].num / lonTag.values[2].den)
    longitude = longitudeDeg + (longitudeMin / 60) + (longitudeSec / 3600)
    if lonTagRef.values == 'W':
        longitude = -longitude
    return [latitude, longitude]

def readAltitude(fileName):
    photo = open(fileName,'rb')
    tags = exifread.process_file(photo)
    altTag = tags.get('GPS GPSAltitude')
    altTagRef = tags.get('GPS GPSAltitudeRef')
    
    altitude = float((altTag.values[0].num) / (altTag.values[0].den))
    
    return altitude
    
# print(readLatLon('G0036179.jpg'))
# print(readAltitude('G0036179.jpg'))
