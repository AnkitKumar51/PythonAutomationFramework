from Config.locators import Locator
from Pages.BasePage import BasePage


class RibbonAlarmsPage(BasePage):

    def goTo_Alarms(self):
        self.do_click(Locator.OptionsButton)
        self.do_click(Locator.RibbonOptions)
        self.do_click(Locator.RibbonAlarms)
