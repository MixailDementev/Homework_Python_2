import pytest                      # необходимо установить в окружение


from seminar_13_task_5 import UserWorkshop, User
from Exceptions import AccesErorr, LevelError
from seminar_13_user import User
@pytest.fixture()
def set_up():
    return UserWorkshop()

def test_access_fail_1(set_up):
    with pytest.raises(AccesErorr, match='Access denied'):
        set_up.login('Nesterovs', '1')

def test_access(set_up):                                    # тест на проверку валидных данных, то что должна вернуться
    assert set_up.login('Nesterov', '1') == '5'             # вводятся валидные двнные и проверяем на совпадение с результатом


def test_access_fail_2(set_up):                                    # тест на проверку того, что  будет выброс исключения AccesErorr при вводе невалидных данных, AccesErorr  прописан в Exceptions.py
    with pytest.raises(LevelError):
        set_up.login('Nesterov', '1')
        set_up.create_user('New_user', '1', '3')



if __name__ == '__main__':
    pytest.main(['-v'])