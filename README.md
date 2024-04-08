# Project Proposal - Aryan Subramanian

## The Big Idea
The main idea of the project would be to develop a web-based application that essentially takes in user input and using the most basic discrete/continuous, it would output a final result along with a relevant graph that can help the user visualise the answer. The application would ideally allow the user to input probability questions in natural language, whilst the code parses through the text to identify which type of distribution is required for based on the relevant parameters. The MVP of this project will focus on implementing key probability distributions like binomial, normal, poisson, etc. The stretch goal would be the addition of natural language (which is what I will strive to aim for), but a fallback input option would be for the user to input the relevant numbers and distribution, and the application would run accordingly.

## Learning Objectives
I was primarily interested in this project as I'm currently taking a course called Probabilities for Risk Management, and found it very interesting. I found myself using a lot of external applications in the class, and figured it would be interesting to create my own application that I could potentially use. It would also be interesting if I could promote the application to my professor, who may be interested in using it in future classes.

## Implementation Plan 
I plan to explore some of the libraries that we have already explored in class such as NLTK. This would allow me to implement the natural language aspect of the code, which can analyse user input. I also plan to use plotly to provide the visualisations for the user. Some of the assignments and concepts we have learnt in class have helped me strengthen my ability using the Flask server and HTML/CSS. These sklls would be very useful to develop the front-end of the application. A new library I'm keen on exploring is the SciPy library. This would optimise the code as it already have pre-built functions for the distributions I plan to use, as it eliminates me having to manual enter code for different use cases. As I progress throughout the project, I'm confident I will find more interesting libraries to utilise in my project.

## Project Schedule
1. **Primary Code**: Completion by Thursday 04/18
2. **Front-end Flask/HTML/CSS**: Completion by Sunday 04/21
3. **Natural Language**: Completion by Thursday 04/25

*The code will first be completed using manual user inputs using forms on HTML, just to ensure that my web application is working. Once this is completed I aim to introduce the NLTK library*

## Collaboration Plan
I intend on working on this project alone, hence all the work will be completed by myself

## Risks & Limitation
The most significant limitation in this project will be to successfully introduce natural language processing, as this is a complex topic. Especially when it comes to accurately parsing through the user input and correctly identifying the right distribution to use and also interpreting the diverse range of inputs that could be used. Another limitation could be timing, due to projects/papers/exams from other classes that all fall during the same week. 

## Additional Course Content
I believe that Machine Learning would be extremely beneficial for my application as it would help increase the accuracy and efficiency of the natural language processing element. Furthermore, advanced NLP algorithm and methodologies would also have the same effect on the application, ultimately providing a better user experience

