#include "lists.h"


listint_t *insert_node(listint_t **head, int number){
   listint_t *new;
    listint_t *current, *temp;

    current = *head;

    new = malloc(sizeof(listint_t));
    temp = NULL;
    if (new == NULL)
        return (NULL);


    new->n = number;
    new->next = NULL;

    if (*head == NULL)
        *head = new;
    else
    {
        while (current->next != NULL &&  current->n < number)
        {
            temp = current;
            current = current->next;

        }
        new->next = current;
        if (temp != NULL)
		temp->next = new;
        else
		temp = new;





        }

    return (new);
}
