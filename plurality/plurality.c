#include <cs50.h>
#include <stdio.h>
#include <string.h>

// Max number of candidates
#define MAX 9

// Candidates have name and vote count
typedef struct
{
    string name;
    int votes;
}
candidate;

// Array of candidates
candidate candidates[MAX];

// Number of candidates
int candidate_count;

// Function prototypes
bool vote(string name);
void print_winner(void);

int main(int argc, string argv[])
{
    // Check for invalid usage
    if (argc < 2)
    {
        printf("Usage: plurality [candidate ...]\n");
        return 1;
    }

    // Populate array of candidates
    candidate_count = argc - 1;
    if (candidate_count > MAX)
    {
        printf("Maximum number of candidates is %i\n", MAX);
        return 2;
    }
    for (int i = 0; i < candidate_count; i++)
    {
        candidates[i].name = argv[i + 1];
        candidates[i].votes = 0;
    }

    int voter_count = get_int("Number of voters: ");

    // Loop over all voters
    for (int i = 0; i < voter_count; i++)
    {
        string name = get_string("Vote: ");

        // Check for invalid vote
        if (!vote(name))
        {
            printf("Invalid vote.\n");
        }
    }

    // Display winner of election
    print_winner();
}

// Update vote totals given a new vote
bool vote(string name)
{
    int i = 0;
    int n = 0;
    
    for (i = 0, n = 3; i < n; i++)
    {
        if (strcmp(candidates[i].name, name) == 0)
        {
            candidates[i].votes = candidates[i].votes + 1;
            return true;
        }
    }
    return false;
}

// Print the winner (or winners) of the election
void print_winner(void)
{
    // TODO
    int a = candidates[0].votes;
    int b = candidates[1].votes;
    int c = candidates[2].votes;
    if (a > b)
    {
        if (a > c)
        {
            printf("%s\n", candidates[0].name);
        }
        else if (c > a)
        {
            printf("%s\n", candidates[2].name);
        }
        else if (c == a)
        {
            printf("%s\n%s\n", candidates[0].name, candidates[2].name);
        }
    }
    else if (b > c)
    {
        if (b > a)
        {
            printf("%s\n", candidates[1].name);
        }
        else if (b == a)
        {
            printf("%s\n%s\n", candidates[0].name, candidates[1].name);
        }
    }
    else if (c > b)
    {
        printf("%s\n", candidates[2].name);
    }
    else if (c == b)
    {
        if (a == b && b == c)
        {
            printf("%s\n%s\n%s\n", candidates[0].name, candidates[1].name, candidates[2].name);
        }
        else if (c == b && b > a)
        {
            printf("%s\n%s\n", candidates[1].name, candidates[2].name);
        }
    }
    return;
}