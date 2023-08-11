import pytest

from seminar_13_task_5 import Project, User
from Exceptions import AccesErorr, LevelError


@pytest.fixture()
def set_up():
    return Project()


def test_access_fail_1(set_up):
    with pytest.raises(AccesErorr, match="Access denied"):
        set_up.login("Nesterovs", "1")


def test_access(set_up):
    assert set_up.login("Nesterov", "1") == "5"


def test_access_fail_2(set_up):
    with pytest.raises(LevelError):
        set_up.login("Nesterov", "1")
        set_up.create_user("New_user", "1", "3")


if __name__ == "__main__":
    pytest.main(["-v"])
