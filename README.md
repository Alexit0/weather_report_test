<h1>Selenium Automation test wor the weather website launched via telegram bot.</h1>

Opens the website, searches for the location, logs today's weather, 
selects weekly option, logs weekly forecast.

## Requirements
 <li>Python 3.9.10



## Install
1. Create a bot and obtain a token from  @BotFather

>(You can find a step-by-step guide [here](https://core.telegram.org/bots/tutorial))

Save the token in .env file in the root folder as BOT_TOKEN variable.

2. Install dependencies from requirements.txt
    ````
    pip install -r requirements.txt
    ````
## Start
````
python bot/bot.py
````

## Usage
Find the bot, send '/start' to activate. Send '/report' to run the test.