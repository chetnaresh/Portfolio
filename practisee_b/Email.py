def is_valid_email(email):
    if '@' not in email or '.' not in email:
        return False
    if email.count('@') != 1:
        return False

    local, domain = email.split('@')
    if not local or not domain:
        return False
    if '.' not in domain:
        return False

    if domain.startswith('.') or domain.endswith('.'):
        return False

    return True

print(is_valid_email("test@gmail.com"))
print(is_valid_email("invalid@com")) 