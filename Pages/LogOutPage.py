from Config.locators import Locator
from Pages.BasePage import BasePage


class LogOutPage(BasePage):

    def do_logout(self):
        self.do_click(Locator.LogOutOption)
        self.do_click(Locator.LogOutButton)
