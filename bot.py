import telebot
from telebot import types
import time

# Токен бота (ключ для доступа и программирования бота)
TOKEN = '6775598496:AAGzBUo7k3Z6jNIFp6cgl4X1lIE_4hmsCDw' 


seller = 540425921
#seller = 718959170
bot = telebot.TeleBot(TOKEN)

# Обработчик команды /stop
@bot.message_handler(commands=['stop'])
def handle_stop(message):
    # Ваш код для завершения текущего диалога или возвращения в главное меню
    bot.send_message(message.chat.id, "Вы завершили ввод")


# Старт бота
@bot.message_handler(commands = ['start'])
def handle_start(message):
    bot.send_message(message.chat.id,"""Добро пожаловать в наш магазин холстов! 🎨

Чтобы начать, используйте команды:
/product - для ознакомления с нашим ассортиментом 🎨
/about - побробная информация о боте ℹ️
/cost - для расчета стоимости холста 🖼️
/order - оформление заказа 📦
/contacts - связь с продавцом 📩📞

Если у вас есть какие-либо вопросы или нужна помощь, просто наберите /help.

Спасибо, что выбрали наш магазин! 

""", parse_mode="Markdown")


# Подробная информация о боте 
@bot.message_handler(commands = ['about'])
def handle_product(message):
    bot.send_message(message.chat.id, """Занимаемся изготовлением грунтованных холстов,подрамников на заказ)Выполним любые ваши пожелания!
Сформировать заказ поможет бот ХолстБери🎨🖌 Грунтованные холсты имеют уже подготовленную для работы поверхность – на производстве на них сразу же наносится проклейка и грунт. Грунтованные холсты в рулоне продаются в больших размерах, для работы на таком холсте нужно предварительно отрезать нужный формат и натянуть его на глухой подрамник.

Очень удобны грунтованные холсты мелкого зерна(плотное переплетение) на подрамнике и на картоне - они не требуют никакой дополнительной подготовки к работе.
Приятного творчества :)""")



# Помощь в пользовании 
@bot.message_handler(commands = ['help'])
def handle_product(message):
    bot.send_message(message.chat.id, """Добро пожаловать в раздел справки нашего бота!

Наш Telegram-бот предоставляет следующие команды:

/start - начало работы с ботом 🏁
/stop - завершить ввод ⛔️
/about - подробная информация о нашем боте ℹ️
/product - для просмотра нашего ассортимента холстов 🎨
/cost - чтобы узнать стоимость выбранного холста 🖼️
/order - для оформления заказа и передачи его продавцу 📦
/contacts - для связи с нашей поддержкой и получения контактной информации продавца 📩📞

Если у вас есть вопросы по разделу /cost (расчет стоимости) то перейиде по команде /cost_info ℹ️
Если у вас есть вопросы по разделу /product (описание продукции) то перейдите по команде /product_info ℹ️
Если у вас есть вопросы по разделу /order (оформление заказа) то перейдите по команде /order_info ℹ️                    

Если у вас остались вопросы или вам нужна дополнительная помощь, связывайтесь с нами через команду /contacts 📩📞 Мы готовы вам помочь!

Спасибо за выбор нашего бота. Мы ценим ваш интерес и готовы обеспечить вас лучшими продуктами и обслуживанием! 🎨🖼️
""")


# Более подробная информация о разделе cost
@bot.message_handler(commands = ['cost_info'])
def handle_cost_info(message):
    bot.send_message(message.chat.id, """Команда /cost позволяет вам рассчитать стоимость выбранного художественного холста. Для этого выполните следующие шаги:

1. Выберите интересующий вас холст из нашего ассортимента
2. Введите команду /cost, чтобы начать расчет стоимости. Бот попросит ввести необходимые параметры для рассчета.
3. Уточните характеристики холста, такие как ширина, длина, тип холста (при расчете доступен выбор) и количество холстов этого типа.
4. В ответ на ваши введенные данные, бот предоставит вам итоговую стоимость выбранного товара.

Если у вас есть дополнительные вопросы по этому разделу - связывайте с нами через команду /contacts 📩📞
Если вы готовы оформить заказ, вы можете воспользоваться командой /order 🖼️, чтобы перейти к процессу оформления заказа.
""")

