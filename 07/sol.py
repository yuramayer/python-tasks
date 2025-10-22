def is_palindrome(string: str) -> bool:
    """Checks if the string is palindrome"""
    left = 0
    right = len(string) - 1

    while left < right:
        if not string[left].isalnum():
            left += 1
            continue
        if not string[right].isalnum():
            right -= 1
            continue
        if string[left].lower() != string[right].lower():
            return False
        left += 1
        right -= 1
    
    return True
