import pytest
import System

def test_grade_change(grade_system):
    username = 'cmhbf5'
    password = 'bestTA'
    grade_system.login(username,password)
    grade_system.usr.change_grade('yted91', 'cloud_computing', 'assignment1', 24)
    grade_system.reload_data()
    assert grade_system.usr.users['yted91']['courses']['cloud_computing']['assignment1']['grade'] == 24


@pytest.fixture
def grade_system():
    gradeSystem = System.System()
    gradeSystem.load_data()
    return gradeSystem