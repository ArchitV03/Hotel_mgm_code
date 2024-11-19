import pickle
import os


#clear
def clear():
    for x in range(65):
        print(' ')
        
clear()


#program for making records for hotel bookings
def menu():
    print('             WELCOME TO OUR HOTEL                ')
    print('                     MENU                        ')
    print('(1)  BOOKING')
    print('(2)  CHANGE YOUR ROOM')
    print('(3)  FOOD ORDER')
    print('(4)  ROOM FACILITIES')
    print('(5)  BILL ')
    print('(6)  SEARCH YOUR BOOKING')
    print('(7)  MODIFY RECORD')
    print('(8)  DELETE RECORD')
    return ' '




def booking():
    File=open('Booking.pkl','ab')
    print(' \n'*100)
    print('     WHICH ROOM YOU WANT     ')
    print('(1) 1 ROOM')
    print('(2) 2 ROOM')
    choice=int(input('ENTER YOUR CHOICE HERE : '))
    if choice==1:
        print(' \n'*100)
        print('HOW MANY DAYS YOU WANT ROOM')
        print('1 DAY')
        print('2 DAYS')
        a=int(input('ENTER YOUR CHOICE : '))
        if a==1 or a==2:
            print(' \n'*100)
            b=str(input('NAME OF THE PERSON PAYING BILL (IN CAPITAL LETTERS) : '))
            if b!=b.upper():
                print('PLEASE ENTER YOUR NAME IN CAPITAL LETTER ')
            if b==b.upper():
                print(' \n'*100)
                c=str(input('ENTER YOUR PHONE NUMBER : '))
                if len(c)>10 or len(c)<10 :
                    print('PLEASE ENTER YOUR CORRECT PHONE NUMBER ')
                if len(c)==10 :
                    person_1=int(input('NUMBER OF PERSON LIVING : '))
                    print(' \n'*100)
                    print('THANKU FOR REGISTERING')
                    booking_1={'ROOM':choice,'DAYS':a,'NAME':b,'PHONE NUMBER':c,'NUMBER OF PERSONS':person_1}
                    pickle.dump(booking_1,File)
            


    if choice == 2 :
        print(' \n'*100)
        print('HOW MANY DAYS YOU WANT ROOM')
        print('1 DAY')
        print('2 DAYS')
        a=int(input('ENTER YOUR CHOICE : '))
        if a==1 or a==2:
            print(' \n'*100)
            b=str(input('NAME OF THE PERSON PAYING BILL (IN CAPITAL LETTERS) : '))
            if b!=b.upper():
                print('PLEASE ENTER YOUR NAME IN CAPITAL LETTER ')
            if b==b.upper():
                print(' \n'*100)
                c=str(input('ENTER YOUR PHONE NUMBER : '))
                if len(c)>10 or len(c)<10 :
                    print('PLEASE ENTER YOUR CORRECT PHONE NUMBER ')
                if len(c)==10 :
                    person_1=int(input('NUMBER OF PERSON LIVING : '))
                    print('THANKU FOR REGISTERING')
                    booking_1={'ROOM':choice,'DAYS':a,'NAME':b,'PHONE NUMBER':c,'NUMBER OF PERSONS':person_1}
                    pickle.dump(booking_1,File)


    File.close()
    return ' '
    
       



