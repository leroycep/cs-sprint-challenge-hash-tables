# Sprint Challenge: Hash Tables

**Read these instructions carefully. Understand exactly what is expected
_before_ starting this Sprint Challenge.**

This challenge allows you to practice the concepts and techniques learned over
the past sprint and apply them in a concrete project. This sprint explored hash
tables. During this sprint, you studied hash functions, collision resolution,
complexity analysis of hash tables, load factor, resizing, and various use cases
for hash tables. In your challenge this week, you will demonstrate mastery of
these skills by solving five problems related to hash tables.

The sprint challenge is an individual assessment. All work must be your own.
Your challenge score is a measure of your ability to work independently using
the material covered through this sprint. You need to demonstrate proficiency in
the concepts and objectives introduced and practiced in preceding days.

You are not allowed to collaborate during the sprint challenge. However, you are
encouraged to follow the twenty-minute rule and seek support from your TL if you
need direction.

_You have **three hours** to complete this challenge. Plan your time
accordingly._

## Introduction

This challenge requires you to solve algorithm problems that are amenable to
being solved efficiently with a hash table.

### Commits

Commit your code regularly and meaningfully. This practice helps both you (in
case you ever need to return to old code for any number of reasons) and your
Team Lead as they evaluate your solution.

## Interview Questions

Be prepared to demonstrate your understanding of this week's concepts by
answering questions on the following topics. You might prepare by writing down
your answers beforehand.

1. Hashing functions
   - Generate pseudo-random numbers based on it's input
   - The same input always generates the same output
   - A good hash function will:
     - have very different outputs for small changes in the input
     - have uniformly distributed output values (outputs don't cluster around
       certain values)
2. Collision resolution
   - Problem: Two hashes come out to the same index in the hashtables array
   - There are many strategies for handling this problem
     - One solution is to make each slot in the array a linked list
       - Then the collision is handled by appending to the linked list
     - Another solution is just going to the next position in the array
3. Performance of basic hash table operations
   - Hashtables, on average, implement `Get`, `Set`, and `Delete` in `O(1)` time
4. Load factor
   - This is how full the hash table is
   - Calculated as number of filled slots over the capacity of the hashtable
     array
   - A low load factor means that space is being wasted
   - A high load factor means that the hashtable is getting slower
   - 0.7 is a "magic number" that the load factor should be less than
5. Automatic resizing
   - 0.7 is a "magic number" that the load factor should be less than
   - When a hashtable's load factor exceeds `0.7`, the array should resized
   - Making the hashtable double in size prevents excessive resizing
6. Various use cases for hash tables
   - Since hash tables implement `get`, `set`, and `delete` in constant time
     they have a lot uses
   - Caching
     - If something is expensive to calculate, but cheap to store, you can stick
       it in a hashmap, using the input as a key and the output as the value
   - Key-Value Map
     - Without a hashtable, you have two simple ways to store key value pairs:
       - Constant offsets in memory that you know ahead of time, the key in this
         case being the offset from the pointer, and the value at the pointer
         plus the offset
         - This doesn't allow dynamic key values
       - A list of key-value pairs
         - This solution allows dynamic key values, but has `O(n)` lookup times
     - Hashtables takes the list of key-value pairs, and place them in an array
       according to it's hash function
       - The hash functions a "shortcut" to the key-value pair in the array
       - Since hash tables are just lists with keys placed in a convienent
         index, it's performance can degrade to `O(n)`
         - That's why it's important to have a good hash function and to
           maintain a low load factor

We expect you to be able to answer questions in these areas. Your responses
contribute to your Sprint Challenge grade.

## Instructions

### Task 1: Project Set-Up

- [x] Create a forked copy of this project
- [x] Add your team lead as a collaborator on Github
- [x] Clone your OWN version of the repository (Not Lambda's by mistake!)
- [x] Create a new branch: git checkout -b `<firstName-lastName>`.
- [x] Implement the project on your newly created `<firstName-lastName>` branch,
      committing changes regularly
- [x] Push commits: git push origin `<firstName-lastName>`

### Task 2: Project Requirements

Your finished project must include all of the following requirements:

- [x] Solve any three of the five problems

For each problem that you choose to solve, complete the following:

- [x] Navigate into each exercise's directory
- [x] Read the instructions for the exercise in the README
- [x] Implement your solution in the `.py` skeleton file
- [x] Make sure your code passes the tests running the test script with make
      tests

_Note: For these exercises, we expect you to use Python's built-in `dict` as a
hashtable. That said, if you wish, you can attempt to solve using your own
hashtable implementation, as well. All solutions should utilize a `dict` or
hashtable. You should not use Sets. (Though you can make a `dict` behave like a
set if you wish.)_

### Task 3: Stretch Goals

After finishing your required elements, you can push your work further. These
goals may or may not be things you have learned in this module, but they build
on the material you just studied. Time allowing, stretch your limits, and see if
you can deliver on the following optional goals:

- [x] Solve any four of the five problems
- [x] Solve all five problems

## Submission format

Follow these steps to complete your project.

- [x] Submit a Pull-Request to merge <firstName-lastName> Branch into master
      (student's Repo). **Please don't merge your own pull request**
- [x] Add your team lead as a reviewer on the pull-request
- [x] Your team lead will count the project as complete after receiving your
      pull-request
