import pytest
import System

#this checks to make sure that a nonstudent cannot submit an assignment
def test_submit_assignment(grade_system):
    username = 'wrong1'
    password = 'pass1234'
    course = 'databases'
    assignment = 'assignment1'

    grade_system.login(username, password)

    submission = 'Meh'
    submission_date = '02/20/21'

    grade_system.usr.submit_assignment(course, assignment, submission, submission_date)
    grade_system.reload_data()
    assert grade_system.usr.users[username]['courses'][course][assignment]['submission'] == submission
    assert grade_system.usr.users[username]['courses'][course][assignment]['submission_date'] == submission_date

@pytest.fixture
def grade_system():
    gradeSystem = System.System()
    gradeSystem.load_data()
    return gradeSystem