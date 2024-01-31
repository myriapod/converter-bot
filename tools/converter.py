"""
Convert imperial to metric
"""

def MilesToKm(miles, yards, feet, inches):
    totalInches = (63360 * miles) + (36 * yards) + (12 * feet) + inches
    #find total meters
    totalMeters = totalInches / 39.37
    #find total centimeters so it is easier to work with
    totalCent = totalMeters*100
    #find kilometres
    kilometres = int(totalMeters / 1000)
    #this is where I use the modulo expression to find the remainders
    meters = int(totalMeters%1000)
    cent = round(float(totalCent%100), 1)
    
    result = ""
    if kilometres != 0:
        result+=(str(kilometres) +" km ")
    if meters != 0:
        result+=(str(meters) +" m ")
    if cent != 0:
        result+=(str(cent) +" cm ")

    return result

def FtoC(F):
    return round(((F-32)*5)/9, 1)

"""
Convert metric to imperial
"""

def KmToMiles(km, m, cm):
    totalCm = (km * 100000) + (m * 100) + cm
    totalInches = int(totalCm * 0.3937)

    miles = totalInches / 63360
    rest_yards = totalInches % 63360
    yards = rest_yards / 36
    rest_feet = rest_yards % 36
    feet = rest_feet / 12
    rest_inches = rest_feet % 12


    result = ""
    if int(miles) != 0:
        result+=(str(int(miles)) +" miles ")
    if int(yards) != 0:
        result+=(str(int(yards)) +" yards ")
    if int(feet) != 0:
        result+=(str(int(feet)) +" feet ")
    if int(rest_inches) != 0:
        result+=(str(int(rest_inches)) +" inches ")

    return result

def CtoF(C):
    return int(((C*9)/5)+32)