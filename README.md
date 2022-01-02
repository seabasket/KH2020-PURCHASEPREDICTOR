# KH2020-PURCHASEPREDICTOR
PurchasePredictor is a tool that analyzes patterns in purchase behavior and relays that information to the customer as well as predict their purchase habits in the future.

# Inspiration
Capital One left us with a very open ended challenge in which we could build anything related to finance. So our group had the idea of creating an intelligent finance tool that would make purchase habits known to the consumer. How cool would it be if you could be made aware of unknown purchasing habits that you already have! With this information the consumer would be able to make more intelligent purchasing decisions and thus be more financially sound. We thought this would be a challenging opportunity because none of us had ever worked with API's or AI' before (as we are all first time hackathoners) and, if successful, could be a powerful and practical tool for tens of thousands of people.

# What it does
Our program analyses a given Purchase history (Category of Purchase, Place Purchased, Price of Transaction, and Date/Time) recognises its patterns, and spits out analysis across several different categories, predicting the users purchasing habits in the future.

# How we built it
We built it using the Python programming language and shared our work on GitHub. We split up our work based upon our skill levels and specialties. Sebastian worked on making a fake Purchase history in excel and imported it into the code. Hunter worked on the API and troubleshooted its integration into our code, then made a program that could associate the different aspects of the strings with each other (a dictionary). Santiago worked on the mathematical analysis of that data. We worked collaboratively while working on our sections of the project so that they would fit together Once we had each of our individual functions, we began to splice them together so that our inputs and outputs lined up, and the program could start taking shape.

# Challenges we ran into
We came across multiple challenges with API calls. It was our first experience with APIs, and it was rough to get started with no experience with them. When we tried to run API calls, we were first surprised that each of them had their own unique url, so it was a drastic change from what we were used to. We also hit a wall when we started working with json. We had no experience in both the requests and json libraries. In addition to that, our program had a lot of errors that dealt with "keys" in the url and when, where, and how to use them. We managed to rise higher and pull through and find out what was occurring in all these challenges, despite the near constant 400 errors (shout out Mr. [Mentor] Carsten Neumann!!!).

We also came across some difficulties when trying to import data from the Excel Spreadsheet into our code as strings that could be seperated with a .split() command. Whenever we would copy and paste data of that magnitude it would always paste as a column within the code and jumble everything up, creating a flurry of syntax errors. To solve this, (after much headache) we eventually just copied and pasted the columns into the Google search bar which would then format it automatically into horizontal plan text with spaces between the data in the cell, then we copied and pasted that into a string within our code.

In the process of implementing formulas for tuning our model's parameters, a major challenge was finding a straightforward method for computing the matrices that relate with the sought after coefficients since each component involved an integration of complex-valued functions. Since there aren't many pre-existing tools on efficient computations of such integrals, it was time-consuming finding a good enough approximation for our purposes. Besides the numerical imprecision challenge, testing and debugging code throughout the development stage was frustratingly difficult since each sub-problem produced results whose interpretations relied so tightly with the end product. It wasn't until the code was being finalized that we could actually test the validity of sub-algorithms. Of course this brought up a couple of bugs overlooked at the beginning. But overall, facing these challenges pushed us to stay on our objective

# Accomplishments that we're proud of
On Fourier Analysis: Developing on a gamble and having the proof of concept actually work after hours struggling over computational subtleties was absolutely thrilling if not terrifying. Overall, a great experience and exciting seeing one's idea coordinate into a functioning whole, even if it was hacked together. On Learning API's: We learned how to navigate and tweak websites using APIs, and transfer data between computers and the cloud. It also was amazing to learn how to convert easily between other data types and json files. On Learning Python: Sebastian had little to no experience with python nor API's. He got a "crash course" in both of those topics this weekend and was able to contribute to the groups efforts while learning these topics himself.

# What we learned
None of us were familiar with API's whatsoever nor complex Fourier Analysis and we were able to get a "stepping stone" grasp on these concepts.

# What's next for PurchasePrediction
Though they could not be achieved in this 32 hour period, we have some very realistic short-term ideas for this project and some more ambitious long-term ideas for the future.

# Short Term Ideas
We could add more analysis categories than we have. (ex: Most likely day of the week for a particular Category/Purchase, Average price per visit to a particular Place/Category, Percentage of total purchases for Category via Place or Total Purchases via Category, etc...)
Create a more user friendly front-end experience where data could be directly input into the website and the analysis could be spit back out rather than input through the backdoor.
Increase accuracy of the Fourier Analysis.
Allow for analysis of deposits and bills

# Long Term Ideas
Integrate this code into an existing banking app where the data syncing becomes automatic with the local Purchase info.
Suggest budget plans automatically based on account balance and expert opinion.
Make Purchase Database updates automatic.
Automatic Categorization of Purchases using Google Maps information.
Location based analysis. (ex: everytime you are near "place" you buy "item")
Interpersonal Analysis (ex: everytime you are near "person" you go to "place" and buy "item")
Automatically suggest purchases based on location (ex: "You are at [place] would you like to make your usual order?")

# Notes on Running
To run the demo successfully, this project requires Python 3.5 or greater as well as the latest versions of NumPy, SciPy, and request. A demo of the Purchasing Prediction algorithm can be run via the command line or terminal with the command python3 main.py which will output the expected costs for a fictional character in the future given a purchasing history that stretches for approximately 3 months.
