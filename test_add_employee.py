import pytest
from employees.utils import add_employee

def test_add_employee_success():
    result = add_employee("Valeria", "HR", 25)
    assert result == {"name": "Valeria", "department": "HR", "age": 25}

def test_add_employee_minimum_age():
    result = add_employee("Juan", "IT", 18)
    assert result["age"] == 18

def test_add_employee_no_name():
    with pytest.raises(ValueError, match="Name and Department are required"):
        add_employee("", "HR", 25)

def test_add_employee_no_department():
    with pytest.raises(ValueError, match="Name and Department are required"):
        add_employee("Valeria", "", 25)

def test_add_employee_underage():
    with pytest.raises(ValueError, match="Employee must be at least 18 years old"):
        add_employee("Valeria", "HR", 17)
