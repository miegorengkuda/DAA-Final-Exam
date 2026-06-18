import json
from collections import defaultdict, deque

def get_courses_by_department(courses, department):
    return [course for course in courses if course.get('department') == department]

def build_graph(courses):
    pass

def kahn_topological_sort(courses):
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

def dfs_topological_sort(courses):
    graph = build_graph(courses)

    UNVISITED = 0
    VISITING = 1
    VISITED = 2

    state = {course: UNVISITED for course in courses}

    result = []

    def dfs(course):
        if state[course] == VISITING:
            raise ValueError("Cycle detected")

        if state[course] == VISITED:
            return

        state[course] = VISITING

        for neighbor in graph[course]:
            dfs(neighbor)

        state[course] = VISITED
        result.append(course)

    for course in courses:
        if state[course] == UNVISITED:
            dfs(course)

    result.reverse()

    return result

def main():
    with open('courses.json', 'r') as file:
        courses = json.load(file)
    