# Более подробная информация о разделе product
@bot.message_handler(commands = ['product_info'])
def handle_product_info(message):
    bot.send_message(message.chat.id, """Раздел /product 🎨 предназначен для просмотра нашего разнообразного ассортимента художественных холстов. Этот раздел позволяет вам подробно ознакомиться с нашими товарными предложениями и выбрать холст, который соответствует вашим вкусам и потребностям. Вот, как вы можете использовать этот раздел:

1. Выполните команду /product, чтобы перейти в раздел с ассортиментом холстов.
2. После этого бот предоставит вам описание. Вы сможете узнать характеристики холста.
3. Если вы заинтересованы в заказе определенного холста, вы можете перейти к команде /cost 🖼️, чтобы рассчитать его стоимость, учитывая выбранные параметры, или перейти к оформлению заказа /order 📦.

Если у вас возникли какие-либо вопросы о товарах или вам нужна дополнительная информация, обращайтесь к команде /contacts 📩📞 для связи с продавцом.

Раздел /product разработан для удобства выбора и покупки холстов, предоставляя вам полную информацию о наших товарах. Мы надеемся, что вы найдете в нем искусство, которое вас вдохновит!
""")

# Более подробная информация о разделе order
@bot.message_handler(commands = ['order_info'])
def handle_order_info(message):
    bot.send_message(message.chat.id,"""Раздел /order 📦 предназначен для оформления заказа выбранных вами художественных холстов. Этот раздел поможет вам превратить ваш выбор в реальный заказ и передать его продавцу. Вот, как вы можете использовать этот раздел:

1. После того как вы выбрали холст и рассчитали его стоимость с помощью команды /cost, вы можете перейти к разделу /order 📦.
2. В этом разделе бот предоставит вам форму заказа, в которой вам потребуется ввести необходимые данные. Обычно это включает в себя ваши контактные данные (имя, номер телефона, адрес доставки) и другие детали заказа, такие как количество выбранных холстов и специфические инструкции.
3. Вы можете дополнительно добавить товар в корзину указав команду да когда бот вас спросит об этом
4. В чеке товара в разделе провукт (1 строка) сначала идет наименование товара, после его ширина, длина и количество указанного товара.
5. После заполнения формы заказа, вы можете отправить ее продавцу с помощью бота. Заказ будет передан продавцу для обработки.

Если у вас возникнут какие-либо дополнительные вопросы или вам потребуется консультация по заказу, вы можете использовать команду /contacts 📩📞, чтобы связаться с продавцом или получить поддержку. Продавец свяжется с вами для подтверждения заказа, уточнения деталей. Вы также можете использовать команду /contacts для обсуждения дополнительных вопросов или изменений к заказу.

Раздел /order 📦 разработан, чтобы сделать процесс покупки художественных холстов максимально удобным и эффективным. Мы ценим ваш выбор и готовы обеспечить вас качественными товаром и обслуживанием! 
""")

# Описание товара
@bot.message_handler(commands = ['product'])
def handle_product(message):
    bot.send_message(message.chat.id, """Холст льняной
Зернистость мелкая
Проклейка двойная
Клей менздровый
Грунт эмульсионный """)






# Используйте словарь для хранения данных каждого пользователя
user_data = {}

def get_user_data(chat_id):
    if chat_id not in user_data:
        user_data[chat_id] = {
            "order": [],
            "towar": [],
            "result": [],
            "i": 0
        }
    return user_data[chat_id]

@bot.message_handler(commands=['order'])
def handler_order(message):
    data = get_user_data(message.chat.id)
    data['i'] = 0
    data['order'].clear()
    data['result'].clear()
    data['towar'].clear()

    bot.send_message(message.chat.id, 'Оформление заказа')
    time.sleep(0.3)

    bot.send_message(message.chat.id, 'Введите имя:')
    bot.register_next_step_handler(message, get_surname)

def get_surname(message):
    data = get_user_data(message.chat.id)

    if message.text.lower() == "/stop":
        handle_stop(message)
        return

    surname = message.text
    data['order'].append(surname)

    bot.send_message(message.chat.id, 'Введите отчество:')
    bot.register_next_step_handler(message, get_name)

