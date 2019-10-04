from telegram.ext import (Updater, CommandHandler, ConversationHandler)
from telegram.ext import MessageHandler,Filters,CallbackQueryHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup,ReplyKeyboardMarkup
from SimpleQIWI import *
import webbrowser

QIWItoken = 'c68bae64ca03295a750dd6637bbc0609'
QIWIphone = '+79172933327'
api = QApi(token=QIWItoken, phone=QIWIphone)
TOKEN='872672242:AAEV8XTI6Ijjk1xdyaVmTzZVSKnUA2WQqPg'
Link1 = 'https://vk.com/id399330400'
Link2 = 'https://python-scripts.com/loops-for-while'
Link3 = 'https://www.youtube.com/watch?v=uAzEtle04lw'
Link4 = 'https://www.youtube.com'
Link5 = 'https://vk.com'
PASSWORD_FROM_ADMIN_PANEL = '512413579Zz'
b = False
is_cange_money = False
is_adm_panel = False
is_link = False
is_get_money = False

button_change_number =  'Сменить номер QIWI'
button_get_money  = 'Вывести деньги'
button_watch_money = 'Баланс'
button_tasks = 'Задания'
button_menu = 'Меню'
secret_admin_panel = 'AdminPanel'
button_link1 = 'Заданиe 1'
button_link2 = 'Заданиe 2'
button_link3 = 'Заданиe 3'
button_link4 = 'Заданиe 4'
button_link5 = 'Заданиe 5'


# создаём основное меню
reply_keyboard = [[button_change_number,button_get_money,button_watch_money],[button_tasks,button_menu]]
markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True, resize_keyboard=True)

def watch_money(bot, update):
    f = open('logs.txt', 'r')
    IsRegistred = False
    for line in f:
        if line.strip().split()[0] == str(update.message.chat_id):
            balance = 'Ваш баланс: ' + line.strip().split()[2] + ' рублей'
            IsRegistred = True
    if IsRegistred == False:
        bot.send_message(chat_id=update.message.chat_id, text="Зарегестрируйтесь с помощью команды /start для дальнейших операций")
    else:
        bot.send_message(chat_id=update.message.chat_id, text=balance)
        f.close()

def handle_change_Qiwi(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="Введите новый номер в форме 8(ххх)ххх-хх-хх")
    global is_cange_money
    is_cange_money = True

def handle_change_Qiwi2(bot, update):
    global is_cange_money
    mes = update.message.text
    is_cange_money = False
    newnum = '+7'
    for i in range(1, len(mes)):
        if mes[i] != ' ':
            newnum = newnum + mes[i]
    if len(newnum) != 12:
        bot.send_message(chat_id=update.message.chat_id, text="Вы неправильно ввели номер. Введите номер в форме 8(ххх)ххх-хх-хх")
    else:
        mes = newnum
        ff = open('logs.txt', 'r')
        n = ''
        for line in ff:
            if line.strip().split()[0] == str(update.message.chat_id):
                n = n + str(update.message.chat_id) + ' ' + mes + ' ' + line.strip().split()[2] + ' ' + line.strip().split()[3] + ' ' + line.strip().split()[4] + ' ' + line.strip().split()[5] + '\n'
            else:
                n = n + line
        ff.close()
        fi = open("logs.txt", 'w')
        fi.write(n)
        fi.close()
        bot.send_message(chat_id=update.message.chat_id, text="Ваш номер изменён на " + mes)

def get_money(bot,update):
    balance = 0
    global is_get_money
    ff = open('logs.txt','r')
    for line in ff:
        if line.strip().split()[0] == str(update.message.chat_id):
            balance = int(line.strip().split()[2])
    ff.close()
    if balance < 27:
        print('sagsgd')
        bot.send_message(chat_id=update.message.chat_id, text="Минимальный вывод 27 рублей.😫😫😫 Ваш балнс: " + str(balance))
    else:
        bot.send_message(chat_id=update.message.chat_id, text="Какую сумму вы хотите вывести?🤔🤔🤔 Ваш балнс: " + str(balance))
        print('gsgsdgfsd')
        is_get_money = True

