# Import our dependencies
import csv
import os

# Assign a variable to load from a path
file_to_load = os.path.join("Resources/election_results.csv")
# Assign a variable to save the file to a path
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initalize a total vote counter.
total_votes = 0

# Candidate options and candidate votes
candidate_options = []
candidate_votes = {}

#Challenge County Options and county votes
county_names = []
county_votes = {}

# Track Winning vote count and percentage
winning_candidate = ""
winning_count = 0
winning_percentage = 0

#Challenges track the largest county voter turnout and its percentage
largest_county_turnout = ""
largest_county_votes = 0

# Read the csv file and convert it into a list of dictionaries
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    #print(reader)

    # Read the header
    headers = next(file_reader)
    #print(header)

    # For each row in the csv file
    for row in file_reader:
        # Add to the total vote count
        total_votes += 1
        # Get the candidate name from each row
        candidate_name = row[2]

        # Extract th county name from each row
        county_name = row[1]

        # If the candidate does not match any existing candidate add it into the list
        if candidate_name not in candidate_options:
            # Add it candidate name to the list of candidates.
            candidate_options.append(candidate_name)
            # Begin tracking that candidates's vote count.
            candidate_votes[candidate_name] = 0
        # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

        # Challenge county
        if county_name not in county_names:
            # Challenge add county name to the list
            county_names.append(county_name)
            # Tracking that candidate vote count
            county_votes[county_name] = 0
        county_votes[county_name] += 1
    
 # Save the results to our text file       
with open(file_to_save, "w") as txt_file:
    # Print the final vote count to the terminal
    election_results =(
        f"\nElection Results\n"
        f"\n---------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"---------------------\n"
        f"\nCounty Votes:\n"
      )  
    print(election_results, end="")
    txt_file.write(election_results)

    # Challenge save the final county votes to the text file
    for county in county_votes:
        # Retrieve vote county and percentage
        county_vote = county_votes[county]
        county_percent = int(county_vote) / int(total_votes) * 100
        county_results = (
            f"{county}: {county_percent:.1f}% ({county_vote:,})\n"
        )
        print(county_results, end="")
        txt_file.write(county_results)
        # Determine winning vote count and canddiate
        if(county_vote > largest_county_votes):
            largest_county_votes = county_vote
            largest_county_turnout = county
    # Print the county with the largest turnout
    largest_county_turnout = (
        f"\n---------------------------\n"
        f"Largest County Turnout: {largest_county_turnout}\n"
        f"-----------------------------\n"
    )
    print(largest_county_turnout)
    txt_file.write(largest_county_turnout)

    # Determine the percentage of votes for each candidate by looping through the counts
    for candidate in candidate_votes:
        #Retrieve vote count of a candidate
        votes = candidate_votes[candidate]
        # Calculate the percentage of votes
        vote_percentage = int(votes) / int(total_votes) * 100
        candidate_results = (
            f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n"
        )
        print(candidate_results)
        # Save the candidate results to our text file
        txt_file.write(candidate_results)

        # Determine winning vote count, winning percentage, and candidate
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate
            winning_percentage = vote_percentage

    winning_candidate_summary = (
        f"-----------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-----------------------------\n"
    )
    print(winning_candidate_summary)

    # Save the winning candidate name to the text file.
    txt_file.write(winning_candidate_summary) 

    