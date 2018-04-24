from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from datetime import datetime


class Human(object):

    def __init__(self):
        self.users_name = 'John Doe'
        self.users_email = 'doe@gmail.com'
        self.size_number = '52607'
        self.cc_year = '2018'
        self.users_telephone = '8045557860'
        self.address = '1234 Nowehere Ave'
        self.address_number = '10'
        self.zip_code = '55555'
        self.user_orcer = '678'
        self.credit_card_number = '1234-5678-1234-2345'
        self.users_credit_card_month = '09'
        self.users_credit_card_year = '2022'


class Bot(object):

    def __init__(self):
        self.human = Human()

    def getSupreme(self,url_to_product="http://www.supremenewyork.com/shop/accessories/z5d9bt1e3/yybt603d8",path_to_chrome_driver="/Users/lusenii/Downloads/chromedriver"):
        # TODO: change location of chromedriver
        driver = webdriver.Chrome(path_to_chrome_driver)
        link = url_to_product
        driver.get(link)

        size = Select(driver.find_element_by_name('s'))
        size.select_by_value(self.human.size_number)

        addToCart = driver.find_element_by_xpath("//fieldset[@id='add-remove-buttons']/input")
        addToCart.click()

        checkoutNowButton = driver.find_element_by_xpath("//a[@class='button checkout']")

        while not checkoutNowButton.is_displayed():
            if checkoutNowButton.is_displayed():
                break

        checkoutNowButton.click()

        name = driver.find_element_by_xpath("//input[@id='order_billing_name']")
        name.send_keys(self.human.users_name)
        name.send_keys(Keys.TAB)

        email = driver.find_element_by_xpath("//input[@id='order_email']")
        email.send_keys(self.human.users_email)

        credit_card_month = Select(driver.find_element_by_name('credit_card[year]'))
        credit_card_month.select_by_value(self.human.cc_year)

        telephone = driver.find_element_by_xpath("//input[@id='order_tel']")
        telephone.send_keys(self.human.users_telephone)

        order_billing_address = driver.find_element_by_xpath("//input[@name='order[billing_address]']")
        order_billing_address.send_keys(self.human.address)

        billing_address_2 = driver.find_element_by_xpath("//input[@name='order[billing_address_2]']")
        billing_address_2.send_keys(self.human.address_number)

        order_billing_zip = driver.find_element_by_xpath("//input[@id='order_billing_zip']")
        order_billing_zip.send_keys(self.human.zip_code)

        orcer = driver.find_element_by_xpath("//input[@id='orcer']")
        orcer.send_keys(self.human.user_orcer)

        credit_card = driver.find_element_by_xpath("//input[@name='credit_card[nlb]']")
        credit_card.send_keys(self.human.credit_card_number)

        credit_card_month = Select(driver.find_element_by_name('credit_card[month]'))
        credit_card_month.select_by_value(self.human.users_credit_card_month)

        credit_card_month = Select(driver.find_element_by_name('credit_card[year]'))
        credit_card_month.select_by_value(self.human.users_credit_card_year)

        checkbox = driver.find_element_by_class_name("terms")
        checkbox.click()

        store_address = driver.find_element_by_id("store-address")
        store_address.click()

        submit = driver.find_element_by_name("commit")
        submit.click()

    def getSupremeWithSoup(self,url_to_product):

        driver = webdriver.Chrome('/Users/lusenii/Downloads/chromedriver')
        link = url_to_product
        driver.get(link)

        # bs_obj = BSoup(driver.page_source, 'html.parser')



if __name__ == '__main__':
    start = datetime.now()
    currentUser = Bot()
    currentUser.getSupreme()
    finish = datetime.now() - start
    print(finish)







