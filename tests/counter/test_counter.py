from src.pre_built.counter import count_ocurrences


def test_counter():
    result_counter = count_ocurrences(('data/jobs.csv'), 'python')
    assert result_counter == 1639