def change_room():
    File_1=open('Change_room.pkl','ab')
    print(' \n'*100)
    print('       WHICH ROOM YOU WANT :       ')
    print('(1) 1 ROOM')
    print('(2) 2 ROOM')
    choice_room=int(input('ENTER YOUR CHOICE : '))
    if choice_room==1: 
        print(' \n'*100)
        print('WHICH FLOOR YOU WANT : ')
        print('(1) 1 FLOOR')
        print('(2) 2 FLOOR')
        choice_floor=int(input('ENTER YOUR CHOICE : '))
        if choice_floor==1:
            person_3=int(input('NUMBER OF PERSON LIVING : '))
            person_room=str(input('NAME OF THE PERSON CHANGING ROOM (IN CAPITAL LETTERS) : '))
            if person_room!=person_room.upper():
                print('PLEASE ENTER YOUR NAME IN CAPITAL LETTER ')
            if person_room==person_room.upper():
                change_room_1={'ROOM':choice_room,'FLOOR':choice_floor,'NUMBER OF PERSONS':person_3,'NAME':person_room}
                pickle.dump(change_room_1,File_1)
        elif choice_floor==2:
            person_3=int(input('NUMBER OF PERSON LIVING : '))
            person_room=str(input('NAME OF THE PERSON CHANGING ROOM (IN CAPITAL LETTERS) : '))
            if person_room!=person_room.upper():
                print('PLEASE ENTER YOUR NAME IN CAPITAL LETTER ')
            if person_room==person_room.upper():
                change_room_1={'ROOM':choice_room,'FLOOR':choice_floor,'NUMBER OF PERSONS':person_3,'NAME':person_room}
                pickle.dump(change_room_1,File_1)
    elif choice_room==2:
        print(' \n'*100)
        print('WHICH FLOOR YOU WANT : ')
        print('(1) 1 FLOOR')
        print('(2) 2 FLOOR')
        choice_floor=int(input('ENTER YOUR CHOICE : '))
        if choice_floor==1:
            person_3=int(input('NUMBER OF PERSON LIVING  : '))
            person_room=str(input('NAME OF THE PERSON CHANGING ROOM (IN CAPITAL LETTERS) : '))
            if person_room!=person_room.upper():
                print('PLEASE ENTER YOUR NAME IN CAPITAL LETTER ')
            if person_room==person_room.upper():
                change_room_1={'ROOM':choice_room,'FLOOR':choice_floor,'NUMBER OF PERSONS':person_3,'NAME':person_room}
                pickle.dump(change_room_1,File_1)
        elif choice_floor==2:
            person_3=int(input('NUMBER OF PERSON LIVING : '))
            person_room=str(input('NAME OF THE PERSON CHANGING ROOM (IN CAPITAL LETTERS) : '))
            if person_room!=person_room.upper():
                print('PLEASE ENTER YOUR NAME IN CAPITAL LETTER ')
            if person_room==person_room.upper():
                change_room_1={'ROOM':choice_room,'FLOOR':choice_floor,'NUMBER OF PERSONS':person_3,'NAME':person_room}
                pickle.dump(change_room_1,File_1)
    File_1.close()
    return ' '    





