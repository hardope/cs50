from project import search_contacts
from project import new_contact
from project import list_names
from project import delete_contact

def test_search_contacts():
    assert search_contacts('check') == 'correct'
def test_new_contact():
    assert new_contact('check') == 'correct'
def test_delete_contact():
    assert delete_contact('check') == 'correct'
def test_list_names():
    assert list_names('check') == 'correct'