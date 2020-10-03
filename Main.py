from selenium import webdriver
import time

PATH = "C:/Program Files (x86)\chromedriver.exe"

driver = webdriver.Chrome(PATH)
'''def is_it_int(var):'''

def login(user, password):
    driver.get('https://huskyct.uconn.edu/') #goes to huskyCT
    driver.find_element_by_class_name("button-1").click() #gets rid of asking for cookies
    driver.find_element_by_id("cas-login").click()
    driver.find_element_by_id("username").send_keys(user)
    driver.find_element_by_id("password").send_keys(password)
    driver.find_element_by_id("button").click()


def prompt_login_info():
    username = input("What is your NetID?\n")
    password = input("What is your password?\n")

    return [username, password]


def return_classes():
    driver.maximize_window()
    driver.find_element_by_xpath("//*[@id=\"base_tools\"]/bb-base-navigation-button[4]/div/li/a/ng-switch/span").click()
    time.sleep(2)
    classes = []
    for j, i in enumerate(driver.find_elements_by_tag_name('h4')):
        classes.append(i.get_attribute("Title"))
        print ("Class " + str(j + 1) + ": " + i.get_attribute("Title"))
    return classes


'''def getting_grades():'''





def main():
    print("Grade module has begun. Start time : " + time.ctime())
    while True:
        try:
            y_or_n = int(input("Please respond with 1 (yes) or 2 (no) if you want the grading module\n"))
            y_or_n = int(y_or_n)
            break
        except ValueError:
            print("Was that an integer? Please try again...")


    if y_or_n == 1:  #need to make excpetion if user types a string
        username,password = prompt_login_info() if True else quit() and driver.close()
    login(username, password)
    return_classes()
    int(input("\n 1:Returns class grades "))



    print("Grade module has ended. End Time : " + time.ctime())


main()

#key takeaways
'''what to work on: making while, break, except a function. / do grading module for all classes, specific class + 
assignments, and assignments that are due'''