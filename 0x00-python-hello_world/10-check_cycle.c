#include "lists.h"

int check_cycle(listint_t *list)
{
  listint_t *head, *temp;




    if(list == NULL || list->next == NULL)
                            return(0);

    head = list;
    temp = head->next;

    while(head != NULL && temp->next != NULL && temp->next->next != NULL){
        if(head == temp)
        {
            return(1);
        }
        head = head->next;
        temp = temp->next->next;
    }

    return(0);





}

