import os
from dotenv import load_dotenv

import logging
from telegram import ForceReply, Update
from telegram.ext import Application, CommandHandler, ContextTypes

import pytest

load_dotenv()
bot_token = os.getenv('BOT_TOKEN')


def run_test():
    return pytest.main(["-x", "./test_e2e_weather.py"])


# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /start is issued."""
    user = update.effective_user
    await update.message.reply_html(
        rf"Hi {user.mention_html()}! "
        rf"To run the test send me '/report'",
        reply_markup=ForceReply(selective=True),
    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /help is issued."""
    await update.message.reply_text("To run the test send me '/report'")


async def report_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Run automation test, send logs in messages when /report is issued"""
    await update.message.reply_text('Running test...')
    run_test()
    with open('./logfile.log') as logfile:
        for line in logfile:
            await update.message.reply_text(line)


def main() -> None:
    """Start the bot."""
    # Create application and pass to it bot's token.
    application = Application.builder().token(bot_token).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("report", report_command))

    # Run the bot until the user presses Ctrl-C
    application.run_polling()


if __name__ == "__main__":
    main()








