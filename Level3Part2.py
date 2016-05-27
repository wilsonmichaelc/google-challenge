#!/usr/bin/python
from sets import Set

# Minglish lesson
# ===============
#
# Welcome to the lab, minion. Henceforth you shall do the bidding of Professor Boolean. Some say he's mad, trying to develop a zombie serum and all... but we think he's brilliant!
#
# First things first - Minions don't speak English, we speak Minglish. Use the Minglish dictionary to learn! The first thing you'll learn is how to use the dictionary.
#
# Open the dictionary. Read the page numbers, figure out which pages come before others. You recognize the same letters used in English, but the order of letters is completely different in Minglish than English (a < b < c < ...).
#
# Given a sorted list of dictionary words (you know they are sorted because you can read the page numbers), can you find the alphabetical order of the Minglish alphabet? For example, if the words were ["z", "yx", "yz"] the alphabetical order would be "xzy," which means x < z < y. The first two words tell you that z < y, and the last two words tell you that x < z.
#
# Write a function answer(words) which, given a list of words sorted alphabetically in the Minglish alphabet, outputs a string that contains each letter present in the list of words exactly once; the order of the letters in the output must follow the order of letters in the Minglish alphabet.
#
# The list will contain at least 1 and no more than 50 words, and each word will consist of at least 1 and no more than 50 lowercase letters [a-z]. It is guaranteed that a total ordering can be developed from the input provided (i.e. given any two distinct letters, you can tell which is greater), and so the answer will exist and be unique.
#
# Languages
# =========
#
# To provide a Python solution, edit solution.py
# To provide a Java solution, edit solution.java
#
# Test cases
# ==========
#
# Inputs:
#     (string list) words = ["y", "z", "xy"]
# Output:
#     (string) "yzx"
#
# Inputs:
#     (string list) words = ["ba", "ab", "cb"]
# Output:
#     (string) "bac"

def answer(words):
    # Build the grap and keep track of entry points
    graph, start = dag(words)
    # Place to store the final alphabet
    alphabet = []
    # Place to store nodes we have visited whe traversign the graph (Depth First)
    visited = Set()

    # Visit the nodes
    def visit(node):
        # If node has not been visited
        if node not in visited:
            # Mark it as visited
            visited.add(node)
            # If node is in graph
            if node in graph:
                # Visit each of this nodes edges
                for edge in graph[node]:
                    visit(edge)
            alphabet.insert(0, node)

    # For each node in the entry point set... This should be only ONE node becuase the question stated there is a single unique solution.
    for node in start:
        visit(node)
        
    # Return the alphabet
    return ''.join(alphabet)


def dag(words):
    # The graph
    graph = {}
    # Where to enter the graph
    start = Set()

    def find_edge(word1, word2):
        # look over the letter pairs (shorter word of course)
        for l in range(min(len(word1), len(word2))):
            # if letters do not match, we found a new edge connection
            if word1[l] != word2[l]:
                # Keep track of possible entry points
                start.add(word1[l])
                start.add(word2[l])
                # return the edge
                return word1[l], word2[l]

    for i in range(len(words) - 1):
        # make sure the graph will contain all nodes
        if not graph.has_key(words[i]):
            graph[words[i]] = Set()
        if not graph.has_key(words[i+1]):
            graph[words[i+1]] = Set()

        # Find an edge
        edge = find_edge(words[i], words[i+1])

        # If we found an edge, make sure to add it
        if edge is not None:
            a,b = edge
            # Dont forget to remove the edge node from the potential starting points list
            if b in start:
                start.remove(b)
            # If node is already in graph, add the edge
            if a in graph:
                graph[a].add(b)
            # If not, add them both... this might be redundant...
            else:
                graph[a] = Set(b)

    # Return teh graph and start position
    return graph, start

words = ["y", "z", "xy"]
# output = "yzx"
words1 = ["z", "yx", "yz"]
# output = "xzy"
words2 = ["ba", "ab", "cb"]
# output = "bac"
words3 = ["bbc", "bac", "cba"]
# output = "bac"
print(answer(words1))