def get_name(message):
    data = get_user_data(message.chat.id)

    if message.text.lower() == "/stop":
        handle_stop(message)
        return

    name = message.text
    data['order'].append(name)

    bot.send_message(message.chat.id, 'Введите телефон:')
    bot.register_next_step_handler(message, get_phone)

def get_phone(message):
    data = get_user_data(message.chat.id)

    if message.text.lower() == "/stop":
        handle_stop(message)
        return

    phone = message.text
    data['order'].append(phone)

    bot.send_message(message.chat.id, 'Адрес доставки:')
    bot.register_next_step_handler(message, get_adres)

def get_adres(message):
    data = get_user_data(message.chat.id)

    if message.text.lower() == "/stop":
        handle_stop(message)
        return

    adres = message.text
    data['order'].append(adres)

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    button1 = types.KeyboardButton("На подрамнике")
    button2 = types.KeyboardButton("Без подрамника")
    markup.add(button1, button2)

    bot.send_message(message.chat.id, 'Выберите продукт в каталоге:', reply_markup=markup)
    bot.register_next_step_handler(message, get_product)

def get_product(message):
    data = get_user_data(message.chat.id)

    if message.text.lower() == "/stop":
        handle_stop(message)
        return

    product = message.text

    if product not in ['На подрамнике', 'Без подрамника']:
        bot.send_message(message.chat.id, "Пожалуйста, выберите один из предложенных вариантов:")
        bot.register_next_step_handler(message, get_product)
        return

    data['towar'].append(product)

    bot.send_message(message.chat.id, 'Введите ширину холста (в см):')
    bot.register_next_step_handler(message, width_get)

def width_get(message):
    data = get_user_data(message.chat.id)

    if message.text.lower() == "/stop":
        handle_stop(message)
        return

    width = message.text

    try:
        width = float(width)  
        data['towar'].append(width)
    except ValueError:
        bot.send_message(message.chat.id, "Пожалуйста, введите ширину холста (в см)")
        bot.register_next_step_handler(message, width_get)
        return

    bot.send_message(message.chat.id, "Введите длину холста (в см):")
    bot.register_next_step_handler(message, length_get)

def length_get(message):
    data = get_user_data(message.chat.id)

    if message.text.lower() == "/stop":
        handle_stop(message)
        return

    length = message.text

    try:
        length = float(length)  
        data['towar'].append(length)
    except ValueError:
        bot.send_message(message.chat.id, "Пожалуйста, введите длину холста (в см)")
        bot.register_next_step_handler(message, length_get)
        return

    bot.send_message(message.chat.id, 'Введите количество холстов:')
    bot.register_next_step_handler(message, count_get)

def count_get(message):
    data = get_user_data(message.chat.id)

    if message.text.lower() == "/stop":
        handle_stop(message)
        return

    count = message.text

    try:
        count = float(count)  
        data['towar'].append(count)
    except ValueError:
        bot.send_message(message.chat.id, "Пожалуйста, введите количество холстов")
        bot.register_next_step_handler(message, count_get)
        return

    if data['towar'][data['i']] == 'На подрамнике':
        answer = calculation_stretcher(float(data['towar'][data['i'] + 1]), float(data['towar'][data['i'] + 2]), float(data['towar'][data['i'] + 3]))
        data['result'].append(answer)
    elif data['towar'][data['i']] == 'Без подрамника':
        answer = calculation_nostretcher(float(data['towar'][data['i'] + 1]), float(data['towar'][data['i'] + 2]), float(data['towar'][data['i'] + 3]))
        data['result'].append(answer)

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    button1 = types.KeyboardButton("Да")
    button2 = types.KeyboardButton("Нет")
    markup.add(button1, button2)

    bot.send_message(message.chat.id, 'Добавить еще товары в корзину?', reply_markup=markup)
    bot.register_next_step_handler(message, get_add)

def get_add(message):
    data = get_user_data(message.chat.id)

    if message.text.lower() == "/stop":
        handle_stop(message)
        return

    add = message.text

    if add.lower() == 'нет':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        button1 = types.KeyboardButton("Наличные")
        button2 = types.KeyboardButton("По карте")
        markup.add(button1, button2)

        bot.send_message(message.chat.id, 'Выберите способ оплаты:', reply_markup=markup)
        bot.register_next_step_handler(message, get_payment)
    elif add.lower() == 'да':
        data['i'] += 4
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        button1 = types.KeyboardButton("На подрамнике")
        button2 = types.KeyboardButton("Без подрамника")
        markup.add(button1, button2)

        bot.send_message(message.chat.id, 'Выберите продукт в каталоге:', reply_markup=markup)
        bot.register_next_step_handler(message, get_product)

