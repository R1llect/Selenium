import undetected_chromedriver
import time


try:
    driver = undetected_chromedriver.Chrome()
    driver.get('https://www.ozon.ru/product/elektricheskaya-zubnaya-shchetka-oral-b-pro-3-3500-goluboy-281045877/?sh=DN74W5yMAg')
    time.sleep(15)
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()
