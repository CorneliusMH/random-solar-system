import random
import bisect
import numpy as np
import json
import time

f = open("tables.json")
g = json.load(f)

# print (g.keys())

sizeref = g['REFERENCE: Planet Size']

smallerthan = {
    "A":"A",
    "B":"A",
    "C":"B",
    "D":"C",
    "E":"D",
    "F":"E",
    "G":"F",
    "H":"G",
    "I":"H",
    "J":"I"
}

class OptionsWeightsLengthMismatchException(BaseException):
    """Raises when the number of elements in the options list doesn't match the number of elements in the weight list."""
    pass

# =============================================================================
# using a closure (functional programming approach)
def make_roll_table(options: list, weights):
    # Do the input validation here
    pdf = weights/np.sum(weights)
    cdf = np.cumsum(pdf)

    def get_item():
        roll = np.random.random()
        idx = bisect.bisect_left(cdf, roll)
        return options[idx]

    return get_item

def get_table_roll(i):
    step = g[i]
    stepweight_pre = np.array(step["weight"])
    stepresult = step["result"]
    stepweight = stepweight_pre.astype(float)
    get_item_from_table = make_roll_table(stepresult, stepweight)
    return get_item_from_table()

# =============================================================================
def get_body_stats(bodyType,maxSize):
    bodyTable = ''
    for i in (['STEP 6.1: Air',
        'STEP 6.1: Earth',
        'STEP 6.1: Liveworld',
        'STEP 6.1: Water',
        'STEP 6.1: Fire'
    ]):
        if bodyType in i:
            bodyTable = i
    sizelist = ['A','B','C','D','E','F','G','H','I','J']
    while i in sizelist:
        sizelist.pop()
    bodySize = get_table_roll(bodyTable)
    while bodySize not in sizelist:
        bodySize = get_table_roll(bodyTable)
    sizeInfo = sizeref[bodySize]
    diameter = random.randrange(sizeInfo["min"]*1,sizeInfo["max"])
    bodyShape = get_table_roll('STEP 6.2: Shape')
    bodyInfo = {
        "type":bodyType,
        "size class":bodySize,
        "diameter":diameter,
        "shape":bodyShape
    }
    return bodyInfo

def get_goodies(existingGoodies,maxGoodies):
    goodies = {}
    goodies[0] = get_table_roll('STEP 6.3: Goodies (Optional)')
    for i in goodies:
        if 'Roll twice' in goodies[i]:
            goodies[i] = get_table_roll('STEP 6.3: Goodies (Optional)')
            goodies[i+1] = get_table_roll('STEP 6.3: Goodies (Optional)')
        elif 'Roll again' in goodies[i]:
            goodies[i+1] = get_table_roll('STEP 6.3: Goodies (Optional)')
        elif 'roll again' in goodies[i]:
            goodies[i+1] = get_table_roll('STEP 6.3: Goodies (Optional)')
    return goodies

def get_moon(maxSize):
    
    return moon

def get_planet(maxSize):
    planetType = get_table_roll('STEP 2.1: Planet Type')
    planetBodystats = get_body_stats(planetType,maxSize)
    distance = random.randrange(1,7)
    planetInfo = {
        "type":planetType,
        "bodyStats":planetBodystats,
        "distance":distance
    }
    # if random.randint(1,100) > 50:

    #     planetInfo['goodies'] = get_goodies();
    return planetInfo

def get_sun(sunType='roll'):
    if sunType == 'roll':
        sunType = get_table_roll('STEP TWO: Primary Type')
    body = {}
    if 'Sun' in sunType:
        body = get_body_stats('Fire','J')
    elif 'Planet' in sunType:
        bodyType = get_table_roll('STEP 2.1: Planet Type')
        body = get_body_stats(bodyType,'J')
    elif 'Portal' in sunType:
        body = get_table_roll('STEP 2.2: Portal')
    elif 'void' in sunType:
        body =  {"type":"void","size class":"H"}
    sunInfo = {
        "type":sunType,
        "bodyStats":body
    }
    return sunInfo

