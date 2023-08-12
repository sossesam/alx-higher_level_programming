#include "lists.h"



int is_palindrome(listint_t **head)
{
listint_t *check = *head;
listint_t *temp = *reverse_listint(head);

if(head == NULL){
return(0);
}

while(check != NULL){
if (check->n == temp->n)
{
check = check->next;
temp = temp->next;
}
else{
return (0);
}
}
return (1);
}
