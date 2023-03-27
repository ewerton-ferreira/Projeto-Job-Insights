from src.pre_built.sorting import sort_by
from src.insights.jobs import read


def test_sort_by_criteria():
    file = read("data/jobs.csv")
    result = [row for row in file]

    mock_min_salary = [result[1], result[2]]
    sort_by(mock_min_salary, 'min_salary')
    assert mock_min_salary == [result[1], result[2]]

    mock_max_salary = [result[1], result[2]]
    sort_by(mock_max_salary, 'max_salary')
    assert mock_max_salary == [result[1], result[2]]

    mock_date_posted = [result[1], result[2]]
    sort_by(mock_date_posted, 'date_posted')
    assert mock_date_posted == [result[2], result[1]]
