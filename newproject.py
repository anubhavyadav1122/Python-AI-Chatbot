# Rule Based AI Python Chatbot

import datetime 
import time


name= input("enter your name : ")
presentHour= datetime.datetime.now().hour


if 5 <= presentHour <= 11:
   print("good morning,", name)
elif 11 <= presentHour <= 17:
   print("good afternoon,", name)
elif 17 <= presentHour <= 20:
   print("good evening,", name)
else: 
   print("good night,", name)    





print("Namaste! Welcome to your chatbot")
print(" You can ask me basic question, Type 'bye to exit from the bot ")

#  chatbot memory question [dictionary of response]

responses ={
    "hello":"hi, welcome, How can i help you?",
    "how are you": "I am very fine. thank you",
    "who are you":"I am smart AI chatbot ",
    "motivate me":"keep going. every bug of your project makes you a  better developer",
    "happ":" great to here that ",
    "function kya hota hai": " jakar chapter 7 padho"
}

# method/functions to get response of chatbot 

def getResponseOfBot(userQuestion):
    userQuestion= userQuestion.lower()
    for eachkey in responses:
        if eachkey in userQuestion:
            return responses[eachkey]

# take user input 


while True:  
     userInput= input("please ask your question:")
     reply= getResponseOfBot(userInput)
     print("Bot Response :", reply)
     if "bye" in userInput.lower():
      break 
