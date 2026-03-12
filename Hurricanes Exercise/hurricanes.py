# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']


# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']


# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]


# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]


# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]


# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']


# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]


# 1
# Update Recorded Damages
conversion = {"M": 1000000,
              "B": 1000000000}


# test function by updating damages
new_damages = []
def updated_damages(info):
  for i in damages:
    damage_str = i
    if i == 'Damages not recorded':
      new_damages.append(i)
    else:
      numeric_part = float(damage_str[:-1])
      suffix = damage_str[-1]
      if 'M' in suffix:
        converted_num = (conversion['M'] * numeric_part)
        new_damages.append(converted_num)
      elif 'B' in suffix:
        converted_num = (conversion['B'] * numeric_part)
        new_damages.append(converted_num)
  return new_damages
updated_damages(damages)


# 2
# Create a Table
# Create and view the hurricanes dictionary
def new_hurricanes():
  keys = ["Name", "Month", "Year", "Max Sustained Wind", "Areas Affected", "Damage", "Deaths"]
  zipped_data = zip(names, months, years, max_sustained_winds, areas_affected, new_damages, deaths)
  hurricanes = {name: dict(zip(keys, data)) for name, data in zip(names, zipped_data)}
  return hurricanes

hurricanes = new_hurricanes()


# 3
# Organizing by Year
# create a new dictionary of hurricanes with year and key
def hurricanes_by_year(hurricanes):
    hurricanes_by_year = {}
    for hurricane in hurricanes.values():
        current_year = hurricane["Year"]
        current_cane = hurricane
        if current_year not in hurricanes_by_year:
          hurricanes_by_year[current_year] = [current_cane]
        else:
          hurricanes_by_year[current_year].append(current_cane)
    return hurricanes_by_year
hurricanes_by_year(hurricanes)


# 4
# Counting Damaged Areas
# create dictionary of areas to store the number of hurricanes involved in
def count_areas(hurricanes):
    areas_affected = {}
    for hurricane in hurricanes.values():
        for area in hurricane["Areas Affected"]:
            if area not in areas_affected:
                areas_affected[area] = 1
            else:
                areas_affected[area] += 1
    return areas_affected
areas_affected = count_areas(hurricanes)


# 5
# Calculating Maximum Hurricane Count
# find most frequently affected area and the number of hurricanes involved in
def most_affected(areas_affected):
    max_area = ''
    max_area_count = 0
    for area, count in areas_affected.items():
        if count > max_area_count:
            max_area = area
            max_area_count = count
    return max_area, max_area_count
variable = most_affected(areas_affected)


# 6
# Calculating the Deadliest Hurricane
# find highest mortality hurricane and the number of deaths
def deadliest_hurricane(hurricanes):
  max_mortality_cane = ''
  max_mortality = 0
  for area, count in hurricanes.items():
    if count['Deaths'] > max_mortality:
      max_mortality_cane = area
      max_mortality = count['Deaths']
  return max_mortality_cane, max_mortality
deadliest = deadliest_hurricane(hurricanes)


# 7
# Rating Hurricanes by Mortality
def mortality_ratings(hurricanes):
  mortality_scale = {0: 0, 1: 100, 2: 500, 3: 1000, 4: 10000}
  rated_canes = {0: [], 1: [], 2: [], 3: [], 4: []}
  for count in hurricanes.values():
    if count['Deaths'] < mortality_scale[1]:
      rated_canes[0].append(count['Name'])
      rated_canes[0].append(count['Deaths'])
    elif count['Deaths'] >= mortality_scale[1] and count['Deaths'] < mortality_scale[2]:
      rated_canes[1].append(count['Name'])
      rated_canes[1].append(count['Deaths'])
    elif count['Deaths'] >= mortality_scale[2] and count['Deaths'] < mortality_scale[3]:
      rated_canes[2].append(count['Name'])
      rated_canes[2].append(count['Deaths'])
    elif count['Deaths'] >= mortality_scale[3] and count['Deaths'] < mortality_scale[4]:
      rated_canes[3].append(count['Name'])
      rated_canes[3].append(count['Deaths'])
    elif count['Deaths'] >= mortality_scale[4]:
      rated_canes[4].append(count['Name'])
      rated_canes[4].append(count['Deaths'])
  return rated_canes
mortality = mortality_ratings(hurricanes)
# categorize hurricanes in new dictionary with mortality severity as key
def greatest_damage(hurricanes):
  max_damage_cane = ''
  max_damage = 0
  for area, count in hurricanes.items():
    if count['Damage'] == 'Damages not recorded':
      max_damage_cane = count['Damage']
    elif count['Damage'] > max_damage:
      max_damage_cane = area
      max_damage = count['Damage']
  return max_damage_cane, max_damage
greatest = greatest_damage(hurricanes)


# 8 Calculating Hurricane Maximum Damage
# find highest damage inducing hurricane and its total cost
def damages_ratings(hurricanes):
  damage_scale = {0: 0, 1: 100000000, 2: 1000000000, 3: 10000000000, 4: 50000000000}
  rated_damages = {0: [], 1: [], 2: [], 3: [], 4: []}
  for count in hurricanes.values():
    if count['Damage'] == 'Damages not recorded' or count['Damage'] < damage_scale[1]:
      rated_damages[0].append(count['Name'])
      rated_damages[0].append(count['Damage'])
    elif count['Damage'] < damage_scale[2]:
      rated_damages[1].append(count['Name'])
      rated_damages[1].append(count['Damage'])
    elif count['Damage'] < damage_scale[3]:
      rated_damages[2].append(count['Name'])
      rated_damages[2].append(count['Damage'])
    elif count['Damage'] < damage_scale[4]:
      rated_damages[3].append(count['Name'])
      rated_damages[3].append(count['Damage'])
    elif count['Damage'] > damage_scale[4]:
      rated_damages[4].append(count['Name'])
      rated_damages[4].append(count['Damage'])
  return rated_damages
damages = damages_ratings(hurricanes)

# 9
# Rating Hurricanes by Damage
damage_scale = {0: 0,
                1: 100000000,
                2: 1000000000,
                3: 10000000000,
                4: 50000000000}

# categorize hurricanes in new dictionary with damage severity as key
def greatest_severity(hurricanes):
  max_severity_cane = ''
  max_severity = 0
  for area, count in hurricanes.items():
    if count['Damage'] == 'Damages not recorded':
      max_severity_cane = count['Damage']
    elif count['Damage'] > max_severity:
      max_severity_cane = area
      max_severity = count['Damage']
  return max_severity_cane, max_severity
greatest = greatest_severity(hurricanes)