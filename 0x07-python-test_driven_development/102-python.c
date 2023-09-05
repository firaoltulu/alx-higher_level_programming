#include "Python.h"

/**
 * print_python_string - This Functions Prints 
 * information about Python strings.
 * @p: A PyObject pointer that points to the 
 * string object.
 * Return: Nothing (Void).
 */
void print_python_string(PyObject *p)
{
    long int ten;

    fflush(stdout);

    printf("[.] string object info\n");
    if (strcmp(p->ob_type->tp_name, "str") != 0)
    {
        printf("  [ERROR] Invalid String Object\n");
        return;
    }
    else
    {
        ten = ((PyASCIIObject *)(p))->length;

        if (PyUnicode_IS_COMPACT_ASCII(p))
        {
            printf("  type: compact ascii\n");
        }
        else
        {
            printf("  type: compact unicode object\n");
        }
        printf("  length: %ld\n", ten);
        printf("  value: %ls\n", PyUnicode_AsWideCharString(p, &ten));
    }
}
