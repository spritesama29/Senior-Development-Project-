Kyle Stearns
I do not believe there is anything else needed to run my project other than python and an API key
This project gets the data of the top 250 tv shows as well as the user ratings for the 1,50,100,200, and the wheel of time. The program first gets the 250 shows and then uses 
The list to get the show Ids for the shows listed previously in this file. Once it does this it queries the user ratings for those 5 shows and writes them to the file. After this
The 250s are written below it. To make it more readable I have used the .get as well as indexes to get into the dictionaries and take the important information as strings and wrote them in a nicer to read format
For the 250 shows I wrote the data that I thought would be most relevant to the show, which I checked to make sure this was ok previously. 
I also have a secrets file where I have my API key. 
There are also optional functions I made just to navigate the 250 data easier such as search by title or find Id by title. 
I also added error checking into the get userRatings function as the IMDB list updated the show list fairly recently and the 200th show did not have any user ratings so I made a check for zero ratings.

Kyle Stearns Sprint 2

In this sprint, I made two tables, table250 and ratings which take the data of the top 250 shows as well as the data from the ratings of the 1,50,100,200 and the wheel of the time . The 250 table also has the wheel of time in it with zeros for all but the id and title. There is a foreign key that of the show_id in the ratings table that connects to the table250. To put the data into the tables I used sqlite queries and passed in the values from the queried data. For the tests I made one that pulls the 250 data, puts it in a database, and then checks if the database has 250 rows and then confirms it. The second one checks if the mock data was added to the database and then confirms it.

Kyle Stearns Sprint 3

In this sprint, I added the additional tables as well as made a function that took the popularMovies rankUpdown values, ordered them and then put them in the table. For the tests involving making the new tables and checking if they are there, I modified my first test function that already makes the entire database. I then had the test add and check if all the tables are in there. This test encompasses making a new table as we could not check the amount of data added if there was no table in the first place. For the happy path test I added in data and had the orderRankUpDown put them in the correct order from neg to pos and assert that their positions were correct. For the bad path tests I put in empty, spaces, and letters and checked to make sure 4 entries were still in the table afterward, meaning the function noticed the bad data and adjusted accordingly. For the Foreign key test I took the sql table creation statement from sql master for the ratingsMOV table and split it into a list. I then iterated through till i found the word foreign. Then till I found the word references. Since after reference is the table foreign keyed I checked after it and appended each char to a new string until it equaled the name of the popularMOV table, the table we want it foreign keyed to. I then returned a check int to be asserted
