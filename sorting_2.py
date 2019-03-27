"""
list in the nested dictionary sorting
"""
stu_marks = [{"name": "siva", "marks": 100}, {"name": "rams", "marks": 20},
             {"name": "reddy", "marks": 500}]

# using sorted function it will sort the program
# using lambda based on keys
stu_marks = sorted(stu_marks, key=lambda l: l["marks"], reverse=False)
print stu_marks
