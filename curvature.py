# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 12:15:18 2021

calculates profile and plan curvature from dem
"""

import numpy as np

def profile_curvature(dem):
    # dem: 2D ndarray of elevation values
    gradX, gradY = np.gradient(dem)
    slope = np.sqrt(gradX ** 2 + gradY ** 2)
    slopeGradX, slopeGradY = np.gradient(slope)
    curvature = np.sqrt(slopeGradX ** 2 + slopeGradY ** 2)
    
    return curvature

def aspect(dem):
    # dem: 2D ndarray of elevation values
    gradX, gradY = np.gradient(dem)
    aspect = np.arctan2(gradX, gradY)
    aspect = aspect * (180 / np.pi)
    aspect = aspect + 270
    aspect[aspect > 360] = aspect - 360
    
    
    return aspect

def plan_curvature(dem):
    # Not sure if this is correct
    asp = aspect(dem)
    gradX, gradY = np.gradient(asp)
    curvature = np.sqrt(gradX ** 2 + gradY ** 2)
    
    return curvature