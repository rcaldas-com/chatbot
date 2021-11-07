from selenium.webdriver import Firefox, FirefoxProfile
from selenium.webdriver.firefox.options import Options
from datetime import datetime
# import os
import random, psutil, shutil, os, time


profile_path = '/profile'

profile = FirefoxProfile(profile_path)
options = Options()
options.profile = profile

distinguishkey = "-persistentprofileworkaround"+str(random.randint(111111,999999))
options.add_argument(distinguishkey)

options.add_argument('--headless')
# options.add_argument('--no-sandbox')
# options.add_argument('--disable-dev-shm-usage')
driver = Firefox(options=options)

driver.get("https://web.whatsapp.com")

time.sleep(20)

#! Detect qrcode and ask for scan
driver.save_screenshot(f"/app/{datetime.now().strftime('%Y-%m-%d_%H-%M')}_screen.png")

# time.sleep(120)

for pid in psutil.pids():
	try:
		cmdline = open("/proc/"+str(pid)+"/cmdline", "r").read()
		if distinguishkey in cmdline:
		  profile = cmdline.split('-profile')[1].split(' ')[0].replace('\x00', '')
		  break
	except:
		pass

psutil.Process(pid).kill() # kill firefox (nicely) and unlock profile lock
if os.path.isdir(profile_path):
	shutil.rmtree(profile_path, ignore_errors=True)
shutil.copytree(profile, profile_path, symlinks=True, dirs_exist_ok=True) # copy the new profile to profile_path, don't resolve "lock" symlink

try:
    driver.quit() # will throw an error because we killed firefox
except Exception as e:
    print(e)
    pass

# cleanup
if os.path.isdir(profile):
	shutil.rmtree(profile)
if os.path.isdir(driver.profile.tempfolder):
	shutil.rmtree(driver.profile.tempfolder)




# profiletmp = driver.firefox_profile.path

# if os.system("cp -R " + profiletmp + "/* /profile/" ):
#     print("files should be copied :/")


# driver.quit()


# options.headless = True


# name = "Whatsapp Bot"
# input('Enter any key when you scan the qr code')
# user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
# user.click()

# def sendText(msg, driver):
#     msgBox = driver.find_element_by_xpath("//div[@spellcheck='true']")
#     msgBox.send_keys(msg)
#     button = driver.find_element_by_xpath('//span[@data-icon="send"]')
#     button.click()

# msgSent=driver.find_elements_by_class_name('_3zb-j')
# lastMsg = msgSent[-1].text
# print(lastMsg)
# executing=True
# while executing:
#     msgSent=driver.find_elements_by_class_name('_3zb-j')
#     try:
#         lastMsg = msgSent[-1].text
#     except:
#         print('erro ao ler mensagem')
#     if lastMsg=='/ping google':
#         os.system('ping google.com')
#         sendText('Pingando google', driver)
#     elif '/command' in lastMsg:
#         commandOutput = os.popen(lastMsg[8:]).read()
#         sendText('Executando comando {}'.format(lastMsg[8:]), driver)
#         commandOutput = str(commandOutput).replace('\n', '')
#         sendText(commandOutput, driver)
#     elif lastMsg=='/quit':
#         sendText('Quitting...', driver)
#         executing=False


