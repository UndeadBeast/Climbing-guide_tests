# -*- coding: utf-8 -*-
import pytest
from fixture.application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_explore_guide(app):
    app.session.login()
    app.open_some_route()
    app.session.logout()
