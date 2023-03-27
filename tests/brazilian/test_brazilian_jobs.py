from src.pre_built.brazilian_jobs import read_brazilian_file


def test_brazilian_jobs():
    result_jobs = read_brazilian_file('tests/mocks/brazilians_jobs.csv')

    for job in result_jobs:
        # print(job)
        for key, value in job.items():
            assert key in [
                'title', 'salary', 'type']
            assert isinstance(value, str)
        # print(key)
        # print(value)
