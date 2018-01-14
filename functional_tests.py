from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest


class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
    
    def tearDown(self):
        self.browser.quit()

    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')  
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])

    def test_can_start_a_list_and_retrieve_it_later(self):
        self.browser.get('http://localhost:8000')
        #check out the page title
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text

        self.assertIn('To-Do', header_text)
        
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )
    
        #types "buy peacock feathers" into a text box. 
        inputbox.send_keys('Buy peacock feathers')

        #when she hits enter the page updates and now lists "1: buys peackock feathers"
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        self.check_for_row_in_list_table('1: Buy peacock feathers')

        #self.assertTrue(
        #    any(row.text == '1: Buy peakcock feathers' for row in rows), "New to-do item did not appear in table"
        #    f"new to-do item did not appear in table. Contents were:\n{table.text}"
        #)
        # the above lines can be replaced with a single line, nice!
        #self.assertIn('1: Buy peakcock feathers', [row.text for row in rows]) 


        #there is still a text box inviting her to enter another item
        #enters "use feathers to make a fly"
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Use peacock feathers to make a fly')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)
        #the page updates again with both items on her list
        self.check_for_row_in_list_table('1: Buy peacock feathers')
        self.check_for_row_in_list_table('2: Use peacock feathers')

        #the site has generated a unique URL. 
        self.fail('Finish the test')

        #visit the unique URL to validate the to-do list is still there

if __name__ == '__main__':
    unittest.main(warnings='ignore')