from main import add_student, get_students, delete_student

def test_add_student():
    result = add_student("Ash")
    assert "Ash" in result

def test_get_students():
    result = get_students()
    assert isinstance(result, list)

def test_delete_student():
    add_student("Test")
    result = delete_student("Test")
    assert "Test" not in result