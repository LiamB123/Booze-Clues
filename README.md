Booze Clues
This is a community based cocktail recipe book page. The idea is for users to interact sharing recipes or picking up new recipes to brighten up some old menus!.
This is a Python based Flask application that allows users to add, edit and remove on a shared data set with a common goal of sharing recipes which i found difficult during my time in the hospitality industry.

The goal is to get enough users interacting and sharing ideas to populate a book's worth of recipes which could be published, 
their are links to external retailers of ingredients so their is potential for partnership there or to even create liqours or recipe kits for the first time at home hobbiest bartender.


Link to deployed site: https://liams-booze.herokuapp.com/


UX

The user stories i targeted were generally bartenders or cocktail enthusiasts who would be able to contribute to the databae of cocktail recipes. There is the opportunity to tweak recipes that may not be correct and there is an opportunity to find inspiration for new drinks through the shared knowledge on the page.

I am an unexperienced Professional Bartender, i can pull pints but cant make a cocktail and im looking for somewhere to see what the deal is with cocktails. I need recipes with exact measurements and names with the method on how to take it from base ingredients to finished product. 

I am a bar/restaurant manager and my drinks menu is old and stagnant, i need some exciting new cocktails to spice up my menu. But where can i get some inspiration for new creations and find some classic great tasting cocktails to increase my sales!
I want to see variety, full ingredients lists and so interesting/eye-catching names 

I am a Mixologist with a 6th degree black belt in cocktails. I appreciate the balance of sweet and sour and have a wealth of knowledge and quite a few of my own creations i want to share with the world. 
I want a site to see new drinks for inspiration and to share the knowledge I have gained. 

I am a cocktial enthusiast who just loves drinking these concoctions and wants to try making a few at home.
How do i even go about it? i need recipes, where to find the spirit and what ones to use and how much?
I need clear, comprehensive instructions and a few different options to try out! 




Features
In this section, you should go over the different parts of your project, and describe each in a sentence or so.

Existing Features
Feature 1 - allows users X to achieve Y, by having them fill out Z
...
For some/all of your features, you may choose to reference the specific project files that implement them, although this is entirely optional.


Feature 1 - Nav Bar 
         Allows any user to easily jump betweeen the 4 main sections of the site quickly and is clearlty accesible to the user at all times. The nav bar becomes hidden by scrolling down but returns upon scrolling up in any capacity. 
I believe its contrasting color set allows the nav bar to stand out at all times.

Feature 2 - Recipes page   
         Allows any user to see all available recipes in a collapsed card format. any user can click on the recipe they like tha name of the expand the card into the full recipe including ingredients & method. 
The Recipe cards have edit and delete functionality built in, so a user can edit a recipe to impove it or correct typos.
The user can also delete any entrys that were accidentally put in or are wildly incorrect. 
The page displays data from a Mongo DB added through the form page on the site.
I would like to note that the fundamental flaw with this page is without any authorisation or authentication, anyone can delete all entries on the page and it would wipe the database. 
This is a key error I would resolve in future updates for the page i will discuss later.

Feature 3 - Add recipes page
         Allows any user to add to the recipe collection. The form allows the user to contribute to the recipes page and writes to a Mongo DB database. 
         The form itself leaves space to add a search function to the site as the recipes all have a base spirit, which is an ideal key to search based on, particularly for the professional's coming onto the site who would be basing there cocktail on a base spirit not neccessaily on what looked like the best cocktail.
         
Feature 4 - Shop Page
         A card based page linking to all base spirits and ingredients that may not be accessible at every local shop. This page is simply linking off to the amazon marketplace for each of our recommeneded brands for base ingredients.There is potential for partnership here as the site could get sponsored by individual drink brands (Absolut - vodka) or distributing companys (Pernod Ricard) or more realistically an off license that could support the orders on what i imagine would be small scale to start. The shop could grow from ingredients into the equipment such as bottle openers, cocktail tins and even Booze Clues T-Shirts!
 


Features Left to Implement

Feature 1 - Login capabilities
         As was earlier stated the fact that any user on the page can delete the whole recipe book kind of defeats the purpose so an authentication and authorisation app would need to be created for a number of reasons. 
The primary so that users can safely add to the collection without fear of it being deleted. 
If only members can post recipes it gives the user a reason to sign up for the site.



Feature 2 - Search app
           A search option should be added initially by base spirit as it would be the simplest means of categorising the recipes. This is particularly usefull for both professional and first timers. The professional may have too much stock of a spirit and is looking to see what he can make with the excess, the first timer may want to make a cocktail of their own favourite spirit and it would make browsing easier.
