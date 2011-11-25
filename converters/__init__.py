def days_to_seconds(days):
    ''' This function converts days to seconds '''
    return days*24*60*60

def celsius_to_fahrenheit(degrees):
    ''' Converts degrees Celsius to degrees Fahrenheit '''
    return degrees*1.8 + 32

def fahrenheit_to_celsius(degrees):
    ''' Converts degrees Fahrenheit to degrees Celsius '''
    return (degrees-32)/1.8

def surface_of_circle(radius):
    ''' Calculates the surface of a circle. Hint: Use pow(x, exponent) for power '''
    from math import pi
    x = radius**2
    y = x*pi
    return y
    

def cube_volume(length, width, height):
    ''' Returns the volume of the cube '''
    return length*width*height

def usd_to_chf(usd):
    ''' Fetches the current exchange rate and converts to swiss francs '''
    import urllib2
    import json
    req = urllib2.Request('https://raw.github.com/currencybot/open-exchange-rates/master/latest.json')
    opener = urllib2.build_opener()
    f = opener.open(req)
    data = json.loads(f.read())
    exchange_rate = data['rates']['CHF']
    return 0

def lessons_to_minutes(lessons):
    ''' Returns the amount of minutes spent in lessons '''
    return 0

def mwst(amount):
    ''' This returns the amount of tax (mwst) on a given amount. Watch out, the amount already
    includes the tax! '''
    return 0

def joules_to_calories(joules):
    ''' Converts joules to calories '''
    return joules*0.239005736

def kmh_to_mph(kmh):
    return kmh/100*62.137

def distance_between_points(x1, x2):
    ''' Returns the distance between the points x1 and x2.
    The points are tuples (1,5). sqrt() is the root, pow(x, exponent) is the power
    '''
    from math import sqrt
    x12 = (x2[0] - x1[0], x2[1] - x1[1]) 
    return sqrt(x12[0]**2 + x12[1]**2)

def cat_and_dog_speech(animal):
    if animal=='katze':
        return 'miau'
    if animal=='hund':
        return 'wuff'

def element_in_list(element, list):
    ''' Checks if an element is in a list and returns True if so,
    otherwise False
    '''
    if element in list:
        return True
    return False
