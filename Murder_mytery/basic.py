import random

victims    = ["a businessman", "a Bollywood actor" ]

locations  = ["in a 5 star hotel", "on a train" ]

suspects   = ["Butler", "Ex-Wife", "Business Partner"]

weapons    = ["poison in chai", "cricket bat" ]

motives    = ["jealousy", "money", "revenge", "family secret" ]

killer_responses = [
    "I was... busy that evening.",
    "Why does everyone keep asking me?",
    "I had nothing to do with it. Nothing.",
]

innocent_responses = [
    "I saw {killer} near the scene!",
    "Ask {killer}, not me.",
    "Check {killer}'s alibi first.",
]

def setup_mystery():
    victim=random.choice(victims)
    location=random.choice(locations)
    weapon=random.choice(weapons)
    three_suspect=random.sample(suspects,3)
    killer=random.choice(three_suspect)
    motive=random.choice(motives)

    return{
        "victim": victim,
        "location": location,
        "weapon": weapon,
        "suspects": three_suspect,
        "killer":killer,
        "motive":motive
    }
   
mystery = setup_mystery()


def display_intro(mystery):
    print("MURDER MYSTERY")
    print(F"\t{mystery["victim"]} has been found dead {mystery["location"]}")
    print(f"\tweapon: {mystery["weapon"]}")
    print("SUSPECTS: ")
    for i, suspect in enumerate(mystery['suspects'],1):
        print(f"\t{i}. {suspect}")


def inerogation(suspect,mystery):
    if suspect==mystery["killer"]:
        responce=random.choice(killer_responses)
        print(responce)
    else:
        innocent=random.choice(innocent_responses)
        print(innocent)    

def run_game():
    display_intro(mystery)
    for i in range(3):
        print(f"\tinterogation {i} of 3 Who do you want to Interogate")
        user_choice=input("\t\tEnter choice: ")
        

run_game()
