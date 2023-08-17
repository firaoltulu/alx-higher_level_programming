#include "lists.h"

/**
 * add_dnodeint_end - This Function adds
 * a new node at the end of a dlistint_t
 * list.
 *
 * @head: dlistint_t pointer that points to
 * the head of the list.
 * @n: Int That Represent value of the element.
 *
 * Return: the address of the new element.
 */
dlistint_t *add_dnodeint_end(dlistint_t **head, const int n)
{
    dlistint_t *three;
    dlistint_t *four;

    four = malloc(sizeof(dlistint_t));
    if (four == NULL)
    {
        return (NULL);
    }
    else
    {
        four->n = n;
        four->next = NULL;

        three = *head;

        if (three != NULL)
        {
            while (three->next != NULL)
                three = three->next;
            three->next = four;
        }
        else
        {
            *head = four;
        }

        four->prev = three;

        return (four);
    }
}