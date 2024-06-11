# система управления учетными записями пользователей для небольшой компании.
# Компания разделяет сотрудников на обычных работников и администраторов.
# Администраторы, помимо обычных данных пользователей, имеют дополнительный уровень доступа
# и могут добавлять или удалять пользователя из системы.

class User:
    def __init__(self, id, name, prm_deg = "user"):
        self.__id = id
        self.__name = name
        self.__prm_deg = prm_deg

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def set_person(self, idi, name):
        self.__id = idi
        self.__name = name



class Admin(User):
    def __init__(self, id, name, prm_deg = "admin"):
        super().__init__(id, name, prm_deg)


    def add_user(self):
        pass

    def remove_user(self):
        pass


    # Класс должен также содержать методы add_user и remove_user, которые позволяют добавлять и удалять пользователей
    # из списка (представь, что это просто список экземпляров User).
    #
    # 3.Инкапсуляция данных: Убедись, что атрибуты классов защищены от прямого доступа и модификации снаружи.
    # Предоставь доступ к необходимым атрибутам через методы (например, get и set методы).





user2 = User(222, "Lisa")
admin1 = Admin(112, "Den")

empl_list = [user2, admin1]

print(empl_list[0].get_id())
print(empl_list[0].get_name())
print(empl_list[1].get_id())
print(empl_list[1].get_name())

#print(User(111, "Nik").name)
#User(111, "Nik").print_prm()

#admin1.print_name()
#admin1.print_prm()

#print(admin1.name)
