import hashlib
import time
import sys

# Класс User
class User:
    def __init__(self, nickname, password, age):
        # Сохраняем имя пользователя
        self.nickname = nickname
        # Хэшируем пароль и сохраняем его
        self.password = self._hash_password(password)
        # Сохраняем возраст
        self.age = age

    # Метод для хэширования пароля
    def _hash_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest()

    # Метод для проверки пароля
    def verify_password(self, password):
        return self.password == self._hash_password(password)

    # Метод для проверки возраста пользователя (можно ли смотреть контент 18+)
    def can_watch_adult_content(self):
        return self.age >= 18

    # Метод для представления объекта в читаемом формате
    def __repr__(self):
        return f"User({self.nickname}, {self.age})"

# Класс Video
class Video:
    def __init__(self, title, duration, time_now=0, adult_mode=False):
        # Заголовок видео
        self.title = title
        # Продолжительность видео
        self.duration = duration
        # Секунда остановки (по умолчанию 0)
        self.time_now = time_now
        # Ограничение по возрасту (по умолчанию False)
        self.adult_mode = adult_mode

    # Метод для представления объекта в читаемом формате
    def __repr__(self):
        return f"Video({self.title}, {self.duration}, {self.time_now}, {self.adult_mode})"

# Класс UrTube
class UrTube:
    def __init__(self, users=[], videos=[], current_user=None):
        # Список пользователей
        self.users = users
        # Список видео
        self.videos = videos
        # Текущий пользователь
        self.current_user = current_user

    # Метод входа в систему
    def log_in(self, nickname, password):
        # Проверка существования пользователя с данным именем
        for user in self.users:
            if user.nickname == nickname and user.verify_password(password):
                # Если пользователь найден, меняем текущего пользователя
                self.current_user = user
                break
        else:
            # Если пользователь не найден, сообщаем об этом
            print("Неверное имя пользователя или пароль.")

    # Метод регистрации нового пользователя
    def register(self, nickname, password, age):
        # Проверка уникальности имени пользователя
        if any(user.nickname == nickname for user in self.users):
            print(f"Пользователь {nickname} уже существует.")
        else:
            # Создание нового пользователя и добавление его в список
            new_user = User(nickname, password, age)
            self.users.append(new_user)
            # Автоматическая авторизация после регистрации
            self.log_in(nickname, password)

    # Метод выхода из аккаунта
    def log_out(self):
        # Сброс текущего пользователя на None
        self.current_user = None

    # Метод добавления новых видео
    def add(self, *new_videos):
        # Проходим по каждому новому видео
        for video in new_videos:
            # Проверяем, существует ли видео с таким заголовком
            if self.videos.count(video) == 0:
                # Если видео с таким заголовком еще не существует, добавляем его
                self.videos.append(video)

    # Метод поиска видео по ключевому слову
    def get_videos(self, search_word):
        # Приводим поисковое слово к нижнему регистру
        search_word_lower = search_word.lower()
        # Создаем список для совпадающих видео
        same_titles = []
        # Проходим по всем видео
        for video in self.videos:
            # Проверяем, содержится ли поисковое слово в заголовке видео
            if search_word_lower in video.title.lower():
                # Если да, добавляем заголовок в список
                same_titles.append(video.title)
        # Возвращаем список совпадающих заголовков
        return same_titles

    # Метод просмотра видео
    def watch_video(self, video_title):
        # Проверка, вошел ли пользователь в систему
        if self.current_user is None:
            print("Войдите в аккаунт, чтобы смотреть видео")
            return

        # Поиск видео по точному совпадению названия
        # video = next((v for v in self.videos if v.title == video_title), None)
        video = None
        for v in self.videos:
            if v.title == video_title:
                video = v
                break

        # Если видео не найдено
        if video is None:
            print(f"Видео с названием '{video_title}' не найдено.")
            return

        # Если видео найдено, но ограничено по возрасту
        if video.adult_mode and not self.current_user.can_watch_adult_content():
            print("Вам нет 18 лет, пожалуйста покиньте страницу")
            return

        # Просмотр видео
        print(f"Смотрю видео: {video_title}")
        for second in range(video.duration):
            print(f"Сек: {second + 1}", end=" ")
            sys.stdout.flush()  # Принудительно обновляет буфер вывода
            time.sleep(1)
        print("\nКонец видео")

# Тестирование
if __name__ == "__main__":
    # Создаём экземпляр UrTube
    ur_tube = UrTube()
    ur = UrTube()

    v1 = Video('Лучший язык программирования 2024 года', 200)

    v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

    # Добавление видео

    ur.add(v1, v2)

    # Проверка поиска

    print(ur.get_videos('лучший'))

    print(ur.get_videos('ПРОГ'))

    # Проверка на вход пользователя и возрастное ограничение

    ur.watch_video('Для чего девушкам парень программист?')

    ur.register('vasya_pupkin', 'lolkekcheburek', 13)

    ur.watch_video('Для чего девушкам парень программист?')

    ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)

    ur.watch_video('Для чего девушкам парень программист?')

    # Проверка входа в другой аккаунт

    ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)

    print(ur.current_user)

    # Попытка воспроизведения несуществующего видео

    ur.watch_video('Лучший язык программирования 2024 года!')

