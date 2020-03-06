
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


file = "budget_data.csv"


# In[3]:


df = pd.read_csv(file, encoding="ISO-8859-1")


# In[66]:


months = df["Date"].unique()
tot = len(months)
print(f"Total Months: {tot}")


# In[67]:


profit = df["Profit/Losses"].sum()
profit = '{:,}'.format(profit)
print(f"Total: ${profit}")


# In[55]:


total = 0
differences = [0]
for x in range(1, len(df)):
    difference = df["Profit/Losses"][x] - df["Profit/Losses"][x-1]
    differences.append(difference)
    total = total + difference
avg = total / (len(df)-1)
avg = '{:,.2f}'.format(avg)


# In[68]:


print(f"Average Change: ${avg}")


# In[42]:


df["Change"] = differences


# In[57]:


sorted_df = df.sort_values("Change")


# In[ ]:


sorted_df = sorted_df.set_index("Change")


# In[73]:


max_month = sorted_df.loc[max(differences), "Date"]
print(f"Greatest Increase in Profits: {max_month} (${max(differences)})")


# In[74]:


min_month = sorted_df.loc[min(differences), "Date"]
print(f"Greatest Decrease in Profits: {min_month} (${min(differences)})")


# In[76]:


f= open("analysis.txt","w+")
f.write(f"Financial Analysis\n\nTotal Months: {tot}\n")
f.write(f"Total: ${profit}\n")
f.write(f"Average Change: ${avg}\n")
f.write(f"Greatest Increase in Profits: {max_month} (${max(differences)})\n")
f.write(f"Greatest Decrease in Profits: {min_month} (${min(differences)})")
f.close()

