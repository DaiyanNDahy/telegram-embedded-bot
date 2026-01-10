import logging
import warnings
import pytz
from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackContext, Defaults
from config import BOT_TOKEN
from gpiozero import LED
import adafruit_dht
import board
led=LED(18)
DHT_SENSOR = adafruit_dht.DHT11(board.D19)

# Suppress the pytz deprecation warning
warnings.filterwarnings('ignore', category=DeprecationWarning, module='telegram')

# Set up basic logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# Function to start the bot
async def start(update: Update, context: CallbackContext):
    try:
        await update.message.reply_text(
            "Raspberry Pi-based Telegram bot is running!\n"
            "Type /led_on, /led_off, /temp, /humidity, /sensors"
        )
    except Exception as e:
        logger.error(f"Error in /start command: {e}")

# Command to turn LED on
async def cmd_led_on(update: Update, context: CallbackContext):
    try:
        led.on()
    except Exception as e:
        logger.error(f"Error in /led_on command: {e}")
        await update.message.reply_text("Failed to turn LED on")

# Command to turn LED off
async def cmd_led_off(update: Update, context: CallbackContext):
    try:
        led.off()
    except Exception as e:
        logger.error(f"Error in /led_off command: {e}")
        await update.message.reply_text("Failed to turn LED off")

# Command to get humidity
async def cmd_humidity(update: Update, context: CallbackContext):
    try:
        hum =DHT_SENSOR.humidity
        await update.message.reply_text(f"Humidity: {hum}%")
    except Exception as e:
        logger.error(f"Error in /humidity command: {e}")
        await update.message.reply_text("Error reading humidity")

# Command to get temperature
async def cmd_temp(update: Update, context: CallbackContext):
    try:
        temp=round(DHT_SENSOR.temperature,2)
        await update.message.reply_text(f"Temperature: {temp}°C")
    except Exception as e:
        logger.error(f"Error in /temp command: {e}")
        await update.message.reply_text("Error reading temperature")


# Main function
def main():
    try:
        # Create defaults with pytz UTC timezone
        defaults = Defaults(tzinfo=pytz.utc)
        
        # Create Application with defaults
        application = (
            Application.builder()
            .token(BOT_TOKEN)
            .defaults(defaults)
            .build()
        )
        
        # Add command handlers
        application.add_handler(CommandHandler("start", start))
        application.add_handler(CommandHandler("led_on", cmd_led_on))
        application.add_handler(CommandHandler("led_off", cmd_led_off))
        application.add_handler(CommandHandler("temp", cmd_temp))
        application.add_handler(CommandHandler("humidity", cmd_humidity))
        
        # Start polling
        logger.info("Bot starting...")
        application.run_polling()
    except Exception as e:
        logger.error(f"Error in main bot execution: {e}")

if __name__ == "__main__":
    main()
