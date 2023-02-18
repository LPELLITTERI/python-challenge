import os
import csv

def read_csv(csv_path, delimiter=',', has_header=True):
    """Reads a CSV file and returns a list of rows.

    Args:
        csv_path (str): The file path to the CSV file.
        delimiter (str, optional): The delimiter used in the file. Defaults to ','.
        has_header (bool, optional): Whether or not the file has a header row. Defaults to True.

    Returns:
        list: A list of rows from the CSV file.
    """
    with open(csv_path) as csvfile:
        csvreader = csv.reader(csvfile, delimiter=delimiter)
        if has_header:
            header = next(csvreader)
        else:
            header = None
        rows = []
        for row in csvreader:
            rows.append(row)
        return header, rows


def count_candidate_votes(data):
    """Counts the number of votes each candidate received.

    Args:
        data (list): A list of rows from the CSV file.

    Returns:
        dict: A dictionary containing the candidate names and their vote counts.
    """
    candidate_vote_count = {}
    for row in data:
        candidate_name = row[2]
        if candidate_name in candidate_vote_count:
            candidate_vote_count[candidate_name] += 1
        else:
            candidate_vote_count[candidate_name] = 1
    return candidate_vote_count


def print_election_results(total_votes, vote_counts):
    """Prints the election results.

    Args:
        total_votes (int): The total number of votes cast.
        vote_counts (dict): A dictionary containing the candidate names and their vote counts.
    """
    line = "---------------"
    print(line)
    print("ELECTION RESULTS")
    print(line)
    print(f"Total Votes: {total_votes}")
    print(line)
    winning_total = 0
    for key, value in vote_counts.items():
        print(f"{key}: {value} ({round((value/total_votes) * 100, 3)}%)")
        if value > winning_total:
            winning_total = value
            winning_candidate = key
    print(line)
    print(f"WINNER: {winning_candidate} with {winning_total} votes")


if __name__ == '__main__':
    csv_path = os.path.join('Resources', 'election_data.csv')
    header, data = read_csv(csv_path, has_header=True)
    vote_counts = count_candidate_votes(data)
    total_votes = sum(vote_counts.values())
    print_election_results(total_votes, vote_counts)
