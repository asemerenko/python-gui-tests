import pytest
import jsonpickle
import os.path
from fixture.application import Application
from comtypes.client import CreateObject
from model.group import Group


@pytest.fixture(scope="session")
def app(request):
    fixture = Application("C:\\Tools\\AppsForTesting\\Addressbook\\AddressBook.exe")
    request.addfinalizer(fixture.destroy)
    return fixture


def pytest_generate_tests(metafunc):
    for fixture in metafunc.fixturenames:
        if fixture.startswith("json_"):
            testdata = load_from_json(fixture[5:])
            metafunc.parametrize(fixture, testdata, ids=[str(x) for x in testdata])
        elif fixture.startswith("xl_"):
            testdata = load_from_xl(fixture[3:])
            metafunc.parametrize(fixture, testdata, ids=[str(x) for x in testdata])


def load_from_json(file):
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "data/%s.json" % file)) as f:
        return jsonpickle.decode(f.read())


def load_from_xl(file):
    xl = CreateObject("Excel.Application")
    xl.Workbooks.Open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "data/%s.xlsx" % file))
    testdata = []
    n = 2
    for i in range(n):
        data = xl.Range["A%s" % (i + 1)].Value[()]
        testdata.append(Group(name=data))
    xl.Quit()
    return testdata