The search could be expanded from their into categories such as Shots, Martini's or Fish Bowls. 
It could even be leveled based on the difficulty of making from beginner, intermediate and advanced.

Feature 3 - Adding images to the recipes
         People drink cocktails with their eyes, so it is a must for this page to showcase what the finished product should look like. This is currently out of the realms of my ability but it is an absolute must for the success of the site, it could even be used in the book as the imagery of the best cocktails. It also adds to the fun of the page if people can show off their creations with the community!
         
         
         
Feature 4 - Commenting/voting on recipes
            A commenting option for recipes would be invaluable to fueling the community aspect to the page. A user could put up a base recipe that could have twists, ie a Daquiri could have the strawbery daquiri twist. This drives users to regulalry jump back onto the page as they can see updated recipes, popular recipes among the newly added content.
            
Feature 5 - Create Social medias to link to site
         This is not so much a feature of the site as a requirement for "Booze Clues" to grow correctly as a brand. As the 
         
         
Technologies Used
In this section, you should mention all of the languages, frameworks, libraries, and any other tools that you have used to construct this project. For each, provide its name, a link to its official site and a short sentence of why it was used.

The Technologies Used

The key languages i used were HTML, CSS and Python for the majority of the page. 
This Python application utilised the open source library that is Flask to get around many url/file path related issues 
https://www.fullstackpython.com/flask.html
I utilised a bootstrap theme from start bootstrap as the skeleton for my page as i liked the grid layout in it, the name of said theme was agency and can be found here : https://startbootstrap.com/themes/agency/
Bootstrap is particularly useful for navigation and the JQuery elements really help with simplifying the DOM manipulation.
I utilised Mongo DB to store the data from the recipes on the page https://www.mongodb.com/
I used PyMongo to assist with the handling of Python writing to and drawing from the Mongo DB. 


Testing

From a user perspective i went onto the page and clicked all the buttons on the nav bar to make sure it brought me to the places they said they would! i attempted to reload, to back track and jump sporatically from page to page but the navigation held up throughout. 
I attempted on the add recipe page to not give sufficient info, but was thankfully prompted to fill in the missing data at every point.
The recipes page uses a collapsing accordian style card layout, and the key issue ive identified is when opening one recipe, all the recipes open. I think it could be down to how i have the For loop configured on the Recipes page but at the moment i havent been able to rectify the problem.  
The use of Bootstrap allowed me test with Chrome Developer Tools the responsiveness of the pages sizing and boxes, I went through all avaialable screen sizes, which led to slight changes within the html code for sizing, to provide an optimal experience for the user regardless of the medium utilised.

Bugs
The key area I struggled in is the deployment of site to Heroku. I had some initial issues with the Mongo DB not communicating with the site due to my lack of knowledge on how environment variables, and having to use a bashrc file that i hadnt heard fo before undertaking this projct. An issue with the formulation of the password i was using led to errors i couldnt figure out so after many attempts i changed the password removing the * character which allowed it to work?
I was confused on whether it was actually the characters that was the issue as * is a function within a bash file so that made it quite an interesting bug!
The next big issue was getting deployment on Heroku. After learning from the previous bug i had my environ vars in order however it came to pass i had a poorly constructed requiremenets.txt file. This was due to AWS adding unnecceessary libraries to it when i ran a pip freeze command, my own fault for not knowing what each of these libraries did! After consulting with a tutor from the CI i had a much smaller list that allowed hereoku to deploy!


Deployment
I deployed through Heroku after linking it to my Git Hub repository. 
         I had initially to install heroku onto AWS so i could link my git hub to the heroku app. The app itself had environment variables added for increased security purposes. 
These variables included the Port, IP, Mongo DB and secret key values. By hosting these variables on heroku it means the site itself doesnt contain this sensitive information. 
As this was my first succesful deployment on heroku it showed me just how important each key stroke is particularly in a bash file, as well as the importance of having an accurate Procfile and requirements.txt file.


Credits
I had some useful input from the CI tutors, Michael, Xavier, Stephen and Haley.

Content
The text for the recipes was provided by myself as a former bartender i had learned a few things!


Media
The photo used in the site were obtained from a google search which returned this image
https://whatsnewindonesia.com/jakarta/best-cocktail-bars-in-jakarta/

Acknowledgements
I received inspiration as i could never find a bartende centred site when i was in the hospitality industry, no one seemed to mind sharing the information but it was hard to find people who had the knowledge in the first place!
I had
