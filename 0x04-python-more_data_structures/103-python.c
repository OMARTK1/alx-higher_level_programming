#include <Python.h>
#include <stdio.h>

void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);

/**
 * print_python_list - Prints information about a Python list
 * @p: Pointer to the Python list object
 */
void print_python_list(PyObject *p)
{
	int i, size;

	size = (int)PyList_Size(p);
	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", (int)((PyListObject *)p)->allocated);
	for (i = 0; i < size; i++)
	{
		printf("Element %d: %s\n", i, Py_TYPE(PyList_GetItem(p, i))->tp_name);
		if (PyBytes_Check(PyList_GetItem(p, i)))
			print_python_bytes(PyList_GetItem(p, i));
	}
}

/**
 * print_python_bytes - Prints information about a Python bytes object
 * @p: Pointer to the Python bytes object
 */
void print_python_bytes(PyObject *p)
{
	char *str;
	Py_ssize_t size, i;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	size = PyBytes_Size(p);
	str = PyBytes_AsString(p);

	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", str);

	printf("  first 10 bytes:");
	for (i = 0; i < size && i < 10; ++i)
		printf(" %02x", str[i] & 0xff);
	printf("\n");
}
