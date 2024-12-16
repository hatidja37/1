def send_email(message, recipient, sender = "university.help@gmail.com"):

    if "@" not in recipient  or not recipient.endswith(".ru") and not  recipient.endswith(".com") and not recipient.endswith(".net"):
        print("Невозможно отправить письмо с адреса", sender, "на адрес", recipient)
    if "@" not in sender or not sender.endswith(".ru") and not sender.endswith(".com") and not sender.endswith(".net"):
        print("Невозможно отправить письмо с адреса <sender> на адрес <recipient>")
        return
    if sender == recipient:
        print("Нельзя отправить письмо самому себе!")
        return
    if 'university.help@gmail.com' in sender:
        print("Письмо успешно отправлено с адреса", sender, "на адрес", recipient)
    else:
        print("НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса", sender, "на адрес", recipient)


send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')

send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')

send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')

send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')



