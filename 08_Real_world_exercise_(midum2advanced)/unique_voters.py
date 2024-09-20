"""Exercise 2: **Unique Voters List**
You are managing a voting system where each user casts a vote using their ID. Given a list of voter IDs, remove duplicate votes and return the unique voter IDs.
"""


voter_ids = [123, 456, 123, 789, 456, 101, 102, 789]
unique_voter_ids = set(voter_ids)
# print(f"Unique Voter IDs: {unique_voter_ids}")

# if oders matter
unique_voter_ids = list(dict.fromkeys(voter_ids))
print(f"Unique Voter IDs: {unique_voter_ids}")
