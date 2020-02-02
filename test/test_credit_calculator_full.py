
from model.group import Group

def test_calculator_2(app):
    app.credit_form_case_2(Group(loan = '100000', payment='50000', term='12'))
    app.session.submit()