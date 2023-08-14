#include "lists.h"

listint_t *local_reverse_listint(listint_t **head);
int is_palindrome(listint_t **head);

/**
 * is_palindrome - Checks if a singly linked list is a palindrome.
 * @head: A pointer to the head of the linked list.
 *
 * Return: If the linked list is not a palindrome - 0.
 *         If the linked list is a palindrome - 1.
 */
int is_palindrome(listint_t **head)
{
	listint_t *one, *two, *three;
	size_t four = 0, i;

	if (*head == NULL || (*head)->next == NULL)
	{
		return (1);
	}
	else
	{
		one = *head;
		while (one)
		{
			four++;
			one = one->next;
		}

		one = *head;
		for (i = 0; i < (four / 2) - 1; i++)
			one = one->next;

		if ((four % 2) == 0 && one->n != one->next->n)
		{
			return (0);
		}
		else
		{
			one = one->next->next;
			two = local_reverse_listint(&one);
			three = two;

			one = *head;
			while (two)
			{
				if (one->n != two->n)
				{
					return (0);
				}
				else
				{
					one = one->next;
					two = two->next;
				}
			}
			local_reverse_listint(&three);

			return (1);
		}
	}
}

/**
 * local_reverse_listint - This Function Reverses
 * a singly-linked listint_t list.
 * @one: A Douuble pointer that points to the
 * starting node of the list to reverse.
 *
 * Return: A pointer to the head of the reversed list.
 */
listint_t *local_reverse_listint(listint_t **one)
{
	listint_t *two = *one, *three, *four = NULL;

	while (two)
	{
		three = two->next;
		two->next = four;
		four = two;
		two = three;
	}

	*one = four;
	return (*one);
}
