#include "lists.h"

/**
 * sum_dlistint - This Function returns
 * the sum of all the data in property
 * int (n) of a doubly linked list.
 *
 * @head: dlistint_t pointer that points
 * to the head of the list.
 *
 * Return: int that represent the sum of
 * the data.
 */
int sum_dlistint(dlistint_t *head)
{
    int one = 0;

    if (head != NULL)
    {
        while (head->prev != NULL)
            head = head->prev;

        while (head != NULL)
        {
            one += head->n;
            head = head->next;
        }
    }

    return (one);
}
