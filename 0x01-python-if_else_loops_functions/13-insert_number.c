#include "lists.h"
#include <stdlib.h>

/**
 * insert_node - function inserts a number into a sorted singly linked list
 * @head: it's a pointer to pointer of the first node of that list
 * @number: the number to be inserted
 * Return: the address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *newest_node, *acctual, *before;

	newest_node = malloc(sizeof(listint_t));
	if (newest_node == NULL)
		return (NULL);

	newest_node->n = number;
	newest_node->next = NULL;

	acctual = *head;
	before = NULL;

	while (acctual != NULL && acctual->n < number)
	{
		before = acctual;
		acctual = acctual->next;
	}

	if (before == NULL)
	{
		newest_node->next = *head;
		*head = newest_node;
	}
	else
	{
		prev->next = newest_node;
		newest_node->next = acctual;
	}

	return (newest_node);
}

