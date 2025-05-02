import random
from config.config import SHAPES, WORDS, SHAPE_PATHS
from datetime import datetime

# chat gpt assisted me in the logic for checking if the user ordered numbers correctly and checking image paths in identity shape
# also gave me a quick 'crash course' in how to use map


class Test:
    def __init__(self):
        self.score = 0
        self.responses = {}
        
    def ask_initial_questions(self):
        
        # asks preliminary cognitive function questions to asses user's basic orientation
        # stores responses in a list
        
        print("Welcome! Please answer the following questions.")
        
        # date
        date_response = input("What is today's date? (Answer in this format: MM/DD/YYYY): ")
        self.responses['date'] = date_response
        
        # location
        loc_response = input("What city and state are you located in? (Answer in this format: City, State): ")
        self.responses['location'] = loc_response
        
        # attention check 1 / identify
        attention1_response = input("What color is a banana?: ")
        self.responses["check1"] = attention1_response
        
        # identify capital
        identify_response = input(("What is the capital of Illinois?: "))
        self.responses['capital'] = identify_response
        
        # quick math
        math_respone = input("What's 5 plus 20?: ")
        self.responses["math"] = math_respone
        
        # reverse spelling
        reverse_response = input("Spell the word 'table' backwards: ")
        self.responses["reverse"] = reverse_response
        
        # attention check 2 
        attention2_response = input("Please type the word: 'psychology' to continue: ")
        self.responses["check2"] = attention2_response
        
    def word_recall(self):
        sample_words = random.sample(WORDS, 3)
        print("\nPlease remember the following words for later:")
        print(", ".join(sample_words))
        input("\nPress Enter when you're ready to continue...")
        recalled_words = input("Recall the words you just saw, separated by commas: ").lower().split(", ")
        self.responses['recalled_words'] = recalled_words
        self.responses['sample_words'] = sample_words
        
    def order_numbers(self, length):
        digits = [random.randint(0, 100) for _ in range(length)]
        print(f"\nDigit sequence (unsorted): {' '.join(map(str, digits))}")
        user = input("Please enter the follwing numbers in increasing order: ")
        try:
            input_sorted = [int(x) for x in user.split()]
        except:
            input_sorted = []
        self.responses['unordered_prompt'] = sorted(digits)
        self.responses['ordered_input'] = input_sorted
        return input_sorted   
    
    def digit_recall(self, length):
        digits = [random.randint(0,9) for i in range(length)]
        print("\nFor this next task, you will be asked to recall a sequence of numbers.")
        print(f"The numbers will be presented now: {' '.join(map(str, digits))}") 
        input("\nHit the 'enter key when you are ready to keep going. ")
        recall = input("Now recall the digits in the order they appeared. ")
        try:
            recalled  = [int(x) for x in recall.split()]
        except:
            recalled = []
        self.responses['digits_presented'] = digits
        self.responses['digits_recalled'] = recalled
        return recalled

    
    def identify_shape(self, num):
        inputs = []
        self.responses['shape_prompts'] = []
        print("\n For this task, you will identiy shapes. Please idenity the following: ")
        for i in range(num):
            shape = random.choice(SHAPES)
            image_path = SHAPE_PATHS.get(shape)
            self.responses['shape_prompts'].append(shape)
            print(f"Shape {i + 1}: Check image at {image_path}")
            user_guess = input("What shape is this? ")
            inputs.append(user_guess)
        return inputs
        
        
    def calculate_score(self):
        # calculates scores based on all the questions in above tasks
        score = 0
        
        # whats the date
        todays_date = datetime.today().strftime("%m/%d/%Y") # googled how to get accurate date, learned about datetime library
        if self.responses.get("date", "").strip() == todays_date:
            score +=1
        
        # where are you right now
        accepted_locations = ["champaign, il", "champaign, illinoi", "urbana,il", "urbana, illinois"]
        if self.responses.get("location", "").strip().lower() in accepted_locations:
            score += 1
            
        # AC 1 - banana color
        if self.responses.get("check1", "").lower() == "yellow":
            score += 1
        
        # capital
        if self.responses.get("capital", "").lower() == "springfield":
            score += 1
        
        # math
        if self.responses.get("math", "") == "25":
            score += 1
            
        # AC 2
        if self.responses.get("check2", "").lower() == "psychology":
            score += 1
        
        # reverse spelling
        if self.responses.get("reverse", "").lower() == "elbat":
            score += 1
            
        # sorted digits
        if self.responses.get('ordered_input', []) == self.responses.get('unordered_prompt', []):
            score += 1
        
        # recall digits
        if self.responses.get('digits_presented', []) == self.responses.get('digits_recalled', []):
            score += 1
        
        # identify shapes
        chosen_words = self.responses.get("sample_words", [])
        recalled = self.responses.get("recalled_words", [])
        correct_words = [word for word in recalled if word.strip() in chosen_words] # chatgpt helped me w string comprehension 
        score += len(correct_words)
        
        self.score = score
        return score
            

def main():
    test = Test()
    test.ask_initial_questions()
    test.word_recall()
    user_digits_input = test.order_numbers(5)
    memory_digits_input = test.digit_recall(5)
    shape_guesses = test.identify_shape(5)
    final_score = test.calculate_score()
    print(f"\nYour final score: {final_score}")

if __name__ == "__main__":
    main()