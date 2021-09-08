#include "lists.h"
#include <stdlib.h>

/**
 * insert_node - inserts a number into a sorted singly linked list
 * @head: a pointer to the first node in the list
 * @number: The position where the node is to be inserted
 *
 * Return: The address of the new node, else NULL
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *temp, *start, *new;

	start = *head;

	if (!start)
		return (NULL);

	/* Creating a new node */
	new = malloc(sizeof(listint_t));
	if (!new)
		return (NULL);

	new->n = number;
	new->next = NULL;

	/* Trying to insert the node at expected position */
	while (start && start->next)
	{
		temp = start;
		start = start->next;
		if (number < start->n)
		{

			temp->next = new;
			new->next = start;
			break;
		}
	}

	return (new);
}
