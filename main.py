import json
from collections import defaultdict, deque

def get_courses_by_department(courses, department):
    return [course for course in courses if course.get('department') == department]

def build_graph(courses):
    pass

def kahn_semesters(courses):
    graph = build_graph(courses)

    indegree = {course: 0 for course in courses}

    for source in graph:
        for target in graph[source]:
            indegree[target] += 1

    queue = deque()

    for course, degree in indegree.items():
        if degree == 0:
            queue.append(course)

    semesters = []
    processed = 0

    while queue:
        semester_size = len(queue)

        semester = []

        for _ in range(semester_size):
            current = queue.popleft()
            semester.append(current)
            processed += 1

            for neighbor in graph[current]:
                indegree[neighbor] -= 1

                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        semesters.append(semester)

    if processed != len(courses):
        raise ValueError("Cycle detected")

    return semesters

def main():
    with open('courses.json', 'r') as file:
        courses = json.load(file)
    
