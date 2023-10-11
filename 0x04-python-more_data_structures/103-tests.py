import ctypes

lib = ctypes.CDLL('./libPython3.8.so')
lib.print_python_list.argtypes = [ctypes.py_object]
lib.print_python_bytes.argtypes = [ctypes.py_object]

string1 = b"Hello"
lib.print_python_bytes(string1)

bytes1 = b'\xff\xf8\x00\x00\x00\x00\x00\x00'
lib.print_python_bytes(bytes1)

bytes2 = b'What does the \'b\' character do in front of a string literal?'
lib.print_python_bytes(bytes2)

python_list1 = [b'Hello', b'World']
lib.print_python_list(python_list1)

del python_list1[1]
lib.print_python_list(python_list1)

python_list2 = python_list1 + [4, 5, 6.0, (9, 8), [9, 8, 1024],
                              b"Holberton", "Betty"]

lib.print_python_list(python_list2)

empty_list = []
lib.print_python_list(empty_list)

int_list1 = [0]
lib.print_python_list(int_list1)

int_list2 = [0, 1, 2, 3, 4]
lib.print_python_list(int_list2)

int_list2.pop()
lib.print_python_list(int_list2)

str_list = ["Holberton"]
lib.print_python_list(str_list)
lib.print_python_bytes(str_list)
