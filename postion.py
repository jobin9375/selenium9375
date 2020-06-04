from selenium.webdriver import Chrome
driver=Chrome("D:/chromedriver_win32/chromedriver.exe")
driver.get("https://www.facebook.com")
e=driver.find_element_by_name("firstname")
epos=e.location
f=driver.find_element_by_name("reg_email__")
fpos=f.location
g=driver.find_element_by_name("reg_passwd__")
gpos=g.location
if epos["x"]==fpos["x"] or epos["x"]==gpos["x"] :
    print("vertical")
else:
    print("not vertical")

