import time
import os
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
chromePath = "/home/vasu/Downloads/chromedriver"
url = "http://play.pokemonshowdown.com"
f = open("/home/vasu/Work/pokemon_stuff/pokemon_team.txt")
team = f.read()
f2 = open("/home/vasu/Work/pokemon_stuff/darkpokes.txt")
darkpokes = f2.read()
f3 = open("/home/vasu/Work/pokemon_stuff/threats.txt")
threats = f3.read()
f4 = open("/home/vasu/Work/pokemon_stuff/darkthreats.txt")
dark_threats = f4.read()
username = "asdf5556"
driver = webdriver.Chrome(executable_path=chromePath)
driver.get(url)

def login(username):
    time.sleep(1)
    elem = driver.find_element_by_name("login")
    elem.click()
    time.sleep(1)
    user = driver.find_element_by_name("username")
    user.send_keys(username)
    user.send_keys(Keys.RETURN)
    time.sleep(1)

def make_team(team):
    builder = driver.find_element_by_xpath("/html/body/div[2]/div/div[1]/div[2]/div[2]/p[1]/button")
    builder.click()
    new_team = driver.find_element_by_xpath("/html/body/div[4]/div/ul/li[2]/button")
    new_team.click()
    time.sleep(3)
    import_button = driver.find_element_by_xpath("/html/body/div[4]/div[2]/ol/li[4]/button")
    import_button.click()
    textfield = driver.find_element_by_xpath("/html/body/div[4]/textarea")
    textfield.send_keys(team)
    save = driver.find_element_by_xpath("/html/body/div[4]/div/button[3]")
    save.click()
    driver.get(url)
    time.sleep(2)
    form = driver.find_element_by_xpath("/html/body/div[2]/div/div[1]/div[2]/div[1]/form/p[1]/button")
    form.click()
    ou = driver.find_element_by_xpath("/html/body/div[4]/ul[1]/li[4]/button")
    ou.click()

def start_battle():
    url1 = driver.current_url
    battle = driver.find_element_by_xpath("/html/body/div[2]/div/div[1]/div[2]/div[1]/form/p[3]/button")
    battle.click()
    while url1 == driver.current_url:
        time.sleep(1.5)
        print "waiting"
    print "found battle"

def switch_poke(poke):
    if poke == "Smeargle":
        choose = driver.find_element_by_xpath("/html/body/div[4]/div[5]/div/div[2]/div[2]/button[4]")
        choose.click()
    elif poke == "Diglett":
        choose = driver.find_element_by_xpath("/html/body/div[4]/div[5]/div/div[2]/div[2]/button[2]")
        choose.click()
    elif poke == "Dugtrio":
        choose = driver.find_element_by_xpath("/html/body/div[4]/div[5]/div/div[2]/div[2]/button[3]")
        choose.click()
    elif poke == "Clefable":
        choose = driver.find_element_by_xpath("/html/body/div[4]/div[5]/div/div[2]/div[2]/button[5]")
        choose.click()
    elif poke == "Espeon":
        choose = driver.find_element_by_xpath("/html/body/div[4]/div[5]/div/div[2]/div[2]/button[6]")
        choose.click()
    elif poke == "Sableye":
        choose = driver.find_element_by_xpath("/html/body/div[4]/div[5]/div/div[2]/div[2]/button[1]")
        choose.click()
    wait_for_move()
    time.sleep(3)

def make_move(move):
    if move == "Taunt" or move == "Calm Mind"  or move == "Dark Void"  or move == "Earthquake":
        move = driver.find_element_by_xpath("/html/body/div[4]/div[5]/div/div[2]/div[2]/button[1]")
        move.click()
    elif move == "Geomancy" or move == "Reversal"  or move == "Stored Power"  or move == "Knock Off":
        move = driver.find_element_by_xpath("/html/body/div[4]/div[5]/div/div[2]/div[2]/button[2]")
        move.click()
    elif move == "Baton Pass" or move == "Stealth Rock"  or move == "Moonblast"  or move == "Hidden Power Fighting" or move == "Gravity":
        move = driver.find_element_by_xpath("/html/body/div[4]/div[5]/div/div[2]/div[2]/button[3]")
        move.click()
    elif move == "Memento" or move == "Will-O-Wisp"  or move == "Substitute"  or move == "Cotton Guard":
        move = driver.find_element_by_xpath("/html/body/div[4]/div[5]/div/div[2]/div[2]/button[4]")
        move.click()
    wait_for_move()
    time.sleep(3)

def get_team():
    team = driver.find_element_by_xpath("/html/body/div[4]/div[3]/div[1]/div[15]/em")
    print team.text
    team_list = team.text.split("/")
    print team_list
    return team_list

def get_hp():
    if check_exists_by_xpath("/html/body/div[4]/div[1]/div/div[5]/div[2]/div/div[1]") == True and get_player_number() == 2:
        hp_text = driver.find_element_by_xpath("/html/body/div[4]/div[1]/div/div[5]/div[2]/div/div[1]")
        hp = hp_text.text.strip("%")
        hp = int(hp)
    elif check_exists_by_xpath("/html/body/div[4]/div[1]/div/div[5]/div[1]/div/div[1]") == True and get_player_number() == 1:
        hp_text = driver.find_element_by_xpath("/html/body/div[4]/div[1]/div/div[5]/div[1]/div/div[1]")
        hp = hp_text.text.strip("%")
        hp = int(hp)
    else:
        hp = 0
    return hp

