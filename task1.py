import re

def l33t(line):
        line = re.sub('er','xor',line)
        line_new = line.replace('o','0').replace('O','0').replace('a','4').replace('A','4').replace('e','3').replace('E','3').replace('i','1').replace('I','1')
        return line_new


temp = 1
while temp == 1:
    try:
        filename_input = input('file name:')
        fin = open(filename_input)
    except:
        print('no this file')
    else:
        temp = 2
page = input('input page:')



t = 1
while t == 1:
    if page == '1':
        sum = 1
        fin1 = open(filename_input,'r')
        line = fin1.readline()
        line.strip()
        line_new = l33t(line)
        #print(line,end='')
        fin2 = open('output.txt','a')
        fin2.write(line_new)
        fin2.close()
        #print(line_new)
        for line in fin1:
            if sum < 25:
                #print(line,end='')
                line_new = l33t(line)
                fin2 = open('output.txt','a')
                fin2.write(line_new)
                sum += 1
                fin2.close()
            else:
                break
            
    elif page != 1:
        sum = 0
        fin1 = open(filename_input,'r')
        line = fin1.readline()
        page_page = 24 + (int(page)-2)*25
        for i in range(page_page):
            line = fin1.readline()
        for line in fin1:
            if sum < 25:
                #print(line,end='')
                line_new = l33t(line)
                fin2 = open('output.txt','a')
                fin2.write(line_new)
                sum += 1
                fin2.close()
            else:
                break
    while True:
        judge = input('do you want to continue? (y/n)')
        if judge == 'y':
            page = input('input page:')
            break
        elif judge == 'n':
            t = 2
            break
        else:
            print('error input')
