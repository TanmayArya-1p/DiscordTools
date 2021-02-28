# DiscordTools
A package to simulate user experience in Discord programatically using Selenium Web-Scraping(Chrome-Webdriver)#

## Documentation :

### Initialize the Discord Tools Class :

   u = DT(username,password)

After initialising a selenium chrome window will open.
Often,Discord prompts the user with a captcha(Hcpatcha) or will ask the user to confirm new login location.
If Such interruption is faced , DiscordTools will wait until the interruption is longer seen and prompts when faced with one in the terminal.
