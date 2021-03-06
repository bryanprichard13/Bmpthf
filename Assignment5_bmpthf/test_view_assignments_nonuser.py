import pytest
import System

#this checks to make sure that only the correct user can view their assignments
def test_view_assignments(grade_system):
    username = 'wrong1'
    password = '123454321'
    course = 'cloud_computing'
    grade_system.login(username, password)

    final_assignments = []
    assignments = grade_system.usr.view_assignments(course)
    check_assignments = grade_system.usr.all_courses[course]['assignments']
    for key in check_assignments:
        final_assignments.append([key,check_assignments[key]['due_date']])
    
    assert assignments == final_assignments

@pytest.fixture
def grade_system():
    gradeSystem = System.System()
    gradeSystem.load_data()
    return gradeSystem