# welcome the user to the program 

# PRINT flip the lightswitch
# INPUT "did the lamp turn on?"
# IF lamp is on
    # PRINT "yay"
# ELIF lamp is off
    # INPUT "do you have a spare lightbulb?"

# IF spare lightbulb doesn't exist
        # PRINT "go shopping"
# ELIF
    # PRINT "change the lightbulb & turn on lamp"
# END

print("Flip the light switch")

lightswitch = input("Did the lamp turn on?: Y/N")

if lightswitch == "N":
    spare_lightbulb = input("do you have a spare lightbulb? Y/N")
    if spare_lightbulb == "N":
        print("go shopping")
    print("change the lightbulb & turn on lamp")

# if lightswitch == "Y":
#     print("yay")
# elif lightswitch == "N":
#     spare_lightbulb = input("do you have a spare lightbulb? Y/N")

# if spare_lightbulb == "N":
#     print("go shopping")
# else:
#     print("change the lightbulb & turn on lamp")

