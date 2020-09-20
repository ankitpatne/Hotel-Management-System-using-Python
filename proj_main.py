
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






hotel_name = Figlet(font='jazmine')
print(hotel_name.renderText('RADISON \t BLUE\n HOTEL\t AND\t LODGING'))
print()
print()
print('\033[92m' + '\033[4m' + '\033[94m' + '\033[1m' + "WELCOME TO RADISON BLUE HOTEL AND LODGING" + '\033[0m')
print()
print()
print(BOLD + YELLOW + "The city’s financial hub, parliament, stadium, offices and shopping districts are all located within close proximity; as is a flourishing art and heritage precinct with must visit museums, art galleries, churches and synagogues. The airports are an hour away. For those who would like to experience fine dining in style, we host 9 of the city’s most acclaimed restaurants and bars, renowned for delectable cuisines from India, Europe, the Middle East and the Orient. Relish authentic Indian cuisine at Masala Kraft; world famous Japanese dishes at Wasabi by Morimoto; exquisite Eastern Mediterranean food at Souk and Chinese at Golden Dragon. Dine all day at Shamiana and choose from the exotic range of sumptuous desserts at La Patisserie." + END)
print()
print()
print(GREEN + "Our dedicated services towards our guests and the facilities and amenities provided to all, makes the hotel one of the most recommended one in the city. We are available 24 x 7 for our customers.Thank you for choosing us. Here are the following details to reach us: " + END )
print()
print(BOLD + "Email: Generalmanager.radisonblue@gmail.com , Get Assistance: +91 8800880450, +91 8800880455" + END)
print()
print()
print(BOLD + "Hotel Policies \n Check-in from 2:00 PM \n Check-out till 12:00 PM \n Early check-in and late check-out on request \n We accept American Express, Diner's Club, Master Card, Visa, JCB International \n Pets are not allowed." + END)
print()
print()
a = "N/A"
b = "N/A"
c = "N/A"
d = "N/A"
e = input("Enter your CHECK IN DATE in the format (yyyy-mm-dd): ")
f = input("Enter your CHECK OUT DATE in the format (yyyy-mm-dd): ")
print()
print()
room_rent = 100
rest_bill = 0
lau_cost = 0
game_bill = 0
grand_total = 0
print()


