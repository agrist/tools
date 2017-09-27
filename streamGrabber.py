
#first needs phantomJS - http://phantomjs.org/download.html
#set the executable to env PATH
#pip install selenium
from selenium import webdriver
br = webdriver.PhantomJS()
br.get('https://worldcam.live/img/webcams/540/wolbrom3.jpg')
br.save_screenshot('screenshot.png')
br.quit
