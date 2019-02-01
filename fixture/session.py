# -*- coding: utf-8 -*-
author = 'george.trf'


class SessionHelper:

    def __init__(self, app):
        self.app = app

    def login(self):
        driver = self.app.driver
        self.app.open_home_page()
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='Добавить прохождение(я)'])[1]/preceding::span[1]").click()
        driver.find_element_by_id("login-form-login").clear()
        driver.find_element_by_id("login-form-login").send_keys(self.app.config.user)
        driver.find_element_by_id("login-form-password").click()
        driver.find_element_by_id("login-form-password").clear()
        driver.find_element_by_id("login-form-password").send_keys(self.app.config.password)
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='Запомнить меня'])[1]/following::button[1]").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='wraithundead@gmail.com'])[1]/preceding::a[1]").click()
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='Добавить прохождение(я)'])[1]/preceding::li[2]").click()

    def logout(self):
        driver = self.app.driver
        self.app.open_home_page()
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='{0}'])[1]/preceding::a[1]"
                .format(self.app.config.email)).click()
        driver.find_element_by_link_text("Log out").click()
