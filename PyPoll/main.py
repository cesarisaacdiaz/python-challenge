import csv
import os

input_file = os.path.join("election_data.csv")
output_file = os.path.join("election_data_output.txt")

voter_id = []
country = []
candidate = []
dato_write = ''

with open(input_file, newline='') as csvfile:
    csvreader = csv.reader(csvfile,delimiter=',')
    next(csvreader, None)

    for row in csvreader:
        voter_id.append(row[0])
        country.append(row[1])
        candidate.append(row[2])

total_voters = len(voter_id)
Khan_voters = candidate.count('Khan')
correy_voters = candidate.count('Correy')
li_voters = candidate.count('Li')
tooley_voters = candidate.count("O'Tooley")

candidate_list = ['Khan','Correy','Li',"O'Tooley"]
values_list = [Khan_voters,correy_voters,li_voters,tooley_voters]

all_lists = []
all_lists = zip(candidate_list,values_list)

maximo = max(values_list)

print('Election Results')
print('-------------------------------')
print(f"Total Votes: {len(voter_id)}")
print('------------------------------')
print(f"Khan: {(Khan_voters/total_voters)*100:,.3f} % ({Khan_voters})")
print(f"Correy: {(correy_voters/total_voters)*100:,.3f} % ({correy_voters})")
print(f"Li: {(li_voters/total_voters)*100:,.3f} % ({li_voters})")
print(f"O'Tooley: {(tooley_voters/total_voters)*100:,.3f} % ({tooley_voters})")
print('--------------------------------')

for i in all_lists:
    if(i[1]==maximo):
        print(f"Winner: {i[0]}")
        dato_write = ("Winner: " + str(i[0]))


print('--------------------------------')

with open(output_file,'w') as datafile:
    datafile.write('Election Results')
    datafile.write('\n-------------------------------')
    datafile.write("\n"+f"Total Votes: {len(voter_id)}")
    datafile.write('\n------------------------------')
    datafile.write("\n"+f"Khan: {(Khan_voters/total_voters)*100:,.3f} % ({Khan_voters})")
    datafile.write("\n"+f"Correy: {(correy_voters/total_voters)*100:,.3f} % ({correy_voters})")
    datafile.write("\n"+f"Li: {(li_voters/total_voters)*100:,.3f} % ({li_voters})")
    datafile.write("\n"+f"O'Tooley: {(tooley_voters/total_voters)*100:,.3f} % ({tooley_voters})")
    datafile.write('\n--------------------------------')
    datafile.write("\n"+dato_write)
    datafile.write('\n--------------------------------')