name=input("Search name of brand car: ")
year=int(input("Enter year model:"))
prices=int(input("Search price of the car:"))
car = {
    'brand':['mazda','toyota','lamborghini','ford'],
    'year': [2008, 2010,2013,2015],
    'price':[450000,355000,1375000,299000]
}

if name in car['brand']:
    
    if name ==str('mazda') or name in car['brand'] and year==int(2008):
        if prices in car['price'] and int(450000)==prices or car['price'] and int(450000) >= prices:
            prices=int(450000)
            print("Search found!\n\nCar name:",name,"\nYear model:",year,"\nPrice is:",prices,"\n")
        elif car['price'] and int(450000)<=prices:
            prices =int(450000)
            print("Search found!\n\nbBut the price of",name, "is",prices,"only\n")
            
    elif name== str('toyota') or name in car['brand'] and year==int(2010):
        if prices in car['price'] and int(355000)==prices or car['price'] and int(355000) >= prices:
            prices=int(355000)
            print("Search found!\n\nCar name:",name,"\nYear model:",year,"\nPrice is:",prices,"\n")
        elif prices in car['price'] and int(355000)<=prices:
            prices=int(355000)
            print("Search found!\n\nBut the price of",name,"is",prices,"only\n")
            
    elif name== str('lamborghini') or name in car['brand'] and year==int(2013):
        if prices in car['price'] and int(1375000)==prices or car['price'] and int(1375000) >= prices:
            prices=int(355000)
            print("Search found!\n\nCar name:",name,"\nYear model:",year,"\nPrice is:",prices,"\n")
        elif prices in car['price'] and int(1375000)<=prices:
            prices=int(355000)
            print("Search found!\n\nBut the price of",name,"is",prices,"only\n")

    elif name== str('ford') or name in car['brand'] and year==int(2015):
        if prices in car['price'] and int(299000)==prices or car['price'] and int(299000) >= prices:
            prices=int(299000)
            print("Search found!\n\nCar name:",name,"\nYear model:",year,"\nPrice is:",prices,"\n")
        elif prices in car['price'] and int(299000)<=prices:
            prices=int(299000)
            print("Search found!\n\nBut the price of",name,"is",prices,"only\n")
    
else:
    print ("Search cannot found\n")
