<h1>Selenium Automation test wor the weather website launched via telegram bot.</h1>

***
Opens the website, searches for the location, logs today's weather, 
selects weekly option, logs weekly forecast.

***

## Built with
[![Python][Python-badge]][Python-url] <br>
[![python-telegram-bot][PTB-badge]][PTB-url] <br>
[![pytest][pytest-badge]][pytest-url] <br>


## Install
1. Create a bot and obtain a token from  @BotFather. *(You can find a step-by-step guide [here](https://core.telegram.org/bots/tutorial))*

    Save the token in `.env` file in the root folder as `BOT_TOKEN` variable.


2. Install dependencies from requirements.txt
    ````
    pip install -r requirements.txt
    ````
## Start
````
python bot/bot.py
````

## Usage

Find the bot, send `/start` to activate. Send `/report` to run the test.



Change location in `test_data/HomePageData.py`

[Python-badge]: https://img.shields.io/badge/Python-3.9.10-3776AB?style=for-the-badge&logo=python&logoColor=white
[Python-url]: https://www.python.org/downloads/release/python-3910/

[PTB-badge]: https://img.shields.io/badge/python--telegram--bot-20.0-0088CC?style=for-the-badge&logo=telegram&logoColor=white
[PTB-url]: https://pypi.org/project/python-telegram-bot/20.0/

[pytest-badge]: https://img.shields.io/badge/pytest-7.3.0-0A9EDC?style=for-the-badge&logo=python&logoColor=white
[pytest-url]: https://pypi.org/project/pytest/7.3.0/
