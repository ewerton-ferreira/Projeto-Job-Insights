from src.pre_built.counter import count_ocurrences


def test_counter():
    result_counter_word1 = count_ocurrences(('data/jobs.csv'), 'python')
    assert result_counter_word1 == 1639

    result_counter_word2 = count_ocurrences(('data/jobs.csv'), 'Javascript')
    assert result_counter_word2 == 122
