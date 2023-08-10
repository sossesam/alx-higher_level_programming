#include "lists.h"



int is_palindrome(listint_t **head)
{
   listint_t *check = *head;
    listint_t *temp = *reverse_listint(head);



    while(check != NULL){
        if (check->n == temp->n)
        {
            check = check->next;
            temp = temp->next;
        }
        else{
            return (-1);
        }
        return (1);
    }
return (0);
}


