import Constans as keys
from telegram.ext import *
#from cmcapi import price

print("Bot started...")

def start_command(update, context):
    update.message.reply_text('Type /help to find out all commands')

def help_command(update, context):
    update.message.reply_text("""⚙️ You can run the following commands:
/help - Shows the help message 
/price - Shows the price of $UncleDoge
/tokenomics- Shows Tokenomics of $UncleDoge""")

def tokenomics_command(update,context):
    update.message.reply_text("""The tokenomics of $UDOGE are:
Total Supply - 1 Quadrillion Initial Supply

Token Tax - (total) 11% Transaction Tax 

Liquidity - 10% of tax goes to liquidity

Holders - 1% Redistributed to Holders

Presale/Liquidity - Presale 50%, Liquidity 35%

Burn/Airdrop 2.68% Burn, 1% Airdrop""")

from cmcapi import price
def price_command(update, context):
    update.message.reply_text("1,000,000,000 $UDOGE ➡ ️" + price())






# def handle_message(update, context):
#     text = str(update.message.text).lower()
#     response = R.sample_responses(text)
#     print("response: " + response)
#     update.message.reply_text(response)

def error(update, context):
    print(f"update {update} cause error {context.error}")



def main():
    updater = Updater(keys.BOT_API_KEY, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start_command))
    dp.add_handler(CommandHandler("help", help_command))
    dp.add_handler(CommandHandler("tokenomics", tokenomics_command))
    dp.add_handler(CommandHandler("price", price_command))

    #dp.add_handler(MessageHandler(Filters.text, handle_message))

    dp.add_error_handler(error)

    updater.start_polling()
    updater.idle()




main()
