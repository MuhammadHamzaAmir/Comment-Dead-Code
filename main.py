import os
import re


def get_dead_methods(class_file_path:str,usage_file_path:str) -> str:
    """
    The get_dead_methods function takes a class file path and usage file path as input. 
    It returns the names of all methods that are not invoked in the usage file, 
    as well as their return types. The returned value is a string with one method per line, 
    in alphabetical order by method name.
    
    :param class_file_path:str: Used to Specify the path to the class file.
    :param usage_file_path:str: Used to Specify the path to the usage file.
    :return: A string containing the names of all methods that are never called.
    
    :doc-author: Trelent
    """
    res = os.popen("vulture"+" "+class_file_path+" "+usage_file_path).read()
    return res




def get_dead_methods_names_lines_numbers(dead_methods:str) -> dict:
    """
    The get_dead_methods_names_lines_numbers function takes in a string of dead code and returns a dictionary with the line numbers as keys and method names as values.
    
    :param dead_methods:str: Used to Pass the string of dead methods to the function.
    :return: A dictionary with the lines numbers of the dead code as keys and their method names as values.
    
    :doc-author: Trelent
    """
    dict = {}
    dead_methods_list = dead_methods.split('\n')
    dead_methods_list.pop()

    num_regex = re.compile(":[0-9]+:")
    method_regex = re.compile("\'.*\'")

    for i in dead_methods_list:

        if (i.find("method")) != -1:
            method_name = method_regex.search(i)
            method_line = num_regex.search(i)
            dict[method_line.group()[1:-1]] = method_name.group()[1:-1]
    return dict



def comment_dead_methods(dictionary:dict,file_path:str) -> None:
    """
    The comment_dead_methods function takes a dictionary of methods and their line numbers in the file,
    and comments out all lines between the method definition and the end of that method.
    
    :param dictionary:dict: Used to Store the line numbers of all methods that are to be commented.
    :param file_path:str: Used to Specify the file that is being read from.
    :return: None.
    
    :doc-author: Trelent
    """
    if len(dictionary)<1:
        print("No dead methods found")
        return None
    
    file = open(file_path,'r')
    lines = file.readlines()
    file.close()

    current_line_num = 0
    indent_index = 0
    indent_check = int(next(iter(dictionary)))
    indent_index = lines[indent_check-1].find('def')

    string_exp = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ._(){[]}0123456789+-*/%&^"

    for i, (k, v) in enumerate(dictionary.items()):
        current_line_num = int(k)-1

        out_method = False
        while(current_line_num < len(lines)):
            current_line = lines[current_line_num]

            if (current_line_num != (int(k)-1)):
                for i in range(indent_index+1):

                    if (len(current_line)>i):
                        if current_line[i] in string_exp:
                            out_method = True
                            break
            
            if out_method:
                break
            
            current_line = "#"+current_line
            lines[current_line_num] = current_line
            current_line_num += 1
    
    file = open(file_path,'w')
    file.writelines(lines)
    file.close()

            
            






import time
t1 = time.time()
p = get_dead_methods("mc.py","user.py")

q = get_dead_methods_names_lines_numbers(p)
comment_dead_methods(q,"mc.py")
t2 = time.time()
print(t2-t1,q)


