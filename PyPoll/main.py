import pandas as pd

df = pd.read_csv('./resources/election_data.csv')
voteTotal = df['Voter ID'].count()
Khan = df[df['Candidate'] == "Khan"]
Correy = df[df['Candidate'] == "Correy"]
Li = df[df['Candidate'] == "Li"]
OTooley = df[df['Candidate'] == "O\'Tooley"]
print("Election Results")
print("------------------------")
print(f"Total Votes: {voteTotal}")
print("------------------------")
print(f"Khan: {round((Khan.Candidate.count() / voteTotal)*100, 6)}% ({Khan.Candidate.count()})")
print(f"Correy: {round((Correy.Candidate.count() / voteTotal)*100, 6)}% ({Correy.Candidate.count()})")
print(f"Li: {round((Li.Candidate.count() / voteTotal)*100, 6)}% ({Li.Candidate.count()})")
print(f"O\'Tooley: {round((OTooley.Candidate.count() / voteTotal)*100, 6)}% ({OTooley.Candidate.count()})")
print("------------------------")
winner = pd.DataFrame(df['Candidate'].value_counts())
winner['Name'] = winner.index
winner.reset_index()
print(winner.head())

k = winner.loc[winner['Candidate'] == winner['Candidate'].max()]
print (f"WINNER : {k['Name']}")
