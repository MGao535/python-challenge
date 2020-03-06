
# coding: utf-8

# In[102]:


import pandas as pd


# In[103]:


file = "election_data.csv"


# In[104]:


df = pd.read_csv(file, encoding="ISO-8859-1")


# In[105]:


df.head()


# In[106]:


df.count()


# In[107]:


cols = ["Voter ID", "Candidate"]
ext_df = df[cols]
ext_df.head()


# In[108]:


candidates = ext_df.groupby(["Candidate"]).count()
candidates = candidates.sort_values("Voter ID", ascending=False)
candidates


# In[130]:


total = ext_df["Voter ID"].count()
print(f"Total Votes: {total}")


# In[110]:


percentages = []
for x in range(0, len(candidates["Voter ID"])):
    percentages.append(int(candidates["Voter ID"][x])/total)
for x in range(0, len(candidates["Voter ID"])):
    percentages[int(x)] = '{:.2%}'.format(percentages[int(x)])
percentages


# In[111]:


candidates["Percent"] = percentages


# In[132]:


for i, row in candidates.iterrows():
    name = i
    percent = row["Percent"]
    amount = row["Voter ID"]
    print(f"{name}: {percent} ({amount})")


# In[113]:


list(candidates.columns.values) 


# In[133]:


#winner = candidates.iloc(candidates["Percent"].max())
winner = candidates.first_valid_index()
print(f"Winner: {winner}")


# In[141]:


f= open("results.txt","w+")
f.write(f"Election Results\n\nTotal Votes: {total}\n\n")
for i, row in candidates.iterrows():
    name = i
    percent = row["Percent"]
    amount = row["Voter ID"]
    f.write(f"{name}: {percent} ({amount})\n")
f.write(f"\nWinner: {winner}")
f.close()

