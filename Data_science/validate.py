def validate_user(username, minlen):
    assert type(username) == str, "Username must be string"
    if minlen < 1:
        raise ValueError("Username must me atleast 1 charcter")
    if len(username) < minlen:
        return False
    if not username.isalnum():
        return False
    return True
