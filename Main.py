from selenium import webdriver
import time

PATH = "C:/Program Files (x86)\chromedriver.exe"

driver = webdriver.Chrome(PATH)

def is_it_int():
    while True:
        var = input()
        try:
            var = int(var)
            break
        except ValueError:
            print("Was that an integer? Please try again...")
    return var

def is_it_str():
    while True:
        var = input()
        try:
            var = str(var)
            break
        except ValueError:
            print("Was that a String? Please try again...")
    return var

def login(user, password):
    driver.get('https://huskyct.uconn.edu/') #goes to huskyCT
    driver.find_element_by_class_name("button-1").click() #gets rid of asking for cookies
    driver.find_element_by_id("cas-login").click()
    driver.find_element_by_id("username").send_keys(user)
    driver.find_element_by_id("password").send_keys(password)
    driver.find_element_by_id("button").click()


def prompt_login_info():
    print("What is your NetID?")
    username = is_it_str()
    print("What is your password?")
    password = is_it_str()

    return [username, password]


def return_classes():
    driver.maximize_window()
    driver.find_element_by_xpath("//*[@id=\"base_tools\"]/bb-base-navigation-button[4]/div/li/a/ng-switch/span").click()
    time.sleep(2)
    classes = []
    for j, i in enumerate(driver.find_elements_by_tag_name('h4')):
        classes.append(i.get_attribute("Title"))
        print("Class " + str(j + 1) + ": " + i.get_attribute("Title"))
    return classes


'''def getting_grades():'''

def main():
    print("Grade module has begun. Start time : " + time.ctime())
    print("Please respond with 1 (yes) or 2 (no) if you want the grading module")
    if is_it_int() == 1:
        [username,password] = prompt_login_info()
    else:
        quit()
    login(username, password)
    return_classes()
    int(input("\n 1:Returns class grades "))



    print("Grade module has ended. End Time : " + time.ctime())


main()

#key takeaways
'''what to work on: making while, break, except a function. / do grading module for all classes, specific class + 
assignments, and assignments that are due'''