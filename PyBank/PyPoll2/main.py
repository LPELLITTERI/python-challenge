import os
import csv

# Set file paths
csv_path = os.path.join('election_data.csv')
output_path = os.path.join('Analysis.txt')

def read_csv(csv_path):
    """Reads a CSV file and returns a list of rows."""
    with open(csv_path) as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        header = next(csvreader)
        rows = [row for row in csvreader]
    return header, rows

def count_candidate_votes(rows):
    """Counts the number of votes each candidate received."""
    vote_counts = {}
    for row in rows:
        candidate_name = row[2]
        if candidate_name in vote_counts:
            vote_counts[candidate_name] += 1
        else:
            vote_counts[candidate_name] = 1
    return vote_counts

def calculate_results(vote_counts):
    """Calculates and returns the election results."""
    total_votes = sum(vote_counts.values())
    winner = max(vote_counts, key=vote_counts.get)
    results = []
    for candidate, votes in vote_counts.items():
        percentage = votes / total_votes * 100
        results.append((candidate, votes, percentage))
    return total_votes, winner, results

def format_results(total_votes, winner, results):
    """Formats the election results for printing."""
    output = []
    output.append("ELECTION RESULTS")
    output.append("-------------------------")
    output.append(f"Total Votes: {total_votes}")
    output.append("-------------------------")
    for candidate, votes, percentage in results:
        output.append(f"{candidate}: {percentage:.3f}% ({votes})")
    output.append("-------------------------")
    output.append(f"Winner: {winner}")
    output.append("-------------------------")
    return "\n".join(output)

if __name__ == '__main__':
    header, rows = read_csv(csv_path)
    vote_counts = count_candidate_votes(rows)
    total_votes, winner, results = calculate_results(vote_counts)
    output = format_results(total_votes, winner, results)
    print(output)

    with open(output_path, 'w') as file:
        file.write(output)
