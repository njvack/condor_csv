from os import path

from condor_csv import csv_to_submit

DATA_PATH = path.join(path.dirname(path.abspath(__file__)), "examples")


def test_full_integration(capsys):
    # It's dumb simple but hey, this package is too.
    csvfile = path.join(DATA_PATH, "example.csv")
    csv_to_submit.make_submit([csvfile])
    out, err = capsys.readouterr()
    submit_data = open(path.join(DATA_PATH, 'example.submit')).read()
    assert out == submit_data
