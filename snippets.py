# Dictionaries have a function, get, which takes two parameters - the key you want,
#  and a default value if it doesn't exist. I prefer this method to defaultdict as you
# only want to handle the case where the key doesn't exist in this one line of code, not everywhere.
my_dict = {}

my_dict[some_key] = my_dict.get(some_key, 0) + 1





# Consider using a defaultdict instead, replacing this line (in __init__):
from collections import defaultdict
# Now rather than raise a KeyError, self.adj[0].append(edge) will create a list automatically to append to.

self.adj = {}
# with this:

self.adj = defaultdict(list)
# You'll need to import at the top:





# The keys method returns the keys of the dictionary as a list

storyCount.keys()
# The values method returns the values in the dictionary as a list

storyCount.values()

# The for loop below uses the items method to access one (key, value) pair on each iteration of the loop.

for key, value in webstersDict.items():
    print(key, value)





# get two balues and cast to int
graph_nodes, graph_edges = map(int, input().split())

# input =1 2 3 3 2 split and cast to interger and change it into a list
ids = list(map(int, input().rstrip().split()))