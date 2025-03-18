import os
inventory = []
p_name = input("Please enter your name: ")

print("""===================== In a Galaxy far, far away... =======================""")
print(
f"""You are {p_name}, a newly hired mechanic at HyperDrive INC. on Nar Shaddaa—a moon under Hutt control, infamous across the galaxy as the "Smuggler's Moon." 
Your latest assignment? A repair job for Mirra Stray, captain of the Crying Hawk.""")
input("----press enter to continue----")
print(f"""Stepping into the starcraft, your eyes land on a woman with fiery red hair, neatly tied into two buns. 
Her expression is tense, her brow furrowed in concentration. A microtool rests in one hand, while the other is planted firmly on her hip. 
She barely glances up as you enter, clearly preoccupied.""")
input()
print(f"""{p_name}: "So, this is the Crying Hawk I need to fix? You must be Mirra Stray?" """)
input()
print(f"""The woman nodded, stepped aside and invites you in with a quick hand movement.
It was a light freighter, but had a lot of damage on the hull.
{p_name}: "Oh wow, you took good damage here, did you meet some pirates? Hahah"
You laugh nervously. Of course you know not to ask too many questions but she wasn't saying something and you tried to 
loosen up the tension.""")
input()
print(f"""Mirra: "Check on the relays first." """)
input()
print(f"""You cleared your throat.
{p_name}: "Okay, I'll take a look." """)
input()

def room_selection():
    while True:  # Create a loop to allow repeated room selection (I admit that chatgpt helped with this loop, everything else in this code is written manually by myself.)
        print("Do you like to go to the Cockpit, Community Room, Sleeping Quarter or exit the Game?")
        print("1) Cockpit")
        print("2) Community Room")
        print("3) Sleeping Quarter")
        print("4) Exit")
        answer = int(input("Type 1, 2, 3 or 4: "))

        while answer not in [1, 2, 3, 4]:
            answer = int(input("Incorrect input, please try again: "))

        if answer == 1:
            print("You went into the Cockpit.")
            input()
            print(f"""The first thing you see is Mirra Stray on the ship's console. You guessed that she is still doing some damage control.""")
            input()
            print(f"""{p_name}: "Oh, sorry I won't disturb. I am just gonna look into the relays, like you ordered me to." """)
            input()
            print(f"""You see a lot of tools next to her and one tool especially looks familiar. You notice it's missing in your own tool bag.""")
            input()

            # Acquired tool
            choice = input("""Ask Mirra to get the tool? Type "y" for yes or "n" for no: """).lower()
            if choice == "y":
                inventory.append("tool")
                print("""Mirra agrees: "You better put it back later." Tool added to your inventory!""")
                input()
            else:
                print("You leave the tool behind.")
                input()

        elif answer == 2:
            print("You went into the Community Room.")
            input()
            print(
f"""The Community room is at the heart of the Crying Hawk. As you approach, you can hear chattering.
As you enter the room you can see a Twi'lek with blue skin and a creature you haven't seem before.
They sit around the round holotable and play holochess. The creature you couldn't recognize has 
four arms, wearing some pieces of clothes and has an antler. The blue Twi'lek wears a cropped top and some tight
leather trousers. She layed back into her chair, watching the other one thinking.""")
            input()
            print(f"""Twi'lek: "So what's your next move Nah'yuta?", she said raising an eyebrow and a small smirk.""")
            input()
            print(f"""The creature, called Nah'yuta gave her a grunt and moved a figure.""")
            input()
            print(f"""His opponent stands up and yells: "What?! How did you win with that move?" """)
            input()
            print(f"""Nah'yuta shrugs his shoulders and says calmly: " I don't know what you mean, Vex. I have no idea what I am doing." """)
            input()
            print(f""" "There is no way you don't even know how to play!" said the Twi'lek in disbelief. """)
            input()
            print(
f"""You decided not to intervene and do your work. Suddenly on your left you noticed an open electrial panel that throws out sparks.
It's a broken relay. {p_name} decides to repair it since it's your job after all, but unfortunately you need a special tool that 
you accidentaly forgot in the companies workshop. Maybe you can find the right tool inside this ship? """)
            input()
            
            if "tool" in inventory:
                print("Good job, you repaired this dangerous trap for every living being.")
                input()
            else:
                print("You should take another look around.")
                input()

        elif answer == 3:
            print("You went into the Sleeping Quarter.")
            input()
            print(f"""You decided to go through the ship, getting an overview over the damage.""")
            input()
            print(
f"""As you go through the narrow corridors you can see several doors, but all of the sudden
next to one door a shiver runs down your spine, so you stop. You are curious why you feel like 
taking a peak inside, so you yield this feeling and open the door. The room is dimly lit, the hum of the ship barely audible. 
A humanoid figure sits cross-legged on a makeshift mat, eyes closed, lost in meditation. You step in, the door hissing shut behind them.""")
            input()
            print(
f"""{p_name}: "Uh… didn't mean to interrupt." Knowing far too well you just stepped into someones sleeping quarter, as something did
the decision for you.""")
            input()
            print(
f"""His eyes remain closed but he said calmly: "You already have." """)
            input()
            print(
f"""{p_name}: "Right. Uh… I just need to check the power relays. Captain's orders." """)
            input()
            print(
f"""He finally opens an eye and exhales slowly: "Then do what you must, but quietly." """)
            input()
            print(
f"""{p_name}: "Yeah, sure. Stealth mode. Got it." """)
            input()
            print(
f"""You start to work on the relay as quietly as possible, but you can't avoid the soft clinking of your tools. """)
            input()
            print(
f"""???: "Your presence... It hums with unease." """)
            input()
            print(
f"""{p_name}:"What? No, I am fine. Just-y'know-working." """)
            input()
            print(
f"""???: He gives you a smirk and says "Then work... and try not to hum so loudly." """)
            input()
            print(
f"""You roll your eyes and get back to work as this mysterious guy resumes meditating. 
After some time, you finished your work here and decide to step outside.""")
            input()
            print(
f"""{p_name}:"I am done, uhm goodbye--" You hesitate because you don't know his name.""")
            input()
            print(
f"""???: "Solas, my name is Solas" """)
            input()
            print(
f"""{p_name}: "Yes, Solas, goodbye." """)
            input()

        elif answer == 4:
            print("\nHave you finished your work employee #567432? Well done.")
            break

room_selection()
# os.system('cls')   -- unsure if I should keep the terminal output or clear it. 