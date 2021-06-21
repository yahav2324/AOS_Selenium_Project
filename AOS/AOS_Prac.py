from
driver = webdriver.Chrome(executable_path=r'C:\selenium\chromedriver.exe')
        driver.implicitly_wait(10)
        driver.get('https://juliemr.github.io/protractor-demo/')
        driver.maximize_window()