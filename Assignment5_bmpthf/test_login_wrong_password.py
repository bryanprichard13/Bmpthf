import pytest
import System

#this checks to make sure that the username is not the only thing checked on login, the username must be checked too
def test_login(grade_system):
    username = 'akend3'
    password =  'wrongpass'
    grade_system.login(username,password)
    assert grade_system.usr.name == username

@pytest.fixture
def grade_system():
    gradeSystem = System.System()
    gradeSystem.load_data()
    return gradeSystem