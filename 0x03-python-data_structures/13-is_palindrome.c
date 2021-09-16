#include "lists.h"

/**
 * is_palindrome - checks if a linked list is a palindrome
 * @head: a pointer to the starting node of the list
 *
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	int i = 0, count = 0, j;
	listint_t *start, *end, *temp = *head;

	while (temp)
	{
		temp = temp->next;
		count++;
	}

	while (i != count / 2)
	{
		start = end = *head;
		for (j = 0; j < i; j++)
			start = start->next;

		for (j = 0; j < count - (i + 1); j++)
			end = end->next;

		if (start->n != end->n)
			return (0);
		i++;
	}

	return (1);
}

