import numpy as np
import random
import string

file = open('milk_tea_menu.txt')

#starting words
def starts():
    
    print(' ❤️ ❤️ ❤️ ❤️ ❤️  ')
    print('|Tapioca Express|')
    print('|Ordering System|')
    print(' ❤️ ❤️ ❤️ ❤️ ❤️  ')
    print('     Welcome!!!')

#greetings
greeting_words = ('hi','hello','greetings','hey','h')
greeting_response = ['Hi, what would you like to order? ','What can I get for you today? ','Hello,anything you would like to drink?']
else_response = ['Sorry, can you say again?','I do not know what you are talking about']
def check_greetings(sentence):
    for word in sentence:
        if word.lower() in greeting_words:
            #return random.choice(greeting_response)
            return True
        else: 
            #return random.choice(else_response)
            return False
            
       

#place order
def Place_order (number,file):
    global data
    totalCost = 0
    for line in file:
        data = line.split(';')
        if data[0] == number:
            print (data[0]+'-'+data[1]+'-$'+ data[2])
            print ('Enter another number or enter X to exit')
    return str(data[2])


  
#openhours consist of a store's name/number, opening days,time and addresses
class OpenHours():
    shopname = 'Tapioca Express'
    def __init__ (self, name,day, time, place):
        self.name = name
        self.day = day
        self.time = time
        self.place = place
    
    def check (self):
        return (self.name + " is open from "+ self.time + " on "+ self.day + " at "+ self.place)

    
# below I provided my customers with all stores that are avaliable in San Diego. It helps the customers to go to the most convenient store they want.

def tell_time_and_locations():
    a=OpenHours ('Store A','Monday to Friday','9:30 am to 11:00 pm','9500 Gilman Dr, La Jolla, CA 92093')
    b=OpenHours ('Store B','Monday to Friday','11:00 am to 11:00 pm','7770 Regents Rd Ste 101, San Diego, CA 92122')
    c=OpenHours ('Store C','Monday to Sunday','11:00 am to 00:30 am','4646 Convoy St Ste 106B, San Diego, CA 92111')

    print ('Our first spot is ' +  a.check()+ '      '+
            'Our second spot is ' + b.check() + '.   '+
            'Our third spot is ' + c.check())
    
#tester of Openhours and functions
assert OpenHours
assert OpenHours('name', 'day', 'time', 'room')

name = 'Store A'
day = "Monday to friday"
time = "11:00 am to 6:00 pm"
place = "Price Center"

test_oh = OpenHours(name,day, time, place)
assert isinstance(test_oh, OpenHours)

assert test_oh.shopname == "Tapioca Express"
assert test_oh.name == name
assert test_oh.day == day
assert test_oh.time == time
assert test_oh.place == place



# Below I designed a code, that if the customers have any other questions that this Chatbot is not able to answer, he or she can email to me for better assistance.

def is_question(input_string):
    for item in input_string:
        if item == '?':
            output = True
        else:
            output = False

           
    return output
def respond_question(input_sentence):
    for item in input_sentence:
        if is_question(item):
            print('If you have any other questions, please call 858-322-0005 or email us at rulyu@ucsd.edu')
respond_question('What for?')