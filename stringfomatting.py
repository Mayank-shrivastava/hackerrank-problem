def print_formatted(n):
    for i in range(1,n+1):
        width = len(str(bin(n)))-2
        d = str(i).rjust(width,' ')
        o1 = (oct(i)[2:]).rjust(width,' ')
        h1 = (hex(i)[2:]).upper().rjust(width,' ')
    
        b = (bin(i)[2:]).rjust(width,' ')
        ans = "{} {} {} {}".format(d,o1,h1,b)
        print(ans)    
if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
