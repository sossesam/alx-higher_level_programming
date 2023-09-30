#include <Python.h>

void print_python_string(PyObject *p)
{
    if (!PyUnicode_Check(p)) {
        printf("[.] string object info\n");
        printf("  [ERROR] Invalid String Object\n");
        return;
    }

    Py_ssize_t length = PyUnicode_GET_LENGTH(p);
    Py_ssize_t size = PyUnicode_KIND(p);

    printf("[.] string object info\n");
    printf("  type: %s\n", (size == PyUnicode_1BYTE_KIND) ? "compact ascii" : "compact unicode object");
    printf("  length: %ld\n", length);
    printf("  value: %s\n", PyUnicode_AsUTF8(PyUnicode_FromObject(p)));
}
