from time import sleep
from threading import Thread
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

numberOfBots = int(input("Number of bots: "))
baseName = input("Name of bots: ")
gamePin = int(input("Your game pin: "))

delayBeforeLeaving = 20
delayBetweenActions = 2.5

def createBot(pin, name):

    options = Options()
    options.add_argument("--headless")
    options.add_argument("test-type")
    options.add_argument("--js-flags=--expose-gc")
    options.add_argument("--enable-precise-memory-info")
    options.add_argument("--disable-default-apps");
    
    browser = webdriver.Chrome(options = options)
    browser.get("http://kahoot.it")
    
    sleep(delayBetweenActions)
    
    browser.find_element_by_name("gameId").send_keys(pin)
    browser.find_element_by_xpath("""//*[@id="root"]/div[1]/div/main/div[2]/main/div/form/button""").click()
    
    sleep(delayBetweenActions)
    
    browser.find_element_by_name('nickname').send_keys((u'\u200b').join(name))
    browser.find_element_by_xpath("""//*[@id="root"]/div[1]/div/main/div[2]/main/div/form/button""").click()

    sleep(delayBeforeLeaving)

    browser.close()
    
for i in range(numberOfBots): 
    
    Thread(target = lambda : createBot(gamePin, baseName + str(i))).start()
