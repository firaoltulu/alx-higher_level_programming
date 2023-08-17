#include "lists.h"

/**
 * get_dnodeint_at_index - This Function returns
 * the nth node of a dlistint_t linked list.
 *
 * @head: dlistint_t pointer that points to head
 * of the list.
 * @index: int that represent the index of the
 * node to search for, starting from 0.
 *
 * Return: the nth node or null.
 **/
dlistint_t *get_dnodeint_at_index(dlistint_t *head, unsigned int index)
{
	unsigned int two;
	dlistint_t *six;

	two = 0;
	if (head == NULL)
	{
		return (NULL);
	}
	else
	{
		six = head;
		while (six)
		{
			if (index == two)
				return (six);
			two++;
			six = six->next;
		}
		return (NULL);
	}
}