def food_order():
    File_2=open('Food_order.pkl','ab')
    print(' \n'*100)
    print('       WHAT WOULD YOU HAVE :       ')
    print('(1)  BREAKFAST   ')
    print('(2)  LUNCH   ')
    print('(3)  DINNER   ')
    food_choice=str(input('ENTER YOR CHOICE : '))
    print(' \n'*100)
    if food_choice=='1':
        food_choice+=' BREAKFAST'
        print('(1)  OATS   ')
        print('(2)  PRANTHAS  ')
        print('(3)  SANDWICH   ')
        breakfast=str(input('ENTER YOUR CHOICE : '))
        if breakfast=='1' :
            print('NAME OF THE PERSON TAKING MEAL (IN CAPITAL LETTERS) ')
            name_meal=input('ENTER YOUR NAME HERE : ')
            if name_meal!=name_meal.upper():
                print('PLEASE ENTER YOUR NAME IN CAPITAL LETTER ')
            if name_meal==name_meal.upper():
                breakfast+=' OATS'
                foodorder_1={'TYPE OF FOOD':food_choice,'FOOD NAME':breakfast,'NAME':name_meal}
                pickle.dump(foodorder_1,File_2)
        elif breakfast=='2':
            breakfast+=' PRANTHAS'
            print('NAME OF THE PERSON TAKING MEAL (IN CAPITAL LETTERS) ')
            name_meal=input('ENTER YOUR NAME HERE : ')
            if name_meal!=name_meal.upper():
                print('PLEASE ENTER YOUR NAME IN CAPITAL LETTER ')
            if name_meal==name_meal.upper():
                foodorder_1={'TYPE OF FOOD':food_choice,'FOOD NAME':breakfast,'NAME':name_meal}
                pickle.dump(foodorder_1,File_2)
        elif breakfast=='3':
            breakfast+=' SANDWICH'
            print('NAME OF THE PERSON TAKING MEAL (IN CAPITAL LETTERS) ')
            name_meal=input('ENTER YOUR NAME HERE : ')
            if name_meal!=name_meal.upper():
                print('PLEASE ENTER YOUR NAME IN CAPITAL LETTER ')
            if name_meal==name_meal.upper():
                foodorder_1={'TYPE OF FOOD':food_choice,'FOOD NAME':breakfast,'NAME':name_meal}
                pickle.dump(foodorder_1,File_2)
    elif food_choice=='2' :
        food_choice+=' LUNCH'
        print('(1)  DAL RICE   ')
        print('(2)  RAJMA RICE   ')
        print('(3)  CHOLE BATHURE   ')
        lunch=str(input('ENTER YOUR CHOICE :'))
        if lunch == '1' :
            lunch+=' DAL RICE'
            print('NAME OF THE PERSON TAKING MEAL (IN CAPITAL LETTERS) ')
            name_meal=input('ENTER YOUR NAME HERE : ')
            if name_meal!=name_meal.upper():
                print('PLEASE ENTER YOUR NAME IN CAPITAL LETTER ')
            if name_meal==name_meal.upper():
                foodorder_1={'TYPE OF FOOD':food_choice,'FOOD NAME':lunch,'NAME':name_meal}
                pickle.dump(foodorder_1,File_2)
        elif lunch == '2' :
            lunch+=' RAJMA RICE'
            print('NAME OF THE PERSON TAKING MEAL (IN CAPITAL LETTERS) ')
            name_meal=input('ENTER YOUR NAME HERE : ')
            if name_meal!=name_meal.upper():
                print('PLEASE ENTER YOUR NAME IN CAPITAL LETTER ')
            if name_meal==name_meal.upper():
                foodorder_1={'TYPE OF FOOD':food_choice,'FOOD NAME':lunch,'NAME':name_meal}
                pickle.dump(foodorder_1,File_2)
        elif lunch == '3':
            lunch+=' CHOLE BATHURE'
            print('NAME OF THE PERSON TAKING MEAL (IN CAPITAL LETTERS) ')
            name_meal=input('ENTER YOUR NAME HERE : ')
            if name_meal!=name_meal.upper():
                print('PLEASE ENTER YOUR NAME IN CAPITAL LETTER ')
            if name_meal==name_meal.upper():
                foodorder_1={'TYPE OF FOOD':food_choice,'FOOD NAME':lunch,'NAME':name_meal}
                pickle.dump(foodorder_1,File_2)
    elif food_choice=='3' :
        food_choice+=' DINNER'
        print('(1) DAL ROTI    ')
        print('(2)  YELLOW RICE   ')
        print('(3)  FRIED RICE   ')
        dinner=str(input('ENTER YOUR CHOICE : '))
        if dinner=='1' :
            dinner+=' DAL ROTI'
            print('NAME OF THE PERSON TAKING MEAL (IN CAPITAL LETTERS) ')
            name_meal=input('ENTER YOUR NAME HERE : ')
            if name_meal!=name_meal.upper():
                print('PLEASE ENTER YOUR NAME IN CAPITAL LETTER ')
            if name_meal==name_meal.upper():
                foodorder_1={'TYPE OF FOOD':food_choice,'FOOD NAME':dinner,'NAME':name_meal}
                pickle.dump(foodorder_1,File_2)
        if dinner=='2' :
            dinner+=' YELLOW RICE'
            print('NAME OF THE PERSON TAKING MEAL (IN CAPITAL LETTERS) ')
            name_meal=input('ENTER YOUR NAME HERE : ')
            if name_meal!=name_meal.upper():
                print('PLEASE ENTER YOUR NAME IN CAPITAL LETTER ')
            if name_meal==name_meal.upper():
                foodorder_1={'TYPE OF FOOD':food_choice,'FOOD NAME':dinner,'NAMEL':name_meal}
                pickle.dump(foodorder_1,File_2)         
        if dinner=='3' :
            dinner+=' FRIED RICE'
            print('NAME OF THE PERSON TAKING MEAL (IN CAPITAL LETTERS) ')
            name_meal=input('ENTER YOUR NAME HERE : ')
            if name_meal!=name_meal.upper():
                print('PLEASE ENTER YOUR NAME IN CAPITAL LETTER ')
            if name_meal==name_meal.upper():
                foodorder_1={'TYPE OF FOOD':food_choice,'FOOD NAME':dinner,'NAME':name_meal}
                pickle.dump(foodorder_1,File_2)       
    File_2.close() 
    return ' '






