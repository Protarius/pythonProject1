import unittest
from selenium import webdriver




class TestOne(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="C:\GIT\Lib\site-packages\chromedriver_py\chromedriver_win32.exe")


    def test_url(self):
        self.driver.get("https://duckduckgo.com/")
        self.driver.find_element_by_id("search_form_input_homepage").send_keys("Google")
        self.driver.find_element_by_id("search_button_homepage").click()
        self.assertIn("https://duckduckgo.com/?q=Google", self.driver.current_url)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()