# -*- coding: utf-8 -*-
from selenium import webdriver
from fixture.config import Config
from fixture.session import SessionHelper

author = 'george.trf'


# TODO: add reading of config


class Application:

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.verificationErrors = []
        self.accept_next_alert = True
        self.session = SessionHelper(self)
        self.config = Config()

    def open_home_page(self):
        driver = self.driver
        driver.get(self.config.main_url)

    def open_some_route(self):
        driver = self.driver
        driver.find_element_by_link_text(u"Гайд").click()
        driver.find_element_by_link_text(u"База маршрутов").click()
        driver.find_element_by_link_text(u"Скалы Довбуша").click()
        driver.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='Хрест'])[1]/following::div[16]").click()
        driver.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='Привид'])[1]/following::a[1]").click()
        driver.find_element_by_link_text(u"Линия маршрута").click()

    def destroy(self):
        self.driver.quit()
