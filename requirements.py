import mysql.connector as sqltor

mycon = sqltor.connect(host="localhost", user="root", passwd="1234", database="main_project") #auth_plugin='mysql_native_password')  

curs = mycon.cursor()


import pandas as pd
import pyfiglet
from pyfiglet import Figlet
from datetime import date
import twilio
from twilio.rest import Client

# COLORS: 

PURPLE = '\033[95m'
CYAN = '\033[96m'
DARKCYAN = '\033[36m'
BLUE = '\033[94m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
RED = '\033[91m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'
END = '\033[0m'



# customer details table ---   CHOICE 1
curs.execute("create table custom_details(name varchar(20), DOB date, Address varchar(150), Aadhaar_no bigint, check_in_date date, check_out_date date, Phone_no bigint)")

# ROOMS table  -- CHOICE 2
curs.execute("create table rooms(Room_Type varchar(25), Room_Rent_in_Rs int)")

arr = [("Single", 1000), ("Double", 2000), ("Triple", 3000), ("Quad", 4000), ("Queen Deluxe", 4500), ("King Deluxe", 4750), ("Twin Deluxe", 4850), ("Double-double Deluxe", 5000), ("Luxury Master Suite", 5500)]
curs.executemany("insert into rooms values(%s,%s)", arr)
mycon.commit()

# FOOD TABLE  ---- CHOICE 3
curs.execute("Create table food_and_beverages(S_No int, Beverages varchar(40), Cost_of_beverages int, Dishes varchar(50), Cost_of_dishes int )")
sno = [o for o in range(1,11)]
liquid = ["Tea", "Coffee", "Wine","Beer","Soup","Coca-Cola", "Milky Choco Shake", "Orange Juice", "Champagne", "Lemonade"]
liq_price = [99,99,199,249,299,99,159,149,399,79]
solid = ["Paneer Tikka", "Veg Manchurian", "Kadai Paneer","Palak Paneer","Malai Kofta","Plain Dosa", "Shahi Chicken Biryani", "Chicken Kebaab", "Chicken Lollipop", "Combo of Ras Malai and Gulab Jamun"]
sol_price = [199,299,399,549,399,299,559,649,499,179]

liq_food = list(zip(sno, liquid, liq_price,solid,sol_price))

curs.executemany("insert into food_and_beverages values(%s,%s,%s,%s,%s)", liq_food)
mycon.commit()


# LAUNDRY TABLE ---- CHOICE 4
curs.execute("create table laundry(S_No int, Men_Garments varchar(20), Rate_M int, Women_Garments varchar(20), Rate_W int)")
sno2 = [o for o in range(1,9)]
mens_clothing = ["Shirt", "T-shirt", "Trouser", "Suit", "Jacket", "Coat", "Kurta", "Pajama"]
mens_rate = [100,300,350,250,300,500,110,120]
womens_clothing = ["Top", "Skirt", "Saree", "Zari Saree", "Salwar", "Dupatta", "Kurta", "Long skirt"]  
womens_rate = [100,150,350,450,300,170,200,250]
laundry_data = list(zip(sno2, mens_clothing, mens_rate, womens_clothing, womens_rate ))
curs.executemany("insert into laundry values(%s,%s,%s,%s,%s)", laundry_data)
mycon.commit()


# GAME CLUB ---- CHOICE 5
curs.execute("create table club_games(S_No int, Games varchar(25), Charges_per_hour int)")
ser_num = [abk for abk in range(1,8)]
game_types = ["Golf", "Billiards and Snooker", "Table Tennis", "Bowling", "VR Games", "Video Games", "Pool Games"]
game_cost = [1000,300,450,500,700,650,900]
gameclub_data = list(zip(ser_num ,game_types, game_cost))
curs.executemany("insert into club_games values(%s,%s,%s)", gameclub_data)
mycon.commit()


# BILLING ----- CHOICE 6
curs.execute("create table total_bill(Customer_Name varchar(30), Check_IN_Date date, Check_OUT_Date date, Payment_Amount float(20,3))")

# FEEDBACK ----- choice 7
curs.execute("create table custom_feeds(Customer_Name varchar(30), FEEDBACK varchar(250))")

