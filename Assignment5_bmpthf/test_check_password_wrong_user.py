import pytest
import System

#this checks to make sure that the username as well as the password are checked, not just the password
def test_password(grade_system):
    username = 'wrong1'
    password =  '123454321'
    grade_system.login(username,password)
    assert grade_system.usr.password == password

@pytest.fixture
def grade_system():
    gradeSystem = System.System()
    gradeSystem.load_data()
    return gradeSystem