while True:
    print()
    print()

    print(BOLD + "What would you like to do? " + END)
    print()
    print('\033[92m' + "1.--> Enter 1 to fill customer details (CHECK IN).")
    print()
    print("2.--> Enter 2 to Calculate rommrent.")
    print()
    print("3.--> Enter 3 to Calculate restaurant bill.")
    print()
    print("4.--> Enter 4 to Calculate laundry bill.")
    print()
    print("5.--> Enter 5 to Calculate club and gamebill.")
    print()
    print("6.--> Enter 6 to Show Main Bill (Agg. Total).")
    print()
    print("7.--> Enter 7 to EXIT (CHECK OUT)." + '\033[0m')
    print()
    print()
    print()



    choice = int(input("ENTER YOUR CHOICE: "))

    if choice == 1:
        print()
        print()
        today = date.today()
        d2 = today.strftime("%B %d, %Y")
        print(BLUE + BOLD + "Date: " + str(d2) + END)
        print()
        print()                                                # CHOICE 1 CUSTOMER DATA
        custom_fig1 = Figlet(font='big')
        print(custom_fig1.renderText('C U S T O M E R   D A T A :'))
        a = input("Enter your name: ")
        b = input("Enter your date of birth in the format (yyyy-mm-dd): ")
        c = input("Enter your resedential address: ")
        d = int(input("Enter your aadhaar number: "))
        mob_num = int(input("Enter your mobile number: "))
        curs.execute("select Phone_no from custom_details")
        print()
        rec = curs.fetchall()
        ph_nums = []
        for row in rec:
            ph_nums.append(row[0])
        if mob_num in ph_nums:
            print()
            print(DARKCYAN + "Welcome Back, " + a + " !!" + END)
            discount = 15/100
        else:
            discount = 1

        det = (a,b,c,d,e,f,mob_num)
        print(BOLD + GREEN + "Name: " + a)
        print()
        print("Date of Birth: " + b)
        print()
        print("Resedential Address: " + c)
        print()
        print("Aadhaar Number: " + str(d))
        print()
        print("Phone Number: " + str(mob_num))
        print()
        print("CHECK IN DATE: " + str(e))
        print()
        print("CHECK OUT DATE: " + str(f) + END)


        curs.execute("insert into custom_details values(%s,%s,%s,%s,%s,%s,%s)", det)
        mycon.commit()
        print()
        print()
        print()


    elif choice == 2:                                                                   # CHOICE 2 ROOMRENT
        custom_fig2 = Figlet(font='roman')
        print(custom_fig2.renderText('ROOMS'))
        print()
        print(RED + BOLD + "May we show you to your room?" + END)
        print()
        print(BOLD + DARKCYAN + "Choose from 220 rooms and suites with spacious walk in closets, Italian marble bathrooms, teak floors and oak wood desks.\n Breathe easy with state of the art air purification systems that assure air quality on par with global best standards." + END)
        print()
        print(BOLD + YELLOW + "Relax. Replenish. Rejuvenate.\n Our spa, swimming pool and fitness centre in hotel provide the perfect\n escape from a busy schedule and the rush of a bustling city." + END)
        print()
        in_date = date(int(e[:4]), int(e[5:7]), int(e[8:]))                  # yyyy-mm-dd
        out_date = date(int(f[:4]), int(f[5:7]), int(f[8:]))
        n = out_date - in_date        




        print (BOLD + "We have a variety of rooms available for you:-" + END)
        print()
        print()
        
        xy = pd.DataFrame()
        xy["Rooms"] = ["Single","Double","Triple","Quad","Queen Deluxe","King Deluxe","Twin Deluxe", "Double-double Deluxe", "Luxury Master Suite"]

        xy["Price(INR/Night)"] = [1000,2000,3000,4000,4500,4750,4850,5000,5500]
        xy.index += 1
        
        print("-"*50)
        print()
        print(xy)
        print()
        print("-"*50)
        ch = int(input("Which room would you like to opt for? "))
        print()
        print()



        room_rent = 0                                                   
        for rom in list(xy.index):
            if ch in list(xy.index) and ch == rom:
                room_rent += n.days*xy.iat[rom-1, 1]
                print("You have opted for " + xy.iat[rom-1, 0] + " Bedroom." + " CHARGES: Rs. " + str(xy.iat[rom-1, 1]) + " PER NIGHT.")
                print()
                #print(room_rent)
                print(BLUE + "Number of days spent in the hotel: " + str(n.days) + END)
                print()
                # room_rent = n.days*pay                                                                                   # ROOM RENT BILL
                print(BOLD + CYAN + UNDERLINE + "Your total room rent is Rs. " + str(room_rent) + END)
                



        
 
        print()
        print()
        print()
    
    elif choice == 3:                                                                     # CHOICE 3 RESTAURANT
        custom_fig3 = Figlet(font='big')
        print(custom_fig3.renderText('R ESTAUR AN T   S E R V I C E : '))
        print()
        print()
        print(CYAN + BOLD +  "Where would you like to dine?" + END)
        print()
        print(BOLD + "From the classic to the casual, from the Oriental to modern authentic Indian, there is much to delight the palate at The Radison Blue, New Delhi." + END)
        fod_cost = 0
        bvg_cost = 0
        purchases = []
        costs = []
        qq1 = []
        while True:
            
            food = int(input("What would you like to have now? \n 1.Beverages \n 2.Food --\n ENTER A NUMBER (1 or 2) OR Enter 3 to EXIT the restaurant menu !!"))

            

            if food == 1:
                custom_fig4 = Figlet(font='bubble')
                print(custom_fig4.renderText('BEVERAGES'))
                print()
                print("*"*50)
                print()
                print()
                bvg = pd.DataFrame()
                bvg["BEVERAGES"] = ["Tea", "Coffee", "Wine","Beer","Soup","Coca-Cola", "Milky Choco Shake", "Orange Juice", "Champagne", "Lemonade"]
                bvg["Price(INR)"] = [99,99,199,249,299,99,159,149,399,79]
                bvg.index += 1
                print(bvg)
                print()
                print()
                print("*"*50)
                print()
                
                
                
                while True:
                    bvg_ch = int(input("Please enter your choice: "))

                    for bb in list(bvg.index):
                        if bvg_ch in list(bvg.index) and bvg_ch == bb:
                            bvg_q = int(input("Please enter the quantity"))
                            bvg_cost += bvg.iat[bvg_ch-1,1]*bvg_q
                            purchases.append(bvg.iat[bvg_ch-1,0])
                            costs.append(bvg.iat[bvg_ch-1,1]*bvg_q)
                            qq1.append(bvg_q)




                    bvg_more = input("Do you want to have any other beverage also ? (y/n)")
                    if bvg_more == "n" or bvg_more == "N":
                        break
                    else:
                        continue

            elif food == 2:
                custom_fig5 = Figlet(font='bubble')
                print(custom_fig5.renderText('FOOD'))
                print()
                print("*"*50)
                print()
                print()
                fod = pd.DataFrame()
                fod["DISHES"] = ["Paneer Tikka", "Veg Manchurian", "Kadai Paneer","Palak Paneer","Malai Kofta","Plain Dosa", "Shahi Chicken Biryani", "Chicken Kebaab", "Chicken Lollipop", "Combo of Ras Malai and Gulab Jamun"]
                fod["Price(INR)"] = [199,299,399,549,399,299,559,649,499,179]
                fod.index += 1
                print(fod)
                print()
                print()
                print("*"*50)
                print()
                
                
                while True:
                    fod_ch = int(input("Please enter your choice: "))

                    for cc in list(fod.index):
                        if fod_ch in list(fod.index) and fod_ch == cc:
                            fod_q = int(input("Please enter the quantity"))
                            fod_cost += fod.iat[fod_ch-1,1]*fod_q
                            purchases.append(fod.iat[fod_ch-1,0])
                            costs.append(fod.iat[fod_ch-1,1]*fod_q)
                            qq1.append(fod_q)


                    


                    fod_more = input("Do you want to have any other dish also ? (y/n)")
                    if fod_more == "n" or fod_more == "N":
                        break
                    else:
                        continue
            else:
                break

        prev1 = pd.DataFrame()
        prev1["Items"] = purchases
        prev1["Quantity"] = qq1
        prev1["Cost"] = costs
        prev1.index += 1
        print()
        print(BOLD + "Your expenses in the restaurant are: " + END)
        print()
        print("-"*60)
        print()
        print(prev1)
        print()
        print("-"*60)
        rest_bill = bvg_cost +  fod_cost                                                # food bill

        print()
        print(BOLD + GREEN + UNDERLINE + "Your restaurant bill is Rs." + str(rest_bill) + END)
        
        # also see if we could insert images in the food menu tomorrow
        print()
        print()
        print()
    
    elif choice == 4:                                                        # CHOICE 4 LAUNDRY 
        custom_fig6 = Figlet(font='big')
        print(custom_fig6.renderText('E X P R E S S              L A U N D R Y : '))
        gg = []
        ff = []
        qq = []


        

        print()
        print()
        print(BOLD + BLUE + "We provide our customers with express laundry services on their finger tips. Ring us anytime and we will assist you in the next 5 minutes. Express laundry services are more than capable of offering a wide variety of washing and drying methods that suit your clothes. Whether you are allergic to a specific detergent or your items are made of delicate fibers needing special treatment, the laundry services are equipped to meet your needs. We are available 24/7 !!" + END)
        print()
        print()
        print(BOLD + "Express Laundry Service -- RATECARD" + END)
        print()
        print("-"*60)
        print(RED + "FOR MEN: " + END)
        print()
        lau_men = pd.DataFrame()
        lau_men["Garment Type"] =["Shirt", "T-shirt", "Trouser", "Suit", "Jacket", "Coat", "Kurta", "Pajama"]
        lau_men["Rate"] = [100,300,350,250,300,500,110,120]
        lau_men.index += 1
        print(lau_men)
        print()
        print("-"*60)
        print()
        print(BLUE + "FOR WOMEN: " + END)
        lau_women = pd.DataFrame()
        lau_women["W-Garment Type"] =["Top", "Skirt", "Saree", "Zari Saree", "Salwar", "Dupatta", "Kurta", "Long skirt"]
        lau_women["W-Rate"] = [100,150,350,450,300,170,200,250]
        lau_women.index += 1
        print(lau_women)
        print()
        print("-"*60)
        lau_cost = 0                                                                # LAUNDRY BILL
        while True:
            lau_choi = input("Select clothing type for laundry service. Enter M for Men's Clothing and enter W for Women's Clothing: ")
            if lau_choi == "M" or lau_choi == "m":
                men_choi = int(input("Select the types of clothes for laundry from the above ratecard for men by entering respective numbers for garment type: "))
                quantity_men = int(input("Enter the quantity: ")) 
                for lau in list(lau_men.index):
                    if men_choi in list(lau_men.index) and men_choi == lau:
                        lau_cost += quantity_men*lau_men.iat[lau-1, 1]
                        gg.append(lau_men.iat[lau-1, 0])
                        qq.append(quantity_men)
                        ff.append(quantity_men*lau_men.iat[lau-1, 1])


            else:
                women_choi = int(input("Select the types of clothes for laundry from the above ratecard for women by entering respective numbers for garment type: "))
                quantity_women = int(input("Enter the quantity: "))  
                for lau in list(lau_women.index):
                    if women_choi in list(lau_women.index) and women_choi == lau:
                        lau_cost += quantity_women*lau_women.iat[lau-1, 1]
                        gg.append(lau_women.iat[lau-1, 0])
                        qq.append(quantity_women)
                        ff.append(quantity_women*lau_women.iat[lau-1, 1])

            ffg = input("Do you want to add more clothes to your list? Enter Y for yes, if not, enter N for no. ")
            if ffg == "y" or ffg == "Y":
                continue
            else:
                break
        # curs.execute("create table laundry(S_No int, Men_Garments varchar(20), Rate_M int, Women_Garments varchar(20), Rate_W int)")
        # sno2 = [o for o in range(1,9)]
        # mens_clothing = ["Shirt", "T-shirt", "Trouser", "Suit", "Jacket", "Coat", "Kurta", "Pajama"]
        # mens_rate = [100,300,350,250,300,500,110,120]
        # womens_clothing = list(lau_women.iloc[:,0])      # directly creating a list from dataframe 
        # womens_rate = list(lau_women.iloc[:,1])
        prev2 = pd.DataFrame()
        prev2["Clothes_for_Laundry"] = gg
        prev2["Quantity"] = qq
        prev2["Expenditure"] = ff
        print()
        print()
        print(BOLD + CYAN + "Your expenses in laundry are: " + END)
        print()
        print("-"*60)
        print()
        print(prev2)
        print()
        print("-"*60)
        print()
        print()
        print(BOLD + CYAN + UNDERLINE + "Your laundry bill is " + str(lau_cost) + END)
        
        # laundry_data = list(zip(sno2, mens_clothing, mens_rate, womens_clothing, womens_rate ))
        # curs.executemany("insert into laundry values(%s,%s,%s,%s,%s)", laundry_data)
        # mycon.commit()
        print()
        print()
        print()


    
    elif choice == 5:                                                         # CHOICE 5 CLUB AND GAME BILL
        custom_fig7 = Figlet(font='univers')
        print(custom_fig7.renderText('CLUB  & GAMES'))
        prev3 = pd.DataFrame()
        xx = []
        yy = []
        zz = []

        print()
        print()
        print("-"*60)
        print()
        clubg = pd.DataFrame()
        clubg["GAMES"] = ["Golf", "Billiards and Snooker", "Table Tennis", "Bowling", "VR Games", "Video Games", "Pool Games"]
        clubg["COST (per hour)"] = [1000,300,450,500,700,650,900]
        clubg.index += 1
        print(clubg)
        print()
        print("-"*60)
        print()
        print()
        game_bill = 0                                                          # GAME BILL
        while True:
            game_play = int(input("Which Game would you like to play? "))
            for gam in list(clubg.index):
                if game_play in list(clubg.index) and game_play == gam:
                    hours_played = int(input("For how many hours did you play? "))
                    kh = hours_played*clubg.iat[gam-1, 1]
                    game_bill += kh
                    xx.append(clubg.iat[gam-1, 0])
                    yy.append(hours_played)
                    zz.append(kh)
            more_play = input("Do you wanna play another games? Enter Y for YES, enter N for NO: ")
            if more_play == "y" or more_play == "Y":
                continue
            else:
                print(BOLD + CYAN + UNDERLINE + "Your total Game & Club bill is: " + str(game_bill) + END)
                break

        print()
        prev3["Games Played"] = xx
        prev3["Hours Played"] = yy
        prev3["Expenditure"] = zz
        print()
        print(BOLD + CYAN + "Your Expenses in Club & Games are: " + END)
        print()
        print(prev3)

        print()
        print()
    

    elif choice == 6:                                                                   # CHOICE 6 TOTAL BILL
        Total_Bill = Figlet(font='roman')
        print(Total_Bill.renderText('HOTEL BILL'))
        hotel_bill = pd.DataFrame()
        print()

        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y")
        print(PURPLE + BOLD + "Date: " + str(dt_string))	
        print("Time: " + now.strftime("%H:%M:%S") + END )       
        print()
        print()
        print(BOLD + GREEN + "Customer Name: " + a + END)
        print()
        print(BOLD + GREEN + "Check IN date: " + e + END)
        print()
        print(BOLD + GREEN + "Check OUT date: " + f + END)
        print()
        print()
        print(PURPLE + BOLD + "Your various expenses are summarised below: " + END)
        print()
        print(CYAN + "1. Restaurant Expenses: " + END)
        print()
        print(prev1)
        print()
        print()
        print(CYAN + "2. Laundry Expenses: " + END)
        print()
        print(prev2)
        print()
        print()
        print(CYAN + "3. Club & Games Expenses: " + END)
        print()
        print(prev3)
        print()
        print()
        print(PURPLE + "Total Bill: " + END)

        print()
        print("="*60)
        print()
        print()
        
        cgst = 9/100
        sgst = 9/100

        hotel_bill["SERVICES"]  = ["ROOM",'RESTAURANT','LAUNDRY','GAMES & CLUB']
        hotel_bill["CHARGES"] = [room_rent, rest_bill, lau_cost, game_bill]
        hotel_bill["CGST"] = [cgst*room_rent, cgst*rest_bill, cgst*lau_cost, game_bill*cgst]
        hotel_bill["SGST"] = [sgst*room_rent, sgst*rest_bill, sgst*lau_cost, game_bill*sgst]
        hotel_bill["TOTAL AMOUNT"] = [room_rent + 2*cgst*room_rent, rest_bill + 2*cgst*rest_bill, lau_cost + 2*sgst*lau_cost, game_bill + 2*game_bill*sgst ]
        hotel_bill.index += 1 
        print(hotel_bill)
        print()
        print()
        print("="*60)
        print()
        print()
        grand_total = hotel_bill.iat[0,4] + hotel_bill.iat[1,4] + hotel_bill.iat[2,4] + hotel_bill.iat[3,4]
        if mob_num in ph_nums:
            print(BOLD + GREEN + "PROMOTION APPLIED..!! Congratulations..!" + END)
            print(BOLD + BLUE + "Since you are a returning customer you will be getting an additional discount of 15%..! Thank You for chosing our services again..!! " + END)
            grand_total -= discount*grand_total
        else:
            print()
        print(BOLD + DARKCYAN + UNDERLINE + "GRAND TOTAL IS: " + str(round(grand_total, 2)) + END)
        print()

        # Find these values at https://twilio.com/user/account

        account_sid = "AC794d7cfa30f5728f05ffa3e26effdef8"
        auth_token = "f8e38798d7bd9895332970d6ca1c8b1a"
        client = Client(account_sid, auth_token)

        payment_method = int(input("Select Payment Method: 1.Credit Card 2. Debit Card 3.PayTm Wallet 4.Cash: "))
        if payment_method == 1 or payment_method == 2:
            card_no = int(input("Enter card number: "))
            exp_date = input("Enter card expiry date in the format(mm/yy): ")
            cvv = int(input("Enter CVV number: "))
            if len(str(card_no)) < 16 or len(str(card_no)) > 16 or len(exp_date) > 5 or len(exp_date) < 5 or "/" not in exp_date or len(str(cvv)) > 3 or len(str(cvv)) < 3:
                print(BOLD + RED + "INVALID CARD DETAILS ENTERED !!! TRANSACTION FAILED !!" + END)
                continue
            else:
                client.messages.create(                  
                    to="+919607419237",
                    from_="+15087611283",
                    body="Hello there! Your bank account is credited with an amount of Rs. " + str(grand_total))
                print(BOLD + GREEN + "TRANSACTION SUCCESSFUL ! THANK YOU !" + END)
        elif payment_method == 3:
                     
            #print(GREEN + BOLD + UNDERLINE + "Payment Successful !!" + END)



            mob_no = int(input("Please enter your mobile number registered with your PayTm account: "))
            if len(str(mob_no)) < 10 or len(str(mob_no)) > 10:
                print(BOLD + RED + "Invalid Mobile Number Entered !! TRANSACTION FAILED !" + END)
                continue
            else:


                client.messages.create(
                    to="+919607419237",
                    from_="+15087611283",
                    body="Hello there! Your Paytm wallet is credited with an amount of Rs. " + str(grand_total))




                print(BOLD + GREEN + "TRANSACTION SUCCESSFULL !! THANK YOU ! " + END)
        else:
            print(BOLD + GREEN + "CASH PAYMENT ACCEPTED !! PAYMENT SUCCESSFULL ! THANK YOU !!" + END)


        # curs.execute("create table total_bill(Customer_Name varchar(30), Check_IN_Date date, Check_OUT_Date date, Payment_Amount int)")
        curs.execute("insert into total_bill values(%s,%s,%s,%s)", (a, e, f, float(round(grand_total, 2))))
        mycon.commit()
        print()
        print()
        print()

            
    elif choice == 7:                                                       # CHOICE 7 EXIT

        # print("Thank You !!")
        gg = input("Would you like to give us a feedback? We will be grateful to you if you share your experience with us. ENTER Y for YES, or N for NO.: ")
        if gg == "y" or gg == "Y":
            rate = float(input("On a scale of 1 to 10 what would you like to rate us? "))
            if rate < 8:
                print(GREEN + "Thank you for rating us. We are regularly improving our services for the customers. Next target 10/10 rating !!!" + END )
            else:
                print(GREEN + "We are extremely happy that you enjoyed the experience here with us !! Thanks for giving us a chance to serve you !!" + END)
            print()
            print()
            print(BOLD + "Please enter your feedback here: " + END)
            print()
            feed = input("FEEDBACK: ")
            curs.execute("insert into custom_feeds values(%s,%s)", (a,feed))
            mycon.commit()
            print(BOLD + UNDERLINE + "Your feedback: " + END)
            print()
            print(feed)
            print()
            print()
            wishing = Figlet(font='roman')
            print(wishing.renderText('Thanks For Visiting Us !!'))

        else:
            wishing = Figlet(font='roman')
            print(wishing.renderText('Thanks For Visiting Us !!'))
        break
