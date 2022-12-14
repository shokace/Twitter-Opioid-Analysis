# CSC665---Twitter-Opioid-Analysis

Program Use

	Using the script we created requires python 3.x, using libraries necessary to build. Code will be published by the time this project is submitted.


	Code Reasoning and Prerequisites

		Excluding  python, make sure to have the following libraries installed:
Requests
Json
Pandas
textblob

		Requests will be used to ensure communication between the Twitter API and the 
local machine running the script. 

JSON will be used to grab and parse the information given from the API.

Pandas will be used to parse the data further, allowing us to reorganize the data 
produced by the API call. This will also be used to give us infographics to the data we get from Twitter.

Textblob is used to analyze our data to the core information, producing us with results. These results will then be graphed using Pandas as explained above.

After installation of the required libraries, you will simply run the program using
either your preferred IDE or command line. After extracting the folder from GitHub, running the script “Parser.py” will create a pdf in the current working directory called “chart.pdf” with metrics on the result, followed by more data in a csv file called “response_python.csv” with more metrics underneath in more or less plain text.
