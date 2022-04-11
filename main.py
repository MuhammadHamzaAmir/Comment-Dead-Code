
import os
import re

def get_dead_methods(class_file_path,usage_file_path):
    """
    The get_dead_methods function takes a class file path and usage file path as arguments. 
    It returns a list of all the methods that are not used in any of the classes.
    
    :param class_file_path: Used to Specify the path to the class file.
    :param usage_file_path: Used to Specify the path to the usage file.
    :return: A list of all the methods that are not used in the code.
    
    :doc-author: Trelent
    """
    res = os.popen("vulture"+" "+class_file_path+" "+usage_file_path).read()
    return res

def get_methods_names_lines_numbers(dead_methods):
    dict = {}
    dead_methods_list = dead_methods.split('\n')
    dead_methods_list.pop()

    if len(dead_methods_list) < 1:
        raise Exception("No dead code found")
    num_regex = re.compile(":[0-9]+:")
    method_regex = re.compile("\'.*\'")

    for i in dead_methods_list:

        if (i.find("method")) != -1:
            method_name = method_regex.search(i)
            method_line = num_regex.search(i)
            dict[method_line.group()[1:-1]] = method_name.group()[1:-1]

    if len(dict)<0:
        raise Exception("No dead methods found")
    return dict







p = get_dead_methods("mc.py","user.py")

q = get_methods_names_lines_numbers(p)
print(q)