def get_log():
     log = driver.find_element_by_xpath("/html/body/div[4]/div[3]/div[1]")
     return log.text

def get_player_number():
    player = driver.find_element_by_xpath("/html/body/div[4]/div[3]/div[1]/div[1]/small")
    print player.text
    if username in player.text:
        return 1
    else:
        return 2
'''
def get_opp_poke(oppTeam):
    log = get_log()
    biggest = 0
    biggestPoke = "your mom"
    for i in oppTeam:
        current = log.rfind(i)
        if current > biggest:
            biggest = log.rfind(i)
            biggestPoke = i
    return biggestPoke.lower().strip()
'''
def get_opp_poke(oppTeam):
    img = driver.find_element_by_xpath("/html/body/div[4]/div[1]/div/div[4]/div[1]/img[6]")
    text = img.get_attribute('src')
    back = text.rindex('.')
    poke = text[46:back]
    if "shiny" in poke:
        poke = poke[6:]
    return poke

def check_sub():
    return None

def check_exists_by_xpath(xpath):
    try:
        driver.find_element_by_xpath(xpath)
    except NoSuchElementException:
        return False
    return True

def check_exists_by_name(name):
    try:
        driver.find_element_by_name(name)
    except NoSuchElementException:
        return False
    return True

def wait_for_move():
    time_exists = check_exists_by_name("setTimer")
    while time_exists:
        print "waiting for their move"
        time.sleep(2)
        time_exists = check_exists_by_name("setTimer")
    print "their move just ended"
    time.sleep(5)

login(username)
time_exists = check_exists_by_name("setTimer")
make_team(team)
login("asdf5556")
start_battle()
time.sleep(10)
team = get_team()
opp_team = [x.encode('ascii','ignore').strip() for x in team]
print type(opp_team)
print opp_team
player = get_player_number()
print "i am player " + str(player)
switch_poke("Sableye")
opp_poke = get_opp_poke(opp_team)
print opp_poke
print "used taunt"
make_move("Taunt")
time.sleep(5)
curr_hp = get_hp()
print curr_hp
if curr_hp > 60:
    while curr_hp > 60:
        print "used knock off"
        make_move("Knock Off")
        curr_hp = get_hp()
        print curr_hp
        log = get_log()
        if curr_hp == 0 and "Sableye fainted" in log:
            print "Sableye fainted"
            break
log = get_log();
if "Sableye fainted" not in log:
    wait_for_move()
    make_move("Gravity")
time.sleep(5)
while curr_hp > 0 or "Sableye fainted" not in log:
    print "used taunt"
    make_move("Taunt")
    curr_hp = get_hp()
    log = get_log()
    if "Sableye fainted" in log:
        print "Sableye fainted"
        break
print "switching to diglett"
switch_poke("Diglett")
make_move("Memento")
print "switching to dugtrio"
switch_poke("Dugtrio")
make_move("Memento")
print "switching to smeargle"
switch_poke("Smeargle")
make_move("Geomancy")
print "using Geomancy"
if get_opp_poke(opp_team) in threats:
    print "i see threat"
    make_move("Dark Void")
make_move("Cotton Guard")
print "using cotton guard"
make_move("Baton Pass")
print "using baton pass"

if any(x in dark_threats for x in opp_team):
    print "hello there's a mandibuzz in their team"
    switch_poke("Clefable")
    while True:
        time.sleep(5)
        print get_opp_poke(opp_team)
        if get_opp_poke(opp_team) not in darkpokes:
            print "this is not a dark poke"
            make_move("Stored Power")
            time.sleep(5)
            wait_for_move();
        else:
            print "this is a dark poke"
            make_move("Moonblast")
            time.sleep(5)
            wait_for_move();

else:
    switch_poke("Espeon")
    hp = get_hp()
    log = get_log()

    '''
    FINAL LOGIC: UNFINISHED
    while True:
        while hp > 40:
            if check_sub() == False:
                make_move("Substitute")
                time.sleep(3)
                if check_sub() == True:
                    if get_opp_poke(opp_team) not in darkpokes:
                        make_move("Stored Power")
                    else:
                        make_move("Hidden Power Fighting")
                else:
            else:
                if get_opp_poke(opp_team) not in darkpokes:
                    make_move("Stored Power")
                else:
                    make_move("Hidden Power Fighting")
        '''
    #TEST LOGIC:
    while True:
        time.sleep(5)
        print get_opp_poke(opp_team)
        if get_opp_poke(opp_team) not in darkpokes:
            print "this is not a dark poke"
            make_move("Stored Power")
            time.sleep(5)
            wait_for_move();
        else:
            print "this is a dark poke"
            make_move("Hidden Power Fighting")
            time.sleep(5)
            wait_for_move();

