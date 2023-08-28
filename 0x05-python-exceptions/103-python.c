#include <Python.h>

void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);
void print_python_float(PyObject *p);

/**
 * print_python_list - This Function Prints basic
 * info about Python lists.
 *
 * @p: PyObject pointer that points to the
 * PyObject list object.
 *
 * Return: Nothing(Void).
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t one, two, three;
	const char *four;
	PyListObject *five = (PyListObject *)p;
	PyVarObject *six = (PyVarObject *)p;

	one = six->ob_size;
	two = five->allocated;

	fflush(stdout);

	printf("[*] Python list info\n");
	if (strcmp(p->ob_type->tp_name, "list") != 0)
	{
		printf("  [ERROR] Invalid List Object\n");
		return;
	}
	else
	{
		printf("[*] Size of the Python List = %ld\n", one);
		printf("[*] Allocated = %ld\n", two);

		for (three = 0; three < one; three++)
		{
			four = five->ob_item[three]->ob_type->tp_name;
			printf("Element %ld: %s\n", three, four);

			if (strcmp(four, "bytes") == 0)
			{
				print_python_bytes(five->ob_item[three]);
			}
			else if (strcmp(four, "float") == 0)
			{
				print_python_float(five->ob_item[three]);
			}
		}
	}
}

/**
 * print_python_bytes - This Function Prints basic
 * info about Python byte objects.
 *
 * @p: PyObject pointer that points to the
 * PyObject byte object.
 *
 * Return: Nothing(Void).
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t one, two;
	PyBytesObject *three = (PyBytesObject *)p;

	fflush(stdout);

	printf("[.] bytes object info\n");
	if (strcmp(p->ob_type->tp_name, "bytes") != 0)
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	else
	{
		printf("  size: %ld\n", ((PyVarObject *)p)->ob_size);
		printf("  trying string: %s\n", three->ob_sval);

		if (((PyVarObject *)p)->ob_size >= 10)
		{
			one = 10;
		}
		else
		{
			one = ((PyVarObject *)p)->ob_size + 1;
		}
		printf("  first %ld bytes: ", one);

		for (two = 0; two < one; two++)
		{
			printf("%02hhx", three->ob_sval[two]);
			if (two == (one - 1))
			{
				printf("\n");
			}
			else
			{
				printf(" ");
			}
		}
	}
}

/**
 * print_python_float - This Function Prints
 * basic info about Python float objects.
 * @p: PyObject pointer that points to the A
 * PyObject float object.
 *
 * Return: Nothing(Void).
 *
 */
void print_python_float(PyObject *p)
{
	char *one = NULL;

	PyFloatObject *two = (PyFloatObject *)p;

	fflush(stdout);

	printf("[.] float object info\n");
	if (strcmp(p->ob_type->tp_name, "float") != 0)
	{
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}
	else
	{
		one = PyOS_double_to_string(two->ob_fval, 'r', 0,
				Py_DTSF_ADD_DOT_0, NULL);
		printf("  value: %s\n", one);
		PyMem_Free(one);
	}
}
