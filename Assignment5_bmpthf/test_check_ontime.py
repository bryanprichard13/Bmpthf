import pytest
import System

def test_ontime_assignment(grade_system):
    grade_system.login('hdjsr7', 'pass1234')

    due_date = grade_system.usr.all_courses['cloud_computing']['assignments']['assignment1']['due_date']
    submission_date = grade_system.usr.users['hdjsr7']['courses']['cloud_computing']['assignment1']['submission_date']

    check_ontime = grade_system.usr.users['hdjsr7']['courses']['cloud_computing']['assignment1']['ontime']

    assert check_ontime == grade_system.usr.check_ontime(submission_date, due_date)

    due_date = grade_system.usr.all_courses['databases']['assignments']['assignment2']['due_date']
    submission_date = grade_system.usr.users['hdjsr7']['courses']['databases']['assignment2']['submission_date']

    check_ontime = grade_system.usr.users['hdjsr7']['courses']['databases']['assignment2']['ontime']

    assert check_ontime == grade_system.usr.check_ontime(submission_date, due_date)

@pytest.fixture
def grade_system():
    gradeSystem = System.System()
    gradeSystem.load_data()
    return gradeSystem