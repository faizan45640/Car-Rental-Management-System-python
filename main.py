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
    def __init__(self,userName,password,cnic,phone) -> None:
        self.userName=userName
        self.password=password
        self.cnic=cnic
        self.phone=phone
        self.rented=False #if the car is rented true
        self.rentedCar="0" #numplate of rented car
        pass

    

 

class RentalSystem:
    cars=[]
    customers=[]
    admin=Admin("admin","admin")
    loggedInCustomer=None
    #admin functionalities
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
    
    def addCustomer(self):
        os.system("cls")
        print("Login > Admin Menu > Manage Cars > Add Customers")
        name=input("Enter the username of the customer: ")
        password=input("Enter the password of the customer: ")
        cnic=str(input("Please enter cnic of the customer: "))
        phone=input("Enter the phone of customer: ")
        #validate cnic
       
        if any(customer.cnic==cnic for customer in self.customers):
                print("Customer with this cnic already exists...")
                time.sleep(1.7)
                return
        else:
            self.customers.append(Customer(name,password,cnic,phone))
            print("Customer successfully added...")
            time.sleep(1.7)
            return
    def removeCustomer(self):
        os.system("cls")
        print("Login > Admin Menu > Manage Cars > Remove Customers")
        cnic=str(input("Please enter the cnic of customer to remove: "))
        initialCount=len(self.customers)
        self.customers=[customer for customer in self.customers if customer.cnic!=cnic]
        if(initialCount>len(self.cars)):
            print("Customer Successfully Removed")
            time.sleep(1.7)
            return
        else:
            print("No customer was found...")
            time.sleep(1.7)
            return
    def updateCustomer(self):
        os.system("cls")
        print("Login > Admin Menu > Manage Cars > Update Customers")
        cnic=str(input("Please enter the cnic of customer to update: "))
        for customer in self.customers:
            if(customer.cnic==cnic):
                menuOptions=["1. Update Username" , "2. Update Password" , "3. Update Cnic","4. Update Phone"]
                m=menu.Menu(menuOptions,color=menu.Colors.CYAN,style=menu.Styles.DEFAULT , pretext="Login > Admin Menu > Manage Cars > Update Customers")
                userChoice=m.launch(response="index")+1
                match userChoice:
                    case 1:
                        customer.userName=input("Please enter the new username: ")
                    case 2:
                        customer.password=input("Please enter the new password: ")
                    case 3:
                        cnicNew=str(input("Please enter the new cnic: "))
                        if any(c.cnic==cnicNew for c in self.customers):
                            print("A customer with this cnic already exists!")
                            return
                        else:
                            customer.cnic=cnicNew
                    case 4:
                        phoneNew=int(input("Please enter the new phone: "))
                        if any(c.phone==phoneNew for c in self.customers):
                            print("A customer with this phone already exists!")
                            return
                        else:
                            customer.phone=phoneNew
                print("The Data was Successfully Updated..")
                time.sleep(1.7)
            else:
                print("The Customer was not found...")
                time.sleep(1.7)
    def viewCustomers(self):
         os.system("cls")
         print("Login > Admin Menu > Manage Cars > View Customers")
         t=PrettyTable(["Name","Password","Phone","CNIC"])
         if(len(self.customers)>0):
            for customer in self.customers:
                t.add_row([customer.userName , customer.password, customer.phone , customer.cnic])
                
            else:
                print(t)
                os.system("pause")
         else:
            print("No Customers to show...")
            time.sleep(1.7)
    #customer functionalities
    def rentCar(self,loggedInCustomer:Customer):
        os.system("cls")
        print("Login > Customer Menu > Rent Car")
        if(loggedInCustomer.rented==True):
            print("Sorry! you can't rent 2 cars at a time...")
            time.sleep(1.7)
            return
        else:
            numPlate=input("Please Enter the num plate of the car your want to rent: ")
            for c in self.cars:
                if(c.licensePlate==numPlate and c.available==True):
            
                    print("Car Information: ")
                    print("Model: ", c.model )
                    print("Brand: ", c.brand)
                    print("Rent: ",c.rent , " Pkr/hr")
                    print("Mileage: ",c.mileage, " km")
                    choice=input("Do you want to confirm the rental? (y/n)")
                    if(choice=="y"):
                        for customer in self.customers:
                            if(loggedInCustomer.cnic==customer.cnic):
                                customer.rented=True
                                customer.rentedCar=numPlate
                                c.available=False
                                print("The Car was Succesfully Rented! ")
                                time.sleep(1.7)
                                return
            else:
                print("The Car is not available at the moment...")
                time.sleep(1.7)
                return
  
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
    @staticmethod
    def customerLogin(customers: Customer):
        print("Customer Login")
        username=input("Enter your Username: ")
        password=input("Enter your Password: ")
        for customer in customers:
            if(customer.userName==username and customer.password==password):
                return customer
        else:
            print("Invalid Credentials")
            return None
    
        
        







        


def mainMenu():
    menuOptions=["1. Login as Admin","2. Login as Customer","3. Quit"]
    m=menu.Menu(menuOptions,color=menu.Colors.CYAN,style=menu.Styles.DEFAULT , pretext="")
    userChoice=m.launch(response="index")
    return userChoice+1

def customerMenu(loggedInCustomer : Customer):
    while(True):
        menuOptions=["1. Rent Car" , "2. Return a car" , "3. View Cars","4. My Rental Reports","5. Logout"]
        m=menu.Menu(menuOptions,color=menu.Colors.CYAN,style=menu.Styles.DEFAULT , pretext="Login > Customer Menu")
        userChoice1=m.launch(response="index")+1
        if(userChoice1==1):
            rentalShop.rentCar(loggedInCustomer)
    



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
        if(adminChoice1==2):
                
                    adminChoice2=0
                    while(adminChoice2!=5):
                        manageCusOptions=["1. Add Customer" , "2. Remove Customer" , "3. View Customer Data" , "4. Update Customer Data" , "5. Go Back"]
                        m=menu.Menu(manageCusOptions,color=menu.Colors.CYAN,style=menu.Styles.DEFAULT , pretext="Login > Admin Menu > Manage Customers")
                        adminChoice2=m.launch(response="index")+1
                        if(adminChoice2==1):
                            rentalShop.addCustomer()
                            continue
                        if(adminChoice2==2):
                            rentalShop.removeCustomer()
                            continue
                        if(adminChoice2==3):
                            rentalShop.viewCustomers()
                            continue
                        if(adminChoice2==4):
                            rentalShop.updateCustomer()
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
                continue
        if mainChoice==2:
            customerFound=Login.customerLogin(rentalShop.customers)
            if(customerFound):
                customerMenu(customerFound)
                continue
        
             

        if mainChoice==3:
            break



if __name__=="__main__":
    main()



    
