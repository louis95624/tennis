import pandas as pd
import os


data_list = os.listdir()
data_list = data_list[:-2]
df = pd.DataFrame()
for data in data_list:
    temp = pd.read_excel(data)
    df = pd.concat([df, temp], ignore_index=True)

player_1 = input("Enter winner name:")
player_2 = input("Enter loser name:")

Winner_name = df["Winner"].unique()
Loser_name = df["Loser"].unique()
player_names = set(Winner_name).union(set(Loser_name))

if not (player_1 in player_names and player_2 in player_names):
    print("There is no such name in database")
else:
    total_df = df[df["Winner"] == player_1]
    win_first_round = total_df[total_df["W1"] > total_df["L1"]]
    
    lose_df = df[df["Loser"] == player_2]
    lose_first_round = lose_df[lose_df["W1"] > lose_df["L1"]]
    result = (len(win_first_round)/len(total_df)+len(lose_first_round)/len(lose_df))/2

    print(result)
