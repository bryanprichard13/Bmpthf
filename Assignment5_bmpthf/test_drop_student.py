import pytest
import System

def test_drop_student(grade_system):
    grade_system.login('goggins', 'augurrox')

    grade_system.usr.drop_student('akend3', 'databases')
    grade_system.reload_data()
    courses = grade_system.usr.users["akend3"]['courses']
    assert 'databases' not in courses

@pytest.fixture
def grade_system():
    gradeSystem = System.System()
    gradeSystem.load_data()
    return gradeSystem