import traceback
import time
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

def login(username):
    time.sleep(1)
    elem = driver.find_element_by_name("login")
    elem.click()
    time.sleep(1)
    user = driver.find_element_by_name("username")
    user.send_keys(username)
    user.send_keys(Keys.RETURN)
    time.sleep(1)

def off_sound():
    sound = driver.find_element_by_xpath("/html/body/div[6]/p[3]/label/input")
    sound.click()

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

def start_battle():
    url1 = driver.current_url
    form = driver.find_element_by_xpath("/html/body/div[2]/div/div[1]/div[2]/div[1]/form/p[1]/button")
    form.click()
    ou = driver.find_element_by_xpath("/html/body/div[4]/ul[1]/li[4]/button")
    ou.click()
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
    time.sleep(2)
    start_timer()
    wait_for_move()

def make_move(move):
    if move == "Taunt" or move == "Calm Mind"  or move == "Dark Void"  or move == "Earthquake" or move == "Morning Sun":
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
    time.sleep(2)
    start_timer()
    wait_for_move()
    time.sleep(3)

def get_team():
    team = driver.find_element_by_xpath("/html/body/div[4]/div[3]/div[1]/div[15]/em")
    print team.text
    team_list = team.text.split("/")
    print team_list
    return team_list

def get_hp():
    if check_exists_by_xpath("/html/body/div[4]/div[1]/div/div[5]/div[contains(@class,'statbar rstatbar')]/div/div[1]"):
        hp_text = driver.find_element_by_xpath("/html/body/div[4]/div[1]/div/div[5]/div[contains(@class,'statbar rstatbar')]/div/div[1]")
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

def get_my_poke():
    return None

def check_sub():
    sub = driver.find_element_by_xpath("/html/body/div[4]/div[1]/div/div[4]/div[4]/img[1]")
    sub_text = sub.get_attribute('style')
    sub_text = sub_text[-2:-1]
    opacity = int(sub_text)
    print "my opacity is " + str(opacity)
    if opacity > 1:
        return True
    else:
        return False


def check_exists_by_xpath(xpath):
    try:
        driver.find_element_by_xpath(xpath)
    except NoSuchElementException:
        return False
    return True

def check_exists_by_class_name(name):
    try:
        driver.find_element_by_class_name(name)
    except NoSuchElementException:
        return False
    return True

def check_exists_by_name(name):
    try:
        driver.find_element_by_name(name)
    except NoSuchElementException:
        return False
    return True

def start_timer():
    if check_exists_by_xpath("/html/body/div[4]/div[5]/div/p[2]/button"):
        timer = driver.find_element_by_xpath("/html/body/div[4]/div[5]/div/p[2]/button")
        if timer.text == "Start timer":
            timer.click()

def check_taunt():
    return None

class FinishedException(Exception):
    def __init__(self, won):
        self.won = won

class LostException():
    def __init__(self, lost):
        self.lost = lost

def wait_for_move():
    move_exists = check_exists_by_xpath("/html/body/div[4]/div[5]/div/div[2]/div[2]/button[1]")
    while move_exists == False:
        print "waiting for their move"
        time.sleep(2)
        move_exists = check_exists_by_xpath("/html/body/div[4]/div[5]/div/div[2]/div[2]/button[1]")
        if check_exists_by_xpath("/html/body/div[4]/div[5]/div/p[1]/em/button[2]"):
            save_replay = driver.find_element_by_xpath("/html/body/div[4]/div[5]/div/p[1]/em/button[2]")
            save_replay.click()
            time.sleep(10)
            raise FinishedException(True)

    print "their move just ended"

