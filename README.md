# movieProject

Dependencies to install:
 - pip install cinemagoer
 - pip install mysql-connector-python

Initial version: Webscraper used to take in input from a user and the script will return the general sentiment of the movie selected.
Created Script to Get latest movie reviews of movies in theatres (30-100 movies) (should refresh script every couple months)
Model Chosen : distillbert-base-multilingual-cased-sentiments-student
Next Steps:

Phase 1
-------
 - Figure out how to store the data in dataset, interact with dataset.
 - Cloud Server? 
 - Dataset should hold Latest Movie Reviews
 - Determine Proper Structure for Dataset


 Phase 2
 -------
 - see what the model requires, clean data based on that (Special Characters, review length, etc)
 - Do we want to do Aspect Based Sentiment Analysis? If so find some potential models to work with. Map out how to structure database to accomodate. Account for how scoring may be, avoid skewing.  
 - Determine what we want it to output, how we come up with quantitative metric


Phase 3
-------
 - Build Frontend, content to backend  


