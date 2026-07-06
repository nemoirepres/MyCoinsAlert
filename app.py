import os
from threading import Thread
from flask import Flask
from bot import main

app = Flask('')

@app.route('/')
def home():
    return "Bot is running!"

def run_bot():
    # Запускаем основную функцию бота из файла bot.py
    main()

if __name__ == "__main__":
    # Запускаем бота в отдельном потоке
    t = Thread(target=run_bot)
    t.start()
    # Запускаем Flask-сервер, который слушает порт, назначенный Render
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
