def reverse(x: int) -> int:
    x = reversed(str(x))
    joined = "".join(list(x))
    if joined.endswith("-"):
        joined = "-" + joined[0:-1]
    if int(joined).bit_length() > 31:
        return 0
    return(int(joined))

if __name__ == '__main__':
    print(reverse(123))
    print(reverse(-123))
    print(reverse(120))
    print(reverse(1534236469))
    
### Solved
    