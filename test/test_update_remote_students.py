from src.update_remote_students import update_remote_students

def test_returns_empty_list_given_empty_list():
    assert update_remote_students([]) == []

def test_returns_copy_input_if_no_change_required():
    test_students = [{"name": "Hypatia", "age": 31, "location": "leeds"}]
    expected = [{"name": "Hypatia", "age": 31, "location": "leeds"}]
    assert update_remote_students(test_students) == expected

def test_returns_updated_location_given_one_change_required():
    test_students = [{ "name": 'Ramanujan', "age": 22}]
    expected = [{ "name": "Ramanujan", "age": 22, "location": "remote"}]
    assert update_remote_students(test_students) == expected

def test_returns_multiple_updates():
    test_students = [
        {"name": "Hypatia", "age": 31, "location": "leeds"},
        {"name": "Ramanujan", "age": 22},
        {"name": "Tao", "age": 47, "location": "manchester"},
        {"name": "Brian", "age": 23}
    ]
    expected = [
        {"name": "Hypatia", "age": 31, "location": "leeds"},
        {"name": "Ramanujan", "age": 22, "location": "remote"},
        {"name": "Tao", "age": 47, "location": "manchester"},
        {"name": "Brian", "age": 23, "location": "remote"}
    ]
    assert update_remote_students(test_students) == expected

def test_input_unchanged():
    test_students = [
        {"name": "Hypatia", "age": 31, "location": "leeds"},
        {"name": "Ramanujan", "age": 22},
        {"name": "Tao", "age": 47, "location": "manchester"},
        {"name": "Brian", "age": 23}
    ]
    copy_test_students = [
        {"name": "Hypatia", "age": 31, "location": "leeds"},
        {"name": "Ramanujan", "age": 22},
        {"name": "Tao", "age": 47, "location": "manchester"},
        {"name": "Brian", "age": 23}
    ]
    update_remote_students(test_students)
    assert test_students == copy_test_students