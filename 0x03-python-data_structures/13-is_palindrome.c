#include "lists.h"

/**
 * is_palindrome - function checks if a linked list is a palindrome
 * @head: it's a pointer to a pointer to the head of the linked list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *s_moves = *head, *f_moves = *head, *prev_p = NULL, *temp;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	while (f_moves != NULL && f_moves->next != NULL)
	{
		f_moves = f_moves->next->next;

		temp = s_moves->next;
		s_moves->next = prev_p;
		prev_p = s_moves;
		s_moves = temp;
	}

	if (f_moves != NULL)
		s_moves = s_moves->next;

	while (prev_p != NULL && s_moves != NULL)
	{
		if (prev_p->n != s_moves->n)
			return (0);

		prev_p = prev_p->next;
		s_moves = s_moves->next;
	}

	return (1);
}
