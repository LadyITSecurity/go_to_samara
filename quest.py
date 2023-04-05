"""
Данный объект отвечает за структуру квест-загадок.
Будет специальнвя функция-инициализатор, которая создает 6-9 квест-загадок в оператике.
Далее - ссылки на эти загадки будут использоваться в ваших функциях.

Приведённая структура является примером для вашего кода.
Опирайтесь на неё.

По существу, в вашу функцию будет передаваться объект класса Quest.
"""


class Quest():
    def __init__(self, id, type, priority, question, hints, media):
        self.id = id
        self.type = type
        self.priority = priority

        self.question = question
        self.hints = hints
        self.media = media

        self.__free = True


    def is_free(self):
        '''
        Если квест сейчас свободен - вернёт True.
        Иначе - False.
        '''

        return self.__free


    def occupy(self):
        """
        Занимает данный квест, если он свободен.
        """

        if self.__free == True:
            self.__free = False

            return True

        else:
            return False


    def free(self):
        '''
        Освобождает квест, если пользователь его прошёл.
        '''

        if self.__free == False:
            self.__free = True

            return True

        else:
            return False
