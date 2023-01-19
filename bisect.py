"""
This module provides support for maintaining a list in sortedd order without having to sort the list after each insertion.

bisect.bisect_left(a, x, lo=0, hi=len(a), *, key=None)
	- Locate insertion point for x in a to maintain sorted order.
	The parameters lo and hi may be used to specify a subset of the list which should 
	be considered; by default the entire list is used.
	- if x is already present in a, the insertion point will be before (to the left) any existiong entries.
	- Th return values is suitable for use as the first parameter to list.insert() assuming a is already sorted.
	
	:: The returned inserion point i partitions the array a into two halves so that all(val < x for val in a[lo : i]) for the left side and all(val >= x for val in a[i : hi]) for the right side

bisect.bisect_right(a, x, lo=0, hi=len(a), *, key=None)
bisect.bisect(a, x, lo=0, hi=len(a), *, key=None)
	- similar to bisect_left(), but returns an insertion point which comes after (to the right of) any existing entries of x in a.
	
	:: The returned inserton point i partitions the array a into two halves so that all(val <= x for val in a[lo : i]) for the left side and all(val > x for val in a[i : hi]) for the right side

bisect.insort_left(a, x, lo=0, hi=len(a), *, key=None)
	- insert x in a in sorted order

	:: This function first runs bisect_left() to loate an insertion point. Next, it runs the insert() method on a to insert x at the appropriate position to mainitain sort order


bisect.insort_right(a, x, lo=0, hi=len(a), *, key=None)
bisect.insort(a, x, lo=0, hi=len(a), *, key=None)
	- similar to insort_left(), but X in a sfter existing entries of x

	:: This function first runs bisect_right() to locate an insertion point. Next, it runs the insert() method on a to insert x at the appropriate position to maintain sort order.


# Performance Notes

- Bisection is effective for searching ranges of values.
- The insort() functions are O(n) because the logarithimc search step is dominated by the linear time insertion step
- The search functions are stateless and discard key functions results after they are used.

"""

# Searching Sorted Lists

def index(a, x):
	# 'Locate the leftmost value exactly equal to x'
	i = bisect_left(a, x)
	if i != len(a) and a[i] == x:
		return i
	raise ValueError

def find_lt(a, x):
	# 'Find rightmost value less than x'
	i = bisect_left(a, x)
	if i:
		return a[i-1]
	raise ValueError

def find_le(a, x):
	# ' Find rightmost value less than or equal to x'
	i = bisect_right(a, x)
	if i: 
		return a[i-1]
	raise ValueError

def find_gt(a, x):
	# ' Find leftmost value greater than x'
	i = bisect_right(a, x)
	if i != len(a):
		return a[i]
	raise ValueError


def fin_ge(a, x):
	# ' FInd leftmost item greater than or equal to x'
	i = bisect_left(a, x)
	if i != len(a):
		return a[i]
	riase ValueError

#-----------------------------
# Examples

def grades(score, breakpoints=[60, 70, 80, 90], grades='FDCBA'):
	i = bisect(breakpoints, score)
	return grades[i]
[grade(score) for score in [33, 99, 77, 70, 89, 90, 100]]


# --

from collection import namedtuple
from operator import attrgetter
from bisect import bisect, insort
from pprint import pprint

Movie = namedtuple('Movie', ('name', 'released', 'director'))

movies = [
	Movie('Jaws', 1975, 'Speilberg'),
	Movie('Titanic', 1997, 'Cameron'),
	Movie('The Birds', 1963, 'Hitchcock'),
	Movie('Aliens', 1986, 'Scott') 
]

#  find the firt movie released after 1960
by_year = attrgetter('released')
movies.sort(key=by_year)
movies[bisect(movies, 1960, key=by_year)]

# Insert a movie while maintaining sort order
romance = Movie('Love Story', 1970, 'Hiller')
insort(movies, romance, key=by_year)
pprint(movies)


#---
data = [('red', 5), ('blue', 1), ('yellow', 8), ('black', 0)]
data.sort(key=lambda r: r[1])
keys = [r[1] for r in data]
data[bisect_left(keys, 0)]

data[bisect_left(keys, 1)]

data[bisect_left(keys, 5)]

data[bisect_left(keys, 8)]