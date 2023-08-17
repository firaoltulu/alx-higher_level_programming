#include "lists.h"

/**
 * add_dnodeint - This Function adds a new
 * node at the beginning of a dlistint_t
 * list.
 *
 * @head: dlistint_t pointer that points to
 * the head of the list
 * @n: Int that represents a value of the
 * element.
 * Return: the address of the new element
 */
dlistint_t *add_dnodeint(dlistint_t **head, const int n)
{
	dlistint_t *one;
	dlistint_t *two;

	one = malloc(sizeof(dlistint_t));
	if (one == NULL)
	{
		return (NULL);
	}
	else
	{
		one->n = n;
		one->prev = NULL;
		two = *head;

		if (two != NULL)
		{
			while (two->prev != NULL)
				two = two->prev;
		}

		one->next = two;

		if (two != NULL)
			two->prev = one;

		*head = one;

		return (one);
	}
}
