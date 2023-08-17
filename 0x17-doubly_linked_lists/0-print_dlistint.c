#include "lists.h"

/**
 * print_dlistint - This Function prints all
 * the elements of a dlistint_t list.
 *
 * @h: dlistint_t pointer that points to the
 * head of the list.
 * Return: the number of nodes.
 */
size_t print_dlistint(const dlistint_t *h)
{
	int one;

	one = 0;

	if (h == NULL)
	{
		return (one);
	}
	else
	{
		while (h->prev != NULL)
			h = h->prev;

		while (h != NULL)
		{
			printf("%d\n", h->n);
			one++;
			h = h->next;
		}

		return (one);
	}
}
