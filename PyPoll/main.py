import csv
data = csv.reader(open('Resources/election_data.csv'))

votes = 0
candidates = {}
winner_votes = 0
winner = ''
next(data)

for row in data:
    votes+=1
    candidate=row[2]
    
    if candidate not in candidates.keys():
        candidates[candidate] = 0
    
    candidates[candidate] += 1

    if candidates[candidate] > winner_votes:
        winner = candidate
        winner_votes = candidates[candidate]

output = f'''
  Election Results
  -------------------------
  Total Votes: {votes:,}
  -------------------------
'''
for candidate in candidates:
    can_votes = candidates[candidate]

    output += f'  {candidate}: {can_votes/votes*100:.3f}% ({can_votes:,})\n'

output += f'----------------------------\nWinner: {winner}\n----------------------------'
# -------------------------
# Winner: Khan
# -------------------------'''
open('analysis/report.txt', 'w').write(output)
print(output)