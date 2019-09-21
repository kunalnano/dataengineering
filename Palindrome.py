def reverse(string):
    string = string[::-1]
    return string


s = input('')

if s == reverse(s):
    print('Palindrome!')
else:
    print('Womp womp, not a palindrome')
