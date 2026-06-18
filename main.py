import json

def getCourseByDepartment(courses, department):
    return [course for course in courses if course.get('department') == department]

def makeGraph(selected_courses):
    # Implementation for creating a graph from selected courses
    pass

def main():
    with open('courses.json', 'r') as file:
        courses = json.load(file)
    