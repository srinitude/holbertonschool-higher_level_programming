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
 * print_hex_string - Prints the hex value of the PyBytesObject's string
 * @size: Size of the object
 * @str: The PyBytesObject's string
 *
 * Return: None
 */
void print_hex_string(Py_ssize_t size, char *str)
{
	Py_ssize_t i;

	if (size > 10)
	{
		printf("first 10 bytes: ");
		for (i = 0; i < 10; i++)
		{
			if (i != 9)
				printf("%2x ", str[i]);
			else
				printf("%2x\n", str[i]);
		}
	}
	else
	{
		if (size == 10)
			printf("  first 10 bytes: ");
		else
			printf("  first %li bytes: ", size + 1);
		for (i = 0; i < size; i++)
		{
			if (i != (size - 1))
				printf("%2x ", str[i]);
			else
				printf("%2x", str[i]);
		}
		if (i == 10)
			printf("\n");
		else
			printf(" 00\n");
	}
}

/**
 * print_python_bytes - Prints info about a PyBytesObject
 * @p: The PyObject
 *
 * Return: None
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t size;
	char *str = NULL;

	if (!p)
		return;
	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	size = PyBytes_Size(p);
	str = PyBytes_AsString(p);

	printf("  size: %li\n", size);
	printf("  trying string: %s\n", str);
	print_hex_string(size, str);
}

/**
 * print_python_list - Prints info about a PyListObject
 * @p: The PyObject
 *
 * Return: None
 */
void print_python_list(PyObject *p)
{
	PyListObject *list = NULL;
	PyObject *object = NULL;
	PyTypeObject *type = NULL;
	Py_ssize_t i, list_length, num_allocated;

	if (!p || !PyList_Check(p))
		return;

	list_length = compute_list_length(p);
	num_allocated = number_of_allocated_elements(p);
	list = (PyListObject *)p;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %li\n", list_length);
	printf("[*] Allocated = %li\n", num_allocated);
	for (i = 0; i < list_length; i++)
	{
		object = list->ob_item[i];
		type = object->ob_type;
		printf("Element %li: %s\n", i, type->tp_name);
		if (!strcmp(type->tp_name, "bytes"))
			print_python_bytes(object);
	}
}
