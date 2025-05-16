# zubak-finalproj
 
**1. Program logic:**

My project will be an implementation of a combination of the Mini-Mental State Examination (MMSE), and the Digit Span test, and other memory recall tasks. The MMSE is a series of questions that is aimed to measure cognitive impairment. Digit span is a test that measures short-term memory and working memory by testing one's ability to repeat a series of numbers in order. The MMSE is specifically designed to measure cognitve impairment in older individuals, but I believe that it can be integrated with the digit span test to be able to measure a larger range of people. 


**2. UPDATED FUNCTIONS:**

### Function 1: start(self)
Begins the experiment by loading initial instructions and starting the questions.

### Function 2: submit_answer(self)
Collects and stores user responses to the initial questions.

### Function 3: word_recall(self)
Gives three words for the user to memorize, then prompts them to recall those words after a delay.

### Function 4: digit_recall(self)
this function presents 5 digits for users to remember, after 10 second delay the users will be prompted to recall the words
*need to implement delay*

### Function 5: calculate_score(self)
Calculates the user’s total score by grading each task response by accuracy. (+1 for correct answer, +0 for incorrect answer)

### Function 6: show_final_score(self)
Shows the user’s final score and gives them feedback based on their results.


**3. Example use cases:**

- in a hospital setting to quickly measure preliminary cognitive function
- research settings to compare cognitive function of younger and older patients
- personal or self testing to measure one's own cognitive health. 

