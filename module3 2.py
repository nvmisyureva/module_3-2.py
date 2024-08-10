#Домашняя работа по уроку "Способы вызова функции"
#Задача "Рассылка писем"

def send_email(message, recipient, sender="university.help@gmail.com"):

    if  ('@' or'.com' or '.ru' or '.net') not in (recipient or sender):
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
    elif recipient == sender:
         print('Нельзя отправить письмо самому себе!')
    elif sender == 'university.help@gmail.com':
        print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}.')
    else:
         print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.')

send_email('messagje', 'university.help@gmail.com', '@.com')
send_email('messagje', 'university.help@gmail.com')
send_email('messagje', 'uchenik.com')
send_email('messagje', 'uchenik@.ru')
send_email('messagje', 'uchenik.net')
send_email('messagje', 'uchenik@.net')

