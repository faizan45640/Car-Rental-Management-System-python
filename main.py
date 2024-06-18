import menu
import time
import os


class Admin:
    def __init__(self,username,password) -> None:
        self.username=username
        self.password=password
    





    






class Login:
    @staticmethod
    def adminLogin(admin: Admin):
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
        menuOptions=["1. Manage Cars" , "2. Manage Customers" , "3.Manage Reports","4. Logout"]
        m=menu.Menu(menuOptions,color=menu.Colors.CYAN,style=menu.Styles.DEFAULT , pretext="Login > Admin Menu")
        adminChoice1=m.launch(response="index")+1
        if(adminChoice1==4):
            return
        

    time.sleep(4)

    



def main():
    admin=Admin("admin","admin")
    while(True):
        mainChoice=mainMenu()
        if mainChoice==1:
            adminFound=Login.adminLogin(admin)
            if(adminFound==True):
                AdminMenu()
             

        if mainChoice==3:
            break



if __name__=="__main__":
    main()



    