def room_facilities():
    File_3=open('Room_facilities.pkl','ab')
    print(' \n'*100)
    print('       WHAT FACILITIES WOULD YOU WANT :       ')
    print('(1)  WANT AN AC ROOM ')
    print('(2)  WANT A BATHROOM ')
    print('(3)  WANT A WAITER ')
    choice_facilities=str(input('ENTER YOUR CHOICE'))
    if choice_facilities=='1':
        choice_facilities+='WANT AN AC ROOM'
        ac=int(input('HOW MANY AC YOU WANT : '))
        if ac==1:
            NAME=input('ENTER YOUR NAME (IN CAPITAL LETTERS) : ')
            if NAME!=NAME.upper():
                print('PLEASE ENTER YOUR NAME IN CAPITAL LETTER ')
            if NAME==NAME.upper():
                print('THANK YOU FOR TAKING OUR FACILITIES')
                data_8={'FACILITY':choice_facilities,'NUMBER OF AC':ac,'NAME OF PERSON':NAME}
                pickle.dump(data_8,File_3)
        if ac==2:
            NAME=input('ENTER YOUR NAME(IN CAPITAL LETTERS) : ')
            if NAME!=NAME.upper():
                print('PLEASE ENTER YOUR NAME IN CAPITAL LETTER ')
            if NAME==NAME.upper():
                print('THANK YOU FOR TAKING OUR FACILITIES')
                data_8={'FACILITY':choice_facilities,'NUMBER OF AC':ac,'NAME OF PERSON':NAME}
                pickle.dump(data_8,File_3)
    if choice_facilities=='2' :
        choice_facilities+='WANT A BATHROOM' 
        shower=str(input('DO YOU WANT SHOWER IN BATHROOM :\n ENTER YOUR CHOICE  : \n(1) YES  (2) NO    :'))
        if shower=='1' :
            shower+='shower'
            NAME=input('ENTER YOUR NAME(IN CAPITAL LETTERS) : ')
            if NAME!=NAME.upper():
                print('PLEASE ENTER YOUR NAME IN CAPITAL LETTER ')
            if NAME==NAME.upper():
                ROOM=input('ENTER YOUR ROOM NUMBER')
                print('THANK YOU FOR TAKING OUR FACILITIES')
                data_8={'FACILITY':choice_facilities,'shower':shower,'ROOM':ROOM,'NAME OF PERSON':NAME}
                pickle.dump(data_8,File_3)
        if shower=='2' :
            shower+='shower'
            print('THANK YOU')
            data_8={'FACILITY':choice_facilities,'shower':shower,'ROOM':ROOM}
            pickle.dump(data_8,File_3)
    if choice_facilities=='3':
        choice_facilities+='WANT A BATHROOM' 
        waiter=int(input('WHAT TYPE OF WORK DO YOU WANT FROM WAITER :\n (1) FOOD SERVICE \n (2) PERSONAL WORK '))
        if waiter==1 or 2 or 3:
            NAME=input('ENTER YOUR NAME (IN CAPITAL LETTERS) : ')
            if NAME!=NAME.upper():
                print('PLEASE ENTER YOUR NAME IN CAPITAL LETTER ')
            if NAME==NAME.upper():
                ROOM_NO=input('ENTER YOUR ROOM NUMBER : ')
                print('THANK YOU FOR TAKING OUR FACILITIES')
                data_8={'FACILITY':choice_facilities,'WAITER':waiter,'ROOM':ROOM,'NAME OF PERSON':NAME}
                pickle.dump(data_8,File_3)
    File_3.close()
    return ' '







