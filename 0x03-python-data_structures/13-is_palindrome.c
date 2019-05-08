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
	listint_t *seek = *head;
	int i = 0, j = 0, test = 0;
	int arr[20];


	if (!head)
		return (0);
	if (!*head || (*head)->next == NULL)
		return (1);
	for (; seek; seek = seek->next, i)
		arr[i] = seek->n;
	for (i--; i > j; i--, j++)
	{
		if (arr[i] == arr[j])
			test = 1;
		else
			test = 0;
	}
	if (test != 1)
		return (0);
	return (1);
}
