import time
import os
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
chromePath = "/home/vasu/Downloads/chromedriver"
url = "http://play.pokemonshowdown.com"
f = open("/home/vasu/Work/pokemon_stuff/pokemon_team")
team = f.read()
username = "asdf5555"
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
        choose = driver.find_element_by_xpath("/html/body/div[4]/div[5]/div/div[2]/div[2]/button[1]")
        choose.click()
    elif poke == "Diglett":
        choose = driver.find_element_by_xpath("/html/body/div[4]/div[5]/div/div[2]/div[2]/button[2]")
        choose.click()
    elif poke == "Dugtrio":
        choose = driver.find_element_by_xpath("/html/body/div[4]/div[5]/div/div[2]/div[2]/button[3]")
        choose.click()
    elif poke == "Clefable":
        choose = driver.find_element_by_xpath("/html/body/div[4]/div[5]/div/div[2]/div[2]/button[4]")
        choose.click()
    elif poke == "Espeon":
        choose = driver.find_element_by_xpath("/html/body/div[4]/div[5]/div/div[2]/div[2]/button[5]")
        choose.click()
    elif poke == "Sableye":
        choose = driver.find_element_by_xpath("/html/body/div[4]/div[5]/div/div[2]/div[2]/button[6]")
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
    elif move == "Baton Pass" or move == "Stealth Rock"  or move == "Moonblast"  or move == "Hidden Power [Fighting]" or move == "Gravity":
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
    if check_exists_by_xpath("/html/body/div[4]/div[1]/div/div[5]/div[2]/div/div[1]") == True:
        hp_text = driver.find_element_by_xpath("/html/body/div[4]/div[1]/div/div[5]/div[2]/div/div[1]")
        hp = hp_text.text.strip("%")
        hp = int(hp)
    else:
        hp = 0
    return hp

def get_log():
     log = driver.find_element_by_xpath("/html/body/div[4]/div[3]/div[1]")
     return log.text

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

def sub_exists():
    return 0

login("asdf5555")
time_exists = check_exists_by_name("setTimer")
make_team(team)
login("asdf5555")
start_battle()
time.sleep(10)
opp_team = get_team()
switch_poke("Sableye")
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
        log = get_log()
        if "Sableye fainted" in log:
            print "Sableye fainted"
            break
make_move("Gravity")
time.sleep(5)
while curr_hp > 0:
    print "used knock off"
    make_move("Knock Off")
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
make_move("Cotton Guard")
make_move("Baton Pass")
if "Mandibuzz" in opp_team:
    switch_poke("Clefable")
    make_move("Substitute")

else:
    switch_poke("Espeon")



