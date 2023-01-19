import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math


euro12 = pd.read_csv('data.txt')  # step 1 and 2
print(euro12)
goals = euro12['Goals']   # selected the goals column
print(goals)
teams = euro12['Team']
print(len(teams))  # number of teams

print(len(euro12.columns))  # number of columns

discipline = pd.DataFrame()
discipline['Team'], discipline['Yellow Cards'], discipline['Red Cards'] = euro12['Team'], euro12['Yellow Cards'], euro12['Red Cards']
print(discipline)

sort_list = ['Red Cards', 'Yellow Cards']
discipline = discipline.sort_values(by=sort_list, ascending=False)
print(discipline)

goals6 = euro12[euro12.Goals > 6]
print(goals6)

team_g = euro12[euro12.Team.str.startswith('G')]
print(team_g)
s7 = euro12.iloc[:, 0:7]
print(s7)

el3 = euro12.iloc[:, 0:-3]
print(el3)

s_shoot_acc = euro12.iloc[[3, 7, 12], [0, 4]]
print(s_shoot_acc)

print(euro12.info())
euro12['passing accuracy'] = round(euro12['Passing Accuracy'].str.replace('%', '').astype(float)/100, 2)
print(euro12['passing accuracy'])

euro12 = euro12.sort_values(by='passing accuracy', ascending=False)
print(euro12['passing accuracy'])

def bar_graph():
    plt.title('Teams to shooting accuracy')
    plt.ylabel('accuracy')
    plt.xlabel('teams')
    plt.xticks(rotation=90)
    team = euro12['Team']
    acc = euro12['passing accuracy']
    plt.bar(team, acc)
    plt.show()

bar_graph()

