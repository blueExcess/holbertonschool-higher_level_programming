/* 13. Test if a LL is also a palindrome */
#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * is_palindrome - test if a LL is also a palindrome
 * @head: begining of list
 *
 * Return: 1 for yes, 0 for no or fail
 */
int is_palindrome(listint_t **head)
{
	listint_t *seek;
	int i = 0, j = 0;
	int arr[4096];


	if (!head)
		return (0);
	seek = *head;
	if (!*head || (*head)->next == NULL)
		return (1);

	for (; seek; seek = seek->next, i++)
		arr[i] = seek->n;
	for (i--; i > j; i--, j++)
	{
		if (arr[j] == arr[i])
			;
		else
			return (0);
	}
	return (1);
}
