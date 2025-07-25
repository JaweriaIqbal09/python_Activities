while True:  
    n=int(input("Enter the number of candidates (upto 9): "))
    if n>10 or n<1:
        print("Enter the Correct Number !")
    else :
        break    
   

results={}
    
for i in range(1,n+1):
    name=input(f"Enter name of candidate {i} : ")
    results[name]=0

v=int(input("Enter the number of voters: "))
for i in range(1,v+1):
    vote=input(f"Voter {i} , enter the name of candidate you vote for: ")
    if vote in results:
        results[vote]+=1
    else:
        print("No such candidate is found ! Sorry your votes has wasted ")
  
max_vote=max(results.values()) 
winner=[]
print("📊 Votes received by each candidate: ")
for candidates,votes in results.items():
    print(f"{candidates} : {votes} votes ")

for keys,value in results.items():
    if value==max_vote:
        winner.append(keys)

if len(winner)==1:
     print(f"The winner is {winner[0]} with {max_vote} votes")
elif len(winner)>1:
    print("The result is tied between "+"," .join(winner) + f" on {max_vote} votes ")