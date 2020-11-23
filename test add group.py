# -*- coding: utf-8 -*-
from selenium import webdriver
import unittest
from group import Group


class UntitledTestCase(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Chrome()
        self.wd.implicitly_wait(5)

    def login(self, wd, username, password):
        wd.get("http://localhost/addressbook/")
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def test_add_group(self):
        wd = self.wd
        self.login(wd, username="admin", password="secret")
        self.create_group(wd, Group("Group12", "header12", "footer12"))
        self.logout()

    def test_add_empty_group(self):
        wd = self.wd
        self.login(wd, username="admin", password="secret")
        self.create_group(wd, Group(group_name="", header="", footer=""))
        self.logout()

    def create_group(self, wd, group):
        # create group
        wd.find_element_by_link_text("groups").click()
        wd.find_element_by_name("new").click()
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.group_name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)
        self.submit_group_creation()
        self.return_to_groups_page()

    def submit_group_creation(self):
        wd = self.wd
        wd.find_element_by_name("submit").click()

    def return_to_groups_page(self):
        wd = self.wd
        wd.find_element_by_link_text("group page").click()

    def logout(self):
        wd = self.wd
        wd.find_element_by_link_text("Logout").click()

    def tearDown(self):
        self.wd.quit()

    def test_add_contact(self):
        wd = self.wd
        self.login(wd, username="admin", password="secret")
        self.create_contact(wd)
        self.logout()

    def create_contact(self, wd):
        # init contact form
        wd.find_element_by_link_text("add new").click()
        # fill contact form
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys("Jerry")
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys("Spoon")
        wd.find_element_by_name("middlename").click()
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys("M")
        wd.find_element_by_name("middlename").click()
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys("M.")
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys("Spoon")
        wd.find_element_by_name("nickname").click()
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys("Spooky")
        wd.find_element_by_name("title").click()
        wd.find_element_by_name("company").click()
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys("YVB GmbH")
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys("test ave. 1")
        wd.find_element_by_name("home").click()
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys("123123132")
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys("654654654")
        wd.find_element_by_name("work").clear()
        wd.find_element_by_name("work").send_keys("98798879887")
        wd.find_element_by_name("fax").clear()
        wd.find_element_by_name("fax").send_keys("789789789")
        # wd.find_element_by_name("theform").click()
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys("js@test.com")
        wd.find_element_by_name("notes").click()
        wd.find_element_by_name("notes").clear()
        wd.find_element_by_name("notes").send_keys("this is our first client")
        # submit contact
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        # return to the home page
        wd.find_element_by_link_text("home page").click()


if __name__ == "__main__":
    unittest.main()
