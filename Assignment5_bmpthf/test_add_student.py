import pytest
import System

def test_add_student(grade_system):
    grade_system.login('goggins', 'augurrox')

    grade_system.usr.add_student('akend3', 'databases')
    grade_system.reload_data()
    courses = grade_system.usr.users["akend3"]['courses']
    assert 'databases' in courses

@pytest.fixture
def grade_system():
    gradeSystem = System.System()
    gradeSystem.load_data()
    return gradeSystem