def get_planets(maxSize,motion,number='roll'):
    if 'roll' in str(number):
        number = get_table_roll('STEP THREE: Number of Planets')
    if '1d20' in str(number):
        number = random.randrange(1,21)
    elif 'No planets' in str(number):
        number = 0
    planetsInfo = {}
    planetsInfo['number'] = int(number)
    distance = 0
    for i in range(0,number):
        planetsInfo[i] = get_planet(maxSize)
        if 'independently' in str(motion):
            planetsInfo[i]['motion'] = get_table_roll('STEP 5.1: Special Motion Table')
        else:
            planetsInfo[i]['motion'] = motion
        distance += planetsInfo[i]['distance']
    planetsInfo['distance'] = distance
    return planetsInfo

def get_system_type(sysType='roll'):
    if 'roll' in sysType:
        sysType = get_table_roll('STEP ONE: Type of System')
    primeBody = {}
    if 'Special System' in sysType:
        sysType = g['STEP 1.1: Special System Table']
    if 'Single Planet' in sysType:
        # Get planet info and get off this ride
        primeBody = get_sun(sysType)
    elif 'Void' in sysType:
        primeBody = get_sun('void')
    elif 'Multiple Primary System' in sysType:
        numPrimary = max(1,round(random.randrange(1,7)/2))
        for i in range(0,numPrimary):
            primeBody[i] = get_sun()
    else:
        primeBody = get_sun()  
    systemType = {
        "type":sysType,
        "primaryBody":primeBody
    }
    return systemType

def get_system():
    motion = get_table_roll('STEP FIVE: Planetary Motion')
    system = get_system_type()
    primary = system['primaryBody']
    if 'Single Planet' in system['type']:
        planets = {"distance":1}
    else:
        # print (primary['bodyStats'])
        planets = get_planets(smallerthan[primary['bodyStats']['size class']],motion)
    outputInfo = {
        "system":system,
        "planets":planets,
        "solarSea":int(planets['distance'])*2
    }
    return outputInfo

def get_basic_system():
    motion = "Clockwise orbit"
    system = get_system_type("Normal System")
    primary = system['primaryBody']
    planets = get_planets(smallerthan[primary['bodyStats']['size class']],motion,4)
    outputInfo = {
        "system":system,
        "planets":planets,
        "solarSea":int(planets['distance'])*2
    }
    return outputInfo

# out = json.dumps(get_system())    
# print(out)

# print(get_system())
# print ("==================================================")
# print(json.dumps(get_planets('F','Each planet moves independently. Roll on Special Motion Table (STEP 5.1) individually for each planet.',20)))

# print(system)

# sun = get_sun()
# print(sun)
# print(get_planet(smallerthan[sun['bodyStats']['size class']]))




# =============================================================================
# Testing junk lives below here

order = [
    'STEP ONE: Type of System',
    'STEP 1.1: Special System Table',
    'STEP TWO: Primary Type',
    'STEP 2.1: Planet Type',
    'STEP 2.2: Portal',
    'STEP THREE: Number of Planets',
    'STEP FOUR: Planetary Movement',
    'STEP FIVE: Planetary Motion',
    'STEP 5.1: Special Motion Table',
    'STEP SIX: Planet Type',
    'STEP 6.1: Air',
    'STEP 6.1: Earth',
    'STEP 6.1: Liveworld',
    'STEP 6.1: Water',
    'STEP 6.1: Fire',
    'STEP 6.2: Shape',
    'STEP 6.3: Goodies (Optional)',
    'STEP SEVEN: Planetary Location Assignment',
    'REFERENCE: Planet Size'
]

# for i in order:
#     print (i)
#     out = get_table_roll(i)
#     print(out)
#     if "STOP HERE" in out:

#         