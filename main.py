import menu
import time
import os
from prettytable import PrettyTable

class Admin:
    def __init__(self,username,password) -> None:
        self.username=username
        self.password=password


class Car:
    def __init__(self,brand,model,mileage,rent,licensePlate):
        self.brand=brand
        self.model=model
        self.mileage=mileage
        self.rent=rent
        self.licensePlate=licensePlate
        self.available=True
   
    def __str__(self):
        return f"{self.licensePlate}"

class Customer:
    pass
    

 

class RentalSystem:
    cars=[]
    customers=[]
    admin=Admin("admin","admin")
    def addCar(self):
        os.system("cls")
        print("Login > Admin Menu > Manage Cars > Add Car")
        brand=input("Enter Car Brand: ")
        model=input("Enter Car Model: ")
        plateNum=input("Enter License Plate: ")
        try:
            rent=int(input("Enter rent (pkr/hr): "))
        except:
            print("Please enter an integer...")
            time.sleep(1.7)
            return
        try:
            milage=int(input("Enter mileage (km): "))
        except:
            print("Please enter an integer...")
            time.sleep(1.7)
            return
    
        
        for car in self.cars:
            if plateNum==car.licensePlate:
                print("The License Plate already exists")
                time.sleep(2)
                return
        self.cars.append(Car(brand,model,milage,rent,plateNum))
        print("The Car was successfully added...")
        time.sleep(1.7)
    def removeCar(self):
        os.system("cls")
        print("Login > Admin Menu > Manage Cars > Remove Car")
        plateNum=input("Enter license plate num of the car you want to remove: ")
        initialCount=len(self.cars)
        self.cars=[car for car in self.cars if car.licensePlate!=plateNum]
        if(len(self.cars)<initialCount):
            print("Car successfully removed...")
            time.sleep(1.7)
        else:
            print("No Car Found....")
            time.sleep(1.7)

                
        
        
    def viewCars(self):
        os.system("cls")
        print("Login > Admin Menu > Manage Cars > View Cars")
        t=PrettyTable(["Brand","Model","Mileage","Rent","License Plate","Available"])
        if(len(self.cars)>0):
            for car in self.cars:
                t.add_row([car.brand , car.model, car.mileage , car.rent , car.licensePlate , car.available])
                
            else:
                print(t)
                os.system("pause")
        else:
            print("No Cars to show...")
            time.sleep(1.7)
    
    def updateCars(self):
        os.system("cls")
        print("Login > Admin Menu > Manage Cars > Update Cars")
        plateNum=input("Enter the plate num of car you want to update: ")
        for car in self.cars:
            if(plateNum==car.licensePlate and car.available==True):
                 menuOptions=["1. Update Model" , "2. Update Brand" , "3. Update Rent","4. Update Mileage","5. Update License Plate"]
                 m=menu.Menu(menuOptions,color=menu.Colors.CYAN,style=menu.Styles.DEFAULT , pretext="Login > Admin Menu > Manage Cars > Update Cars")
                 userChoice=m.launch(response="index")+1
                 match userChoice:
                    case 1:
                         car.model=input("Please enter new model: ")
                    case 2:
                         car.brand=input("Enter new brand: ")
                    case 3:
                         try:
                            car.rent=int(input("Enter new rent (pkr/hr): "))
                            car.rent=abs(car.rent)
                         except:
                             print("Please enter a valid value")
                     
                    case 4:
                         car.mileage=input("Enter new mileage: ")
                    case 5:
                         newPlate=input("Enter the new license plate of car: ")
                         if any(c.licensePlate==newPlate for c in self.cars):
                             print("Car with this license plate already exists...")
                             time.sleep(1.7)
                             return
                         else:
                             car.licensePlate=newPlate
                 print("Car Successfully Updated...")
                 time.sleep(1.7)
            else:
                print("No car was found with this number plate...")
                time.sleep(1.7)
                    
                         
                    
                     

                




        

        
        


rentalShop=RentalSystem()
    
        


class Login:
    @staticmethod
    def adminLogin(admin: Admin):
        print("Login ")
        username=input("Enter your Username: ")
        password=input("Enter your Password: ")
        if(username==admin.username and password==admin.password):
            return True
        else:
            print("Wrong Credentials!")
            time.sleep(3)
            return False
    
        
        







        


def mainMenu():
    menuOptions=["1. Login as Admin","2. Login as Customer","3. Quit"]
    m=menu.Menu(menuOptions,color=menu.Colors.CYAN,style=menu.Styles.DEFAULT , pretext="")
    userChoice=m.launch(response="index")
    return userChoice+1

def AdminMenu():
    while(True):
        menuOptions=["1. Manage Cars" , "2. Manage Customers" , "3. Manage Reports","4. Logout"]
        m=menu.Menu(menuOptions,color=menu.Colors.CYAN,style=menu.Styles.DEFAULT , pretext="Login > Admin Menu")
        adminChoice1=m.launch(response="index")+1
        if(adminChoice1==1):
            adminChoice2=0
            while(adminChoice2!=5):
                manageCarOptions=["1. Add Cars" , "2. Remove Cars" , "3. View Cars" , "4. Update Cars" , "5. Go Back"]
                m=menu.Menu(manageCarOptions,color=menu.Colors.CYAN,style=menu.Styles.DEFAULT , pretext="Login > Admin Menu > Manage Cars")
                adminChoice2=m.launch(response="index")+1
                if(adminChoice2==1):
                    rentalShop.addCar()
                    continue
                if(adminChoice2==2):
                    rentalShop.removeCar()
                    continue
                if(adminChoice2==3):
                    rentalShop.viewCars()
                    continue
                if(adminChoice2==4):
                    rentalShop.updateCars()
                    continue




        if(adminChoice1==4):
            return
        

    time.sleep(4)

    



def main():
    
    while(True):
        mainChoice=mainMenu()
        if mainChoice==1:
            adminFound=Login.adminLogin(rentalShop.admin)
            if(adminFound==True):
                AdminMenu()
             

        if mainChoice==3:
            break



if __name__=="__main__":
    main()



    
