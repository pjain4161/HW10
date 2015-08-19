
def numbered_lines():
    with open("small.txt", ) as f:        
        list_ = []
        for lines in f:
            list_.append(lines)
                       
    with open("new_small.txt", "w") as f:
        count = 1
        for item in list_:
            f.writelines(str(count) + " " + item )
            count += 1
        
def main():
    numbered_lines()    
    
    
if __name__ == '__main__':
    main()