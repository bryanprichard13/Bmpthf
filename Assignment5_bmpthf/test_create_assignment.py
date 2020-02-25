import pytest
import System

def test_create_assignment(grade_system):
    username = 'cmhbf5'
    password = 'bestTA'
    course = 'software_engineering'
    grade_system.login(username,password)

    grade_system.usr.create_assignment("test", "2/29/20", course)
    grade_system.reload_data()
    assignments = grade_system.usr.all_courses[course]['assignments']

    assert 'test' in assignments

@pytest.fixture
def grade_system():
    gradeSystem = System.System()
    gradeSystem.load_data()
    return gradeSystem