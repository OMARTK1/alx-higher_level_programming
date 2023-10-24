#include <Python.h>
#include <stdio.h>

/**
 * print_python_bytes - Print information about Python bytes objects
 * @p: Pointer to the Python object
 */
void print_python_bytes(PyObject *p)
{
	PyBytesObject *bytes = (PyBytesObject *)p;

	printf("[.] bytes object info\n");

	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	Py_ssize_t size = PyBytes_Size(p);
	char *data = bytes->ob_sval;

	printf("  size: %ld\n", size);
	printf("  first %ld bytes: ", size < 10 ? size : 10);

	for (Py_ssize_t i = 0; i < size && i < 10; ++i)
	{
		printf("%02x ", (unsigned char)data[i]);
	}
	printf("\n");
}

/**
 * print_python_list - Print information about Python list objects
 * @p: Pointer to the Python object
 */
void print_python_list(PyObject *p)
{
	PyListObject *list = (PyListObject *)p;

	printf("[*] Python list info\n");

	if (!PyList_Check(p))
	{
		printf("  [ERROR] Invalid List Object\n");
		return;
	}

	printf("[*] Size of the Python List = %ld\n", PyList_Size(p));
	printf("[*] Allocated = %ld\n", list->allocated);

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

	if (!PyFloat_Check(p))
	{
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}

	printf("  value: %f\n", PyFloat_AsDouble(p));
}
