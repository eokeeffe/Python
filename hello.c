#include "C:\Python27\include\Python.h"

/*
python setup.py build
gcc -c nameOfModule.c
gcc -shared nameOfModule.o -L/Python27/libs -lpython27 -o nameOfModule.dll

python setup.py build --compiler=mingw32
python setup.py install
*/
 
static PyObject* say_hello(PyObject* self, PyObject* args)
{
    const char* name;
 
    if (!PyArg_ParseTuple(args, "s", &name))
        return NULL;
 
    printf("Hello %s!\n", name);
 
    Py_RETURN_NONE;
}
 
static PyMethodDef HelloMethods[] =
{
     {"say_hello", say_hello, METH_VARARGS, "Greet somebody."},
     {NULL, NULL, 0, NULL}
};
 
PyMODINIT_FUNC
 
inithello(void)
{
     (void) Py_InitModule("hello", HelloMethods);
}