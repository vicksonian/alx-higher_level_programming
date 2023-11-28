#include <stdlib.h>
#include "lists.h"

/**
* insert_node - Inserts a number into a sorted singly linked list.
* @head: A pointer to the head of the linked list.
* @number: The number to be inserted.
* Return: The address of the new node, or NULL if it failed.
*/
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node, *current;

	/* Allocate memory for the new node */
	new_node = malloc(sizeof(listint_t));

	if (new_node == NULL)
	return (NULL);

	/* Set the data for the new node */
	new_node->n = number;
	new_node->next = NULL;

	if (*head == NULL || number < (*head)->n)
	{
	new_node->next = *head;
	*head = new_node;
	return (new_node);
	}

	/* Find the position to insert the new node */
	current = *head;

	while (current->next != NULL && current->next->n < number)
	{
	current = current->next;
	}

	/* Insert the new node into the list */
	new_node->next = current->next;
	current->next = new_node;

	return (new_node);
}
