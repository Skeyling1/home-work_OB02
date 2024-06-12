# система управления учетными записями пользователей для небольшой компании.
# Компания разделяет сотрудников на обычных работников и администраторов.
# Администраторы, помимо обычных данных пользователей, имеют дополнительный уровень доступа
# и могут добавлять или удалять пользователя из системы.

class User:
    def __init__(self, id, name, prm_deg = "user"):
        self.__id = id
        self.__name = name
        self.__prm_deg = prm_deg

    def get_info(self):
        i = [self.__id, self.__name, self.__prm_deg]
        return i

    def set_person(self, idi, name):
        self.__id = idi
        self.__name = name

class Admin(User):
    def __init__(self, id, name, prm_deg = "admin"):
        super().__init__(id, name, prm_deg)

    def add_user(self, id, name, prm_deg = "user"):
        u = User(id, name, prm_deg)
        return u

    def remove_user(self, empl_list_numb):
        empl_list.remove(empl_list_numb)
        return empl_list

    def print_list(self):
        for i in range(len(empl_list)):
            t = empl_list[i].get_info()
            print(t)


admin1 = Admin(111, "Den")

empl_list = []
empl_list.append(admin1.add_user(222, "Ted"))
empl_list.append(admin1.add_user(333, "Gizmo"))
empl_list.append(admin1.add_user(444, "Kate"))

admin1.print_list()




