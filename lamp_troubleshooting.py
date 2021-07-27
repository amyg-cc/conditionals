# PRINT flip the lightswitch
# INPUT "did the lamp turn on?"
# IF lamp is off
    # INPUT "do you have a spare lightbulb?"
    # IF spare lightbulb doesn't exist
        # PRINT "go shopping"
# PRINT "change the lightbulb & turn on lamp"
# END

print("Flip the light switch")

lightswitch = input("Did the lamp turn on?: Y/N")

if lightswitch == "N":
    spare_lightbulb = input("do you have a spare lightbulb? Y/N")
    if spare_lightbulb == "N":
        print("go shopping")
    print("change the lightbulb & turn on lamp")