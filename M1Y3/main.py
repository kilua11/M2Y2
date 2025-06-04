import telebot
from logic import gen_pass, kill
import random, os
import requests
free = 6
decompos = ["Туалетная бумага", "Огрызок яблока", "Банановая кожура", "Мясопродукты", "Кожура апельсина", "Фотографии", "КостИ", "Жевательная резинка", "Одежда", "Резиновые покрышки", "Пластиковые бутылки", "Губки", "Подгузники", "Прокладки", "Леска", "Стекло"]
non_decomposable = ["Свинец", "Ртуть", "Мышьяк", "Пластмассы", "Синтетика", "Золото"]
bot = telebot.TeleBot("")
it_meme = os.listdir("./memes/sec_meme")
anim_meme = os.listdir("./memes/animal_meme")
def get_duck_image_url():    
        url = 'https://random-d.uk/api/random'
        res = requests.get(url)
        data = res.json()
        return data['url']
@bot.message_handler(commands=['duck'])
def duck(message):
        '''По команде duck вызывает функцию get_duck_image_url и отправляет URL изображения утки'''
        image_url = get_duck_image_url()
        bot.reply_to(message, image_url)



@bot.message_handler(commands=['старт', "start"])   
def send_welcome(message):
    bot.reply_to(message, "Привет! Я твой Telegram бот.Если что используй /help")
@bot.message_handler(commands=['привет', "hello"])
def send_hello(message):
    user_id = message.from_user.first_name
    bot.reply_to(message, "Привет!", str(user_id))

@bot.message_handler(commands=['пока', "buy"])
def send_bye(message):
    bot.reply_to(message, "Пока!")

@bot.message_handler(commands=['pass'])
def send_bye(message):
    words = message.text.split()
    if len(words) < 2:
        bot.reply_to(message, (10))
    else: 
        lenght = int(words[1])
        bot.reply_to(message, gen_pass(lenght))
@bot.message_handler(commands=['shot'])
def send_bye(message):
    life = kill(free)
    free -= 1
    if life:
        if free == 1:
            free = 6
            bot.reply_to("Вы одержали победу")
        else:
            bot.reply_to("Выстрел не произошёл")
    else:
        free = 6 
        bot.reply_to("В")
@bot.message_handler(commands=['spam'])
def send_heh(message):
    words = message.text.split()
    if len(words) < 3:
        bot.reply_to(message, "Нехватает данных")
    else:
        text = "" 
        w = words[1:len(words) - 1]
        for i in w:
            text += i + " "
        for i in range(int (words [-1])):
            bot.reply_to(message, text)

@bot.message_handler(commands=['помощь', "help"])
def send_welcome(message):
    bot.reply_to(message, "Вот список команд которые ты можешь использовать --\n  /quest - делаю тебе квест \n /hello,/привет - поздороваться \n /bye, /пока - попрощаться \n newpassword (кол-во символов в пароле) - сгенерировать пароль \n /rulet - поиграть в русскую рулетку \n /heh (кол-во 'heh') - похехекать")


@bot.message_handler(commands=["memes"])
def memes(message):
    words = message.text.split()
    if len(words) < 2:
        bot.reply_to(message, "Укажите категорию мема")
    else:   
        cat = words[1].lower()
        if cat == "sec_meme":
            with open(f"./memes/sec_meme/{random.choice(it_meme)}","rb") as f:
                bot.send_photo(message.chat.id, f)
@bot.message_handler(commands=["animals"])
def memes(message):
    words = message.text.split()
    if len(words) < 2:
        bot.reply_to(message, "Укажите категорию мема")
    else:   
        cat = words[1].lower()
        if cat == "animal_meme":
            with open(f"./memes/animal_meme/{random.choice(anim_meme)}","rb") as f:
                bot.send_photo(message.chat.id, f)
@bot.message_handler(commands=["decompose"])   
def send_welcome(message):
    words = message.text.split()
    if len(words) < 2:
        bot.reply_to(message, "Укажите материал")
    else:   
        material = words[1].lower()
        if material in  decompos:
            bot.reply_to(message, "Этот предмет разлагается")
        if material in non_decomposable:
            bot.reply_to(message, "Этот предмет не разлагается")
@bot.message_handler(commands=["ekosovet"])   
def send_welcome(message):
    bot.reply_to(message, "Привет ты выбрал экосоветы выбери категорию экологических советов - 1.Дома 2.На улице")




@bot.message_handler(commands=['heh'])
def send_heh(message):
    count_heh = int(message.text.split()[1]) if len(message.text.split()) > 1 else 5
    bot.reply_to(message, "he" * count_heh)
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    sovet = message.text
    if sovet == "1":
        bot.reply_to(message, "1.Сократить потребление воды 2.Оптимизировать энергопотребление 3.Использовать естественное освещение 4.Сократить количество мяса и увеличить долю овощей 5.Использовать замороженные овощи")
    elif sovet == "2":
        bot.reply_to(message, "1.Собирать отходы отдельно 2.Сдавать отходы на переработку 3.Заменять одноразовые предметы 4.Использовать посуду из дома 5.Использовать многоразовую бутылку для воды")
bot.polling()
