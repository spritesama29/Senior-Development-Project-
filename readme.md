Kyle Stearns
I do not believe there is anything else needed to run my project other than python and an API key
This project gets the data of the top 250 tv shows as well as the user ratings for the 1,50,100,200, and the wheel of time. The program first gets the 250 shows and then uses 
The list to get the show Ids for the shows listed previously in this file. Once it does this it queries the user ratings for those 5 shows and writes them to the file. After this
The 250s are written below it. To make it more readable I have used the .get as well as indexes to get into the dictionaries and take the important information as strings and wrote them in a nicer to read format
For the 250 shows I wrote the data that I thought would be most relevant to the show, which I checked to make sure this was ok previously. 
I also have a secrets file where I have my API key. 
There are also optional functions I made just to navigate the 250 data easier such as search by title or find Id by title. 
I also added error checking into the get userRatings function as the IMDB list updated the show list fairly recently and the 200th show did not have any user ratings so I made a check for zero ratings.
