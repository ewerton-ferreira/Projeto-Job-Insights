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
    salary_min = (
        int(job['min_salary'])
        if type(job['min_salary'] == int) and job['min_salary'] >= 0
        else float('-inf')
        )
    salary_max = (
        int(job['max_salary'] >= 0)
        if type(job['max_salary'] == int) and job['max_salary'] >= 0
        else float('inf')
        )
    salary_range = salary_min <= int(salary) <= salary_max
    return salary_range


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
