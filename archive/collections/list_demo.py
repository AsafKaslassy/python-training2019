courses = ['History', 'Math', 'Physics', 'CompSci']
courses_2 = ['Art', 'Education']

editing_courses = courses

print('Prints the list of all courses:')
print(editing_courses)

print('Prints the space 0 at the courses list(like array):')
print(editing_courses[0])

print('Negative works also, always gets the last item:')
print(editing_courses[-1])

print('Range of values, not includes the ending index value(0:2):)')
print(editing_courses[0:2])

print('Range of values, starting in the variable and print all the list,it called \'slicing\' (2:):')
print(editing_courses[2:])

print('Another list insertion in index 0:')
editing_courses.insert(0, courses_2)
print(editing_courses)
editing_courses.remove(courses_2)
print('After removed: {}'.format(editing_courses))

print('Another list extend, in index 0 and 1:')
editing_courses.extend(courses_2)
print(editing_courses)


def clear_list(self, edited_courses):
    self.editing_courses = edited_courses
    while not len(courses_2):
        x = 0
        self.editing_courses = edited_courses
        editing_courses.remove(courses_2[x])
        x += 1
        print('courses.remove(courses_2[x]):\n {}'.format(editing_courses))
    return self.editing_courses


clear_list(courses)

print(editing_courses)

# print(courses)
