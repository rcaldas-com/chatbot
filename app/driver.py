from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
import os


options = Options()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
driver = Firefox(options=options)


driver.get("https://web.whatsapp.com")

driver.save_screenshot('screen.png')


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
