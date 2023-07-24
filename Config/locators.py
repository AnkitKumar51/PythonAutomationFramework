from selenium.webdriver.common.by import By


class Locator:
    """LoginPage Objects"""
    USERNAME = (By.XPATH, '//input[@id="txtEmail"]')
    PASSWORD = (By.XPATH, '//input[@id="txtPassword"]')
    LoginButton = (By.XPATH, '//input[@id="btnLogin"]')
    """LogOutPage Objects"""
    LogOutOption = (By.XPATH, '//span[@id="lblUser"]')
    LogOutButton = (By.XPATH, '//a[@id="cmdLogout"]')
    """RibbonAlarmsPage Objects"""
    OptionsButton = (By.XPATH, '//a[@aria-label="Open Menu"]')
    RibbonOptions = (By.XPATH, '//*[@id="hc-nav-1"]/div/div/div/ul/li[9]/div[1]/a')
    RibbonAlarms = (By.XPATH, '(//a[contains(text(),"Alarms")])[3]')

    list_items_xpath = "//ul[@class='error_list']/li"


