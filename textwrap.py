


def wrap(string, max_width):
    c = [string[i:i+max_width] for i in range(0,len(string),max_width)]
    return '\n'.join(c)
        
    


    

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
