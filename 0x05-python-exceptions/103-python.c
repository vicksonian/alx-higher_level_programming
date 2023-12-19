#define PY_SSIZE_T_CLEAN
#include <Python.h>

/**
* print_python_bytes - prints Python bytes information
* @p: Python object
*/
void print_python_bytes(PyObject *p)

{
	Py_ssize_t size, i;
	char *str;

	printf("[.] bytes object info\n");

	if (!PyBytes_Check(p)) {
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	size = PyBytes_Size(p);
	str = PyBytes_AsString(p);

	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", str);

	printf("  first 10 bytes: ");
	for (i = 0; i < size && i < 10; i++)
		printf("%02x%c", (unsigned char)str[i], i == size - 1 || i == 9 ? '\n' : ' ');
}

/**
* print_python_list - prints Python list information
* @p: Python object
*/
void print_python_list(PyObject *p)

{
	Py_ssize_t size, i;
	PyObject *item;

	printf("[*] Python list info\n");

	if (!PyList_Check(p)) {
		printf("  [ERROR] Invalid List Object\n");
		return;
	}

	size = PyList_Size(p);

	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

	for (i = 0; i < size; i++) {
		item = PyList_GetItem(p, i);
		printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
	}
}

/**
* print_python_float - prints Python float information
* @p: Python object
*/

void print_python_float(PyObject *p)
{
	double value;

	printf("[.] float object info\n");

	if (!PyFloat_Check(p)) {
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}

	value = ((PyFloatObject *)p)->ob_fval;
	printf("  value: %f\n", value);
}
