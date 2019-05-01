import telebot
from lastfm import LastFM

TelegramBot = telebot.TeleBot('734127522:AAGBKswjLU9gXLmiEQVbee6D5_PAMJIDtLs')
LastFM = LastFM()


@TelegramBot.message_handler(content_types=['text'])
def get_text_messages(message):
    """
    Main function of bot, which reads messages and does various outputs, according to the input
    :param message:
    :return:
    """
    if message.text == '/help':
        TelegramBot.send_message(message.from_user.id,
                                 "/help - помощь. \n"
                                 " /artist_albums - показать топ альбомы артиста. \n "
                                 "/artist_tracks - показать треки артиста. \n "
                                 "/similar_tracks - показать похожие треки")
    else:
        if LastFM.state == 'state: home':
            if message.text == '/artist_albums':
                TelegramBot.send_message(message.from_user.id, "Напиши артиста")
                LastFM.state = 'state: /artist_albums. phase: get_artist'
            elif message.text == '/artist_tracks':
                LastFM.state = 'state: /artist_tracks. phase: get_artist'
                TelegramBot.send_message(message.from_user.id, "Напиши артиста")
            elif message.text == '/similar_tracks':
                LastFM.state = 'state: /similar_tracks. phase: get_artist'
                TelegramBot.send_message(message.from_user.id, "Напиши артиста")
            else:
                TelegramBot.send_message(message.from_user.id, "Напиши /help.")
        elif LastFM.state == 'state: /artist_albums. phase: get_artist':
            LastFM.artist = message.text
            LastFM.state = 'state: /artist_albums. phase: get_num'
            TelegramBot.send_message(message.from_user.id, "Напиши сколько вывести альбомов")
        elif LastFM.state == 'state: /artist_albums. phase: get_num':
            try:
                LastFM.num = int(message.text)
                data_sender(message, LastFM.artist_albums(LastFM.artist, LastFM.num))
            except Exception:
                TelegramBot.send_message(message.from_user.id, 'Error')
            LastFM.state = 'state: home'
        elif LastFM.state == 'state: /artist_tracks. phase: get_artist':
            LastFM.artist = message.text
            LastFM.state = 'state: /artist_tracks. phase: get_num'
            TelegramBot.send_message(message.from_user.id, "Напиши сколько вывести треков")
        elif LastFM.state == 'state: /artist_tracks. phase: get_num':
            try:
                LastFM.num = int(message.text)
                data_sender(message, LastFM.artist_tracks(LastFM.artist, LastFM.num))
            except Exception:
                TelegramBot.send_message(message.from_user.id, 'Error')
            LastFM.state = 'state: home'
        elif LastFM.state == 'state: /similar_tracks. phase: get_artist':
            LastFM.artist = message.text
            LastFM.state = 'state: /similar_tracks. phase: get_track'
            TelegramBot.send_message(message.from_user.id, "Напиши трек")
        elif LastFM.state == 'state: /similar_tracks. phase: get_track':
            LastFM.track = message.text
            LastFM.state = 'state: /similar_tracks. phase: get_num'
            TelegramBot.send_message(message.from_user.id, "Напиши сколько")
        elif LastFM.state == 'state: /similar_tracks. phase: get_num':
            try:
                LastFM.num = int(message.text)
                data_sender(message, LastFM.artist_tracks(LastFM.artist, LastFM.num))
            except Exception:
                TelegramBot.send_message(message.from_user.id, 'Error')
            LastFM.state = 'state: home'


def data_sender(message, data):
    """
    Function which does output
    :param message:
    :param data:
    :return:
    """
    for i in range(len(data)):
        TelegramBot.send_message(message.from_user.id, str(data[i][0]))


TelegramBot.polling(none_stop=True, interval=0)
