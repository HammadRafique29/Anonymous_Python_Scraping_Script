
# Web Scraping with Selenium WebDriver

This repository contains a web scraping tool that utilizes **Selenium WebDriver** with the latest version of FireFox to scrape data from the web. The tool supports proxy rotating and manual user agents for additional privacy and flexibility.
This is the initial build of script using proxy rotating, user agents and other techniques to stay anonymous.
I am know this is the not professional script but will be useful for moderate scraping.
## Requirements

The following dependencies are required to run the web scraping tool:

- Python 3.x
- Selenium WebDriver
- geckodriver (for FireFox)
- Requests (for sending HTTP requests)
- Random (for parsing HTML)
- Time (for rotating proxies)
- Beautiful Soup (for parsing HTML)

You can install the dependencies using pip:

####pip install selenium requests beautifulsoup4

## Usage

To use the web scraping tool, just go the main file do whatever you want, but make sure you use the `Anonymous` class for making the object of WebDriver. `Anonymous` class will do work on his behalf. The `main.py` file should contain the following information:

- `base_url`: the base URL of the website you want to scrape
- `search_query`: the search query to be used to fetch data

The `Anonymous.py` file should contain the following information:
- `proxies`: a list of proxy servers to be used for scraping.
- `user_agents`: a list of user agents to be used for scraping.
- `setup_webdriver`: create a web driver with desired capabilities and options.

All the data like proxies and user agents stored in text files (`Data Folder`), you can edit it if you want, before running actual work program will ask to download again the proxies to increase efficiency and speed.

- `proxies`: up http proxies downloaded from `geonode.com`


To start the web scraping tool, run the following file:

###python main.py

You can add additional command line arguments as needed.

## Contact

If you have any questions or issues, please contact the author at [hammadrafique029@gmail.com](mailto:hammadrafique029@gmail.com) or [codingmagician0@gmail.com](mailto:codingmagician0@gmail.com).