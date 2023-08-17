#include "lists.h"

/**
 * delete_dnodeint_at_index - This Function deletes
 * the node at index of a dlistint_t linked list.
 *
 * @head: dlistint_t pointer that points to the head
 * of the list.
 * @index: int that represent the index of the new
 * node.
 * 
 * Return: 1 if it succeeded, -1 if it failed.
 */
int delete_dnodeint_at_index(dlistint_t **head, unsigned int index)
{
	dlistint_t *six;
	dlistint_t *one;
	unsigned int two;

	six = *head;

	if (six != NULL)
		while (six->prev != NULL)
			six = six->prev;

	two = 0;

	while (six != NULL)
	{
		if (two == index)
		{
			if (two == 0)
			{
				*head = six->next;
				if (*head != NULL)
					(*head)->prev = NULL;
			}
			else
			{
				one->next = six->next;

				if (six->next != NULL)
					six->next->prev = one;
			}

			free(six);
			return (1);
		}
		one = six;
		six = six->next;
		two++;
	}

	return (-1);
}
