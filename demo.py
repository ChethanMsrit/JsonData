import json

selectCity = input("Please Select the City:\n 1. Bengaluru\n 2.Chennai \n 3. Hyderabad\n 4.Mumbai\n 5.Delhi\n 6. Exit\n")

def timeManner(city):
    place = city +".json"
    f = open(place)
    data = json.load(f)
    options = input("Please select the type of data you need :\n 1. Hourly \n 2. For Next 6 Hourly \n 3. For Next 5 days\n 4.Exit\n")
    while(options != None ):
        if options == "1":
            today(data,city)
            return
        elif options == "2":
            nextSixHour(data,city)
            return
        elif options == "3":
            nextFiveDays(data,city)
            return
        else:
            exit()


def today(data,city):
    hourly = data['hourly']
    print("The Weather for ",city," is : ")
    print(hourly[0]['Temperature'] ['Value'], hourly[0]['Temperature'] ['Unit'] ) 

def nextSixHour(data,city):
    hourly = data['hourly']
    print("The Weather for next 6 hours ",city," is : ")
    i =0
    while(i < 5):
       print(hourly[i]['Temperature'] ['Value'], hourly[i]['Temperature'] ['Unit'] ) 
       i = i+1

def nextFiveDays(data,city):
    fiveDays = data['5-day']
    print("The Weather for next 5 days ",city," is :\n ")
    i =0
    while(i < 5):
       dateSplit = fiveDays[i]['Date']
       Min = fiveDays[i]['Temperature']['Minimum']['Value']
       Max = fiveDays[i]['Temperature']['Maximum']['Value']
       Avg = (Min+Max)/2
       print("Date - ", dateSplit.split("T")[0] ) 
       print("The Minimum Temperature is ",Min )
       print("The Maximum Temperature is ", Max)
       print("The Average Temperature is ", Avg)
       print()
       i = i+1
                

while(selectCity != '6'):
    if selectCity == '1' :
        timeManner('Bangalore')     
    elif selectCity == '2' :
        timeManner('Chennai')  
    elif selectCity == '3' :
        timeManner('Hyderabad')  
    elif selectCity == '4' :
        timeManner('Mumbai')  
    elif selectCity == '5' :
        timeManner('Delhi')



    











   



# f = open('Delhi.json')

# data = json.load(f)
 
# for i in data['hourly']:
#     print(i)
    
# f.close()