def get_money2(bot,update):
    global is_get_money
    is_get_money = False
    mes = update.message.text
    balance = 0
    numb = ''
    ff = open('logs.txt', 'r')
    for line in ff:
        if line.strip().split()[0] == str(update.message.chat_id):
            numb = line.strip().split()[1]
            balance = int(line.strip().split()[2])
    balance1 = 0
    if mes.isdigit():
        balance1 = int(mes)
        if balance1 <= balance:
            api.pay(account=numb, amount=balance1, comment='От MoneyBot')
            ff = open('logs.txt', 'r')
            n = ''
            for line in ff:
                if line.strip().split()[0] == str(update.message.chat_id):
                    n = n + str(update.message.chat_id) + ' ' + line.strip().split()[1] + ' ' + str(int(line.strip().split()[2]) - balance1) + ' ' + line.strip().split()[3] + ' ' + line.strip().split()[4] + ' ' + line.strip().split()[5] + '\n'
                else:
                    n = n + line
            ff.close()
            fi = open("logs.txt", 'w')
            fi.write(n)
            fi.close()
            bot.send_message(chat_id=update.message.chat_id, text="Перевод выполнен успешно🤝")
        else:
            bot.send_message(chat_id=update.message.chat_id, text="Вывод должен быть меньше чем баланс☹. Ваш баланс: " + str(balance))
    else:
        bot.send_message(chat_id=update.message.chat_id, text="Введите только число без пробелов и букв ☺☺☺")

def tasks(bot,update):
    # кнопки выбора типа сайта
    keyboard = [[InlineKeyboardButton("Задание 1", callback_data='Задание 1'),
                 InlineKeyboardButton("Задание 2", callback_data='Задание 2'),
                 InlineKeyboardButton("Задание 3", callback_data='Задание 3'),
                 InlineKeyboardButton("Задание 4", callback_data='Задание 4'),
                 InlineKeyboardButton("Задание 5", callback_data='Задание 5')]]

    # формирование кнопок
    reply_markup = InlineKeyboardMarkup(keyboard)

    # вывод сообщения и кнопок для выбора типа сайта
    update.message.reply_text('Вот ваши задания, доступные на данный момент. Для выполнения, перейдите по ссылке и зарегистрируйтесь!', reply_markup=reply_markup)

def back_to_menu(bot,update):
    bot.send_message(chat_id=update.message.chat_id, text="Вы в главном меню",reply_markup=markup)


def adminpanel(bot,update):
    global is_adm_panel
    is_adm_panel = True
    #bot.send_message(chat_id=update.message.chat_id, text="Введите пароль")

def adminpassword(bot,update):
    mes = update.message.text
    global is_adm_panel
    global is_link
    is_adm_panel = False
    if mes == PASSWORD_FROM_ADMIN_PANEL:
        bot.send_message(chat_id=update.message.chat_id,text="Введите пять ссылок через пробел👅👅👅")
        is_link = True


def addlinks(bot,update):
    mes = update.message.text
    global is_link
    global Link1
    global Link2
    global Link3
    global Link4
    global Link5
    for i in [0, 1, 2, 3, 4]:
        if i == 0:
            Link1 = mes.strip().split()[0]
        if i == 1:
            Link2 = mes.strip().split()[1]
        if i == 2:
            Link3 = mes.strip().split()[2]
        if i == 3:
            Link1 = mes.strip().split()[3]
        if i == 4:
            Link1 = mes.strip().split()[4]        
    is_link = False

