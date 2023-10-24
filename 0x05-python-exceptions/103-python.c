#include <Python.h>
#include <stdio.h>

/**
 * print_python_bytes - Print information about Python bytes objects
 * @p: Pointer to the Python object
 */
void print_python_bytes(PyObject *p)
{
	printf("[.] bytes object info\n");
	printf("  size: %ld\n", (size_t)PyBytes_Size(p));
	printf("  trying string: %s\n", PyBytes_AsString(p));
	printf("  first %ld bytes: ", (size_t)PyBytes_Size(p) < 10 ? (size_t)PyBytes_Size(p) : 10);
	for (size_t i = 0; i < (size_t)PyBytes_Size(p) && i < 10; ++i)
	{
		printf("%02x ", (unsigned char)PyBytes_AsString(p)[i]);
	}
	printf("\n");
}

/**
 * print_python_list - Print information about Python list objects
 * @p: Pointer to the Python object
 */
void print_python_list(PyObject *p)
{
	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", PyList_Size(p));
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);
	for (Py_ssize_t i = 0; i < PyList_Size(p); ++i)
	{
		printf("Element %ld: %s\n", i, Py_TYPE(PyList_GetItem(p, i))->tp_name);
	}
}

/**
 * print_python_float - Print information about Python float objects
 * @p: Pointer to the Python object
 */
void print_python_float(PyObject *p)
{
	printf("[.] float object info\n");
	printf("  value: %f\n", PyFloat_AsDouble(p));
}
