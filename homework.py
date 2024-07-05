# WAP to print display displaygarnus('Something to print')

# a=input ()
# if a.startswith('displaygarnus(\'') and a.endswith('\')'):
#     print (a[15:-2])
# elif a.startswith('displaygarnus(') and a.endswith(')'):
#     print(eval(a[14:-1]))





#WAP FOR A BANK MANAGEMENT SYSTEM.
# Withdraw
# Deposit
# Transfer
# balance

# balance=1000
# def withdraw():
#     withdraw_amount=int(input("enter the amount you want to withdraw: "))
#     a=balance-withdraw_amount
#     print("The amount has been successfully withdrawl. ")
#     print("remaining amount is Rs.",a)
# def deposit():
#     deposit_amount=int(input("enter the amount you want to deposit: "))
#     a=balance+deposit_amount
#     print("The amount has been successfully deposited. ")
#     print("total amount is Rs.",a)
# def transfer():
#     transfer_amount=int(input("enter the amount you want to transfer: "))
#     a=balance-transfer_amount
#     print("The amount has been successfully withdrawl. ")
#     print("remaining amount is Rs.",a)
# def Exit():
#     print("See You soon. Have a good Day Sir")
# def balance_check():
#     print("Your current balance is: ",balance)
# print ("Select what you want to do")
# print ("1.Withdraw")
# print ("2.Deposit")
# print("3.Transfer")
# print ("4.Check Balance")
# print ("5.Exit")
# a=input("Enter your choice(1,2,3,4): ")
# while True:
#     if a =="1":
#         withdraw()
#         break
#     elif a=="2":
#         deposit()
#         break
#     elif a=="3":
#         transfer()
#         break
#     elif a=="4":
#         balance_check()
#         break
#     elif a=="5":
#         exit()


# WAP FOR A SHOP.

# name=input("Enter your name\n")
# print(f"Welcome {name}, to our store")
# balance=int(input("Enter your balance"))
# print("Here is the list of items: 1.Potato  50/kg   2.Apple  320/kg   3.Mango  100/kg\n")
# item=input()
# cart={}
# if item=='Apple':
#     Quantity=int(input("Enter the amount of kg"))
#     cost=Quantity*50
#     cart[item]=cost
#     print (cart)
    

# WAP FOR ENCRYPTION AND DECRYPTION

# a=input("Enter the word: ")
# def encryption():
#     b=(a[1:6])
#     c=b+a[0]
# encryption()
# def decryption():

# WAP PROGRAM FOR ARRAY.

# 1.      FOR APPEND

#       L1=['a','b','c','d']
#       L1.append('e')
#       print (L1)

# 2.      FOR CLEARING
#       L1=['a','b','c','d']
#       L1.clear()
#       print(L1)

# 3.      FOR COPYING
#       L1=['a','b','c','d']
#       L2=L1.copy()
#       print(L2)

# 4.        FOR COUNTING
#       L1=['a','b','c','d']
#       a=L1.count('a')
#       print(a)

# 5.        FOR EXTENDING
#       L1=['a','b','c','d']
#       L2=['e','f']
#       L1.extend(L2)
#       print(L1)

# 6.       FOR INDEX
#       L1=['a','b','c','d']
#       L=L1.index('a')
#       print (L)

# 7.        FOR INSERTING
#       L1=['a','b','c','d']
#       L1.insert(4,'z')
#       print (L1)

# 8.        FOR POP.
#       L1=['a','b','c','d']
#       L1.pop(1)
#       print (L1)

# 9.        FOR REMOVING
#       L1=['a','b','c','d']
#       L1.remove('a')
#       print(L1)

# 10.        FOR REVERSING
#       L1=['a','b','c','d']
#       L1.reverse()
#       print(L1)

# 11.       FOR SORTING
#       L1=['d','c','b','a']
#       L1.sort()
#       print (L1)

# WRITE A PROGRAM FOR ADDING AND DELETING IN DICTIONARIES.

# a={}

# def add():
#     global a
#     topic=input("Topic: ")
#     intro=input("Introduction about it: ")
#     a[topic]=intro
#     print(a)

# def delete():
#     global a
#     delete_choice=input("Enter the topic you want to delete: ")
#     a.pop(delete_choice)
#     print (a)

# def to_do_task():
#     while True:
#         print('Enter your choice')
#         print('1.add task')
#         print ('2.delete task')
#         a=int(input("Enter your choice: "))
#         if a==1:
#             add()
#         if a==2:
#             delete()
#         if a==3:
#             break
# to_do_task()

# WRITE A PROGRAM FOR CREATING , ADDING AND DELETING IN AN FILE.

def create():
    try:
        file_created=str(input("Enter the file name you want to create: "))
        file=open(file_created,"w")
        a=input("Enter the contans you want to add in it: \n")
        file.write(a+"\n")
        file.close()
    except Exception:
        print("Error! PLEASE TRY AGAIN")

def add():
    file_to_add_text=(input("Enter the file name where you want to add text: "))
    file=open(file_to_add_text,"a")
    added_text=input("Enter the text that you want to add: ")
    file.write(added_text+"\n")
    file.close()

def read():
    try:
        a=input("Enter the file name you want read: ")
        file=open(a,"r")
        print(file.read()+"\n")
        file.close()
    except Exception:
        print("MATCH NOT FOUND: Invalid file name. ")

def delete():
    import os
    try:
        deleting_file=input("Enter the name of the file to delete: ")
        os.remove(deleting_file)
    except Exception:
        print("MATCH NOT FOUND: Invalid file name. ")

def main():
    while True:
        print ("Enter the option you want to do")
        print("1.Create file")
        print("2.Add in file")
        print("3.Read a file")
        print("4.Delete file")
        print("5.Exit")
        input_ask=input("Choice: ")
        if input_ask=="1":
            create()
        if input_ask=="2":
            add()
        if input_ask=="3":
            read()
        if input_ask=="4":
            delete()
        if input_ask=="5":
            break
main()