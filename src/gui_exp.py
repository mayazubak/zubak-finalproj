import random
from datetime import datetime
from config.config import Config

from PIL import Image, ImageTk

import tkinter as tk

SHAPES = Config.SHAPES
WORDS = Config.WORDS
SHAPE_PATHS = Config.SHAPE_PATHS
from datetime import datetime

# chat gpt assisted me in the logic for checking if the user ordered numbers correctly and checking image paths in identity shape
# also gave me a quick 'crash course' in how to use map


class GUITest:
    def __init__(self, root):
        self.root = root
        self.frame = tk.Frame(self.root, bg="white")
        self.frame.pack(expand=True, fill="both")
        
        self.score = 0
        self.responses = {}
        self.shape_score = 0

        
        self.questions = [
            "What is today's date? (Answer in this format: MM/DD/YYYY): ",
            "What city and state are you located in? (Answer in this format: City, State): ",
            "What color is a banana?: ",
            "What is the capital of Illinois?: ",
            "What's 5 plus 20?: ",
            "Spell the word 'table' backwards: ",
            "Please type the word: 'psychology' to continue: "
        ]
        
        self.label = tk.Label(self.frame, text="", font =(Config.instructions_font, Config.instructions_font_size), bg="white")
        self.entry = tk.Entry(self.frame, font=(Config.instructions_font, 16), width= 25)
        self.button = tk.Button(self.frame, text="Submit", command=self.submit_answer)
     
    def start(self):
        self.next_question()
        
    def next_question(self):
        if self.question_index == len(self.questions):
            self.label.config(text="Thank you for your responses!")
            self.entry.pack_forget()
            self.button.pack_forget()
            return
        
        self.label.config(text=self.questions[self.question_index])
        self.label.pack(pady=20)
        self.entry.pack(pady=20)
        self.button.pack(pady=20)
         
         
    def submit_answer(self):
        answer = self.entry.get().strip()
        key = self.questions[self.question_index][1]
        self.responses[key] = answer
        self.question_index += 1
        self.next_question()
        
# word recall tasks
    
    def word_recall(self):
        self.sample_words = random.sample(WORDS, 3)
        self.label.config(text="Please remember the presented words:\n\n" + ", ".join(self.sample_words))
        self.button.config(text="Continue", command=self.recall_words)
        self.entry.pack_forget()
        # print("\nPlease remember the following words for later:")
        # print(", ".join(sample_words))
        # input("\nPress Enter when you're ready to continue...")
        # recalled_words = input("Recall the words you just saw, separated by commas: ").lower().split(", ")
        # self.responses['recalled_words'] = recalled_words
        # self.responses['sample_words'] = sample_words
        
    def recall_words(self):
        self.label.config(text="Recall the words you just saw, separated by commas: ")
        self.entry.delete(0, tk.END)
        self.entry.pack(pady=10)
        self.button.config(text="Submit", command=self.score_recall)
        
    def score_recall(self):
        recalled = self.entry.get().strip().lower().split(", ")
        self.responses['recalled_words'] = recalled
        self.responses['sample_words'] = self.sample_words
        correct_words = [word for word in recalled if word.strip() in self.sample_words]
        self.score += len(correct_words)
        
