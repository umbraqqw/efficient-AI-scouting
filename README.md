# AI-driven football scouting

This is a small project I wish to work on, I’ve had an idea brewing in my head for a while and I kinda want to just explore and see what happens. At clubs where the current economical situation of the club doesn’t allow the budget for high-tech player datamapping, actually standing out as an amateur player can be hard - and it can be time consuming for the scouts, too. 

Take IK Start for example. Since IK Start doesn’t have the financial needs to gather large amounts of data from their youth teams, scouting heavily leans towards the “eye-test”. 

My goal is for clubs to not have to spend large amounts of money through investing in technological tracking devices, but rather train AI to watch through matches throughout the season and track player data through visual queues. These raw data are then fed and sorted into a database, before being put on a platform readily available for scouts.

In theory, scouts should be able to look for a “highly technical winger, high shot accuracy on his right foot, good defensive coverage” and have players presented clearly and neatly on an application or website. These player profiles should have data covered matches presented in a way that is easy to understand, and clearly present development rates and analyze who these players are, what systems suit them best etc. Scouts can then use these player profiles to determine if they should sign the player or not. Young players now have the ability to have their data recorded and easily available, they are easier to notice. The data may also be used to develop these players further in terms of training.

Due to the nature and sheer scale of the project, I have attempted to circle down and simplify it. AI recognition software is a large cooperative task currently in development, hence too large of a task for a junior IT-student like me. Instead, I have created a simple Python script to generate semi-realistic but random data from three LW players throughout a season. 

Issues to handle:

* How to visualize differences in positional play? Perhaps a common pool of stats with compare? How to visualize this with star graphs, and what stats should we have for each position?
* In possession, out of possession, in transition?
* How should teams upload match footage? Should they also release a match line-up for each match?
* How do we visualize potential? A blind spot in looking at pure stats is that you can’t do an eye-test
* AI summary of each player based on stats?
* OCR recognition on low quality match footage

Brainstorming:
Player card with name, club and position. Three core star graphs + click for detail. Comparison tab?
