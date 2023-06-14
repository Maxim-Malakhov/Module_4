def is_palindrome(string: str) -> bool:
    '''Returns `True` if parameter `string` is palindrome,
    else returns `False`'''
    return string == string[::-1]

if __name__ == '__main__':
    print(
        is_palindrome("лепсспел"),
        is_palindrome('helloworld')
        )
