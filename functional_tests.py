from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest


class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
    
    def tearDown(self):
        self.browser.quit()
    
    def test_can_start_a_list_and_retrieve_it_later(self):
        self.browser.get('http://localhost:8000')
        #check out the page title
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text

        self.assertIn('To-Do', header_text)

        self.assertEqual(
            iputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )
    
        #types "buy peacock feathers" into a text box. 
        inputbox.send_keys('Buy peakcock feathers')

        #when she hits enter the page updates and now lists "1: buys peackock feathers"
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        table = self.browser.find_element_by_id('id_list_table')
        rows  = table.find_elements_by_tag_name('tr')
        self.assertTrue(
            any(row.text == '1: Buy peakcock feathers for row in rows')
        )
        #there is still a text box inviting her to enter another item
        self.fail('Finish the test')

        #enters "use feathers to make a fly"

        #the page updates again with both items on her list

        #the site has generated a unique URL. 

        #visit the unique URL to validate the to-do list is still there

if __name__ == '__main__':
    unittest.main(warnings='ignore')