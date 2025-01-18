# class Singleton:
#     _instance = None
#
#     def __new__(cls, *args, **kwargs):
#         if not cls._instance:
#             cls._instance = super().__new__(cls, *args, **kwargs)
#         return cls._instance
#
#     @classmethod
#     def get_instance(cls):
#         return cls._instance
#
# # Пример использования
# class MyClass(Singleton):
#     def print_message(self):
#         print("Hello, World!")
#
# obj1 = MyClass()
# obj2 = MyClass()
#
# assert obj1 is obj2  # Оба объекта ссылаются на один и тот же экземпляр
#
# my_class_instance = MyClass.get_instance()
# my_class_instance.print_message()  # Выводит "Hello, World!"

import time
import hashlib


class User:

    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = self.hash_password(password)
        self.age = age

    def verify_password(self, password):
        return self.password == self.hash_password(password)

    @staticmethod
    def hash_password(password):
        return hashlib.sha256(password.encode()).hexdigest()

    def can_watch_adult_content(self):
        return self.age >= 18


class UrTube:

    def __init__(self, users, videos, current_user):
        self.users = users
        self.videos = videos
        self.current_user = current_user

    class Users:
        def __init__(self):
            self.users = {}

       def log_in(self, nickname, password):
            user_ = self.find_user(nickname, password)
            if user_ is not None:
                self.current_user = user_

        def find_user(self, nickname, password):
            try:
                user_ = self.users[nickname]
                if user_.verify_password(password):
                    return user_
            except KeyError:
                return None

        def register(self, nickname, password, age):
            if self.check_unique_nickname(nickname):
                self.users[nickname] = User(nickname, password, age)
                self.log_in(nickname, password)
            else:
                print(f"Пользователь {nickname} уже существует.")

        def check_unique_nickname(self, nickname):
            return nickname not in self.users

        def log_out(self):
            self.current_user = None

    class VideoLibrary:
        def __init__(self):
            self.videos = {}

        def add_video(self, *videos):
            for video in videos:
                if video.title not in self.videos:
                    self.videos[video.title] = video

        def get_videos(self, search_word):
            matching_titles = []
            search_word_lower = search_word.lower()

            for title in self.videos.keys():
                if search_word_lower in title.lower():
                    matching_titles.append(title)

            return matching_titles

        def watch_video(self, video_title):
            if self.current_user is None:
                print("Войдите в аккаунт, чтобы смотреть видео")
                return

            video = self.videos.get(video_title)
            if video is None:
                print(f"Видео с названием '{video_title}' не найдено.")
                return

            if video.adult_mode and not self.current_user.can_watch_adult_content():
                print("Вам нет 18 лет, пожалуйста покиньте страницу")
                return

            print(f"Смотрю видео: {video_title}")
            for second in range(60):
                print(f"Секунда: {second + 1}")
                time.sleep(1)
            print("Конец видео")

    class Video:
        def __init__(self, title, duration, time_now, adult_mode=False):
            self.title = title
            self.duration = duration
            self.time_now = time_now
            self.adult_mode = adult_mode