def bill():
    File_4=open('Bill.pkl','ab')
    ROOM=int(input('HOW MANY ROOM YOU HAVE : '))
    if ROOM==1 or 2:
        DAYS=int(input('HOW MANY DAYS YOU BOOK YOUR ROOM : '))
        if DAYS==1 or 2:
            BILL_1=500
            print(' \n'*100)
            print(BILL_1)
            print('DO YOU HAVE ANY FOOD ORDERS : \n(1) YES  (2) NO    :')
            Food=int(input('ENTER YOUR CHOICE : '))
            if (Food==1):
                print(' \n'*100)
                print('(1) BREAKFAST')
                print('(2) LUNCH')
                print('(3) DINNER')
                food_select=input('WHICH ONE YOU HAVE CHOOSE : ')
                if (food_select=='1'):
                    food_select+=' BREAKFAST'
                    print('YOUR FOOD COST IS RS100')
                    BILL_1+=100
                    print('TOTAL BILL IS : ',BILL_1) 
                    data_9={'ROOM':ROOM,'DAYS':DAYS,'BILL':BILL_1,'FOOD':Food,'FOOD CATEGORY':food_select,'TOTAL BILL':BILL_1}
                    pickle.dump(data_9,File_4)
                if (food_select=='2'):
                    food_select+=' LUNCH'
                    print('YOUR FOOD COST IS RS200')
                    BILL_1+=200 
                    print('TOTAL BILL IS : ',BILL_1)
                    data_9={'ROOM':ROOM,'DAYS':DAYS,'BILL':BILL_1,'FOOD':Food,'FOOD CATEGORY':food_select,'TOTAL BILL':BILL_1}
                    pickle.dump(data_9,File_4)
                if (food_select=='3'):
                    food_select+=' DINNER'
                    print('YOUR FOOD COST IS RS300')
                    BILL_1+=300
                    print('TOTAL BILL IS : ',BILL_1) 
                    data_9={'ROOM':ROOM,'DAYS':DAYS,'BILL':BILL_1,'FOOD':Food,'FOOD CATEGORY':food_select,'TOTAL BILL':BILL_1}
                    pickle.dump(data_9,File_4)
            if (Food==2):
                print('TOTAL BILL IS : ',BILL_1) 
    File_4.close() 
    return ' '







       
def search():
    print('         HOW DO YOU WANT TO SEARCH YOUR RECORDS          ')
    print('(1)  BY NAME ')
    print('(2)  BY PHONE NUMBER')
    search_choice=int(input('ENTER YOUR CHOICE : '))
    found=0
    if search_choice==1:
        DATA=input('ENTER NAME THAT YOU WANT TO FIND (IN CAPITAL LETTERS): ')
        File=open('Booking.pkl','rb')
        while (True) :
            try:    
                data=pickle.load(File)
                if data['NAME'] == DATA :
                    print('NAME FOUND')
                    found+=1
                    N=int(input('DO YOU WANT TO SEE YOUR RECORD : \n(1) YES  (2) NO    : '))
                    if N==1:
                        print(data)
                    if N==2:
                        print('THANK YOU ')
            except:
                break
        if found==0:
                print('NAME YOU HAVE ENTERED DOES NOT EXIST')
        File.close()
    if search_choice==2:
        DATA=str(input('ENTER PHONE NUMBER THAT YOU WANT TO FIND : '))
        File=open('Booking.pkl','rb')
        found=0
        while (True) :
            try:    
                data=pickle.load(File)
                if data['PHONE NUMBER'] == DATA :
                    print('PHONE NUMBER FOUND')
                    found+=1
                    N=int(input('DO YOU WANT TO SEE YOUR RECORD : \n(1) YES  (2) NO    : '))
                    if N==1:
                        print(data)
                    if N==2:
                        print('THANK YOU  ')
            except:  
                break
        if found==0 :
            print('PHONE NUMBER YOU HAVE ENTERED DOES NOT EXIST')
        File.close()
    return ' '





