#include <stddef.h>
#include "lists.h"

/**
 * reverse_list - function reverses a linked list
 * @head: it's a pointer to the head of the linked list
 * Return: the pointer to the new head of the reversed linked list
 */
listint_t *reverse_list(listint_t *head)
{
	listint_t *prev_h = NULL, *current_h = head, *next = NULL;

	while (current_h != NULL)
	{
		next = current_h->next;
		current_h->next = prev_h;
		prev_h = current_h;
		current_h = next;
	}
	return (prev_h);
}

/**
 * is_palindrome - function checks if a linked list is a palindrome
 * @head: it's a pointer to a pointer to the head of the linked list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	if (*head == NULL || (*head)->next == NULL)
		return (1);

	listint_t *slow_p = *head, *fast_p = *head, *prev_slow_p = *head;
	listint_t *second_half_list, *first_half_list;
	int is_palindrome = 1;

	while (fast_p != NULL && fast_p->next != NULL)
	{
		fast_p = fast_p->next->next;
		prev_slow_p = slow_p;
		slow_p = slow_p->next;
	}
	if (fast_p != NULL)
	{
		slow_p = slow_p->next;
	}
	second_half_list = reverse_list(slow_p);
	first_half_list = *head;

	while (second_half_list != NULL)
	{
		if (first_half_list->n != second_half_list->n)
		{
			is_palindrome = 0;
			break;
		}
		first_half_list = first_half_list->next;
		second_half_list = second_half_list->next;
	}
	second_half_list = reverse_list(second_half_list);

	prev_slow_p->next = second_half_list;

	return (is_palindrome);
}
