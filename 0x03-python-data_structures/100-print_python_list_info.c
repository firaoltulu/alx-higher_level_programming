#include <stdio.h>
#include <stdlib.h>
#include <Python.h>
/**
 * print_python_list_info - This Function Print
 * some basic info about Python lists.
 * @p: PyObject.
 *
 * Return: Nothing(void).
 */
void print_python_list_info(PyObject *p)
{
	PyObject *two;
	PyListObject *one = (PyListObject *)p;
	int three, four, five;

	four = Py_SIZE(p);
	five = one->allocated;
	printf("[*] Size of the Python List = %d\n", four);
	printf("[*] Allocated = %d\n", five);

	for (three = 0; three < four; three++)
	{
		two = PyList_Gettwo(p, three);
		printf("Element %d: %s\n", three, Py_TYPE(two)->tp_name);
	}
}
