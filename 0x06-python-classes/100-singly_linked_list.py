#!/usr/bin/python3
"""
This module demonstrates the implementation of a Singly Linked List
"""

class Node:
    """
    Implementation of a Node within a SinglyLinkedList

    Attributes:
        data (int): The integer data within a Node
        next_node (Node): The next Node in the list
    """
    def __init__(self, data, next_node=None):
        """Initialization of a Node

        Args:
            self (Node): The Node instance
            data (int): The data within a Node
            next_node (Node): Pointer to the next Node in the list
        """
        if type(data) != int:
            raise TypeError("data must be an integer")
        if (type(next_node) != Node) and (next_node != None):
            raise TypeError("next_node must be a Node object")
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        """
        Getter for private __data attribute

        Args:
           self (Node): The square instance

        Returns:
           The data within the Node
        """
        return self.__data

    @data.setter
    def data(self, value):
        """
        The setter for private __data attribute

        Args:
            self (Node): The Node instance
            value (int): The value to set private __data attribute to

        Returns:
            None
        """
        if type(value) != int:
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """
        Getter for private __next_node attribute

        Args:
           self (Node): The Node instance

        Returns:
           The next node in the list or None if there is no next node
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        The setter for private __next_node attribute

        Args:
            self (Node): The Node instance
            value (Node): The value to set private __next_node attribute to

        Returns:
            None
        """
        if (type(value) != Node) and (value != None):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value

class SinglyLinkedList:
    """
    Implementation of a SinglyLinkedList

    Attributes:
        __head (Node): The head of the SinglyLinkedList
    """
    def __init__(self):
        """Initialization of a SinglyLinkedList

        Args:
            self (SinglyLinkedList): The SinglyLinkedList instance
        """
        self.__head = None

    def __repr__(self):
        """String representation of SinglyLinkedList instance

        Args:
            self (SinglyLinkedList): The SinglyLinkedList instance
        """
        list_rep = []
        current = self.__head
        while current:
            list_rep.append(str(current.data))
            if current.next_node:
                list_rep.append("\n")
            current = current.next_node
        return "".join(list_rep)

    def __str__(self):
        """String representation of SinglyLinkedList instance

        Args:
            self (SinglyLinkedList): The SinglyLinkedList instance
        """
        list_rep = []
        current = self.__head
        while current:
            list_rep.append(str(current.data))
            if current.next_node:
                list_rep.append("\n")
            current = current.next_node
        return "".join(list_rep)

    def sorted_insert(self, value):
        head = self.__head
        new_node = Node(value)

        if head == None:
            self.__head = new_node
            return
        current = head.next_node
        if current == None:
            if new_node.data <= head.data:
                new_node.next_node = head
                self.__head = new_node
            else:
                head.next_node = new_node
            return
        current = self.__head
        while current:
            previous = current
            current = current.next_node
            if current == None:
                previous.next_node = new_node
                return
            if current.data <= new_node.data:
                continue
            previous.next_node = new_node
            new_node.next_node = current
            return
