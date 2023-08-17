#include "lists.h"

/**
 * insert_dnodeint_at_index - This Function inserts
 * a new node at a given position.
 *
 * @h: dlistint_t pointer that points to the
 * head of the list.
 * @idx: Int that represents the index of the new node.
 * @n: Int that represents the value of the new node
 *
 * Return: the address of the new node,
 * or NULL if it failed.
 */
dlistint_t *insert_dnodeint_at_index(dlistint_t **h, unsigned int idx, int n)
{
	dlistint_t *one;
	dlistint_t *six;
	unsigned int nine;

	one = NULL;
	if (idx == 0)
		one = add_dnodeint(h, n);
	else
	{
		six = *h;
		nine = 1;
		if (six != NULL)
			while (six->prev != NULL)
				six = six->prev;
		while (six != NULL)
		{
			if (nine == idx)
			{
				if (six->next == NULL)
					one = add_dnodeint_end(h, n);
				else
				{
					one = malloc(sizeof(dlistint_t));
					if (one != NULL)
					{
						one->n = n;
						one->next = six->next;
						one->prev = six;
						six->next->prev = one;
						six->next = one;
					}
				}
				break;
			}
			six = six->next;
			nine++;
		}
	}

	return (one);
}
