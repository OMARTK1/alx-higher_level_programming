#include <Python.h>

/**
 * print_python_list_info - function prints basic information
 *				about a Python list object
 * @pt: it's a pointer to the Python list object
 */
void print_python_list_info(PyObject *pt)
{
	Py_ssize_t size, allocated, i;
	PyObject *item;

	size = PyList_Size(pt);
	allocated = ((PyListObject *)pt)->allocated;

	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", allocated);

	for (i = 0; i < size; ++i)
	{
		item = PyList_GetItem(pt, i);
		printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
	}
}
