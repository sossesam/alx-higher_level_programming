#include "lists.h"


listint_t **reverse_listint(listint_t **head)
{
listint_t *p;
listint_t *n;

p = NULL;
n = NULL;

while (*head != NULL)
{
n = (*head)->next;
(*head)->next = p;
p = *head;
*head = n;
}

*head = p;
return (head);
}



int is_palindrome(listint_t **head)
{
listint_t *check = *head;
listint_t *temp = *reverse_listint(head);

if (check == NULL || *check == NULL)
{
return (1);
}

while (check != NULL)
{
if (check->n == temp->n)
{
check = check->next;
temp = temp->next;
}
else
{
return (0);
}
}
return (1);
}
