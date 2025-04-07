# zubak-finalproj
 
**1. Program logic:*
*
My project will be an implementation of a combination of the Mini-Mental State Examination (MMSE), and the Digit Span test. The MMSE is a series of questions that is aimed to measure cognitive impairment. Digit span is a test that measures short-term memory and working memory by testing one's ability to repeat a series of numbers in order. The MMSE is specifically designed to measure cognitve impairment in older individuals, but I believe that it can be integrated with the digit span test to be able to measure a larger range of people. 


**2. Functions and the parameters they take:*
*
Function 1: generateDigits(length, delivery)

this function will be how the program will autopopulate numbers for the digit span aspect of this test. length will dictate how long the list is, and delivery will be if the list is in a forward, backward, ordered, or unordered manner. 

Function 2: generateShape()

one part of the MMSE is to draw a shape. Since this is an online test, I instead want to generate a shape and ask the tester to identify the shape.

Function 3: calculateScore(responses)

this function will combine the score from the digit span test and the MMSE to display the results of the measure of cognitive function.

responses will store the users responses in a list from the whole test to calculate the score in the end. 

**3. Example use cases:*
*
- in a hospital setting to quickly measure preliminary cognitive function
- research settings to compare cognitive function of younger and older patients
- personal or self testing to measure one's own cognitive health. 

