import pytest
import System

def test_check_grades(grade_system):
    username = 'hdjsr7'
    password = 'pass1234'
    course = 'cloud_computing'
    grade_system.login(username, password)

    grades = grade_system.usr.check_grades(course)
    assignments = grade_system.usr.users[username]['courses'][course]
    check_grades = []
    for key in assignments:
        check_grades.append([key, assignments[key]['grade']])
    
    assert grades == check_grades

@pytest.fixture
def grade_system():
    gradeSystem = System.System()
    gradeSystem.load_data()
    return gradeSystem