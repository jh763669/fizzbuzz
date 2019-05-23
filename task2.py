import os
import task1.py

def get_file(root_path,all_files=[]):
    files = os.listdir(root_path)
    for file in files:
        if not os.path.isdir(root_path + '/' + file):  
            all_files.append(root_path + '/' + file)
        else:  
            get_file((root_path+'/'+file),all_files)
    return all_files

path = '/Users/misakamikoto/Downloads/fizzbuzz-yourname'
file_list = get_file(path)
file_dict = {}
for file in file_list:
    file_split = file.split('/')
    temp = file_split[-1]
    if file_split[-1] == '.DS_Store':
        continue
    if file_split[-2] not in file_dict:
        file_dict[file_split[-2]] = [file_split[-1]]
    else:
        file_dict[file_split[-2]].append(temp)
print(file_dict)

fin = open('file.list','a')
for file in file_list:
    file_split = file.split('/')
    temp1 = file_split[-1]
    temp2 = file_split[-2]
    if file_split[-1] == '.DS_Store':
        continue
    fin.write(file_split[-1])
    fin.write(' - ')
    fin.write(file_split[-2])
    fin.write(' - ')
    fin.write(str(len(file_split[-1])+len(file_split[-2])))
    fin.write('\n')
fin.close()

