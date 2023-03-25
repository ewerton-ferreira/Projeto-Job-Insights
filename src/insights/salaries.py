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
    if not isinstance(salary, (int, str)):
        raise TypeError('Salary precisa ser um número inteiro')

    mins = min_salary = job.get('min_salary')
    maxs = max_salary = job.get('max_salary')

    if not all(
        isinstance(s, (int, str)) and s.isdigit() for s in [mins, maxs]
    ):
        raise ValueError('Invalid job data')

    if int(min_salary or 0) > int(max_salary or 0):
        raise ValueError('Invalid job data')

    if int(salary) < int(mins or 0) or int(salary) > int(maxs or 0):
        return False

    return True


def filter_by_salary_range(
    jobs: List[dict],
    salary: Union[str, int]
) -> List[Dict]:
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    raise NotImplementedError