def get_payment(message):
    data = get_user_data(message.chat.id)

    if message.text.lower() == "/stop":
        handle_stop(message)
        return

    payment = message.text

    if payment not in ['Наличные', 'По карте']:
        bot.send_message(message.chat.id, "Пожалуйста, выберите один из предложенных вариантов:")
        bot.register_next_step_handler(message, get_payment)
        return

    data['order'].append(payment)

    bot.send_message(message.chat.id, 'Ваш заказ:')
    
    bot.send_message(message.chat.id, f"""*Продукт* -- {data['towar']}
*Имя Отчество* -- {data['order'][0].capitalize()} {data['order'][1].capitalize()}
*Телефон* -- {data['order'][2]}
*Адрес доставки* -- {data['order'][3].capitalize()}
*Способ оплаты* -- {data['order'][4]}

*Стоимость заказа* 
---------------------------
{round(sum(data['result']), 2)}
""", parse_mode="Markdown")

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    button1 = types.KeyboardButton("Да")
    button2 = types.KeyboardButton("Нет")
    markup.add(button1, button2)

    bot.send_message(message.chat.id, """
Проверьте введенные данные! 🚨
В случае неправильно указанных данных продавец не сможет связаться с вами
Если какие-то данные введены неверно, нажмите /stop и сделайте заказ заново.
                     
Подтвердить заказ?""", reply_markup=markup)
    bot.register_next_step_handler(message, get_decoration)

# Отправка продавцу
def get_decoration(message):
    data = get_user_data(message.chat.id)

    if message.text.lower() == "/stop":
        handle_stop(message)
        return

    decoration = message.text.lower()

    if decoration == 'да':
        
        
        bot.send_message(seller, "✅ Поступил новый заказ:\n\n" + f"""*Продукт* -- {data['towar']}
*Имя Отчество* -- {data['order'][0].capitalize()} {data['order'][1].capitalize()}
*Телефон* -- {data['order'][2]}
*Адрес доставки* -- {data['order'][3].capitalize()}
*Способ оплаты* -- {data['order'][4]}

*Стоимость заказа* 
---------------------------
{round(sum(data['result']), 2)}
""", parse_mode="Markdown")

            
        


        # Отправка сообщению об отправке товара пользователю 
        bot.send_message(message.chat.id, """Заказ отправлен ✅ ✅ ✅
Продавец свяжется с вами в ближайшее время!
Спасибо за заказ! 
Ждем вас снова 🎨""")
        


    elif decoration == 'нет':
        bot.send_message(message.chat.id,"""Выберите дальшейную команду из меню:
/start - начало работы с ботом
/help - помощь в работе с ботом 
/abou - подробное описание бота
/product - для ознакомления с нашим ассортиментом
/cost - для расчета стоимости холста
/order - оформление заказа
/contacts - связь с продавцом""")





user_orders = {}
# Расчитать стоимость
@bot.message_handler(commands=['cost'])
def handler_cost(message):
    user_id = message.chat.id
    user_orders[user_id] = {'cost': [], 'step': 0}
    bot.send_message(user_id, 'Здесь будет происходить расчет стоимости')
    time.sleep(0.3)

    # Задаем варианты ответа в виде кнопок
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    button1 = types.KeyboardButton("На подрамнике")
    button2 = types.KeyboardButton("Без подрамника")
    markup.add(button1, button2)

    bot.send_message(user_id, 'Выберите продукт в каталоге:', reply_markup=markup)

# На подрамнике
@bot.message_handler(func=lambda message: message.text == "На подрамнике")
def get_stretcher(message):
    user_id = message.chat.id
    user_orders[user_id]['cost'].clear()  # Clear previous values
    user_orders[user_id]['cost'].append(message.text)
    bot.send_message(user_id, 'Вы выбрали расчет стоимости на подрамнике')
    time.sleep(0.3)

    bot.send_message(user_id, 'Введите ширину холста (в см):')
    user_orders[user_id]['step'] = 1

