# -*- coding: utf-8 -*-
"""
Created on Fri Mar 12 14:56:37 2021

This function takes a csv of WGS84 coordinates (lat, lon, elevation)
and uses the UNAVCO geoid height calculator to find the EGM96 orthometric
height for each point.

Check out the calculator at
https://www.unavco.org/software/geodetic-utilities/geoid-height-calculator/geoid-height-calculator.html

As of 8/18/21, the calculator has changed. This function won't work, but the new format
allows you to submit the inputs and save results via csv directly on the web page.

@author: jckgn
"""

import pandas as pd
import selenium as se
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def calculateGeoidHeight(inputFileName,outputFileName,latName,lonName,elevName):
    
    # Start up web browser
    driver = se.webdriver.Chrome() # make sure driver is for the right browser and added to the path
        
    # Load csv of input points
    dfIn = pd.read_csv(inputFileName)
    columnNames = [latName,lonName,elevName]
    coordIn = dfIn[columnNames].to_numpy()
    heightsEGM96 = []
    
    for row in coordIn:
        # load website
        driver.get('https://www.unavco.org/software/geodetic-utilities/geoid-height-calculator/geoid-height-calculator.html')
        
        # Identify text boxes
        latBox = driver.find_element_by_name('lat')
        lonBox = driver.find_element_by_name('lon')
        gpsHeightBox = driver.find_element_by_name('gpsheight')
        
        # Get original coordinates
        lat = row[0]
        lon = row[1]
        height = row[2]
        
        # Fill in text boxe and submit
        latBox.send_keys(str(lat))
        lonBox.send_keys(str(lon))
        gpsHeightBox.send_keys(str(height))
        submitButton = driver.find_element_by_name('submit')
        submitButton.click()
        
        # read orthimetric height
        orthoHeight = driver.find_element_by_xpath("/html/body/p[5]/span").text
        orthoHeight = float(orthoHeight[0:5])
        heightsEGM96.append(orthoHeight)
        
        
    dfOut = dfIn
    dfOut[elevName] = heightsEGM96
    dfOut.to_csv(outputFileName)
    
######################### Test Run

# calculateGeoidHeight('../../../GNSS/Capers918.csv', 'Capers918_EGM96.csv', 'latitude', 'longitude', 'elevation')
