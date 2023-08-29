#!/usr/bin/python3

class Node:
    """This class Represent a node in a singly-linked list."""

    def __init__(self, data, next_node=None):
        """This Method Initialize a new Node.

        Arguments:
            data (int): Int that contains
                        The data of the new Node.
            next_node (Node): The next node of the new Node.
                              Default to None.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """This method Get/set the data of the Node."""
        return (self.__data)

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """This method Get/set the next_node of the Node."""
        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value

class SinglyLinkedList:
    """This class Represent a singly-linked list."""

    def __init__(self):
        """This Method Initalize a new SinglyLinkedList."""
        self.__head = None

    def sorted_insert(self, value):
        """This Method Insert a new Node to the SinglyLinkedList.

        The node is inserted into the list at the correct
        ordered numerical position.

        Args:
            value (Node): Node type that contains The new Node
                          To insert.
        """
        one = Node(value)
        if self.__head is None:
            one.next_node = None
            self.__head = one
        elif self.__head.data > value:
            one.next_node = self.__head
            self.__head = one
        else:
            two = self.__head
            while (two.next_node is not None and
                    two.next_node.data < value):
                two = two.next_node
            one.next_node = two.next_node
            two.next_node = one

    def __str__(self):
        """This Method Define the print() representation of a SinglyLinkedList."""
        two = []
        one = self.__head
        while one is not None:
            two.append(str(one.data))
            one = one.next_node
        return ('\n'.join(two))

