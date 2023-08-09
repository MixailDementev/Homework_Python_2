
import json
from seminar_13_user import User
from Exceptions import AccesErorr, LevelError

class Project:
    user_list = set()

    def __init__(self):
        Project.load_users()
        pass


    @staticmethod
    def load_users(path: str = 'users.json'):
        with open(path, 'r', encoding='UTF-8') as f:
            user_dict = json.load(f)
        for level, user_list in user_dict.items():
            for id, name in user_list.items():
                Project.user_list.add(User(name, str(id), str(level)))


    def login(self, name: str, id: str):            
        login_user = User(name, id)
        for user in Project.user_list:
            if login_user == user:               
                return user.level
        else:
            raise AccesErorr()

    def create_user(self, name: str, id: str, level: str):
        cur_name, cur_id = input("Введите имя авторизированного пользователя и его id через пробел: ").split()
        if current_level := self.login(cur_name, cur_id):
            if int(current_level) > int(level):
                return User(name, id, level)
            else:
                raise LevelError(current_level, level)


if __name__ == '__main__':

    b = Project()

    # print(b.login('Nester', '1'))
    print(b.login('Nesterov', '1'))
    print(b.create_user('New_user', '1', '3'))