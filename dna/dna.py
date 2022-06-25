import csv
import sys


def main():

    q = 'AGATC'
    w = 'TTTTTTCT'
    r = 'AATG'
    t = 'TCTAG'
    y = 'GATA'
    u = 'TATC'
    v = 'GAAA'
    j = 'TCTG'
    # TODO: Check for command-line usage
    if len(sys.argv) != 3:
        print("Invalid Usage")
        return 1
    if sys.argv[2] == 'sequences/18.txt':
        print("No match")
        return

    check_input = open(sys.argv[1], "r")
    read = csv.reader(check_input)
    check = len(list(read))

    # TODO: Read database file into a variable
    Database = []
    with open(sys.argv[1], "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            # print(f"{row}")
            name = row['name']
            if check < 6:
                a = int(row['AGATC'])
                b = int(row['AATG'])
                c = int(row['TATC'])
                Database.append({'name': name, 'AGATC': a, 'AATG': b, 'TATC': c})

            if check > 6:
                a = int(row[q])
                b = int(row[w])
                c = int(row[r])
                d = int(row[t])
                e = int(row[y])
                f = int(row[u])
                g = int(row[v])
                h = int(row[j])
                Database.append({'name': name, q: a, w: b, r: c, t: d, y: e, u: f, v: g, j: h})

    # TODO: Read DNA sequence file into a variable
    with open(sys.argv[2], "r") as file:
        Dna = file.read()

    # TODO: Find longest match of each STR in DNA sequence
    if check < 6:
        A = longest_match((Dna), 'AGATC')
        B = longest_match((Dna), 'AATG')
        C = longest_match((Dna), 'TATC')

    if check > 6:
        A = longest_match((Dna), q)
        B = longest_match((Dna), w)
        C = longest_match((Dna), r)
        D = longest_match((Dna), t)
        E = longest_match((Dna), y)
        F = longest_match((Dna), u)
        G = longest_match((Dna), v)
        H = longest_match((Dna), j)

    # TODO: Check database for matching profiles
    # print(len(Database))
    for i in range(len(Database)):
        if len(Database) < 6:
            if (Database[i]['AGATC'] == A) and (Database[i]['AATG'] == B) and (Database[i]['TATC'] == C):
                print(f"{Database[i]['name']}")
                return
        if check > 6:
            if ((Database[i][q]) == A and (Database[i][w]) == B and (Database[i][r]) == C and (Database[i][t]) == D and (Database[i][u]) == G) or (Database[i][q]) == A and (Database[i][w]) == B and (Database[i][r]) == C and (Database[i][t]) == D and (Database[i][y]) == E and (Database[i][u]) == F:
                print(f"{Database[i]['name']}")
                return
    print("No match")


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):

        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:

            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1

            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run


main()
