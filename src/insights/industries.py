from typing import List, Dict
from src.insights.jobs import read


def get_unique_industries(path: str) -> List[str]:
    file = read(path)
    industries_list = set()
    for row in file:
        if row["industry"] != '':
            industries_list.add(row['industry'])
    return list(industries_list)


def filter_by_industry(jobs: List[Dict], industry: str) -> List[Dict]:
    return [job for job in jobs if job['industry'] == industry]
