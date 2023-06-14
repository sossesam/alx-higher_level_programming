#include "lists.h"

int check_cycle(listint_t *list)
{
  listint_t *head, *temp;



    head = malloc(sizeof(listint_t));
    temp = malloc(sizeof(listint_t));


    head = list->next;
    temp = head;

    while(head != NULL){


        if(head->next == temp)
        {
            return(1);
        }
        head = head->next;
    }

    return(0);





}

