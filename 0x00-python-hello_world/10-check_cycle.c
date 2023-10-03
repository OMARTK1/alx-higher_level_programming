#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

/**
 * check_cycle - function checks if a singly linked list has a cycle in it
 * @list: it's a pointer to the head of the linked list
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *slow_move = list, *fast_move = list;

	while (slow_move && fast_move && fast_move->next)
	{
		slow_move = slow_move->next;
		fast_move = fast_move->next->next;

		if (slow_move == fast_move)
			return (1);
	}

	return (0);
}
