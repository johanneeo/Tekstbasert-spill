#En chatbot som bare gir gåter

navn=input("Please write your name ")                         

print("Hello ", navn, ".")


svar1="lounger"
svar2="1"
svar3="2"
svar4="3"
svar5="4"
Escape="E"


antall=int(input("You can solve 5 riddles maximum. How many do you want to solve? Remember you can press the E-button to escape any time."))        #skriv inn en knapp de kan trykke på for å avslutte



for x in range(0,antall):
    if x==1:
        spm1=input("I'm a seven-letter word that becomes longer when my third letter is removed. What am I? ")
        if spm1==svar1:
                print("Very good! Here is another one.")
        else:
            while (spm1!= svar1):
                    print("Wrong.")
                    spm1 = input("Please try again.")
    elif x==2:
        spm1=input("I'm a seven-letter word that becomes longer when my third letter is removed. What am I? ")
        if spm1==svar1:
                print("Very good! Here is another one.")
        else:
            while (spm1!= svar1):
                    print("Wrong.")
                    spm1 = input("Please try again.")
        print("Until I'm measured, I'm not known. Yet you miss me when I have flown. What am I?")
       