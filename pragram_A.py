#make a code to 
#print output as given voice input

"""def voice(n):
    print(n)
voice ("Welcome to Diproma Infotech")

x=input("voice")
print(input)"""

voice=input("Welcome to Diproma Infotech")
def voice(limit):
    for i in range(0,limit+1,50):
        yield i 
    for words in voice:
        print(words)
