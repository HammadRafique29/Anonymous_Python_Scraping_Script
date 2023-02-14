from proxies import *
import random


class Anonymous:
    def __init__(self):
        self.proxies = []
        self.user_agents = []
        self.temp_user_choice = False
        self.temp_val = False

    def setup_proxies(self):
        if len(self.proxies) == 0 and self.temp_user_choice is False:
            self.proxies = FreeProxies().verify_proxies()
            self.temp_user_choice = True
        elif len(self.proxies) == 0 and self.temp_user_choice is True:
            self.proxies = FreeProxies().read_proxies()

    def setup_desired_capabilities(self):
        try:
            proxy = random.choice(self.proxies)
            print("\n" + proxy)
            desired_capabilities = webdriver.DesiredCapabilities.FIREFOX
            desired_capabilities['proxy'] = {
                "proxyType": "MANUAL",
                "httpProxy": proxy,
            }
            return desired_capabilities
        except Exception as e:
            print("\n\tGOT ERROR IN DEFINING DESIRED CAPABILITIES! ERROR BELOW:\n\t" + str(e))

    def setup_agents(self):
        if len(self.user_agents) == 0:
            self.user_agents = FreeProxies().read_user_agents()

        try:
            selected_agent = random.choice(self.user_agents)
            print(selected_agent)
            options = webdriver.FirefoxOptions()
            options.add_argument(f"--user-agent={selected_agent}")
            return options
        except Exception as e:
            print("\n\tGOT ERROR IN DEFINING USER AGENTS! ERROR BELOW:\n\t" + str(e))

    def setup_webDriver(self):
        try:
            self.setup_proxies()
            driver = webdriver.Firefox(desired_capabilities=self.setup_desired_capabilities(),
                                       options=self.setup_agents())
            return driver
        except Exception as e:
            print("\n\tGOT ERROR IN DEFINING WEB DRIVER! ERROR BELOW:\n\t" + str(e))
