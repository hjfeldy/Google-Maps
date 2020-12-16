from selenium import webdriver
from selenium.webdriver import FirefoxOptions
from selenium.webdriver.common.keys import Keys
import pandas as pd
from config import places, filename
import re, time, sys
tm = time.time()
coordPattern = re.compile(r'@(-?\d+\.\d+),(-?\d+\.\d+)')

def getCoords(url):
    lat = float(coordPattern.search(url).group(1))
    lng = float(coordPattern.search(url).group(2))
    return lat, lng

opts = FirefoxOptions()
opts.headless = True
driver = webdriver.Firefox()

timeout = False
df = {'Place': [], 'Lat': [], 'Lng': []}
for place in places:
    #Go to maps
    driver.get('https://Google.com/maps')
    time.sleep(1)

    #Input place
    elem = driver.find_element_by_id('searchboxinput')
    elem.send_keys(place)
    time.sleep(.5)

    #Send request
    elem.send_keys(Keys.RETURN)
    while driver.current_url == 'https://www.google.com/maps':
        continue
    check = time.time()
    while 'search' in driver.current_url:
        timeElapsed = time.time() - check
        if timeElapsed > 5:
            timeout = True
            print(f'Google couldn\'t find any results for {place}. Try being more specific.')
            break
        continue

    if timeout:
        timeout = False
        continue

    url = driver.current_url
    try:
        lat, lng = getCoords(url)
    except:
        print(f'Error at {place}')
        print(f'URL: {url}')
        continue
    df['Place'].append(place)
    df['Lat'].append(lat)
    df['Lng'].append(lng)
    print(f'{place}: ({lat}, {lng})')

df = pd.DataFrame(df)

if filename == '':
    filename = input('You seem to have left the filename field unchanged in config.py. What would you like to name the csv file?')
    while filename[-4:] != '.csv':
        filename = input('Error: You must name it as a CSV file.\nWhat would you like to name the csv file?')

filename = 'Data/' + filename
df.to_csv(filename)

driver.quit()
complete = (time.time() - tm) / 60

print(f'It took you {complete} minutes to scrape {len(places)} places!')