from typing import Union, List, Dict
from src.insights.jobs import read


def get_max_salary(path: str) -> int:
    file = read(path)
    salary_max = 0
    for job in file:
        if job['max_salary'].isdigit():
            if int(job['max_salary']) > salary_max:
                salary_max = int(job['max_salary'])

    return salary_max


def get_min_salary(path: str) -> int:
    file = read(path)
    salary_min = float('inf')
    for job in file:
        if job['min_salary'].isdigit():
            if int(job['min_salary']) < salary_min:
                salary_min = int(job['min_salary'])

    return salary_min


def matches_salary_range(job: Dict, salary: Union[int, str]) -> bool:
    if "max_salary" not in job or "min_salary" not in job:
        raise ValueError(
            'A "max_salary" and "min_salary"'
            'key must be provided in job dictionary.')

    try:
        int(job['min_salary'])
        int(job['max_salary'])
        int(salary)

    except TypeError:
        raise ValueError(
            'min_salary, max_salary and salary must be an integer')

    if int(job['min_salary']) > int(job['max_salary']):
        raise ValueError(
            'Minimum value cannot be greater than the maximum value')

    return int(job["min_salary"]) <= int(salary) < int(job["max_salary"])


def filter_by_salary_range(
    jobs: List[dict],
    salary: Union[str, int]
) -> List[Dict]:
    filter_salary = []
    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                filter_salary.append(job)
        except ValueError:
            ('Invalid salary range')
    return filter_salary
