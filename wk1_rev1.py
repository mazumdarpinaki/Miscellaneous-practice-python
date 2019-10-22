def reverse(s):
    """ (str) -> str

    Return a reversed version of s.

    >>> reverse('hello')
    'olleh'
    >>> reverse('a')
    'a'
    """
    rev=''
    for ch in s:
	    rev=ch+rev
    return rev

def is_palindrome_v1(s):
    """ (str) -> bool

    Return True if and only if s is a palindrome.

    >>> is_palindrome_v1('noon')
    True
    >>> is_palindrome_v1('racecar')
    True
    >>> is_palindrome_v1('dented')
    False
    """

    return (reverse(s)==s)


print(__name__)
word=input('enter a word:   ')
if is_palindrome_v1(word):
    print('word'+' '+'is a palindrome')
else:
    print('word'+' '+'not a palindrome')
import doctest
doctest.testmod()
