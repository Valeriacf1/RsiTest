def add_employee(name, department, age):
    if not name or not department:
        raise ValueError("Name and Department are required")
    if age < 18:
        raise ValueError("Employee must be at least 18 years old")
    return {"name": name, "department": department, "age": age}
