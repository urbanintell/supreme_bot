from selenium import webdriver
from datetime import datetime
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys


class Account(object):
    def __init__(self,name,email,size,phone,address,zipcode,cvv,cardNumber,cardMonth,cardYear,baseURL,keywords,orcer):
        self.name = name
        self.email_address = email
        self.size = size
        self.phone_number = phone
        self.address = address
        self.zip_code = zipcode
        self.c_v_v = cvv
        self.card_month = cardMonth
        self.card_year = cardYear
        self.card_number = cardNumber
        self.base_url = baseURL
        self.keywords = keywords
        self.user_orcer = orcer


class Bot(object):
    # added list for user to insert proxies
    def __init__(self):
        self.account = Account("John Doe","doe@gmail.com","54401","8045557860","1234 Nowehere Ave","55555","808","1234567812342345","09","2022","http://www.supremenewyork.com/shop/all","jackets+Taped+Seam+Red","678")
        self.proxies = []
        file = open("proxies.txt","r")
        for line in file:
            self.proxies.append(line.strip())

    def getSupreme(self):

        # TODO: change location of chromedriver
        # driver = webdriver.Chrome(chrome_options=crome_options, executable_path=path_to_chrome_driver)
        driver = webdriver.PhantomJS()
        link = self.generateURL(self.account.keywords,self.account.base_url)
        driver.get(link)

        items = driver.find_elements_by_tag_name("article")

        keys = ["Taped", "Seam", "Red"]
        for item in items:
            if keys[0] in item.text and keys[1] in item.text and keys[2] in item.text:
                driver.get(item.find_element_by_css_selector("a[class='name-link']").get_attribute("href"))
                break

        size = Select(driver.find_element_by_name('s'))
        size.select_by_value(self.account.size)

        addToCart = driver.find_element_by_xpath("//fieldset[@id='add-remove-buttons']/input")
        addToCart.click()

        checkoutNowButton = driver.find_element_by_xpath("//a[@class='button checkout']")

        while not checkoutNowButton.is_displayed():
            if checkoutNowButton.is_displayed():
                break

        checkoutNowButton.click()

        name = driver.find_element_by_xpath("//input[@id='order_billing_name']")
        name.send_keys(self.account.name)
        name.send_keys(Keys.TAB)

        email = driver.find_element_by_xpath("//input[@id='order_email']")
        email.send_keys(self.account.email_address)

        credit_card_month = Select(driver.find_element_by_name('credit_card[year]'))
        credit_card_month.select_by_value(self.account.card_year)

        telephone = driver.find_element_by_xpath("//input[@id='order_tel']")
        telephone.send_keys(self.account.phone_number)

        order_billing_address = driver.find_element_by_xpath("//input[@name='order[billing_address]']")
        order_billing_address.send_keys(self.account.address)

        order_billing_zip = driver.find_element_by_xpath("//input[@id='order_billing_zip']")
        order_billing_zip.send_keys(self.account.zip_code)

        orcer = driver.find_element_by_xpath("//input[@id='orcer']")
        orcer.send_keys(self.account.user_orcer)

        credit_card = driver.find_element_by_xpath("//input[@name='credit_card[nlb]']")
        credit_card.send_keys(self.account.card_number)

        credit_card_month = Select(driver.find_element_by_name('credit_card[month]'))
        credit_card_month.select_by_value(self.account.card_month)

        credit_card_month = Select(driver.find_element_by_name('credit_card[year]'))
        credit_card_month.select_by_value(self.account.card_year)

        checkbox = driver.find_element_by_class_name("terms")
        checkbox.click()

        store_address = driver.find_element_by_id("store-address")
        store_address.click()

        submit = driver.find_element_by_name("commit")
        submit.click()
        
    def generateURL(self,keywords,baseUrl):
            keywords_list = keywords.split("+")
            base = baseUrl
            return base+"/"+keywords_list[0]




if __name__ == '__main__':
    start = datetime.now()
    currentUser = Bot()
    currentUser.getSupreme()
    finish = datetime.now() - start
    print(finish)
