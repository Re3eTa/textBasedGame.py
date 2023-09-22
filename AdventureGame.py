### welcome message
def adventureGameMain():
    
    print("welcome to 'delinquents-computing' Main testing facility.")
    print("you seem to be restrained to a chair in some sort of vehicle that is coming to a halt.")
    print("as the vehicle stops your restraints are released and a bright blue screen materialises before your eyes and starts playing compressed voice-announcements")
    name = str(input("Announcer: please enter your name:"))
    print(f"\nAnnouncer: Hello {name}! you have been selected out of a random  group of candidates to particpate in our new trial \n'Xen computing.'")
    print("Announcer: Xen computing is a new form of super-computer that links the users brain to the CPU to achieve levels of computing we have never seen before. these trials will commence in our top secret level located 400m under the facility.")
    print("Anouncer: we have finished running diagnositics on the grey matter in your head. please exit the vehicle and make your way to the elevator.")
    print("leaving the vehicle you now recognise as a boarded up sleek looking train, you see an entryway with some vending machines.")
    print("would you like to proceed to the elevator or inspect the vending machine?")
          
    ### prompt first choice
    roomChoice = input("> ")
          
    if(roomChoice == 'vending machine'):
        print("\nyou decide to check out the solitary vending machine!")
        print("the vending machine is bright red spouting the facade of a 'coce' machine")
        print("'interesting' you think, as you remember that coke is spelled C O K E")
        print("do you want to press some 'buttons' to relive your 90s-2000s nostolga? 'punch' machine? or enter 'elevator'")
          
          ###prompt first optional choice
          
        vendingChoice = input("> ")
          
        if(vendingChoice == 'buttons'):
            print("\nyou decide to press some buttons!")
            print("like you remember, the vending machine lights up and starts to growl like an old man")
            print("to your horror and discust the machine does the inevitable and breaks right before your can of coce is dispensed")
            print("feeling ragefull you can either go to the 'elevator' like the announcer sugessted or you can give the machine the 'punch' it deserves")
          
            coceChoice = input("> ")
                
            if(coceChoice == 'elevator'):
                print("\nyou decide that the vending machine is a total waste of time and enter the elevator to proceed to the trials.")
                
                coce = False
                elevator = True
                
            elif(coceChoice == 'punch'):
                print("\nyou remember your history with these god forsaken 'vending machines' (its not good) and give the machine the uppercut of a lifetime")
                print("you are now in a lot of pain due to fractured fingers (oh no!) luckily the machine spits out a luke warm can of coce to help you live with your choices")
                print("you decide to enter the elevator seeing as you have just been wasting time.")
                coce = True
                elevator = True
                
            else:
                print("-----------invalid selection, please enter appropriate choice.-----------------")
                
               
                
        elif(vendingChoice == 'punch'):
            print("you remember your history with these god forsaken 'vending machines' (its not good) and give the machine the uppercut of a lifetime.")
            print("you are now in alot of pain due to fractured fingers (oh no!) luckily the machine spits out a luke warm can of coce to hel you live with your choices.")
            print("you decide to enter the elevator seeing as you have just been wasting time.")
            coce = True
            elevator = True
                
        elif(vendingChoice == 'elevator'):
            print("you decide that the vending machine is a waste of time and proceed to the elevator.")
                
            coce = False
            elevator = True
                
        else:
            print("-----------invalid selection, please enter appropriate choice.-----------------")
          
          
    elif(roomChoice == 'elevator'):
        print("\nyou're eager to get to testing so you enter the elevator right away.")
        coce = False
        elevator = True
    else:
        print("-----------invalid selection, please enter appropriate choice.-----------------")
                
                #second choice depends on first optional choice
                
    if(elevator & coce == True):
                print("\nthe elevator starts its journey down to the depths of the facility")
                print("as the dull elevator music blares loudly over the elevator speakers you look down at the bloody mess that is your right hand, cracked and broken, the pain starts to make you sweat.")
                print("seeing as you have a can of coce you decide to drink it.")
                print("miraculously after the warm red liquid is in your belly you notice the pain immidiately dissapear, your hand is Healed!")
                print("'Maybe I should keep an eye out for more vending machines' you say to yourself as the elevator finally approaches level 400.")
                
                
    elif(elevator == True):
                print("\nthe elevator starts its journey down to the depths of the facility.")
                print("after singing happy tunes to yourself for 10 minutes the elevator finally approaches level 400.") 
                
    print("\nas the elevator doors open, a man in a white and blue lab coat stands waiting for your arrival.")
    print(f"scientist- 'Hello {name}! its nice to finally meet you! my name is doctor huffman and I will be over-seeing your trials")
    print(f"huffman- 'as you are the first applicant with compatible grey matter we are excited to finally test this on humans *cough cough* I mean willing participants *cough cough* ahh never mind'.")
    print("huffman- 'our team here at deliquents computing told us that we have your permission to do all of the various tests required to see this project through to the early development stages'.")
    print("huffman- 'I hope you dont mind being our labrat'")  
    print("\nhuffman prompts you to follow directs you down a number of long hallways lit by the constant lound hum of early 2000s flourescent lights")
    print("huffman makes a final turn into a large chamber with two rooms")
    print("in the entryway of the chamber you can make out a desk with a few chairs and screens displaying  what looks like a 'task manager' showing all of the various processes and the impact on hardware.")
    print("infront of the desk is a large wall that looks re-enforced far past the usual standards. there is an obervation window above the desk and an airlock seperating the two rooms.")
    print("in the other room is a singular chair in front of a glass prism shaped cage, probably the size of a full grown elephant, inside the cage lies the 'XEN' computer. you try and make out some well known components but XEN hardware looks far too complicated for you.")

adventureGameMain()