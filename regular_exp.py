#                                     REGEX
# findall

# import re
# a="Hello,Hi"
# pattern=re.compile(r"Hi")
# z=pattern.findall(a)
# print (z)

# search

# import re
# a="Hello,Hi"
# pattern=re.compile(r"Hi")
# z=pattern.search(a)
# print (z)

# match

# import re
# a="Hello,Hi"
# pattern=re.compile(r"Hi")
# z=pattern.match(a)
# print (z)

#                                      METACHARACTERS

# WAP TO CHECK WHETHER THE PHONE NUMBER IS VALID OR NOT

# import re
# while True:
#     a=(input("Enter your phone number :"))
#     result=re.match(r'^98|97{8}',a)
#     if result:
#         print ("Your entered number is valid ")
#     else:
#         print ("Number you have entered is invalid or too short")
#         print("Try again later.")


# ...............................................................................................................................................................


# WAP FOR VERIFYING EITHER THE ENTERED NUMBER IS NCELL OR NTC OR NONE.

# import re
# while True:
#     number=(input('Enter the number :'))
#     result=re.match(r"^984|986|97",number)
#     a=re.match(r"^980|982",number)
#     if result:
#         print ("NTC")
#     elif a:
#         print ("Ncell")
#     else:
#         print("Invalid number")

# .........................................................................................................................................

# WAP FOR VERIFYING A 8 DIGIT PASSWORD .

# import re
# while True:
#     password=input("Enter your password :")
#     pw=re.match(r'(?=.*[a-zA-Z])(?=.*\d)[A-Za-z\d]{8,}',password)
#     if pw:
#         print("The password you have entered is valid")
#     else:
#         print("The password you have entered doesn't contain 8 charactes with(A-Z,a-z,0-9)")

# .....................................................................................................................................................

# WAP FOR A EMAIL VERIFICATION.

# import re
# while True:
#     email=input("Enter your email :")
#     em=re.match(r'(?=.*[a-z])(?=.*\d)',email)
#     if email[-10:]=="@gmail.com":
#         if em:
#             print("ok")
#         else:
#             print ("A email must contain numbers and small letters")
#     else:
#         print("invalid email")


