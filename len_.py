def len_list(s):
    count = 0
    for item in s:
        count+=1
    return count

def main():
    a = "abcd"
    b = ['1', '2', '3', '4']
    c = {'a':1, 'b':2}
    d = ('hi',123, [1,2])

    print len_list(a)
    print len_list(b)
    print len_list(c)
    print len_list(d)

if __name__ == '__main__':
    main()
