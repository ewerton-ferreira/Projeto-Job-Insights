from functools import lru_cache
from typing import List, Dict
import csv


@lru_cache
def read(path: str) -> List[Dict]:
    if not path.endswith('.csv'):
        raise ValueError('File must be a CSV')
    with open(path) as file:
        data = list(csv.DictReader(file))
    return data


def get_unique_job_types(path: str) -> List[str]:
    file = read(path)
    job_types = set()
    for row in file:
        job_types.add(row['job_type'])
    return list(job_types)


def filter_by_job_type(jobs: List[Dict], job_type: str) -> List[Dict]:
    return [job for job in jobs if job['job_type'] == job_type]
