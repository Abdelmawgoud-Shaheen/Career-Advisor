import telebot
import requests

# توكن البوت من @BotFather
TELEGRAM_TOKEN = "7638366339:AAEa_0w1gprV0AqOPrAgjqjOD1UiFFG9ol0"
WIT_TOKEN = "NAMJUVIZJIYU3EM44XWOUYJ2VR7QUD3M"

bot = telebot.TeleBot(TELEGRAM_TOKEN)


@bot.message_handler(func=lambda message: True)
def handle_message(message):
    user_input = message.text

    # إرسال رسالة إلى Wit.ai
    wit_response = requests.get(
        f"https://api.wit.ai/message?v=20250724&q={user_input}",
        headers={"Authorization": WIT_TOKEN})

    result = wit_response.json()

    # تحليل مبسط للرد
    intent = result.get("intents")
    traits = result.get("traits")

    reply = "تحليل رسالتك:\n"
    if intent:
        reply += f"- النية (Intent): {intent[0]['name']}\n"
    if traits:
        for trait in traits:
            reply += f"- سمة: {trait} → {traits[trait][0]['value']}\n"

    # إرسال الرد للمستخدم
    bot.send_message(message.chat.id, reply)


# تشغيل البوت
bot.polling()
