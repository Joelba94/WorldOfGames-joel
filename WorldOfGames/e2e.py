from selenium import webdriver
driver = webdriver.Chrome('chromedriver')


def test_scores_service():
    driver.get("http://127.0.0.1:5000/")
    score_element = int(driver.find_element_by_id("scores").text)
    if 1000 >= score_element >= 1:
        return True
    else:
        return False


def main_function():
    test = test_scores_service()
    if test:
        return 0
    else:
        return -1


main_function()