#include "lists.h"

/**
 * dlistint_len - This Function returns
 * the number of elements in a double
 * linked list.
 *
 * @h: dlistint_t pointer that points to
 * the head of the list.
 * Return: the number of nodes.
 */
size_t dlistint_len(const dlistint_t *h)
{
	int two;

	two = 0;

	if (h == NULL)
	{
		return (two);
	}
	else
	{
		while (h->prev != NULL)
			h = h->prev;

		while (h != NULL)
		{
			two++;
			h = h->next;
		}

		return (two);
	}
}
