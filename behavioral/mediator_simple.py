import logging

logging.basicConfig(level='INFO')


class Course(object):
    """Mediator class."""
 
    def display_course(self, user, course_name):
        logging.info("[{}'s course ]: {}".format(user, course_name))
 
 
class User(object):
    '''A class whose instances want to interact with each other.'''
 
    def __init__(self, name):
        self.name = name
        self.course = Course()
 
    def send_course(self, course_name):
        self.course.display_course(self, course_name)
 
    def __str__(self):
        return self.name
 
def main():
    
    mayank = User('Mayank')   # user object
    lakshya = User('Lakshya') # user object
    krishna = User('Krishna') # user object
 
    mayank.send_course("Data Structures and Algorithms")
    lakshya.send_course("Software Development Engineer")
    krishna.send_course("Standard Template Library")

if __name__ == "__main__":
    main()