import pytest
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.app import App

from childApp import childApp



def test_function():
    with warnings.catch_warnings(record=True) as w:
        warnings.simplefilter("always")
        # Your test code here
        assert False, "This test should fail"
    assert len(w) == 1
    assert issubclass(w[-1].category, DeprecationWarning)
    assert "imghdr" in str(w[-1].message)


def test_childApp():
    app = childApp()
    assert isinstance(app, GridLayout)
    assert app.cols == 2

    # Check widgets
    assert isinstance(app.children[0], Label)
    assert app.children[0].text == 'Student Name'
    assert isinstance(app.children[1], TextInput)
    assert app.children[1].hint_text == 'Enter student name'

    assert isinstance(app.children[2], Label)
    assert app.children[2].text == 'Student Marks'
    assert isinstance(app.children[3], TextInput)

    assert isinstance(app.children[4], Label)
    assert app.children[4].text == 'Student Gender'
    assert isinstance(app.children[5], TextInput)

    assert isinstance(app.children[6], Button)
    assert app.children[6].text == 'click me'


def test_click_me():
    app = childApp()
    app.s_name.text = 'John Doe'
    app.s_marks.text = '85'
    app.s_gender.text = 'Male'

    app.click_me(None)

    assert app.s_name.text == ''
    assert app.s_marks.text == ''
    assert app.s_gender.text == ''


def test_click_me_invalid_marks():
    app = childApp()
    app.s_name.text = 'John Doe'
    app.s_marks.text = '85a'
    app.s_gender.text = 'Male'

    with pytest.raises(ValueError):
        app.click_me(None)

    assert app.s_name.text == 'John Doe'
    assert app.s_marks.text == '85a'
    assert app.s_gender.text == 'Male'

if __name__ == '__main__':
    pytest.main(['-vs', 'test_app.py'])