def modify():
    file1=open('booking.pkl','rb')
    file2=open('temp.dat','wb')
    name1=input('ENTER NAME TO FIND : ')
    name2=input('ENTER NAME TO MODIFY : ')
    found=0
    while (True):
        try:
            data=pickle.load(file1)
            if name1==data['NAME']:
                data['NAME']=name2
                found=1
                pickle.dump(data,file2)
            else:
                pickle.dump(data,file2)
        except:
            break
    file1.close()
    file2.close()
    os.remove('booking.pkl')
    os.rename('temp.dat','booking.pkl')
    if found==1:
        print('RECORD CHANGED....')
    if found==0:
        print('NAME DOES NOT EXIST')
    return ' '



def delete():
    DATA=str(input('ENTER NAME THAT YOU WANT TO DELETE : '))
    File=open('Booking.pkl','rb')
    file_1=open('temp.pkl','wb')
    while (True) :
        try:    
            DELETE=pickle.load(File)
            if DELETE['NAME']!=DATA:
                pickle.dump(DELETE,file_1)
            if DELETE['NAME']==DATA :
                print('RECORD DELTED......')
        except:
            break 
    File.close()
    file_1.close()


    os.remove('Booking.pkl')
    os.rename('temp.pkl','booking.pkl')
    return ' '






def login():
    while (True):
        print('\n'*4)
        id1 = input('Enter user ID :')
        pwd = input('Enter password :')
        if(id1 == 'hotelmanagement@gmail.com' and pwd == 'hotel'):
            clear()
            menu()
            break
        else:
            print('PLEASE ENTER CORRECT ID AND PASSWORD....')


login()


Choice=int(input('WHAT SERVICE YOU REQUIRED  : '))


while (Choice==1):
    print(' \n'*100)
    print(booking())
    print('DO YOU WANT TO CONTINUE : ')
    Continue=int(input('ENTER YOUR CHOICE  : \n(1) YES  (2) NO    :'))
    if Continue==1 :
        print(' \n'*100)
        print(menu())
        Choice=int(input('WHAT SERVICE YOU REQUIRED  : '))
        if Choice==1:
            print(booking())
        if Choice==2:
            print(change_room())
        if Choice==3:
            print(food_order())
        if Choice==4:
            print(room_facilities())
        if Choice==5:
            print(bill())
        if Choice==6:
            print(search())
        if Choice==7:
            print(modify())
        if Choice==8:
            print(delete())
    if Continue==2:
        break




    
while (Choice==2):
    print(' \n'*100)
    print(change_room())
    print('DO YOU WANT TO CONTINUE : ')
    Continue=int(input('ENTER YOUR CHOICE  : \n(1) YES  (2) NO    :'))
    if Continue==1 :
        print(' \n'*100)
        print(menu())
        Choice=int(input('WHAT SERVICE YOU REQUIRED  : '))
        if Choice==1:
            print(booking())
        if Choice==2:
            print(change_room())
        if Choice==3:
            print(food_order())
        if Choice==4:
            print(room_facilities())
        if Choice==5:
            print(bill())
        if Choice==6:
            print(search())
        if Choice==7:
            print(modify())
        if Choice==8:
            print(delete())
    if Continue==2:
        break






while (Choice==3):
    print(' \n'*100)
    print(food_order())
    print('DO YOU WANT TO CONTINUE : ')
    Continue=int(input('ENTER YOUR CHOICE  : \n(1) YES  (2) NO    :'))
    if Continue==1 :
        print(' \n'*100)
        print(menu())
        Choice=int(input('WHAT SERVICE YOU REQUIRED  : '))
        if Choice==1:
            print(booking())
        if Choice==2:
            print(change_room())
        if Choice==3:
            print(food_order())
        if Choice==4:
            print(room_facilities())
        if Choice==5:
            print(bill())
        if Choice==6:
            print(search())
        if Choice==7:
            print(modify())
        if Choice==8:
            print(delete())
    if Continue==2:
        break





