import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

proxy_status = -1


class FreeProxies:
    def __init__(self):
        self.proxy = []

    def verify_proxies(self):
        with open("data/free_proxies.txt", "r") as file:
            count_proxies = len(file.readlines())
            if count_proxies > 0:
                print(f"\nWe have found {count_proxies} pre Proxies! Do you want to download it Again (Recommended) or Use the Old Proxies")
                opt = input("WANT TO DOWNLOAD? yes/no: ")
                if opt == "yes" or opt == "Yes" or opt == "YES":
                    self.get_proxy()
                    return self.proxy
                else:
                    print("CONTINUING WITH THE OLD PROXIES ....")
                    return self.read_proxies()
            elif count_proxies == 0:
                self.get_proxy()
                return self.proxy

    def get_proxy(self):
        print("Getting Proxies! Please Wait ....")
        try:
            driver = webdriver.Firefox()
            driver.get("https://geonode.com/free-proxy-list")
            time.sleep(5)

            wait = WebDriverWait(driver, 20)
            element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#headlessui-popover-button-\:r6\:")))
            element.click()

            time.sleep(1)
            driver.find_element(By.CSS_SELECTOR, "#filter-0").click()
            time.sleep(4)

            body_div_of_proxies = driver.find_elements(By.TAG_NAME, "tbody")

            for proxy in body_div_of_proxies:
                rows = proxy.find_elements(By.TAG_NAME, "tr")
                for col in rows:
                    columns = col.find_elements(By.TAG_NAME, "td")
                    proxy_plus_port = columns[0].text + ":" + columns[1].text
                    self.proxy.append(proxy_plus_port)

            self.save_proxies()
            print(f"Number of proxies fetched: {len(self.proxy)}")
            driver.close()
        except Exception as e:
            print(e)
            exit()

    def save_proxies(self):
        with open("data/free_proxies.txt", "w") as file:
            for x in self.proxy:
                file.write(x + "\n")
        print("Proxies Has Been Saved!")
        file.close()

    def read_proxies(self):
        with open("data/free_proxies.txt", "r") as file:
            self.proxy = file.read().split("\n")
        file.close()
        return self.proxy

    @staticmethod
    def modify_proxies(match_val):
        with open("data/free_proxies.txt", "r") as input_file:
            lines = input_file.read().split("\n")

        # Loop through the lines and modify each line based on a condition
        for i in range(len(lines)):
            if match_val == lines[i]:
                print("Get match in modifying")
                lines[i] = lines[i].replace("http://", "")

        # Open the output file for writing
        with open("data/free_proxies.txt", "w") as output_file:
            for x in lines:
                output_file.write(x.replace("http://", "") + "\n")
            print("Proxies has been modified")

    @staticmethod
    def read_user_agents():
        with open("data/user_agents.txt", "r") as file:
            user_agent = file.read().split("\n")
            file.close()
            return user_agent
