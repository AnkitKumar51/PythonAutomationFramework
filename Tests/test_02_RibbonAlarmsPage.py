from Pages.LoginPage import LoginPage
from Pages.LogOutPage import LogOutPage
from Pages.RibbonAlarmsPage import RibbonAlarmsPage
from Tests.TestBase import BaseTest
from Config.conf import testData


class Test_RibbonAlarmsPage(BaseTest):
    def test_visit_alarmsPage(self):
        self.loginPage = LoginPage(self.driver)
        self.logOutPage = LogOutPage(self.driver)
        self.ribbonAlarmsPage = RibbonAlarmsPage(self.driver)

        self.loginPage.do_login(testData.USERNAME, testData.PASSWORD)
        self.ribbonAlarmsPage.goTo_Alarms()
