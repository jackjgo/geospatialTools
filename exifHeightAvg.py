"""
Compute the average height along atransect of photos, using exif geotags
"""

import pandas as pd
import exifread
import numpy as np

def readTransects(txtFile, photoDirectory):
    meanElev = []
    df  = pd.read_csv(txtFile)
    transectStarts  = df['start']
    transectEnds = df['end']
    i = 0
    for transect in transectStarts:
        start = transectStarts[i]
        startnum = int(start[1:8])
        # print(startnum)
        end = transectEnds[i]
        endnum = int(end[1:8])
        # print(endnum)
        photonums = list(range(startnum,endnum+1))
        elevations = []
        for photo in photonums:
            fileName = str(photoDirectory + 'G00' + str(photo) + '.jpg')
            # print(type((fileName)))
            
            try:
                photo = open(fileName,'rb')
                tags = exifread.process_file(photo)
                altitudeTag = tags.get('GPS GPSAltitude')
                altitudeRef =tags.get('GPS GPSAltitudeRef')
                altitude = float((altitudeTag.values[0].num) / (altitudeTag.values[0].den))
                elevations.append(altitude)
            except:
                    continue
            # tags = exifread.process_file(photo)
            # altitudeTag = tags.get('GPS GPSAltitude')
            # altitudeRef =tags.get('GPS GPSAltitudeRef')
            # altitude = float((altitudeTag.values[0].num) / (altitudeTag.values[0].den))
            # elevations.append(altitude)
            # print(tags)
        meanElev.append(np.mean(elevations))
        # print(type(start))
        i = i+1
    return (meanElev)
    
# meanElev = readTransects('poas_transects.csv','./goproAll/')
# df = pd.read_csv('poas_transects.csv')
# df['meanElevation'] = meanElev
# df.to_csv('poas_transects_meanElev.csv')
# elev = []
# df  = pd.read_csv('poas_transects.csv')
# transectS  = [df['start']; df['end']]
# print(transectEnds)