# Без подрамника
@bot.message_handler(func=lambda message: message.text == "Без подрамника")
def get_nostretcher(message):
    user_id = message.chat.id
    user_orders[user_id]['cost'].clear()  # Clear previous values
    user_orders[user_id]['cost'].append(message.text)
    bot.send_message(user_id, 'Вы выбрали расчет стоимости без подрамника')
    time.sleep(0.3)

    bot.send_message(user_id, 'Введите ширину холста (в см):')
    user_orders[user_id]['step'] = 1

# Получение от пользователя ширины 
@bot.message_handler(func=lambda message: user_orders.get(message.chat.id, {}).get('step') == 1)
def get_width(message):
    user_id = message.chat.id
    width = message.text

    try:
        # Попытка преобразовать введенный текст в число
        width = float(width)  
        user_orders[user_id]['cost'].append(width)  # Добавляем число в список
        user_orders[user_id]['step'] = 2
        bot.send_message(user_id, "Введите длину холста (в см):")
    except ValueError:
        # Если не удалось преобразовать в число, сообщаем об ошибке
        bot.send_message(user_id, "Пожалуйста, введите ширину холста (в см)")

# Получение от пользователя длины
@bot.message_handler(func=lambda message: user_orders.get(message.chat.id, {}).get('step') == 2)
def get_length(message):
    user_id = message.chat.id
    length = message.text

    try:
        # Попытка преобразовать введенный текст в число
        length = float(length)  
        user_orders[user_id]['cost'].append(length)  # Добавляем число в список
        user_orders[user_id]['step'] = 3
        bot.send_message(user_id, "Введите количество холстов:")
    except ValueError:
        # Если не удалось преобразовать в число, сообщаем об ошибке
        bot.send_message(user_id, "Пожалуйста, введите длину холста (в см)")

# Получение от пользователя количества холстов
@bot.message_handler(func=lambda message: user_orders.get(message.chat.id, {}).get('step') == 3)
def get_count(message):
    user_id = message.chat.id
    count = message.text

    try:
        # Попытка преобразовать введенный текст в число
        count = float(count)  
        user_orders[user_id]['cost'].append(count)  # Добавляем число в список
        user_orders[user_id]['step'] = 0

        if user_orders[user_id]['cost'][0] == 'На подрамнике':
            answer = calculation_stretcher(user_orders[user_id]['cost'][1], user_orders[user_id]['cost'][2], user_orders[user_id]['cost'][3])
            bot.send_message(user_id, f"""Стоимость на подрамнике составит: {round(answer, 2)} руб.
Количество холстов - {user_orders[user_id]['cost'][3]}""")
        elif user_orders[user_id]['cost'][0] == 'Без подрамника':
            answer = calculation_nostretcher(user_orders[user_id]['cost'][1], user_orders[user_id]['cost'][2], user_orders[user_id]['cost'][3])
            bot.send_message(user_id, f"""Стоимость без подрамника составит: {round(answer, 2)} руб.
Количество холстов - {user_orders[user_id]['cost'][3]}""")
    except ValueError:
        # Если не удалось преобразовать в число, сообщаем об ошибке
        bot.send_message(user_id, "Пожалуйста, введите количество холстов")

# Расчет стоимости на подрамника       
def calculation_stretcher(width, length, count):
    width = width * 0.01
    length = length * 0.01
    
    # Подсчет стоимости
    res = width * length * 2000 * count
    return res

# Расчет стоимости без подрамника       
def calculation_nostretcher(width, length, count):
    width = width * 0.01
    length = length * 0.01
    
    # Подсчет стоимости
    res = width * length * 1500 * count
    return res


# Контакты продавца 
@bot.message_handler(commands = ['contacts'])
def handler_order(message):
    bot.send_message(message.chat.id, """*По вопросам о товаре и товаре:*
Александр Адреевич - продавец
номер - 89168626450
почта - Kotovsasha2001@gmail.com

*По техническим вопросам и работе бота:*
Егор Андреевич - технический специалист
номер - 89772694131
почта - egor.kainov@bk.ru""",  parse_mode='Markdown')


# Включение бота 
bot.polling(none_stop=True)