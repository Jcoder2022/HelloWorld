print("Rabia Shaheen")
#expression
print('*' * 10)
#variables

#Integer as whole numbers
price = 10
print("price",price)

price = 20
print("price",price)

#Floating Number having decimal
rating = 4.9
print(rating)

#String single quote or double quotes

name='Rabia Shaheen'
name="Rabia Shaheen"
print(name)

#user defined variables are lowercase where as special key words first letter is capital letter
#Underscore is used to seperate var name
is_published = True
print(is_published)

patient_name ="John Smith"
patient_age=20
is_new = True

#How to receive input from user inout is built in function provided by python
# in statement below it will print What ..., will retreive name from screen and putt it in variable name
name = input('What is your name ? ')
# + is used for concatenation
print("Hi " + name)

person_name = input("What is your name? ")
person_favourite_color =input("What is your favourite color? ")
print(person_name +" likes "+ person_favourite_color)

#Calculate your age after taking year of birth

birth_year = input("Enter your Birth Year? ")
print(type(birth_year))
current_year = 2021
age = current_year - int(birth_year)
print(type(age))
print("your age is " + str(age) )

# Following are python built-in methods
# bool() to convert string to boolean
# float() to convert string to decimal
# int() to convert string to integer
# str() to convert (int/float/bool to string)
# type() returns type of variable

#Take user weight(pounds) and convert it to kg

user_weight_in_pounds = input("Enter your weight(pounds)? ")
user_weight_in_kilograms = float(user_weight_in_pounds) * 0.45359237

print("User Weight in KGs is " + str(user_weight_in_kilograms) )








