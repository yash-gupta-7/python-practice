#import pyttsx3
#engine = pyttsx3.init()
#engine.say("I will speak this text")
#engine.runAndWait()

"""letter = '''Dear <|Name|>,
You are selected!
<|Date|>
'''

name= input("enter your name")
date= input(" enter date")

print(letter.replace("<|Name|>",name).replace("<|Date|>",date)) """

str = input("enter a sting: ")
a = len(str)
print(f"lenth of your sting is {a}")

for i in range(a-1,-1,-1):
    print(str[i])



