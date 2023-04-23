from aiogram import Bot, Dispatcher
import config


async def q_Animals(self, user, dp):
    """
    тип квеста: 1 (загадка и ответ)

    :param user: объект типа user
    :param: dp: диспетчер бота, к нему обращаемся в хендлере:
    @dp.message_handler()
    """

    pass

    return True


async def q_China(self, user, dp):
    """
    тип квеста: 1 (загадка и ответ)

    :param user: объект типа user
    :param: dp: диспетчер бота, к нему обращаемся в хендлере:
    @dp.message_handler()
    """

    pass

    return True


async def q_Wing(self, user, dp):
    """
    тип квеста: 1 (загадка и ответ)

    :param user: объект типа user
    :param: dp: диспетчер бота, к нему обращаемся в хендлере:
    @dp.message_handler()
    """

    pass

    return True


async def q_Light(self, user, dp):
    """
    тип квеста: 1 (загадка и ответ)

    :param user: объект типа user
    :param: dp: диспетчер бота, к нему обращаемся в хендлере:
    @dp.message_handler()
    """

    pass

    return True


async def q_Shell(self, user, dp):
    """
    тип квеста: 1 (загадка и ответ)

    :param user: объект типа user
    :param: dp: диспетчер бота, к нему обращаемся в хендлере:
    @dp.message_handler()
    """

    pass

    return True

async def q_Case(self, user, dp):
    """
    тип квеста: 1 (загадка и ответ)

    :param user: объект типа user
    :param: dp: диспетчер бота, к нему обращаемся в хендлере:
    @dp.message_handler()
    """

    pass

    return True

async def q_Iron(self, user, dp):
    """
    тип квеста: 1 (загадка и ответ)

    :param user: объект типа user
    :param: dp: диспетчер бота, к нему обращаемся в хендлере:
    @dp.message_handler()
    """

    pass

    return True

async def q_Planet(self, user, dp):
    """
    тип квеста: 1 (загадка и ответ)

    :param user: объект типа user
    :param: dp: диспетчер бота, к нему обращаемся в хендлере:
    @dp.message_handler()
    """

    pass

    return True


async def q_Morze(self, quest, user, dp):
    """
    тип квеста: 2 (азбука морзе, шифрование имени пользователя и его последующее сравнение с ответом)

    :param user: объект типа user
    :param: dp: диспетчер бота, к нему обращаемся в хендлере:
    @dp.message_handler()
    """

    pass

    return True


async def q_Draw(self, quest, user, dp):
    """
    Тип квеста: 3 (анализ типа сообщения пользователя, проверка на Image)

    :param user: объект типа User
    :param: dp: диспетчер бота, к нему обращаемся в хендлере:
    @dp.message_handler()
    """

    pass

    return True












if __name__ == "__main__":

    ### ==========

    # Для инициализации токена необходимо вбить его вместо config.TOKEN.
    # Однако, если вы хотите работать в команде и с git`ом, то лучше заведите файл config,
    # в котором создайте переменную TOKEN и присвойте ей значение вашего TG-бота.
    token = config.TOKEN

    ### ==========






    # Создаём асинхронного бота.
    tg_bot = Bot(token)
    dispatcher = Dispatcher(tg_bot)

    # Заводим список пользователей, проходящих сейчас квесты параллельно.
    list_user = []

    # Заводим список квестов, свободных для прохождения.
    free_quests = []

    # TODO: Написать функцию распрделения пользователей по комнатам.


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
