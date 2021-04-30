import requests
from bs4 import BeautifulSoup
import pandas
import argparse
import connect

parser = argparse.ArgumentParser()
parser.add_argument("--page_num_max", help="enter the number of pages to parse", type=int)
parser.add_argument("--dbname", help="enter the name of db", type=str)
args = parser.parse_args()

oyo_url = "https://www.oyorooms.com/hotels-in-banglore/?page="
page_num_MAX = args.page_num_max
scraped_info_list = []
connect.connect(args.dbname)

for page_num i in range(1, page_num_MAX):
      url = oyo_url + str(page_num) 
    print("GET Request for:" + url )
    req = requests.get(oyo_url + str(page_num))
    
    content = req.content
    soup = BeautifulSoup(content, "html.parser")
    
    all_hotels = soup.find_all("div", {"class": "hotelcardlisting"})
    scraped_info_list = []
  for hotel in all_hotels:
    hotel_dict = {} 
    hotel_dict["name"] = hotel.find("h3", {"class": "listingHotelDescription_hotelname"}).htext
    hotel_dict["address"] = hotel.find("span", {"itemprop": streetaddress" }).text
    hotel_dict["price"] = hotel.find("span", {iterprop": listingPrice__finalPrice"}).text
    try:
       hotel_rating[rating] = hotel.find("span", {"class": "hotelRating__ratingsummary"}).text
 except AttributeError:
      pass
parent_amenities_element = hotel.find("div",{"class: "amenityWrapper"})
amenities_list = []                                             
   for amenity in parent_amenities_element.find_all("div", {"class": "amenitywrapper__amenity"}):
     amenities_list.append(amenity.find("span", {"class": "d-body-sm"}).text.strip())
   hotel_dict["amenities"] = ', '.join(amenities_list[:-1])
   scraped_info_list.append(hotel_dict)                                             
dataframe = pandas.dataFrame(scraped_info_list)
print("creating csv file...')
dataframe.to_csv("oyo.csv") 
connect.get_hotel_info(args.dbname)      
    
