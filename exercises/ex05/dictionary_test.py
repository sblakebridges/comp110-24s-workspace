"""Dictionary Test!"""

__author__ = "730643380"


from exercises.ex05.dictionary import invert, favorite_color, count, alphabetizer, update_attendance


def test_edge_invert() -> None:
    """Edge case test for invert."""
    assert invert({}) == {}


def test_case_invert() -> None:
    """Regular case test for invert."""
    assert invert({'a': 'apple', 'b': 'banana', 'c': 'cherry'}) == {'apple': 'a', 'banana': 'b', 'cherry': 'c'}


def test_case2_invert() -> None:
    """Regular case test for invert."""
    assert invert({'a': 'apple'}) == {'apple': 'a'}


def test_edge_favorite_color() -> None:
    """Edge case test for favorite_color."""
    assert favorite_color({}) == ''


def test_case_favorite_color() -> None:
    """Regular case test for favorite_color."""
    assert favorite_color({'a': 'red', 'b': 'blue', 'c': 'red', 'd': 'green', 'e': 'red'}) == 'red'


def test_case2_favorite_color() -> None:
    """Regular case test for favorite_color."""
    assert favorite_color({'a': 'yellow'}) == 'yellow'


def test_edge_count() -> None:
    """Edge case test for count."""
    assert count({}) == {}


def test_case_count() -> None:
    """Regular case test for count."""
    assert count(['a', 'b', 'a', 'c', 'b', 'a', 'd', 'e', 'e', 'd']) == {'a': 3, 'b': 2, 'c': 1, 'd': 2, 'e': 2}


def test_case2_count() -> None:
    """Regular case test for count."""
    assert count(['red', 'blue', 'green', 'yellow']) == {'red': 1, 'blue': 1, 'green': 1, 'yellow': 1}


def test_edge_alphabetizer() -> None:
    """Edge case test for alphabetizer."""
    assert alphabetizer({}) == {}


def test_case_alphabetizer() -> None:
    """Regular case test for alphabetizer."""
    assert alphabetizer(['apple', 'banana', 'ball', 'cat', 'dog', 'elephant']) == {'a': ['apple'], 'b': ['banana', 'ball'], 'c': ['cat'], 'd': ['dog'], 'e': ['elephant']}


def test_case2_alphabetizer() -> None:
    """Regular case test for alphabetizer."""
    assert alphabetizer(['red', 'blue', 'green', 'yellow']) == {'r': ['red'], 'b': ['blue'], 'g': ['green'], 'y': ['yellow']}


def test_edge_update_attendance() -> None:
    """Edge case test for update_attendance."""
    attendance = {"Blake": ["Monday"], "James": ["Tuesday"]}
    update_attendance(attendance, "", "")
    assert attendance == {"Blake": ["Monday"], "James": ["Tuesday"], "": [""]}


def test_case_update_attendance() -> None:
    """Regular case test for update_attendance."""
    attendance = {"Andre": ["Thursday"], "Emily": ["Tuesday"]}
    update_attendance(attendance, "Emma", "Wednesday")
    assert attendance == {"Andre": ["Thursday"], "Emily": ["Tuesday"], "Emma": ["Wednesday"]}


def test_case2_update_attendance() -> None:
    """Regular case test for update_attendance."""
    attendance = {"Jack": ["Friday"]}
    update_attendance(attendance, "Connor", "Saturday")
    assert attendance == {"Jack": ["Friday"], "Connor": ["Saturday"]}