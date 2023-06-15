#include "lists.h"

int check_cycle(listint_t *list)
{
  listint_t *head, *temp;



    head = malloc(sizeof(listint_t));
    temp = malloc(sizeof(listint_t));

    if(list == NULL || list->next == NULL)
                            return(0);

    head = list->next;
    temp = head;

    while(head != NULL || head->next == NULL){
        if(head->next == temp)
        {
            return(1);
        }
        head = head->next;
    }

    return(0);





}

