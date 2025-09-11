import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class FibonacciCalculatorTest(unittest.TestCase):
    """
    Test case for the Fibonacci calculation feature.
    """

    def setUp(self):
        """
        Set up the Selenium WebDriver.
        """
        self.driver = webdriver.Chrome()  # Ensure the Chrome WebDriver is installed and in PATH

    def tearDown(self):
        """
        Clean up and close the WebDriver.
        """
        self.driver.quit()

    def test_fibonacci_calculation(self):
        """
        Test the Fibonacci calculation by sending a GET request to the /fib/<argument> endpoint.
        """
        argument = 10
        self.driver.get(f'http://localhost:5000/fib/{argument}')  # Adjust the URL as needed

        # Wait for the output.html page to load
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, 'output'))
        )

        # Check for the presence of the first 10 Fibonacci numbers
        expected_fibonacci = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
        output_element = self.driver.find_element(By.ID, 'output')
        output_text = output_element.text

        for number in expected_fibonacci:
            self.assertIn(str(number), output_text)

        # Check for truncation message if applicable
        if len(output_text) > 100:  # Assuming 100 is the display limit
            self.assertIn('Output exceeds display limit', output_text)

if __name__ == '__main__':
    unittest.main()
