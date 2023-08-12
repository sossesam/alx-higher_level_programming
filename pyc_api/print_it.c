#include <stdio.h>
#include <python2.7/Python.h>

int print_it(PyObject *op)
{
    PyListObject *arr;

    arr = (PyListObject *)op;

    printf("[*] Size of the Python List = %ld\n", arr->ob_size);
    printf("[*] Allocated = %ld\n", arr->allocated);

    return(0);
}
