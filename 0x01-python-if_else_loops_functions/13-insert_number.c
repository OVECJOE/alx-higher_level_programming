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
	listint_t *temp, *new;

	/* Creating a new node */
	new = malloc(sizeof(listint_t));
	if (!new)
		return (NULL);

	new->n = number;
	new->next = NULL;

	if (!*head || number <= (*head)->n)
	{
		new->next = *head;
		*head = new;
		return (new);
	}
	else
	{
		temp = *head;
		while (temp->next && number > temp->next->n)
			temp = temp->next;

		new->next = temp->next;
		temp->next = new;
		return (new);
	}

	return (NULL);
}
