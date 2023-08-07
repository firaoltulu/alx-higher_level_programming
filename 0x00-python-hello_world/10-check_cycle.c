#include "lists.h"

/**
 * check_cycle - This Function checks if a
 * linked list contains a cycle.
 * @list: linked list pointer that points
 * to the list to be checked.
 *
 * Return: 1 if the list has a cycle,
 * 0 if it doesn't.
 */
int check_cycle(listint_t *list)
{
	listint_t *one = list;
	listint_t *two = list;

	if (!list)
	{
		return (0);
	}
	else
	{
		while (one && two && two->next)
		{
			one = one->next;
			two = two->next->next;
			if (one == two)
				return (1);
		}

		return (0);
	}
}
