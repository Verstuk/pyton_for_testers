import pytest
from model.group import Group
from fixture.application import Application


def test_calculator(app):
    app.credit_form_case_1(Group(loan = '100000', payment='50000', term='12'))
    app.session.submit()


def test_calculator_empty(app):
    app.credit_form_case_1(Group(loan = '', payment='', term=''))
    app.session.submit()

