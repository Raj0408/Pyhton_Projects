from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters

updater = Updater("1960710307:AAHelnXvvKPr7O3wQP4LhAtJj-izfztaGuk",
                  use_context=True)
# 1960710307:AAHelnXvvKPr7O3wQP4LhAtJj-izfztaGuk
# 5245463955:AAGgsNxLh2or3FF6vMJ4vGw-1mQ6EwcYBx4

def start(update: Update, context: CallbackContext):
    update.message.reply_text(
        """Welcome to MENTOR TELE BOT
To find Something new press /Ready.""")


def Ready(update: Update, context: CallbackContext):
    update.message.reply_text("""Available Commands :-
        /help - If want to reach us
        /pythonCourse - Python RoadMap
        /javaCourse - Java RoadMap
    """)


def help(update: Update, context: CallbackContext):
    update.message.reply_text("""Available Commands :-
/youtube - To get the youtube URL
/linkedin - To get the LinkedIn profile URL
/telegramUserName - To get telegramusername
/geeks - To get the GeeksforGeeks URL
/weather - To get the weather Report
/google - To get the Google URL""")


def pythonCourse(update: Update, context: CallbackContext):
    update.message.reply_text("""Available Commands :-
/UdemyPython - Udemy python Course 
/GeeksForgeeksPython - Geeks For Geeks python crash Course
/python - Documentation for Python Language
""")


def javaCourse(update: Update, context: CallbackContext):
    update.message.reply_text("""Available Commands :-
/UdemyJava - Udemy Java Course 
/GeeksForgeeksJava - Geeks For Geeks Java crash Course
/Java - Documentation for Java Language
	""")


def UdemyPython(update: Update, context: CallbackContext):
    update.message.reply_text(
        "UdemyPyton URL =>https://www.udemy.com/courses/search/?q=python+programming&src=sac&kw=python")


def UdemyJava(update: Update, context: CallbackContext):
    update.message.reply_text(
        "UdemyJava URL =>https://www.udemy.com/courses/search/?q=java+programming&src=sac&kw=java")


def GeeksForgeeksPython(update: Update, context: CallbackContext):
    update.message.reply_text(
        "GeeksForgeeksPython URL =>https://www.geeksforgeeks.org/python-programming-language/")


def GeeksForgeeksJava(update: Update, context: CallbackContext):
    update.message.reply_text(
        "GeeksForgeeksJava URL =>https://www.geeksforgeeks.org/java/")


def python(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Python URL =>https://www.python.org/")


def Java(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Python URL =>https://docs.oracle.com/en/java/")


def telegramUserName(update: Update, context: CallbackContext):
    update.message.reply_text(
        '''@BhavinKhunt
@RajKaneriya0408''')


def youtube_url(update: Update, context: CallbackContext):
    update.message.reply_text("Youtube Link =>\
	https://www.youtube.com/")


def linkedIn_url(update: Update, context: CallbackContext):
    update.message.reply_text(
            "LinkedIn URL => \
		https://www.linkedin.com/in/dwaipayan-bandyopadhyay-007a/")


def google(update: Update, context: CallbackContext):
    update.message.reply_text(
            "Google => \
		https://www.google.co.in/")


def geeks_url(update: Update, context: CallbackContext):
    update.message.reply_text(
        "GeeksforGeeks URL => https://www.geeksforgeeks.org/")


def weather_url(update: Update, context: CallbackContext):
    update.message.reply_text(
        "WEATHER URL => https://weather.com/en-IN/weather/today/l/22.59,72.82?par=google")


def unknown(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Sorry '%s' is not a valid command" % update.message.text)


def unknown_text(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Sorry I can't recognize you , you said '%s'" % update.message.text)


updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('Ready', Ready))
updater.dispatcher.add_handler(CommandHandler('youtube', youtube_url))
updater.dispatcher.add_handler(CommandHandler('help', help))
updater.dispatcher.add_handler(CommandHandler('pythonCourse', pythonCourse))
updater.dispatcher.add_handler(CommandHandler('javaCourse', javaCourse))
updater.dispatcher.add_handler(CommandHandler('linkedin', linkedIn_url))
updater.dispatcher.add_handler(CommandHandler(
    'GeeksForgeeksPython', GeeksForgeeksPython))
updater.dispatcher.add_handler(CommandHandler(
    'GeeksForgeeksJava', GeeksForgeeksJava))
updater.dispatcher.add_handler(CommandHandler('UdemyPython', UdemyPython))
updater.dispatcher.add_handler(CommandHandler('UdemyJava', UdemyJava))
updater.dispatcher.add_handler(CommandHandler('Python', python))
updater.dispatcher.add_handler(CommandHandler('Java', Java))

updater.dispatcher.add_handler(CommandHandler('telegramUserName', telegramUserName))
updater.dispatcher.add_handler(CommandHandler('geeks', geeks_url))
updater.dispatcher.add_handler(CommandHandler('weather', weather_url))
updater.dispatcher.add_handler(CommandHandler('google', google))
updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown))
updater.dispatcher.add_handler(MessageHandler(
    Filters.command, unknown))  # Filters out unknown commands

# Filters out unknown messages.
updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown_text))

updater.start_polling()