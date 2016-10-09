
# Part 1: Discussion

# 1. What are the three main design advantages that object orientation
#    can provide? Explain each concept.
#    1) The three main design advantages of object orientation:
#     A) Encapsulation - meaning our code is organized, susinct and has a predictable pattern to how it is organized for usability

#     B) Abstraction - meaning the functionality of the code is not dependent on line by line understanding of the code runs but its predictable patterend functionality makes it nearly obvious to the user how to interface with the code

#     C) Polymorphism- meaning our code makes it easy to rerun the same code with slight veriation and get a predictable desired output over and over again

# 2. What is a class?
#     A class is an object type that can be interacted with using predictable code interface. These objects have specific attributes and behaviors that have been embuded to it by the creator through a standardized code format to enable the create of many instances of these class objects

# 3. What is an instance attribute?
#     An instance attribute is a unique value that is bound to a method of an instance of a class. 

# 4. What is a method?
#     A method is a way of setting or refering to an instance of a class's instance or class attributes. 

# 5. What is an instance in object orientation?
#     An instance is an example of a class object. When invoked(created) it has all the functionality that the class has capasity for but it can have unique values bound to it called attributes. 

# 6. How is a class attribute different than an instance attribute?
#    Give an example of when you might use each.
#    A class attribute can be over written if you assign a new value after intialization, then the attribute becomes an isntance attribute
#    A class attribute is what comes automatically with the intialization of all objects types of that class.
#    An instance attribute is unique to the instance of the class and may have been granted at intialization or later

#         A) Example of a class attribute: this depends on the class but if we have class human we could intialize them all with two legs, as this is standard human appareance.
#         B) Example of an instance attribute: If the human instance we are working with happens to be unique and be missing a leg we can call the method again on the instance and assign it to 1 leg or 0 legs this normally class attribute has know become an instance attribute specific to this object human is missing some legs!
        
#             An isntance attribute may be passed in at intialization which would be a unique attribute for each new instance like name, not all humans should be intialized with the name bob, roll call would be confussing so we can pass in an instance attribute of name that when we make a human we can pass in unique "instance attributes" of that will be bound to the method name, so we can make humans named Greer, and Nell, etc. 


#    (object):
#        """docstring for 
#        """
#        def __init__(self, arg):
#            super(
#             , self).__init__()
#            self.arg = arg
           




# Parts 2 through 5:
# Create your classes and class methods
#2.1)
class Student(object):
  """ Create a Student Object with instance attributes first name, last name, address"""
  def __init__(self, first_name, last_name, address):
    self.first_name = first_name
    self.last_name = last_name
    self.address = address

#Driver Code for Student Class = pass
# sarah = Student("Sarah", "Story", "195 Brattlebrook ln")
# print sarah
# print sarah.first_name
# print sarah.last_name
# print sarah.address

#2.2)
class Question(object):
  """Creates a Question object takes in instance attributes of question and correct_answer and a method ask_and_evaluate which returns a boolan if the question is answered correctly by user """
  def __init__(self, question, correct_answer):
    self.question = question
    self.correct_answer = correct_answer


  def ask_and_evaluate(self):
    """Asks the user to answer a given question and Returns a boolan if the question is answered correctly by user """
    answer = raw_input("What is the answer to, {}\n>>".format(self.question))
    return answer == self.correct_answer

# Driver Code for Question Class = pass
# id_question = Question("What is your mothers maiden name?", "Golden")
# print id_question
# print id_question.question
# print id_question.correct_answer
# print id_question.ask_and_evaluate()

#2.3)
class Exam(object):
  """Creats an Exam object that takes in a value for a name instance attribute and asigns a list to the class attribute questions, has bethods add_question and administer"""
  def __init__(self, name):
    self.name = name
    self.questions = []

  def add_question(self, question, correct_answer):
    """Intializes a Question object. Takes in perameters question and correct_answer binds these values to the Question object's similiarly named instance attributes"""
    self.questions.append(Question(question,correct_answer.lower()))
 
  def administer(self):
    """Goes through each question in the exam object and returns an interger score.
     Evaluates questions using a Question object method ask_and_evaluate. """
    score = 0
    for question in self.questions:
      if Question.ask_and_evaluate(question):
        score +=1
    return score
    
#Driver Code for Exam Calss = pass
# final_exam = Exam("Final Exam")
# print final_exam
# print final_exam.name
# print final_exam.questions
# final_exam.add_question("What is your mother's maiden name?", "Golden")
# print final_exam.questions
# print final_exam.administer()

class Quiz(Exam):
  """ Creates a Quiz object that inherites from Exam all its intialization attributes. 
  Varies from Exam in administer method """
  def administer(self):
    """ Evaluates all exam questions and returns either True if passed half the questions or False if failed over half the questions"""
    print len(self.questions)
    pass_grade = (len(self.questions))/2.0
    print pass_grade
    return super(Quiz, self).administer() >= pass_grade

#Driver Code for Quiz Class = pass
# quiz = Quiz("Quiz 1")
# quiz.add_question("What color is the sky?", "Sky-Blue")
# print quiz.administer()

      
#PART 4
#4.1

def take_test(exam, student):
  """ Creates a Student object instance attribute called score using Exam object method administer. Returns None, just a feeder method."""
  student.score = exam.administer()

#Driver code for take_test = pass
# exam = Exam("Final")
# student = Student("S", "S", "7th St")
# take_test(exam, student)
# print student.score


def example(student_first_name, student_last_name, student_address, exam_name="My Favorites"):
  """Takes perameters strings of a student first name, second name, and addresss, and an exam name with defult to My Favorites. Returns None but creates an Exam object called exam, a Student Object called student and goes through a set of pre-filled questions with answers and runs method take_test."""
  exam = Exam(exam_name)

  question_list = [("What is my favorite color", "Yellow"), 
                    ("What is my favorite food", "Toast"), 
                    ("What is my favorite Country","Italy"), 
                    ("What is my favorite language", "German")]
  
  for element in question_list:
      exam.add_question(element[0], element[1])
    
  student = Student(student_first_name, student_last_name, student_address)

  take_test(exam, student)

  # print student.score
  

#Driver code for example = pass
# example("Sarah", "Story", "195 Brattlebrook ln") 






