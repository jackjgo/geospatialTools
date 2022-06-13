# -*- coding: utf-8 -*-
"""
Simple functions to take tranlate between degree minutes seconds and decimal 
degrees.
"""

def dms2dd(d,m,s):
    # Degree mintues seconds to decimal degrees
    # d: degrees
    # m: minutes
    # s: seconds
    
    dd = d + (m / 60) + (s / 3600)
    return dd

def dd2dms(dd):
    # Decimal degrees to degrees minutes seconds
    # dd: decimal degrees
    
    d = dd // 1
    remainder = (dd % 1) * 60
    m = remainder // 1
    s = (remainder % 1) * 60
    
    return d, m, s

def dd2ddm(dd):
    # Decimal degrees to degrees decimal minutes
    # dd: decimal degrees
    
    d = dd // 1
    m = (dd % 1) * 60
    
    return d, m

def dms2ddm(d,m,s):
    # Degree mintues seconds to degrees decimal minutes
    # d: degrees
    # m: minutes
    # s: seconds
    
    dd = dms2dd(d, m, s)
    d, m = dd2ddm(dd)
    
    return d, m

print(dd2ddm(42.36002))