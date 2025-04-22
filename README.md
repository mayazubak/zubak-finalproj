# zubak-finalproj
 
**1. Program logic:**

My project will be an implementation of a combination of the Mini-Mental State Examination (MMSE), and the Digit Span test. The MMSE is a series of questions that is aimed to measure cognitive impairment. Digit span is a test that measures short-term memory and working memory by testing one's ability to repeat a series of numbers in order. The MMSE is specifically designed to measure cognitve impairment in older individuals, but I believe that it can be integrated with the digit span test to be able to measure a larger range of people. 


**2. UPDATED FUNCTIONS:**

### Function 1: ask_initial_questions(self)

this function begins with asking users initial questions to measure their orientation (date, location) and general cognition

### Function 2: run_memory_recall(self)
this function presents 3 words for users to remember, after 10 second delay the users will be prompted to recall the words
*need to implement delay*

### Function 3: order_numbers(self, length)
this function will present users with a list of numbers between 0 and 100, and they will be asked to order the numbers in increasing order


### Function 4: digit_recall(self)
this function presents 5 digits for users to remember, after 10 second delay the users will be prompted to recall the words
*need to implement delay*


### Function 5: identify_shape(self, num)
this function presents the user with images of shapes, users are asked to identify what the shape is.


### Function 6: calculate_score(self)
this function calculates the user's overall score, with each correct answer earning 1 point and incorrect answer earning 0.


**3. Example use cases:**

- in a hospital setting to quickly measure preliminary cognitive function
- research settings to compare cognitive function of younger and older patients
- personal or self testing to measure one's own cognitive health. 

