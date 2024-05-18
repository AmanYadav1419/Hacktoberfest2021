def swap_case(s):
    return "".join(
        (let.lower()) if (let.isupper() == True) else (let.upper())
        for let in s
    )

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
