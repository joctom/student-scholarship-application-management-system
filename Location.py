import os 
import json 


phil_json = os.path.join("DATA","philippines.json")

with open(phil_json, "r") as phil_read:
    phil_data = json.load(phil_read)

region = []
province = []
municipality = []  
brgy = []
def region_list():
    for each_region in phil_data.keys():
        region.append(each_region)

region_list()

def province_select(region):
    province.clear()
    for each_province in phil_data[region]['province_list'].keys():
       province.append(each_province)
    return list(province)



def municipality_select(regionx, provincex):
    municipality.clear()
    for each_city in phil_data[regionx]['province_list'][provincex]['municipality_list'].keys():
       municipality.append(each_city)
    return list(municipality)

regionx = "REGION IV-A"
provincex = "QUEZON"
cityx="LUCENA CITY"

def brgy_select(regionx, provincex, cityx):
    brgy.clear()
    for each_brgy in phil_data[regionx]['province_list'][provincex]['municipality_list'][cityx]['barangay_list']:
       brgy.append(each_brgy)
    return list(brgy)