def button(bot,update):
    query = update.callback_query
    linkID = query.data

    link = ''
    if linkID == 'Задание 1':
        link = Link1
    if linkID == 'Задание 2':
        link = Link2
    if linkID == 'Задание 3':
        link = Link3
    if linkID == 'Задание 4':
        link = Link4
    if linkID == 'Задание 5':
        link = Link5        
    ff = open('logs.txt', 'r')
    n = ''
    for line in ff:
        if line.strip().split()[0] == str(query.message.chat_id):
            if line.strip().split()[3] == link or line.strip().split()[4] == link or line.strip().split()[5] == link:
                bot.send_message(chat_id=query.message.chat_id, text='Вы уже выполняли это задание☹')
                n = n + line
            else:
                bot.send_message(chat_id=query.message.chat_id, text=link)
                if line.strip().split()[3] != Link1 and line.strip().split()[3] != Link2 and line.strip().split()[3] != Link3:
                    n = n + str(query.message.chat_id) + ' ' + line.strip().split()[1] + ' ' + str(int(line.strip().split()[2]) + 1) + ' ' + link + ' ' + line.strip().split()[4] + ' ' +line.strip().split()[5] + '\n'
                elif line.strip().split()[4] != Link1 and line.strip().split()[4] != Link2 and line.strip().split()[4] != Link3:
                    n = n + str(query.message.chat_id) + ' ' + line.strip().split()[1] + ' ' + str(int(line.strip().split()[2]) + 1) + ' ' + line.strip().split()[3] + ' ' + link + ' ' + line.strip().split()[5] + '\n'
                elif line.strip().split()[5] != Link1 and line.strip().split()[5] != Link2 and line.strip().split()[5] != Link3:
                    n = n + str(query.message.chat_id) + ' ' + line.strip().split()[1] + ' ' + str(int(line.strip().split()[2]) + 1) + ' ' + line.strip().split()[3] + ' ' + line.strip().split()[4] + ' ' + link + '\n'
        else:
            n = n + line
    ff.close()
    fi = open("logs.txt", 'w')
    fi.write(n)
    fi.close()




button_func = {secret_admin_panel:adminpanel, button_change_number:handle_change_Qiwi, button_watch_money: watch_money, button_get_money: get_money, button_tasks:tasks,button_menu:back_to_menu};

# метод главного меню
def main_menu(bot, update):
    # получаем введёный текст пользователем в чат
    # по факту это текст на кнопки главного меню
    button_text = update.message.text
    print(button_text)
    global b
    global is_cange_money
    if b:
        handle_number_of_card(bot,update)
    elif is_cange_money:
        handle_change_Qiwi2(bot,update)
    elif is_adm_panel:
        adminpassword(bot,update)
    elif is_link:
        addlinks(bot,update)
    elif is_get_money:
        get_money2(bot,update)
    # если в нашем списке функций есть нужная функция, иначе возвращаем ошибку
    elif button_text in button_func:
        return button_func[button_text](bot, update)
    else:
        bot.send_message(chat_id=update.message.chat_id, text="Прости, я понимаю только команды😳")

updater = Updater(TOKEN)

def handle_number_of_card(bot, update):
    global b
    if b:
        b = False
        mes = update.message.text
        newnum = '+7'
        for i in range(1, len(mes)):
            if mes[i] != ' ':
                newnum = newnum + mes[i]
        if len(newnum) != 12:
            bot.send_message(chat_id=update.message.chat_id, text="Вы неправильно ввели номер! Пример: 8(ххх)ххх-хх-хх")
        else:
            mes = newnum
            #print(update.message.chat_id)
            fi = open("logs.txt", 'a')
            wr = str(str(update.message.chat_id) + " " + str(mes) + " 0" + " null" + " null"+" null"+"\n")
            fi.write(wr)
            fi.close();
            bot.send_message(chat_id=update.message.chat_id, text="Поздравляю, вы зарегестрировались!🤘🤘🤘")

def start(bot, update):
    f = open('logs.txt', 'r')
    IsRegistred = False
    for line in f:
        if line.strip().split()[0] == str(update.message.chat_id):
            IsRegistred = True
            bot.send_message(chat_id=update.message.chat_id, text="Вы уже зарегестрированы! Номер вашего QIWI: " + line.strip().split()[1],reply_markup=markup)
    f.close()
    if IsRegistred == False:
        bot.send_message(chat_id=update.message.chat_id, text="""Добро пожаловать!👋
Никогда не хватало денег на телефоне, на чашечку кофе или такси?👀
Напиши боту и забудь о недостатке карманных денег.
Ведь ты можешь всегда получить их за пару действий!🤝""",reply_markup=markup)
        bot.send_message(chat_id=update.message.chat_id,
                          text="""Введи номер своего QIWI кошелька(пример: 8(ххх)ххх-хх-хх), чтобы мы могли переводить тебе деньги🤑""")
        global b
        b = True

dispatcher = updater.dispatcher
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

dispatcher.add_handler(CallbackQueryHandler(button))

Text_handle = MessageHandler(Filters.text, main_menu)
dispatcher.add_handler(Text_handle)

updater.start_polling()

updater.idle()