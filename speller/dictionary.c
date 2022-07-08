
// Implements a dictionary's functionality
#include <stdlib.h>
#include <stdio.h>
#include <strings.h>
#include <ctype.h>
#include <stdbool.h>
#include <string.h>

#include "dictionary.h"

// Number of buckets in hash table
// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
}
node;

const unsigned int N = 27;

//Number of words on dictionary
int COUNTER = -1;

//Check if dictionary is loaded
bool LOAD = false;

// Hash table
node *table[N] = {NULL};

// Returns true if word is in dictionary else false
bool check(const char *word)
{
    unsigned int k = hash(word);

    node *trav = table[k];

    while (trav != NULL)
    {
        if ((strcasecmp(word, trav->word)) == 0)
        {
            return true;
        }
        else
        {
            trav = trav->next;
        }
    }
    return false;
}

// Hashes word to a number
unsigned int hash(const char *word)
{
    // assign a number to the first char of buffer from 0-25
    if ((isalpha(word[0]) > 0))
    {
        return tolower(word[0]) - 'a';
    }
    else
    {
        return 26;
    }
}


// Loads dictionary into memory, returning true if successful else false
char c;
bool load(const char *dictionary)
{

    FILE *file = fopen(dictionary, "r");
    if (file == NULL)
    {
        LOAD = false;
        return false;
    }

    char wordy[LENGTH + 1];

    do
    {
        c = fscanf(file, "%s", wordy);
        node *n = malloc(sizeof(node));
        if (n == NULL)
        {
            LOAD = false;
            return false;
        }
        strcpy(n->word, wordy);
        n->next = NULL;
        unsigned int i = hash(wordy);
        if (table[i] == NULL)
        {
            table[i] = n;
        }
        else
        {
            node *p = table[i];

            while (true)
            {
                if (p->next == NULL)
                {
                    p->next = n;
                    break;
                }
                p = p->next;
            }
        }

        COUNTER++;

    }
    while (c != EOF);

    fclose(file);
    LOAD = true;
    return true;
}

// Returns number of words in dictionary if loaded else 0 if not yet loaded
unsigned int size(void)
{
    if (LOAD)
    {
        return COUNTER;
    }
    else
    {
        return 0;
    }
}

// Unloads dictionary from memory, returning true if successful else false
bool unload(void)
{
    for (int i = 0; i < N; i++)
    {
        node *cursor = table[i];

        while (cursor != NULL)
        {
            node *temp = cursor;
            cursor = cursor->next;
            free(temp);
        }
    }
    LOAD = false;
    return true;
}

// Returns number of words in dictionary if loaded else 0 if not yet loaded
// Returns number of words in dictionary if loaded else 0 if not yet loaded
// Returns number of words in dictionary if loaded else 0 if not yet loaded
// Returns number of words in dictionary if loaded else 0 if not yet loaded
// Returns number of words in dictionary if loaded else 0 if not yet loaded
// Returns number of words in dictionary if loaded else 0 if not yet loaded
// Returns number of words in dictionary if loaded else 0 if not yet loaded