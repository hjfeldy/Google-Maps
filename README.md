# Google Maps Geo-Scraper
I found myself needing the latitude and longitude of very many cities, and was racking up some fees from Google Places API. Since Google maps is free to use, and the latitude and longitude appear directly in the URL, it seemed silly to pay for that information. So I wrote this script! In and of itself, latitude and longitude isn't very helpful, but if you *already have* certain information for a bunch of places, this is a great way to get the data needed in order to generate a heatmap using the (far cheaper) gmaps widget. 
## Extract latitude and longitude values from a list of places (No API needed!)

In order for this script to work, you will need:
Firefox
Selenium (install with pip or conda)
[Geckodriver](https://github.com/mozilla/geckodriver/releases/tag/v0.28.0)

Geckodriver must be added to your [PATH](https://www.youtube.com/watch?v=iTyK5KGNx-Y)

## Instructions:
* Add a list of places to config.py -- these will be the search terms entered into Google
* Fill in the dsired filename for csv output in config.py
* Run main.py
* Enjoy your free latitude and longitude information!

