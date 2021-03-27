from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from time import sleep

PROMISED_SPEED = 100
PROMISED_UP = 50
EMAIL = "YOUR EMAIL ID"
PASSWORD = "YOUR PASSWORD"
webdriver_path = "WEB DRIVER PATH"



class InternetSpeedTwitterBot:
    def __init__(self, driver_path):
        self.driver = webdriver.Chrome(executable_path=driver_path)
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        self.driver.get(url="https://www.speedtest.net/")
        sleep(2)
        check_speed = self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a')
        check_speed.click()
        sleep(60)     #sleep for 2 mins
        result_id = self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[1]/div/div/div[2]/div[2]').text
        print(result_id)

        self.up = self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
        print(f"Up: {self.up}")
        self.down = self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span').text
        print(f"down : {self.down}")



    def tweet_at_provider(self):
        self.driver.get(url="https://twitter.com")
        sleep(2)
        login = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div/main/div/div/div/div[1]/div/div[3]/a[2]')
        login.click()
        sleep(1)
        email = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[1]/label')
        email.send_keys(EMAIL)
        password = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[2]/label')
        password.send_keys(PASSWORD)
        password.send_keys(Keys.ENTER)
        sleep(5)
        tweet = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div/div/div/div')
        tweet.send_keys(f"Hey Internet Provider, why is my internet uploading speed is:"
                        f" {self.up}down/{self.down}up Mbits/s "
                        f"when I pay for {PROMISED_SPEED}down/{PROMISED_UP}up MBits/s."
                        f"\n-Just a Python Project")
        tweeting = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[4]/div/div/div[2]/div[3]')
        tweeting.send_keys(Keys.ENTER)
        if tweeting.get_attribute("data-focusable") == "true":
            print("Tweeted Successfully.")
        else:
            print("Unsuccessful")
            return



bot = InternetSpeedTwitterBot(webdriver_path)
bot.get_internet_speed()
bot.tweet_at_provider()

