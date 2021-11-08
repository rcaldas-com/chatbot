from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from datetime import datetime
import psutil, shutil, os, time

def save_profile():
	for pid in psutil.pids():
		try:
			cmdline = open("/proc/"+str(pid)+"/cmdline", "r").read()
			if distinguishkey in cmdline:
				profile = cmdline.split('-profile')[1].split(' ')[0].replace('\x00', '')
				psutil.Process(pid).kill() # kill firefox (nicely) and unlock profile lock
				if os.path.isdir(profile_path):
					shutil.rmtree(profile_path, ignore_errors=True)
				shutil.copytree(profile, '/profile', symlinks=True, dirs_exist_ok=True) # copy the new profile to profile_path, don't resolve "lock" symlink
				break
		except:
			pass

distinguishkey = "profileworkaround"

options = Options()
options.set_preference('profile', '/profile')
options.add_argument(distinguishkey)
options.add_argument('--headless')
driver = Firefox(options=options)

driver.get("https://web.whatsapp.com")
# driver.get("https://rcaldas.com")

try:
	try:
		WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, "//canvas[@aria-label='Scan me!']")))
		print('ask for scan')
		save_profile()
	except:
		login = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.ID, 'user')))

		login.send_keys('rcaldas')
		driver.find_element(By.ID, 'pwd').send_keys('jsaklfjlksj')
		# driver.find_element(By.ID, 'login').click()
		driver.save_screenshot(f"/app/{datetime.now().strftime('%Y-%m-%d_%H-%M')}_screen.png")
finally:
    driver.quit()


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


