from selenium import webdriver
import time
navegador = webdriver.Chrome()
navegador.get("https://login.live.com/")
time.sleep (2)
navegador.find_element ("xpath" , ('//*[@id="i0116"]')).click ()
time.sleep (2)
navegador.find_element ("xpath" , ('//*[@id="i0116"]')).send_keys ('fernanda@teste.com')
time.sleep (2)
navegador.find_element ("xpath" , ('//*[@id="idSIButton9"]')).click ()
navegador.find_element ("xpath" , ('//*[@id="i0118"]')).send_keys ('teste@teste')
time.sleep (3)
navegador.find_element ("xpath" , ('//*[@id="idSIButton9"]')).click ()
