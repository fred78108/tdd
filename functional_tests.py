from selenium import webdriver
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
        self.fail('Finish the test!')

        #types "buy peacock feathers" into a text box. 

        #when she hits enter the page updates and now lists "1: buys peackock feathers"

        #there is still a text box inviting her to enter another item

        #enters "use feathers to make a fly"

        #the page updates again with both items on her list

        #the site has generated a unique URL. 

        #visit the unique URL to validate the to-do list is still there

if __name__ == '__main__':
    unittest.main(warnings='ignore')