while (Choice==4):
    
    print(' \n'*100)
    print(room_facilities())
    print('DO YOU WANT TO CONTINUE : ')
    Continue=int(input('ENTER YOUR CHOICE  : \n(1) YES  (2) NO    :'))
    if Continue==1 :
        print(' \n'*100)
        print(menu())
        Choice=int(input('WHAT SERVICE YOU REQUIRED  : '))
        if Choice==1:
            print(booking())
        if Choice==2:
            print(change_room())
        if Choice==3:
            print(food_order())
        if Choice==4:
            print(room_facilities())
        if Choice==5:
            print(bill())
        if Choice==6:
            print(search())
        if Choice==7:
            print(modify())
        if Choice==8:
            print(delete())
    if Continue==2:
        break
   





while (Choice==5):
    print(' \n'*100)
    print(bill())
    print('DO YOU WANT TO CONTINUE : ')
    Continue=int(input('ENTER YOUR CHOICE  : \n(1) YES  (2) NO    :'))
    if Continue==1 :
        print(' \n'*100)
        print(menu())
        Choice=int(input('WHAT SERVICE YOU REQUIRED  : '))
        if Choice==1:
            print(booking())
        if Choice==2:
            print(change_room())
        if Choice==3:
            print(food_order())
        if Choice==4:
            print(room_facilities())
        if Choice==5:
            print(bill())
        if Choice==6:
            print(search())
        if Choice==7:
            print(modify())
        if Choice==8:
            print(delete())
    if Continue==2:
        break






while (Choice==6):
    print(' \n'*100)
    print(search())
    print('DO YOU WANT TO CONTINUE : ')
    Continue=int(input('ENTER YOUR CHOICE  : \n(1) YES  (2) NO    :'))
    if Continue==1 :
        print(' \n'*100)
        print(menu())
        Choice=int(input('WHAT SERVICE YOU REQUIRED  : '))
        if Choice==1:
            print(booking())
        if Choice==2:
            print(change_room())
        if Choice==3:
            print(food_order())
        if Choice==4:
            print(room_facilities())
        if Choice==5:
            print(bill())
        if Choice==6:
            print(search())
        if Choice==7:
            print(modify())
        if Choice==8:
            print(delete())
    if Continue==2:
        break





while (Choice==7) :
    print(' \n'*100)
    print(modify())
    print('DO YOU WANT TO CONTINUE : ')
    Continue=int(input('ENTER YOUR CHOICE  : \n(1) YES  (2) NO    :'))
    if Continue==1 :
        print(' \n'*100)
        print(menu())
        Choice=int(input('WHAT SERVICE YOU REQUIRED  : '))
        if Choice==1:
            print(booking())
        if Choice==2:
            print(change_room())
        if Choice==3:
            print(food_order())
        if Choice==4:
            print(room_facilities())
        if Choice==5:
            print(bill())
        if Choice==6:
            print(search())
        if Choice==7:
            print(modify())
        if Choice==8:
            print(delete())
    if Continue==2:
        break





while (Choice==8):
    print(' \n'*100)
    print(delete())
    print('DO YOU WANT TO CONTINUE : ')
    Continue=int(input('ENTER YOUR CHOICE  : \n(1) YES  (2) NO    :'))
    if Continue==1 :
        print(' \n'*100)
        print(menu())
        Choice=int(input('WHAT SERVICE YOU REQUIRED  : '))
        if Choice==1:
            print(booking())
        if Choice==2:
            print(change_room())
        if Choice==3:
            print(food_order())
        if Choice==4:
            print(room_facilities())
        if Choice==5:
            print(bill())
        if Choice==6:
            print(search())
        if Choice==7:
            print(modify())
        if Choice==8:
            print(delete())
    if Continue==2:
        break


if Choice==1 or 2 or 3 or 4 or 5 or 6 or 7 or 8:
    print('THANK YOU')
