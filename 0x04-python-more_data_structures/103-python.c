#include <stdio.h>
#include <Python.h>

/**
 * print_python_bytes - This Function Prints
 * bytes information.
 *
 * @p: Python Object
 *
 * Return: Nothing(Void).
 */
void print_python_bytes(PyObject *p)
{
	char *one;
	long int two, three, four;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	two = ((PyVarObject *)(p))->ob_size;
	one = ((PyBytesObject *)p)->ob_sval;

	printf("  size: %ld\n", two);
	printf("  trying one: %s\n", one);

	if (two >= 10)
		four = 10;
	else
		four = two + 1;

	printf("  first %ld bytes:", four);

	for (three = 0; three < four; three++)
		if (one[three] >= 0)
			printf(" %02x", one[three]);
		else
			printf(" %02x", 256 + one[three]);

	printf("\n");
}

/**
 * print_python_list - This Function
 * Prints list information.
 *
 * @p: Python Object.
 *
 * Return: Nothing(Void).
 */
void print_python_list(PyObject *p)
{
	long int one, two;
	PyListObject *three;
	PyObject *four;

	one = ((PyVarObject *)(p))->ob_size;
	three = (PyListObject *)p;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", one);
	printf("[*] Allocated = %ld\n", three->allocated);

	for (two = 0; two < one; two++)
	{
		four = ((PyListObject *)p)->ob_item[two];
		printf("Element %ld: %s\n", two, ((four)->ob_type)->tp_name);
		if (PyBytes_Check(four))
			print_python_bytes(four);
	}
}