def run(driver):
    driver.get(url)
    login(username)
    start_battle()
    time.sleep(10)
    opponent_team = get_team()
    opp_team = [x.encode('ascii','ignore').strip() for x in opponent_team]
    print opp_team
    player = get_player_number()
    print "i am player " + str(player)
    switch_poke("Sableye")
    x = check_sub()
    print x
    print "used taunt"
    make_move("Taunt")
    #taunt = check_taunt()
    #print "Taunt is " + taunt
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
            if curr_hp == 0 and "bot1 fainted" in log:
                print "Sableye fainted"
                break
    log = get_log();
    if "bot1 fainted" not in log:
        wait_for_move()
        make_move("Gravity")
    time.sleep(5)
    while curr_hp > 0 or "bot1 fainted" not in log:
        print "used taunt"
        make_move("Taunt")
        curr_hp = get_hp()
        log = get_log()
        if "bot1 fainted" in log:
            print "Sableye fainted"
            break
    print "switching to diglett"
    switch_poke("Diglett")
    opp_poke = get_opp_poke(opp_team)
    log = get_log()
    if opp_poke == "terrakion" or opp_poke == "bisharp" or opp_poke == "thundurus":
        print "i see threat, will use earthquake"
        while opp_poke == "terrakion" or opp_poke == "bisharp" or opp_poke == "thundurus":
            make_move("Earthquake")
            opp_poke = get_opp_poke(opp_team)
            log = get_log()
            if "bot2 fainted" in log:
                print "Diglett fainted"
                break
    if "bot2 fainted" not in log:
        make_move("Memento")
    print "switching to dugtrio"
    switch_poke("Dugtrio")
    opp_poke = get_opp_poke(opp_team)
    log = get_log()
    if opp_poke == "terrakion" or opp_poke == "bisharp" or opp_poke == "thundurus":
        print "i see threat, will use earthquake"
        while opp_poke == "terrakion" or opp_poke == "bisharp" or opp_poke == "thundurus":
            make_move("Earthquake")
            opp_poke = get_opp_poke(opp_team)
            log = get_log()
            if "bot3 fainted" in log:
                print "Dugtrio fainted"
                break
    if "bot3 fainted" not in log:
        make_move("Memento")
    print "switching to smeargle"
    switch_poke("Smeargle")
    make_move("Geomancy")
    print "using Geomancy"
    log = get_log()
    if "bot4 fainted" in log:
        raise FinishedException(False)
    log = get_log()
    if get_opp_poke(opp_team) in threats:
        print "i see threat"
        make_move("Dark Void")
        log = get_log()
    make_move("Cotton Guard")
    print "using cotton guard"
    log = get_log()
    if "bot4 fainted" in log:
        raise FinishedException(False)
    make_move("Baton Pass")
    print "using baton pass"
    log = get_log()
    if "bot4 fainted" in log:
        raise FinishedException(False)

    if any(x in dark_threats for x in opp_team):
        print "hello there's a darkthreat in their team"
        switch_poke("Clefable")
        make_move("Substitute")
        while True:
            print get_opp_poke(opp_team)
            if get_opp_poke(opp_team) not in darkpokes:
                print "this is not a dark poke"
                make_move("Stored Power")
                wait_for_move();
            else:
                print "this is a dark poke"
                make_move("Moonblast")
                wait_for_move();

    else:
        switch_poke("Espeon")
        hp = get_hp()
        log = get_log()
        make_move("Substitute")

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
            log = get_log()
            if "bot6 fainted" in log:
                raise FinishedException(False)
            sub = check_sub()
            print "sub is up: " + str(sub)
            hp = get_hp()
            if(sub):
                while(sub):
                    print get_opp_poke(opp_team)
                    hp = get_hp()
                    if get_opp_poke(opp_team) not in darkpokes or get_opp_poke(opp_team) == "gyarados":
                        print "this is not a dark poke"
                        print "my hp is " + str(hp)
                        if hp < 50:
                            make_move("Morning Sun")
                        else:
                            make_move("Stored Power")
                    else:
                        print "this is a dark poke"
                        print "my hp is " + str(hp)
                        if hp < 50:
                            make_move("Morning Sun")
                        else:
                            make_move("Hidden Power Fighting")
                    sub = check_sub()
            elif sub == False and hp > 50:
                if get_opp_poke(opp_team) == "chansey" or get_opp_poke(opp_team) == "gengar":
                    make_move("Stored Power")
                elif get_opp_poke(opp_team) == "bisharp" or get_opp_poke(opp_team) == "tyranitar" or get_opp_poke(opp_team) == "tyranitar-mega" or get_opp_poke(opp_team) == "weavile" or get_opp_poke(opp_team) == "crawdaunt" or get_opp_poke(opp_team) == "greninja":
                    make_move("Hidden Power Fighting")
                else:
                    make_move("Substitute")
            else:
                make_move("Morning Sun")
driver = webdriver.Chrome(executable_path=chromePath)
driver.get(url)
login(username)
make_team(team)
with open("wins", "a") as f:
    while True:
        try:
            run(driver)
        except FinishedException as e:
            print "Actually won (or forfeited)"
            won = e.won
        except Exception as e:
            print traceback.format_exc()
            won = False
        f.write(str(won)+"\t"+driver.current_url+"\n")
        f.flush()
