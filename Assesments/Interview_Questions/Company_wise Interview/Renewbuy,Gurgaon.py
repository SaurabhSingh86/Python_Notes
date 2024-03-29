""" Python Assignment Questions"""
# ------------------------------------------------------------------------------------------------------------------
"""
Question 1:
You are required to write a program to sort the (name, age, height) tuples by ascending order where name is string,
age and height are numbers. The tuples are input by console. The sort criteria is:
1: Sort based on name;
2: Then sort based on age;
3: Then sort by score.
The priority is that name > age > score.
If the following tuples are given as input to the program:
Tom,19,80
John,20,90
Jony,17,91
Jony,17,93
Json,21,85
Then, the output of the program should be:
[('John', '20', '90'), ('Jony', '17', '91'), ('Jony', '17', '93'), ('Json', '21', '85'), ('Tom', '19', '80')] 
"""

# Method 1:
given_input = [('John', '20', '90'), ('Jony', '17', '91'), ('Jony', '17', '93'), ('Json', '21', '85'), ('Tom', '19', '80')]

expected_output = [('John', '20', '90'), ('Jony', '17', '91'), ('Jony', '17', '93'), ('Json', '21', '85'), ('Tom', '19', '80')]

# By using sorted():
s_name = sorted(given_input)
print(s_name)

# In above question, whenever we are using sorted()
# firstly, it'll sort based on Names(i.e. 1st preference),
# if Names are same then it'll sort based on Ages(i.e. 2nd preference),
# if Ages are also same then sort by Scores(i.e. 3rd preference)

# ------------------------------------------------------------------------------------------------------------------

"""
Question 2:
Define a class with a generator which can iterate the numbers, which are divisible
by 7, between a given range 0 and n."""

# Method 1:
class Generator:
    def __init__(self, n):
        self.n = n

    def generator_(self):
        for num in range(1, self.n):
            if num % 7 == 0:
                yield num


res = Generator(int(input("Enter the last limit: ")))
output = res.generator_()

for item in output:
    print(item, end=" ")

# ------------------------------------------------------------------------------------------------------------------

""" Question 3:
Please write a program using a generator to print the numbers which can be divisible by 5 and 7 between 0 and n in 
comma separated form while n is input by console.
Example:
If the following n is given as input to the program: 100
Then, the output of the program should be: 0,35,70"""

# Method 1:

res = (num for num in range(int(input("Enter last limit: "))) if num % 5 == 0 and num % 7 == 0)
print(list(res))

# ------------------------------------------------------------------------------------------------------------------

""" Question 4:
Create a function that takes a list of football clubs with properties: name, wins, loss, draws, scored, conceded, 
and returns the team name with the highest number of points. If two teams have the same number of points, return the
team with the largest goal difference.
How to Calculate Points and Goal Difference
team = { "name": "Manchester United", "wins": 30, "loss": 3, "draws": 5, "scored": 88,
"conceded": 20 }
Total Points = 3 * wins + 0 * loss + 1 * draws = 3 * 30 + 0 * 3 + 5 * 1 = 95 points
Goal Difference = scored - conceded = 88 - 20 = 68

"""

# Method 1:
teams = [{"name": "Manchester United", "wins": 30, "loss": 3, "draws": 5, "scored": 88, "conceded": 20},
         {"name": "India", "wins": 40, "loss": 30, "draws": 5, "scored": 98, "conceded": 20}]
# here second dictionary is just for sample


def calculation(team_):
    total_points = 3 * team_['wins'] + 0 * team_['loss'] + 1 * team_['draws']
    goal_difference = team_['scored'] - team_['conceded']
    return total_points, goal_difference


dd = {team['name']: calculation(team) for team in teams}
print(dd)


if dd['Manchester United'][0] != dd['India'][0]:
    res = sorted(dd.items(), key=lambda item: item[-1][0], reverse=True)
    print(res)
else:
    res = sorted(dd.items(), key=lambda item: item[-1][-1], reverse=True)
    print(res)


# Method 2:
res = {}


def football(team_):
    for i in team_:
        total_points = 3 * i["wins"] + 0 * i["loss"] + 1 * i["draws"]
        goal_difference = i["scored"] - i["conceded"]
        res[i["name"]] = (total_points, goal_difference)


football(team)
print(res)

if res["Manchester United"][0] != res["india"][0]:
    if res["Manchester United"][0] > res["india"][0]:
        print(f"Manchester United: {res.get('Manchester United')}")
    else:
        print(f"India: {res['india']} ")
else:
    if res["Manchester United"][-1] > res["india"][-1]:
        print(f"Manchester United: {res.get('Manchester United')}")
    else:
        print(f"India: {res['india']} ")
#

# Method 3

team_a = {"name":"Ajmer", "W":30, "L":3, "D":5, "S":98, "C":20}
team_b = {"name":"Bhopal", "W":28, "L":3, "D":3, "S":99, "C":10}
team_c = {"name":"Chennai", "W":25, "L":2, "D":2, "S":66, "C":5}
team_d = {"name":"Delhi", "W":30, "L":2, "D":5, "S":99, "C":18}
team_e = {"name":"Electronic", "W":30, "L":3, "D":5, "S":97, "C":20}


def rank(*args):
    l = []
    for i in args:
        total_points = 3 * i['W'] + 0*i['L'] + 1*i['D']
        l.append((i['name'], total_points, i['S']-i['C']))
    s = sorted(l, key=lambda i: i[-2])
    if s[-1][-2] == s[-2][-2]:
        p = set()
        for j in range(len(s)-1):
            if s[j][-2] == s[j+1][-2]:
                p.add(s[j])
                p.add(s[j+1])
        y = sorted(p, key=lambda i: i[-1])
        print((y[-1][0], y[-1][-1]))
    else:
        print((s[-1][0], s[-1][-1]))


rank(team_a, team_b, team_c, team_d, team_e)