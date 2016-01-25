from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Tarquin has heard he should be more organised by using a cool new online to-do app.
        # He goes to check out its homepage
        self.browser.get('http://localhost:8000')

        # He notices the page title and header mention to-do lists
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test!')

        # He is invited to enter a to-do item straight away.

        # He types "Check the estate" into a text box.

        # When he hits enter, the page updates, and now the page lists:

        # "1: Check the estate" as an item in a to-do lists.

        # There is still a text box inviting him to add another item.

        # He enters "Look under the cooker for mice"

        # The page updates again, and now shows both items on his list.

        # Tarquin wonders if the site will remember his list. Then he sees
        # that the site has generated a unique URL for him -- there is some
        # explanatory text to that effect.

        # He visits that URL -- his to-do list is still there.

        # Satisfied, he has a stretch and a little kip.

if __name__ == '__main__':
    unittest.main()
