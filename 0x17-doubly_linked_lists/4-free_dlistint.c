#include "lists.h"

/**
 * free_dlistint - This Function frees
 * a dlistint_t list.
 *
 * @head:dlistint_t pointer that points
 * to head of the list.
 *
 * Return: Nothing(Void).
 **/
void free_dlistint(dlistint_t *head)
{
	if (head == NULL)
	{
		return;
	}
	else
	{
		while (head->next)
		{
			head = head->next;
			free(head->prev);
		}
		free(head);
	}
}
