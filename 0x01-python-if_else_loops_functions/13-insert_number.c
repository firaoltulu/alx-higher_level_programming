#include "lists.h"

/**
 * insert_node - This Function Inserts a number
 * into a sorted singly-linked list.
 * @head: A pointer the head of the linked list.
 * @number: The number to insert.
 *
 * Return: If the function fails - NULL.
 * or a pointer to the new node.
 */
listint_t *insert_node(listint_t **head, int number)
{
    listint_t *node = *head, *six;

    six = malloc(sizeof(listint_t));
    if (six == NULL)
    {
        return (NULL);
    }
    else
    {
        six->n = number;

        if (node == NULL || node->n >= number)
        {
            six->next = node;
            *head = six;
            return (six);
        }

        while (node && node->next && node->next->n < number)
        {
            node = node->next;
        }

        six->next = node->next;
        node->next = six;

        return (six);
    }
}
