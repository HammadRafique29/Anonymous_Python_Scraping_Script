import time

from anonymous_techniques import *

obj = Anonymous()
url = "https://www.goole.com"
driver = obj.setup_webDriver()
driver.get(url)
time.sleep(5)
driver.close()