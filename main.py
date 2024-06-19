import menu
import time
import os



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
   
    def __str__(self):
        return f"{self.licensePlate}"

 

class RentalSystem:
    cars=[]
    customers=[]
    admin=Admin("admin","admin")
    def addCar(self):
        os
        print("Login > Admin Menu > Manage Cars > Add Car")
        brand=input("Enter Car Brand: ")
        model=input("Enter Car Model: ")
        plateNum=input("Enter License Plate: ")
        rent=input("Enter rent (pkr/hr): ")
        milage=input("Enter mileage (km): ")
        
        for car in self.cars:
            if plateNum==car.licensePlate:
                print("The License Plate already exists")
                time.sleep(2)
                return
        self.cars.append(Car(brand,model,milage,rent,plateNum))
        print("The Car was successfully added...")
        time.sleep(1.7)
    def removeCar(self):
        print("Login > Admin Menu > Manage Cars > Remove Car")
        plateNum=input("Enter license plate num of the car you want to remove: ")
        for car in self.cars:
            if plateNum==car.licensePlate:
                self.cars.remove(car)
                print("Car successfully removed...")
                time.sleep(1.7)
                return
        else:
            print("Car Not Found...")
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
            while(adminChoice2!=4):
                manageCarOptions=["1. Add Cars" , "2. Remove Cars" , "3. View Cars" , "4. Go Back"]
                m=menu.Menu(manageCarOptions,color=menu.Colors.CYAN,style=menu.Styles.DEFAULT , pretext="Login > Admin Menu > Manage Cars")
                adminChoice2=m.launch(response="index")+1
                if(adminChoice2==1):
                    rentalShop.addCar()
                    continue
                if(adminChoice2==2):
                    rentalShop.removeCar()
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



    
