import pytest
import System

def test_login(grade_system):
    username = 'akend3'
    password =  '123454321'
    grade_system.login(username,password)
    assert grade_system.usr.name == username

@pytest.fixture
def grade_system():
    gradeSystem = System.System()
    gradeSystem.load_data()
    return gradeSystem