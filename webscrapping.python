import requests
import MySQLdb
from bs4 import BeautifulSoup
import pandas
import  argparse
import connect

oyo_url = "https://www.oyorooms.com/hostels-in-bangalore/?page="
page_num_MAX = 3

db = MySQLdb.connect(hotel_name, hotel_address, hotel_price, hotel_rating, amenities_list )
cur = db.cursor( )
cur.execute("USE scraping")

for page_num in range(1, page_num_MAX):
    req = requests.get(oyo_url)
    content = req.content

    soup = BeautifulSoup(content, "html.parser")

    all_hotels = soup.find_all("div", {"class": "ListingHotelCardWrapper"})
    scraped_info_list = [ ]

    for hotel in all_hotels:
         hotel_name = hotel.find("h3", {"class": "listingHotelDescription__hotelName"}).text
         hotel_address = hotel.find("span", {"itemprop": "streetAddress"}).text
         hotel_price = hotel.find("span",{"class": "listingPrice_finalPrice"}).text
         try:
             hotel_rating = hotel.find("span", {"class": "hotelRating__ratingSummer"}).text
         except AttributeError:
             pass

         parent_amenities_element = hotel.find("div", {"class": "amentityWrapper"})

         amentities_list = [ ]
         
        
         for amenity in parent_amentities_element.find_all("div", {"class": "amenityWrapper__amenity"}):
             amenities_list.append(amenity.find("span",{"class":, "d-body-sm"}).text.strip( ))

         scraped_info_list.append(hotel_dict)   
         
datatframe = pandas.DataFrame(scraped_info_list)
connect.get_hotel_info(args.dbname)
cur.close( )
db.close( )
