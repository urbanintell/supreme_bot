from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from datetime import datetime
import os

crome_options = Options()
crome_options.add_argument('--headless')
crome_options.add_argument('--window-size=1920x1080')

class Info(object):
    def __init__(self,name,email,size,phone,address,zipcode,cvv,cardNumber,cardMonth,cardYear):
        self.name = name
        self.email_address = email
        self.size = size
        self.phon_number = phone
        self.address = address
        self.zip_code = zipcode
        self.c_v_v = cvv
        self.card_month = cardMonth
        self.card_year = cardYear
        self.card_number = cardNumber

#Accounts will allow you to put in as many orders as you want this is where you will specify which items you want to put in an order for
class Accounts(object):
    def __init__(self,basurl,keywords,size):
        self.base_url = base_url
        self.keywords = keywords
        self.size = size


class KrocBot(object):
# was trying out the firefox headless to see speeds didnt finish with that yet.

    def __init__(self):
        self.info = Info("name","email","size","111-111-2525","104 anywhere","27936","808","5252525252525252","05","2020")


    def getSupreme(self,url_to_product="http://www.supremenewyork.com/shop/all/jackets",path_to_chrome_driver="./geckodriver"):


        # TODO: change location of chromedriver
        driver = webdriver.Firefox(firefox_options=crome_options, executable_path=path_to_chrome_driver)
        # driver = webdriver.Chrome(path_to_chrome_driver)
        link = url_to_product
        driver.get(link)

        items = driver.find_elements_by_tag_name("article");

        keys = ["Taped", "Seam", "Red"]
        for item in items:
            if keys[0] in item.text and keys[1] in item.text and keys[2] in item.text:
                driver.get(item.find_element_by_css_selector("a[class='name-link']").get_attribute("href"))
                break
            else:
                print(item.text)


        size = Select(driver.find_element_by_name('s'))
        size.select_by_value(self.info.size)

        addToCart = driver.find_element_by_xpath("//fieldset[@id='add-remove-buttons']/input")
        addToCart.click()

        checkoutNowButton = driver.find_element_by_xpath("//a[@class='button checkout']")

        while not checkoutNowButton.is_displayed():
            if checkoutNowButton.is_displayed():
                break

        checkoutNowButton.click()

        name = driver.find_element_by_xpath("//input[@id='order_billing_name']")
        name.send_keys(self.info.name)
        name.send_keys(Keys.TAB)

        email = driver.find_element_by_xpath("//input[@id='order_email']")
        email.send_keys(self.info.email)

        credit_card_month = Select(driver.find_element_by_name('credit_card[year]'))
        credit_card_month.select_by_value(self.info.card_year)

        telephone = driver.find_element_by_xpath("//input[@id='order_tel']")
        telephone.send_keys(self.info.telephone)

        order_billing_address = driver.find_element_by_xpath("//input[@name='order[billing_address]']")
        order_billing_address.send_keys(self.info.address)

        order_billing_zip = driver.find_element_by_xpath("//input[@id='order_billing_zip']")
        order_billing_zip.send_keys(self.info.zip_code)

        orcer = driver.find_element_by_xpath("//input[@id='orcer']")
        orcer.send_keys(self.info.c_v_v)

        credit_card = driver.find_element_by_xpath("//input[@name='credit_card[nlb]']")
        credit_card.send_keys(self.info.card_number)

        credit_card_month = Select(driver.find_element_by_name('credit_card[month]'))
        credit_card_month.select_by_value(self.info.card_month)

        credit_card_month = Select(driver.find_element_by_name('credit_card[year]'))
        credit_card_month.select_by_value(self.info_card_year)

        checkbox = driver.find_element_by_class_name("terms")
        checkbox.click()

        store_address = driver.find_element_by_id("store-address")
        store_address.click()

        submit = driver.find_element_by_name("commit")
        submit.click()



if __name__ == '__main__':
    start = datetime.now()
    currentUser = KrocBot()
    currentUser.getSupreme()
    finish = datetime.now() - start
    print(finish)
