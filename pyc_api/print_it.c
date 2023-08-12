#include <stdio.h>
#include <Python.h>

int print_it(PyObject *op)
{
    PyObject *bytes = pyBytes_FromObject(op);
    char *s = PyBytes_AsString(bytes);

    printf("%s\n",s);
    return(0);
}