# ORDER NUMBERS TASK        
    def order_numbers(self, length):
        self.digits = [random.randint(0, 100) for i in range(length)]
        self.label.config(text="Please enter the following numbers in increasing order: ")
        self.label.config(text=" ".join(map(str, digits)))
        self.entry.delete(0, tk.END)
        self.entry.pack(pady=10)
        self.button.config(text="Submit", command=self.check_order)
       # print(f"\nDigit sequence (unsorted): {' '.join(map(str, digits))}")
      #  user = input("Please enter the follwing numbers in increasing order: ")
      
    def check_order(self):
        try:
            order = [int(x) for x in self.entry.get().split()]
        except:
            order = []
        self.responses['unordered_prompt'] = sorted(self.digits)
        self.responses['ordered_input'] = order
        if order == sorted(self.digits):
            self.responses["order_score"] = 1
        else:
            self.responses["order_score"] = 0
    
    
 # RECALL DIGITS TASK   
 
    def digit_recall(self, length):
        self.digits = [random.randint(0,9) for i in range(length)]
        # print("\nFor this next task, you will be asked to recall a sequence of numbers.")
        # print(f"The numbers will be presented now: {' '.join(map(str, digits))}") 
        # input("\nHit the 'enter key when you are ready to keep going. ")
        # recall = input("Now recall the digits in the order they appeared. ")
        self.label.config(text="For this next task, you will be asked to recall a sequence of numbers.")
        self.label.config(text=f"The numbers will be presented now: {' '.join(map(str, self.digits))}")
        self.entry.delete(0, tk.END)
        self.entry.pack(pady=10)
        self.button.config(text="Submit", command=self.ask_recall)
        self.entry.pack_forget()
    
    def ask_recall(self):
        self.label.config(text="Now recall the digits in the order they appeared.") 
        self.entry.delete(0, tk.END)
        self.entry.pack(pady=10)
        self.button.config(text="Submit", command=self.check_recall)
        
    def check_recall(self):
        try:
            recalled = [int(x) for x in self.entry.get().split()]
        except:
            recalled = []
        self.responses['digits_presented'] = self.digits
        self.responses['digits_recalled'] = recalled
        if recalled == self.digits:
            self.responses["recall_score"] = 1
        else:
            self.responses["recall_score"] = 0

 # IDENTIFY SHAPES TASK   
    def identify_shape(self, num=5):
        self.shape_index = 0
        self.shape_inputs = []
        self.shape_targets = random.choices(SHAPES, k=num)
        self.responses["shape_prompts"] = self.shape_targets
    
        
        self.label.config(text="For this task, you will identify shapes. Please identify the following:")
        self.entry.delete(0, tk.END)
        self.entry.pack(pady=10)
        self.button.config(text="Submit", command=self.check_shape)
        
        self.next_shape()
        
    def next_shape(self):
        if self.shape_index >= len(self.shape_targets):
            self.responses["shape_prompts"] = self.shape_targets
            self.responses["shape_guesses"] = self.shape_inputs
            self.responses["shape_score"] = self.shape_score
            
            self.label.config(text="The shape task is now complete!")
            self.entry.pack_forget()
            self.button.pack_forget()
            return
        
        shape = self.shape_targets[self.shape_index]
        image_path = SHAPE_PATHS.get(shape)
        img = Image.open(image_path)
        img = img.resize(300,300)
        self.tk_img = ImageTk.PhotoImage(img)
        self.label.config(image=self.tk_img, text="")
        
        self.entry.delete(0, tk.END)
        self.label.pack(pady=20)
        self.button.config(text="Submit", command=self.check_shape)
        
    
    def check_shape(self):
        guess = self.entry.get().strip().lower()
        correct_shape = self.shape_targets[self.shape_index]
        
        if guess == correct_shape:
                self.shape_score += 1
                
        self.shape_inputs.append(guess)
        self.shape_index += 1
        self.entry.delete(0, tk.END)
        self.next_shape()
        
        # inputs = []
        # self.responses['shape_prompts'] = []
        # print("\n For this task, you will identiy shapes. Please idenity the following: ")
        # for i in range(num):
        #     shape = random.choice(SHAPES)
        #     image_path = SHAPE_PATHS.get(shape)
        #     self.responses['shape_prompts'].append(shape)
        #     print(f"Shape {i + 1}: Check image at {image_path}")
        #     user_guess = input("What shape is this? ")
        #     inputs.append(user_guess)
        # return inputs
        
    def calculate_score(self):
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
        
           
    # def ask_initial_questions(self):
        
    #     # asks preliminary cognitive function questions to asses user's basic orientation
    #     # stores responses in a list
        
    #     print("Welcome! Please answer the following questions.")
        
    #     # date
    #     date_response = input("What is today's date? (Answer in this format: MM/DD/YYYY): ")
    #     self.responses['date'] = date_response
        
    #     # location
    #     loc_response = input("What city and state are you located in? (Answer in this format: City, State): ")
    #     self.responses['location'] = loc_response
        
    #     # attention check 1 / identify
    #     attention1_response = input("What color is a banana?: ")
    #     self.responses["check1"] = attention1_response
        
    #     # identify capital
    #     identify_response = input(("What is the capital of Illinois?: "))
    #     self.responses['capital'] = identify_response
        
    #     # quick math
    #     math_respone = input("What's 5 plus 20?: ")
    #     self.responses["math"] = math_respone
        
    #     # reverse spelling
    #     reverse_response = input("Spell the word 'table' backwards: ")
    #     self.responses["reverse"] = reverse_response
        
    #     # attention check 2 
    #     attention2_response = input("Please type the word: 'psychology' to continue: ")
    #     self.responses["check2"] = attention2_response
       
        
        
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
        
        score += self.responses.get("order_score", 0)
        score += self.responses.get("recall_score", 0)
        score += self.responses.get("shape_score", 0)
        score += self.score 

        return self.score
            

    

if __name__ == "__main__":
    root = tk.Tk
    root.title("Experiment")
    root.geometry(f"{Config.window_width}x{Config.window_height}")
    root.configure(bg="white")
    
    test = GUITest(root)
    test.start()
    
    root.mainloop()
    