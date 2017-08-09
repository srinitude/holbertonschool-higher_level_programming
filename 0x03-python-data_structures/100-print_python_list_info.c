#include "Python.h"

/**
 * compute_list_length - Computes the length of a list
 * @p: The PyObject
 *
 * Return: Length of the list
 */
Py_ssize_t compute_list_length(PyObject *p)
{
	Py_ssize_t len;

	if (p)
		len = PyList_Size(p);
	else
		len = 0;
	return (len);
}

/**
 * number_of_allocated_elements - Number of allocated elements in list
 * @p: The PyObject
 *
 * Return: Number of allocated elements
 */
Py_ssize_t number_of_allocated_elements(PyObject *p)
{
	PyListObject *list = NULL;

	list = (PyListObject *)p;
	return (list->allocated);
}

/**
 * print_python_list_info - Prints info about a PyListObject
 * @p: The PyObject
 *
 * Return: None
 */
void print_python_list_info(PyObject *p)
{
	PyListObject *list = NULL;
	PyTypeObject *type = NULL;
	Py_ssize_t i, list_length, num_allocated;

	if (!p || !PyList_Check(p))
		return;
	list_length = compute_list_length(p);
	num_allocated = number_of_allocated_elements(p);
	list = (PyListObject *)p;
	printf("[*] Size of the Python List = %li\n", list_length);
	printf("[*] Allocated = %li\n", num_allocated);
	for (i = 0; i < list_length; i++)
	{
		type = list->ob_item[i]->ob_type;
		printf("Element %li: %s\n", i, type->tp_name);
	}
}
