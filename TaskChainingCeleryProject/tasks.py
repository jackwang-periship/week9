'''
Created on Apr 18, 2017

@author: jackwang
'''
from __future__ import absolute_import
from TaskChainingCeleryProject.celery import app
import requests
from bs4 import BeautifulSoup
import bs4
import pprint


nws_weather_by_zip = "http://forecast.weather.gov/zipcity.php?inputstring="

@app.task()
def update_page_info(zipcode):
    # fetch_page -> parse_page -> store_page
    chain = fetch_page.s(zipcode) | parse_page.s() | store_page_result.s(zipcode)
    chain()

@app.task()
def fetch_page(zipcode):
    result = requests.get(nws_weather_by_zip+zipcode)
    return result.content

@app.task()
def parse_page(page):
    return parse_document(page)

@app.task(ignore_result=True)
def store_page_result(result, zipcode):
    target = open(zipcode, 'w') 
    target.write(result) 
    target.close()
    return True

def parse_document(page):
    
    soup = BeautifulSoup(page, 'html.parser')
    desc_TAG = soup.find("p", attrs={"class": "myforecast-current"})
    tempF_TAG  = soup.find("p", attrs={"class": "myforecast-current-lrg"})
    tempC_TAG = soup.find("p", attrs={"class": "myforecast-current-sm"})

    current_conditions_summary = {}
    current_conditions_summary['desc'] = returnVALUE(desc_TAG)
    current_conditions_summary['tempF'] = tempString2Float(returnVALUE(tempF_TAG))
    current_conditions_summary['tempC'] = tempString2Float(returnVALUE(tempC_TAG))

    current_conditions_detail = {}
    current_conditions_detail_TABLE = soup.find("div", attrs={"id": "current_conditions_detail"})
    if current_conditions_detail_TABLE is not None:
        allHeadingsTAG = current_conditions_detail_TABLE.find_all("td", attrs={"class": "text-right"})
        allValuesTAG = current_conditions_detail_TABLE.find_all("td", attrs={"class": None})
        allHeadings = [s.text.strip() for s in allHeadingsTAG]
        allValues = [s.text.strip() for s in allValuesTAG]
        current_conditions_detail = dict(zip(allHeadings, allValues))

        seven_day_forecast = soup.find("div", attrs={"id": "seven-day-forecast", "class": "panel panel-default"})
        panel_heading = seven_day_forecast.find("div", attrs={"class": "panel-heading"})
        headline = seven_day_forecast.find("div", attrs={"id": "headline-container"})
        seven_day_forecast_list = seven_day_forecast.find_all(class_="tombstone-container")

        period_tags = seven_day_forecast.select(".tombstone-container .period-name")
        periods = [pt.get_text() for pt in period_tags]
        short_descs = [sd.get_text() for sd in seven_day_forecast.select(".tombstone-container .short-desc")]
        temps = [t.get_text() for t in seven_day_forecast.select(".tombstone-container .temp")]
        descs = [d["title"] for d in seven_day_forecast.select(".tombstone-container img")]
    
    s1 = pprint.pformat(current_conditions_summary)
    s2 = pprint.pformat(current_conditions_detail)
    formated_seven_day_forecast = {}
    formated_seven_day_forecast['periods'] = periods
    formated_seven_day_forecast['short_descs'] = short_descs
    formated_seven_day_forecast['temps'] = temps
    formated_seven_day_forecast['descs'] = descs
    s3 = pprint.pformat(formated_seven_day_forecast)
    return(s1 + "\n" + s2 + "\n" + s3)

def returnVALUE(xTag):
    if xTag and type(xTag) is bs4.element.Tag:
        return xTag.text.strip()
    else:
        return ''

def tempString2Float(x):
    
    if x is None:
        return None
    temp = float(x[:-2]) 
    if x[-1]== 'F':
        c=(temp-32)*5/9
        return c
    if x[-1]== 'C':
        f =(temp*9/5)+32
        return f
    return None

