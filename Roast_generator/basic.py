import random
opener = [
"Bhai sun,",
"Arre yaar,",
"Sach bolu?",
"Reality check:",
"Breaking news:",
"Fact:",
"Sun bhai,",
"Honestly,",
"Dekho,",
"Public notice:",
"Alert:",
"Beta sun,",
"Attention:",
"Note kar:",
"Update:",
"Rumour hai,",
"Investigation:",
"Headline:",
"Hot take:",
"Truth:",
"Science says:",
"Report:",
"Exclusive:",
"News flash:",
"System log:",
"Daily update:",
"Internet says:",
"Research:",
"Warning:",
"Observation:",
"Breaking alert:",
"Latest news:",
"Official report:",
"Prediction:",
"Data shows:",
"AI analysis:",
"Public opinion:",
"Survey result:",
"Conclusion:",
"Final verdict:",
"Certified fact:",
"Deep research:",
"Update from NASA:",
"Global news:",
"Study says:",
"Future report:",
"Alert system:",
"Breaking report:",
"Truth bomb:",
"Reality update:"
]

middle = [
"{name} {profession} banega?",
"{name} as {profession}?",
"{name} {profession} career?",
"{name} ka {profession} plan?",
"{name} {profession} level?",
"{name} trying {profession}?",
"{name} future {profession}?",
"{name} ka {profession} talent?",
"{name} {profession} dream?",
"{name} ka {profession} skill?",
"{name} {profession} attempt?",
"{name} ka {profession} logic?",
"{name} learning {profession}?",
"{name} ka {profession} IQ?",
"{name} ka {profession} brain?",
"{name} ka {profession} effort?",
"{name} ka {profession} result?",
"{name} ka {profession} progress?",
"{name} ka {profession} try?",
"{name} doing {profession}?",
"{name} ka {profession} chance?",
"{name} ka {profession} score?",
"{name} ka {profession} future?",
"{name} ka {profession} dream?",
"{name} ka {profession} mindset?",
"{name} ka {profession} talent?",
"{name} {profession} banne wala?",
"{name} learning {profession}?",
"{name} ka {profession} career graph?",
"{name} ka {profession} brain power?",
"{name} ka {profession} training?",
"{name} ka {profession} exam?",
"{name} ka {profession} logic?",
"{name} ka {profession} coding?",
"{name} ka {profession} interview?",
"{name} ka {profession} resume?",
"{name} ka {profession} progress?",
"{name} ka {profession} practice?",
"{name} ka {profession} growth?",
"{name} ka {profession} motivation?",
"{name} ka {profession} plan B?",
"{name} ka {profession} talent test?",
"{name} ka {profession} performance?",
"{name} ka {profession} attempt noob?",
"{name} ka {profession} survival?",
"{name} ka {profession} mission?",
"{name} ka {profession} destiny?",
"{name} ka {profession} confidence?",
"{name} ka {profession} struggle?",
"{name} ka {profession} upgrade?"
]

ending = [
"system error.",
"404 brain not found.",
"loading since 2001.",
"mission failed.",
"try again later.",
"AI confused.",
"logic missing.",
"skill not installed.",
"future buffering.",
"talent not detected.",
"upgrade required.",
"error detected.",
"brain offline.",
"hope crashed.",
"career RIP.",
"confidence bug.",
"talent beta version.",
"success 0%.",
"skill loading...",
"no update found.",
"patch required.",
"destiny cancelled.",
"progress stuck.",
"system reboot needed.",
"try reinstalling brain.",
"feature unavailable.",
"career simulation failed.",
"brain lag detected.",
"talent missing.",
"system overheating.",
"logic crashed.",
"update failed.",
"install common sense.",
"future not responding.",
"mission aborted.",
"brain.exe stopped.",
"talent not supported.",
"server rejected.",
"career loading forever.",
"confidence corrupted.",
"logic.exe crashed.",
"brain in sleep mode.",
"skill expired.",
"hope not found.",
"career beta testing.",
"404 success.",
"destiny timeout.",
"talent under maintenance.",
"system panic.",
"upgrade your brain."
]
def get_roast_opener():
    return random.choice(opener)

def get_roast_middle():
    return random.choice(middle)

def get_roast_end():
    return random.choice(ending)

def roast(name,profession):
    first=get_roast_opener()
    second=get_roast_middle().format(name=name, profession=profession)
    third=get_roast_end()
    result=F"{first} {second} {third}"
    return result

def run_roast():
    Name=input("Enter name: ")
    Prof=input("Enter profession: ")
    count=0
    while True:
        count+=1
        
        Result=roast(Name,Prof)
        print(Result)
        try:
            print("\twant another one? (YES: 1 || NO: 0)\n")
            choice=int(input("\tEnter choice: "))
            if choice==0:
                print("\tGood bye! \n \t total roasts: ",count)
                break
        except(ValueError):
            print("invalid input!")
       

run_roast()   
