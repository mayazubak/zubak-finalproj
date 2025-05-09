from src import exp
from src import gui
from src.gui_test import Test

# test file description

def main():
    test = Test()
    test.ask_initial_questions()
    test.word_recall()
    test.order_numbers(5)
    test.digit_recall(5)
    test.identify_shape(5)
    final_score = test.calculate_score()
    print(f"\nYour final score: {final_score}")

    
    # test launches, programs creates an instance of the Test class
    
    # runs ask_initial_questions(), stores responses/score
    
    # program calls generate_digits() to print a sequence of numbers
    # user tasked with repeating numbers back, stores responses/scores
    
    # program calls generate_shape(), user is asked to identify shape, 
    # stores repsonse/score
    
    # program calls calculate_score() to calculate overall score based on
    # stored information from other tasks, finals scoe then printed. 
   
       

if __name__ == '__main__':
    main()
