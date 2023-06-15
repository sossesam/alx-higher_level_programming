#include "lists.h"

int check_cycle(listint_t *list)
{
  listint_t *head, *temp;




    if(list == NULL || list->next == NULL)
                            return(0);

    head = list->next;
    temp = head;

    while(head != NULL && head->next != NULL && head->next->next != NULL){
        if(head->next == temp)
        {
            return(1);
        }
        head = head->next;
    }

    return(0);





}

