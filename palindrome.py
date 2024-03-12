def is_palindrome(teststr):
    # teststr = [c for c in teststr.lower() if c.isalnum()]
    # return teststr == teststr[::-1]
    left, right = 0, len(teststr) - 1
    while left <= right:
        if not teststr[left].isalnum():
            left += 1
        elif not teststr[right].isalnum():
            right -= 1
        elif teststr[left].lower() != teststr[right].lower():
            return False
        else:
            left += 1
            right -= 1
    return True


def main():
    print("Is 'radar' a palindrome?", is_palindrome("radar"))
    print("Is 'hello' a palindrome?", is_palindrome("hello"))


if __name__ == "__main__":
    main()
