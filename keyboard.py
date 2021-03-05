from telebot import types
import function as func

m_row = lambda row, n=3: [row[i:i+n] for i in range(0, len(row), n)]
#устаревший
def generate_key1(typed, text):
    keyb = types.InlineKeyboardMarkup()
    for key in text:
        back = f'{typed}(){key}'
        keyb.add(types.InlineKeyboardButton(text=text[key], callback_data=back))
    if typed == 'city':
        keyb.add(types.InlineKeyboardButton(text='⏪Ба қафо⏪', callback_data=f'back'))
    elif typed == 'reg':
        keyb.add(types.InlineKeyboardButton(text='❌Баромадан❌', callback_data='exit'))
    return keyb
def generate_key(typed, text): ##знаю хуже не бывает но работает 
    row = []
    keyb = types.InlineKeyboardMarkup()
    for key, value in text.items():
        row.append([key, value])
    big_row = m_row(m_row(row ,2), 2)
    for min_row in big_row:
        for min_row in min_row:
            if len(min_row)>1:
                keyb.add(types.InlineKeyboardButton(text=min_row[0][1], callback_data=f'{typed}(){min_row[0][0]}'),types.InlineKeyboardButton(text=min_row[1][1], callback_data=f'{typed}(){min_row[1][0]}'))
            else:
                keyb.add(types.InlineKeyboardButton(text=min_row[0][1], callback_data=f'{typed}(){min_row[0][1]}'))
    if typed == 'city':
        keyb.add(types.InlineKeyboardButton(text='⏪Ба қафо⏪', callback_data=f'back'))
    elif typed == 'reg':
        keyb.add(types.InlineKeyboardButton(text='❌Баромадан❌', callback_data='exit'))
    return keyb