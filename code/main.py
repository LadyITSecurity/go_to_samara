from quest import Quest
from users import User
from aiogram import Bot, Dispatcher, types
import config



async def q_Animals(self, user, dp):
    """
    тип квеста: 1 (загадка и ответ)

    :param user: объект типа user
    :param: dp: диспетчер бота, к нему обращаемся в хендлере:
    @dp.message_handler()
    """
    функция для написания Юлией.
    тип квеста - загадка и ответ.

    :param quest: объект типа quest
    :param user: объект типа user

    :param: dp: диспетчер бота, к нему обращаемся в хендлере:
    @dp.message_handler()

    :return: true по завершению прохождения квеста.
    """

    """
    тело твоего кода, юлия.
    """

    return True


async def quest_of_morze(self, quest, user, dp):
    """
    функция для написания дарьей.
    тип квеста - азбука морзе, шифрование имени пользователя и его последующее сравнение с ответом.

    :param quest: объект типа quest
    :param user: объект типа user

    :param: dp: диспетчер бота, к нему обращаемся в хендлере:
    @dp.message_handler()

    :return: true по завершению прохождения квеста.
    """

    """
    тело твоего кода, дарья.
    """

    return True


async def quest_of_Image(self, quest, user, dp):
    """
    Функция для написания Ульяной.
    Тип квеста - анализ типа сообщения пользователя.

    :param quest: объект типа Quest
    :param user: объект типа User

    :param: dp: диспетчер бота, к нему обращаемся в хендлере:
    @dp.message_handler()

    :return: True по завершению прохождения квеста.
    """

    """
    Тело твоего кода, Ульяна.
    """

    return True


if __name__ == "__main__":
    # Создаём асинхронного бота.
    tg_bot = Bot(token=config.TOKEN)
    dispatcher = Dispatcher(tg_bot)

    # Заводим список пользователей, проходящих сейчас квесты параллельно.
    list_user = []

    # TODO: Написать функцию создания списка квестов.
    list_quest = []


    @dispatcher.message_handler(commands=['start'])
    async def start(message):
        # TODO: Изменить приветствие, добавить медиа и т.п.

        hello_text = "Привет! Добро пожаловать в квест-комнату музея А. Зеленко! Как тебя зовут?"
        await message.reply(message.from_user.id, hello_text)


    @dispatcher.message_handler(commands=['next_quest'])
    async def run_next_quest(message):
        # TODO: Написать алгоритм выборки свободного квеста по приоритету.
        pass


    @dispatcher.message_handler(commands=['quit'])
    async def quit_from_game(message):
        pass


    @dispatcher.message_handler()
    def process_user_answer(message):
        # TODO: продумать, как нам сохранять имя пользователя.
        pass
