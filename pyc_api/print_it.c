#include <stdio.h>
#include "Python.h"

int print_it(PyObject *op)
{
    PyObject *bytes = PyBytes_FromObject(op);
    Py_ssize_t len = PyBytes_Size(bytes);
    Py_ssize_t i = 0;

    char *s = PyBytes_AsString(bytes);

    for(i = 0; i < len; i++){
        printf("%c",s[i]);
    }
    return(0);
}
