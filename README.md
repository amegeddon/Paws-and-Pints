# Paws & Pints

**Developer: Amy Cook**

[Visit live website](https://paws-and-pints-9f68e52a491c.herokuapp.com/)

![Mockup image](docs/)

## Table of Content

- [Project Goals](#project-goals)
  - [User Goals](#user-goals)
  - [Site Owner Goals](#site-owner-goals)
- [User Experience](#user-experience)
  - [Target Audience](#target-audience)
  - [User Requirements and Expectations](#user-requirements-and-expectations)
- [User Stories](#user-stories)
  - [Site User](#site-user)
  - [Site Owner](#site-owner)
- [Structure](#structure)
  - [Site Structure](#site-structure)
  - [Database Structure](#database-structure)
- [Design](#design)
  - [Colour Scheme](#colour-scheme)
  - [Fonts](#fonts)
  - [Structure](#structure)
  - [Wireframes](#wireframes)
- [Technologies Used](#technologies-used)
  - [Languages](#languages)
  - [Frameworks, Libraries & Tools](#frameworks-libraries--tools)
- [Features](#features)
- [Validation](#validation)
  - [HTML Validation](#html-validation)
  - [CSS Validation](#css-validation)
  - [JavaScript Validation](#javascript-validation)
  - [Accessibility](#accessibility)
  - [Performance](#performance)
- [Testing](#testing)
  - [Performing tests on various devices](#performing-tests-on-various-devices)
  - [Browser compatibility](#browser-compatibility)
  - [Testing user stories](#testing-user-stories)
- [Bugs](#bugs)
- [Deployment](#deployment)
- [Credits](#credits)
- [Acknowledgements](#acknowledgements)

## Project Goals

- Develop a website dedicated to helping dog owners find and review dog-friendly pubs on the beautiful Island of Anglesey. Users can share their experiences, ratings, and recommendations, creating a comprehensive database of pet-friendly establishments. This community-driven platform enables users to make informed choices about where to take their furry companions. Additionally, the site owner can leverage the growing dataset to attract more users and support local businesses in the hospitality industry 

### User Goals
- Discover Dog-Friendly Pubs: Users can easily find pubs that welcome dogs, enabling them to plan outings with their pets more conveniently.
- Share Experiences: Users can contribute their own reviews and ratings of dog-friendly pubs, helping fellow dog owners make informed decisions about where to visit.
- Community Engagement: The platform fosters a sense of community among dog owners, allowing them to connect with others who share similar interests and experiences.
- Contribute to a Growing Resource: By sharing their experiences, users contribute to a comprehensive database of dog-friendly pubs, benefiting both themselves and the wider community of dog owners.
- Support Local Businesses: Users can support local pubs that cater to dog owners by promoting and patronizing these establishments, thereby contributing to the local economy.


### Site Owner Goals

- Develop an entertaining and engaging platform that allows users to contribute to a growing database of dog-friendly pubs by submitting reviews, ratings, and photos, enriching the platform for the benefit of all users. 
- Implement simple and intutive navigation throughout the website.
- Craft a visually appealing design for enhanced user experience.
- Ensure a fully responsive and accessible website.


## User Experience

### Target Audience

- Dog Owners: Individuals who own dogs and are interested in finding pubs and establishments where they can enjoy outings with their pets.
- Local Residents of Anglesey: who are looking for nearby pubs that welcome dogs, either for regular outings or when hosting visitors.
- Tourists: Anglesey attracts many tourists who visit with their k9 companions, these tourists will want to explore the many beutiful walks we have here on the Island and most probably appreciate a post hike pint at a nearby dog friendly pub.
- Pub Owners: Owners and managers of pubs and hospitality establishments that cater to dog owners and want to promote their venues to a wider audience.

### User Requirements and Expectations

- Easy Search and Discovery: Users expect to easily search for dog-friendly pubs based on locations
- The review submission process should be simple and intuitive for users, allowing them to easily share their experiences with dog-friendly pubs. Clear instructions and prompts should guide users through each step, ensuring a seamless and hassle-free process.
- Mobile-Friendly Experience: Users anticipate a mobile-friendly experience that allows them to access the website on their smartphones and tablets while on the go, ensuring convenience and flexibility.
- User-Generated Content: Users expect the website to feature user-generated content such as reviews, ratings, and photos, allowing them to benefit from the experiences of other dog owners.
- Visual Appeal: Users appreciate a visually appealing website design that showcases high-quality images of dog-friendly pubs and creates a pleasant browsing experience
- Accessibility: The website should be accessible to all users, including those with disabilities, by adhering to accessibility standards. This ensures usability and navigability for everyone, regardless of their abilities.

## User Stories

### Site User

1. Discover dog-friendly pubs across Anglesey and explore their amenities and services.
2. Engage with authentic reviews from fellow users to make informed decisions about pub visits.
3. Contribute to the community by adding new dog-friendly pubs and sharing personal experiences through reviews.
4. Enhance their experience by creating an account, enabling them to save favorite pubs for future reference on their profile page. 
5. Enjoy the flexibility of editing their review entries to reflect updated experiences or feedback.
6. Exercise control over their account by having the option to delete it at their discretion, ensuring user autonomy and privacy.



### Site Owner

8. Manage pub entries and reviews seamlessly with options to add, edit, or delete content effortlessly.
9. Create an immersive and user-friendly platform with intuitive navigation, captivating visuals, and an appealing design.
10. Ensure a seamless user experience across all devices by implementing full responsiveness, allowing the website to adapt seamlessly to different screen sizes and device types.
11. The user to be directed to a custom 404 error page upon entering a non-existent URL, eliminating the need to rely on the browser's back button.

## Structure

### Site Structure 

- The site's navigation bar provides access to all main sections, along with additional links for adding or editing content, which are available to logged-in users.
   

   |**Navbar?**| **Logged Out** | **Logged In (non-admin)** | **Logged In (admin)** |
| ----------| -------------- | ------------------------- | --------------------- |
| Yes       | Home           | ----                      | ----                  |
| Yes       | ---            | Profile                   | Profile               |
| yes       | ---            | Add Pub                   | Add Pub               |
| yes       | ---            | ---                       | Manage Reviews        |
| Yes       | log In         | ---                       | ---                   |
| Yes       | Register       | ---                       | ---                   |
| Yes       | ---            | Log out                   | Log out               |


<details><summary>Logged Out Navbar</summary>
<img src="ADD HERE" alt="Navbar for logged out users: Home, Log In, Register.">
</details>

<details><summary>Logged In Navbar</summary>
<img src="ADD HERE " alt="Navbar for logged in users: Home, Profile, Add Pub, Log Out. ">
</details>

<details><summary>Admin Navbar</summary>
<img src="ADDHERE " alt="Navbar for admin: Home, Profile, Add Pub, Manage Reviews, Log out.">
</details>


#### Database Structure

For this dog-friendly pub review site, I've opted to use MongoDB for its non-relational database capabilities. This choice supports dynamic inputs across collections, facilitating diverse data storage such as user reviews, pub details, and photos.


<img src="ADD HERE ">

## Design

### Colour Scheme

- Consistency was maintained in the color scheme across all screens, with the primary background color being #e8f5e9. This choice was made as the light green color gives excellent readability for black text and gives a calm, fresh appearance to the site. The dark blue of the nav bar, #1e3a5f, compliments this background color well and looks quite stark against it. The most important element in considering the design of this site is that it is simple, clear and straightfoward to navigate. 



### Fonts

- Google Fonts were  integrated into the website, with Lora as the primary font, accompanied by a sans-serif fallback for optimal readability across all screens. To inject a stylish but playful touch, Pacifico was selected for the headings, this font pairs nicely with Lato. 




### Wireframes

<details><summary>Laptop & desktop</summary>
<img src="ADD HERE ">
</details>
<details><summary>Mobile</summary>
<img src="ADD HERE ">
</details>

## Technologies Used

### Languages

- HTML
- CSS
- JavaScript
- Jquery
- Python

### Frameworks, Libraries & Tools

- [Flask](https://pypi.org/project/Flask/) - Micro framework for site templating.
- [Materialize v1.0.0](https://materializecss.com) - The framework for the website.
- [Git](https://git-scm.com/)
- [GitHub](https://github.com/) was used as a remote repository to store project code and host the webpage 
- [Chrome dev tools](https://developers.google.com/web/tools/chrome-devtools)
- [Am I Responsive](http://ami.responsivedesign.is/)
- [Adobe Stock Images]
- [Font Awesome](https://fontawesome.com/)
- [Google Fonts](https://fonts.google.com/)
- [WC3 Validator](https://validator.w3.org/), [Jigsaw W3 Validator](https://jigsaw.w3.org/css-validator/), [JShint](https://jshint.com/), [Wave Validator](https://wave.webaim.org/), [Lighthouse](https://developers.google.com/web/tools/lighthouse/) and [Am I Responsive](http://ami.responsivedesign.is/) were all used to validate the website
- [Jinja](https://jinja.palletsprojects.com/en/3.1.x/) - Templating engine.
- [Heroku](https://www.heroku.com) - For website deployment.
- [MongoDB](https://www.mongodb.com) - The database used for storing information for the site.
- [Pip](https://pypi.org/project/pip/) - To install Python packages.

## Features

### NavBar 

The top navigation bar includes the site name and adapts its links based on the user's login status. On smaller screens, the navbar collapses into a sidebar.

For non-logged-in users, links to the home, sign-in, and register pages are available. Once logged in, users gain access to their personal profile, the option to add new pubs, and the ability to write reviews.

<details><summary>See feature</summary>
<img src="ADD HERE ">
</details>

### Home screen

- Title: Dog Friendly Pubs in Anglesey - provides context for the directory and lets the user know immediately if the content is for them or not. 
 - displays all the Pubs listed in the directory using cards that display a photo of the pub, pub name, pub location and the average rating of the pub. Clicking on the reveal button displays a description of the pub alongside all the pub reviews. Users are here invited to leave their own reviews. 
- icons at the very bottom of the card lets users know whether the pub serves food, whether dogs are allowed inside, is water provided for dogs, are meals offered for dogs, is there beautiful walks nearby and, finally, whether the staff were friendly. These aspects were focused on as research revealed that these are the most important consideration for those that like to include their dogs on adventures. 
- Visual feedback on the pub's rating is provided through an average rating, represented by colored stars corresponding to the average rating

- User stories covered:  

<details><summary>See feature</summary>
<img src="ADD HERE">
</details>


### login Page

- Short explaination for user that instructs them of the need to log in to be able to leave a review or add a pub. 
- hyper link that user can click and be redirected to if they dont already have an account and need to register.
- username and password input boxes. 
- show password clickbox that can be toggled to reveal the inputted password.
- flash message to let user know that login has been sucessful.

- User stories covered: 

<details><summary>See feature</summary>
<img src="ADD HERE">
</details>


### Registration page
     
- Redirection if user needs to simply login with link that can be clicked and redirected appropiately.
- Username and password input boxes.  
- show password clickbox that can be toggled to reveal the inputted password.
- flash message that appears to let user know that registration has been successful

- User stories covered: 

<details><summary>See feature</summary>
<img src="">
</details>

### Profile Page   

- brief flash message saying welcome back.
- Displays the users reviews with edit and delete buttons allowing for changes and permanent deletion if necessary.
- Displays the pubs added by the user with edit and delete buttons allowing for changes and permanent deletion if necessary 

- User stories covered: 

<details><summary>See feature</summary>
<img src="docs/incorrect answer screen.png">
</details>


### 404 error page

- A 404 error page is presented when users enter a non-existent URL.


- User stories covered: 12

<details><summary>See feature</summary>
<img src="docs/404 error page.png">
</details>


## Defensive Programming

Defensive programming is implemented in order to ensure secure access control. Conditional checks verify user permissions, ensuring only admins can edit any user's posts or access admin areas. For regular users, they can only edit their own posts. Unauthorized users are redirected to the login page.

Specifically, the profile route includes several security measures:

Session Check: If session["user"] is not set, the user is redirected to the login page.
Session Username Validation: The session username is retrieved from the database to confirm it matches the current session’s username.
URL Username Match: It ensures the session username matches the username in the URL. If they don’t match, access is denied, and the user is redirected to the login page.
These checks prevent unauthorized access and ensure that users can only access their own profiles.

<details><summary>Returns User to login page</summary>
<img src="ADD HERE " alt="The please log in message.">
</details>

## Future Implementations

- Allowing the user to upload their own image and have this stored in mongoDb was a challenge, more defensive programming is needed for this function and also further research into the scaleability of storing images in this way is required, as this could become a problematic area in the future. Also, when a pub is deleted from the database the corresponding image is not being deleted, if I had more time this is something I would want to remedy immediately as this is going to add towards the strain on storage. 

- a sort by function that would arrange pubs in order of highest average reviews would be beneficial as the site grew in numbers of pubs added, alongside the number of reviews. 

- the search bar is operational but clumsy, it does not arrange searches from the top of the page, rather they seem to stay where they are on the page. Whilst various fixes were attempted to remedy the appearence of the search results this is a problem that remains unsolved for now. This is definetely an area to look at in the future, particularly as the number of pub entries grows as currently users are required to scroll down pass empty space to find their search results.

## Deployment & Local Development

### MongoDB Non-Relational Database

This project uses [MongoDB](https://www.mongodb.com) for the Non-Relational Database.

To obtain your own MongoDB Database URI, sign-up on their site, then follow these steps:

- The name of the database on MongoDB should be called "__pub_reviews__".
- The collection(s) needed for this database should be "__photos__", "__pubs__",__users__ and "__reviews__.
- Click on the __pub_reviews__ name created for the project.
- Click on the __Connect__ button.
- Click __Connect Your Application__.
- Copy the connection string, and replace `password` with your own password (also remove the angle-brackets).

### Heroku Deployment

This project uses [Heroku](https://www.heroku.com), a platform as a service (PaaS) that enables developers to build, run, and operate applications entirely in the cloud.

Deployment steps are as follows, after account setup:

- Select __New__ in the top-right corner of your Heroku Dashboard, and select __Create new app__ from the dropdown menu.
- Your app name must be unique, and then choose a region closest to you (EU or USA), and finally, select __Create App__.
- From the new app __Settings__, click __Reveal Config Vars__, and set your environment variables.

| Key | Value |
| --- | --- |
| `DATABASE_URL` | user's own value |
| `IP` | 0.0.0.0 |
| `MONGO_DBNAME` | user's own value |
| `MONGO_URI` | user's own value |
| `PORT` | 5000 |
| `SECRET_KEY` | user's own value |

Heroku needs two additional files in order to deploy properly.

- requirements.txt
- Procfile

You can install this project's __requirements__ (where applicable) using:

- `pip3 install -r requirements.txt`

If you have your own packages that have been installed, then the requirements file needs updated using:

- `pip3 freeze --local > requirements.txt`

The **Procfile** can be created with the following command:

- `echo web: python app.py > Procfile`
- *replace __app.py__ with the name of your primary Flask app name; the one at the root-level*

NOTE: The Procfile uses a capital P and doesn't have a file extension on the end.

For Heroku deployment, follow these steps to connect your own GitHub repository to the newly created app:

Either:

- Select __Automatic Deployment__ from the Heroku app.

Or:

- In the Terminal/CLI, connect to Heroku using this command: `heroku login -i`
- Set the remote for Heroku: `heroku git:remote -a app_name` (replace *app_name* with your app name)
- After performing the standard Git `add`, `commit`, and `push` to GitHub, you can now type:
	- `git push heroku main`

The project should now be connected and deployed to Heroku!

### Local Deployment

This project can be cloned or forked in order to make a local copy on your own system.

For either method, you will need to install any applicable packages found within the *requirements.txt* file.

- `pip3 install -r requirements.txt`.

#### How to Fork

By forking the GitHub Repository, we make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original owner's repository.
You can fork this repository by using the following steps:

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/Melody-Lisa/blissboost)
2. At the top of the Repository (not top of page) just above the "Settings" Button on the menu, locate the "Fork" Button.
3. Once clicked, you should now have a copy of the original repository in your own GitHub account!

#### How to Clone

You can clone the repository by following these steps:

1. Go to the [GitHub repository](https://github.com/amegeddon/Paws-and-Pints) 
2. Locate the Code button above the list of files and click it 
3. Select if you prefer to clone using HTTPS, SSH, or GitHub CLI and click the copy button to copy the URL to your clipboard
4. Open Git shell or Terminal
5. Change the current working directory to the one where you want the cloned directory
6. In your IDE Terminal, type the following command to clone my repository:
	- `git clone https://github.com/amegeddon/Paws-and-Pints.git`
7. Press Enter to create your local clone.

<sup><sub>[*Back to top*](#contents)</sup></sub>

-----


## Validation

### HTML Validation

The website's HTML was validated using the W3C Markup Validation Service, with all pages passing without errors.

<details><summary>index.html</summary>
<img src="docs/w3html.png">
</details>

<details><summary>404 error page</summary>
<img src="docs/404validator.png">
</details>

### CSS Validation

The W3C Jigsaw CSS Validation Service was used to validate the CSS of the website. Upon validation
When validating all website,

<details><summary>All site</summary>
<img src="docs/w3c_css.png">
</details>
<details><summary>Style.css</summary>
<img src="docs/w3cStyles.css.png">
<img src="docs/">
</details>

### JavaScript Validation

JavaScript files were validated using the JSHint JS Validation Service, revealing no significant issues.

<details><summary>game.js</summary><img src="docs/jsHint.png"></details>

### Accessibility

The WAVE WebAIM accessibility evaluation tool was utilized to ensure compliance with accessibility standards. No errors were identified, affirming the website's accessibility. An alert was identified, suggesting that the hidden word might be mistakenly perceived as a header. To enhance accessibility, an ARIA role of "text" and an ARIA level of "0" were implemented, ensuring that the hidden word is explicitly recognized as non-header content. However, the evaulation tool contiuned to flag the alert, therefore I changed from div to a h3 element to resolve the issue.

<details><summary>index.html</summary><img src="docs/wave.png"></details>
<details><summary>404 error page</summary><img src="docs/wave404.png"></details>

### Performance

Google Lighthouse within Google Chrome Developer Tools served as the performance testing tool for the website, providing insights into various aspects such as performance, accessibility, SEO, and best practices. The performance scores for desktop mode were consistently excellent across all testing parameters. However, during mobile testing, the performance score registered at 63. In an effort to enhance this score, all image files underwent resizing, compression, and conversion to webp format. Additionally, to further boost performance, the CSS was minified. The combined effect of these two measures resulted in an improved performance score of 84.

<details><summary>Home page desktop </summary><img src="docs/lighthouse-desktop.png"></details>
<details><summary>Home page mobile </summary><img src="docs/mobileLighthouse.png"></details>
<details><summary>404 page</summary><img src="docs/404 lighthouse .png"></details>


## Testing

### Performing tests on various devices

The website underwent testing with Google Chrome Developer Tools, utilizing the Toggle Device Toolbar to simulate various device viewport sizes.

The website was tested on the following devices:

- lenovo Ideapad L340 (laptop screen)
- Windows Surface pro 5 (small laptop screen size)
- Ipad (tablet screen)
- Huawei P30 (mobile screen)
- Apple 10 (mobile screen)
- Samsung galaxy 21 (mobile screen)

### Browser compatibility

- Testing has been carried out on the following browsers:
  - Googe Chrome Version 120.0.6099.199
  - Firefox Browser 121.0

### Testing user stories

1. Comprehensible Game Instuctions: instructions that are easy to grasp, ensuring a straightforward understanding of how to play the game.

| **Feature**       | **Action**        | **Expected Result**                  | **Actual Result** |
| ----------------- | ----------------- | ------------------------------------ | ----------------- |
|Game instructions button| Click on Instructions button | Modal with game instructions pops up. Click on close button to close modal or click game instructions again to close | Works as expected |

<details><summary>Screenshot</summary>
<img src="docs/instructionsbutton1.png">
<img src="docs/instructionbutton2.png">
</details>

2. Adaptable Difficulty Levels: A feature allowing me to choose from various difficulty levels, tailoring the game's challenge to my preference.

| **Feature**    | **Action**                                                           | **Expected Result**                               | **Actual Result** |
| -------------- | -------------------------------------------------------------------- | ------------------------------------------------- | ----------------- |
| Difficulty select buttons  | Select preferred difficulty using the options of easy, medium and difficult buttons| Attempts left will adjust accordingly (easy=8, medium=6 hard=4) | Works as expected |

<details><summary>Screenshot</summary>
<img src="docs/levelselect1.png">
<img src="docs/level2.png">
<img src="docs/level3.png">
<img src="docs/level4.png">
</details>

3. A hint function that displays on the final attempt at guessing the hidden thinker. 

| **Feature**             | **Action**                                                             | **Expected Result**                                                                                     | **Actual Result** |
| ----------------------- | ---------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- | ----------------- |
| Provide hint function  | When attempts left equals one a hint is provided that gives a clue as to the hidden thinks identity | Hint is correctly displayed at last attempt | Works as expected |

<details><summary>Screenshot</summary>
<img src="docs/hint.png">
</details>

4. Progress Tracking: A visual representation of my progress alongside the remaining number of attempts in each round, ensuring a clear understanding of my progress.

| **Feature**                           | **Action**                               | **Expected Result**                                                       | **Actual Result** |
| ------------------------------------- | ---------------------------------------- | ------------------------------------------------------------------------- | ----------------- |
| Progress bar |The progress bar fills as the user inputs correct letters, visually illustrating their proximity to correctly guessing the philosopher| The progress bar is displayed below the letter submit button and fills according to how many letters are left to guess | Works as expected |

<details><summary>Screenshot</summary>
<img src="docs/progress1.png">
<img src="docs/progress2.png">
<img src="docs/progress3.png">
<img src="docs/progress4.png">
</details>

5. Result Display: After successfully guessing a word, I would like to see a message of congratulations alongside a philosophical quote, adding a sense of achievement to the gameplay.

| **Feature** | **Action**                                                               | **Expected Result**                                                                        | **Actual Result** |
| ----------- | ------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ----------------- |
| End Game screen | Guess the hidden thinker within the given number of attempts | Congratulations screen displays with a picture of Euripides and a philosophical quote | Works as expected |

<details><summary>Screenshot</summary>
<img src="docs/correctscreen.png">
</details>

6.  After incorrectly guessing the word, I would like to immediately know what the correct answer was. 

| **Feature** | **Action**                                                               | **Expected Result**                                                                                              | **Actual Result** |
| ----------- | ------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------- | ----------------- |
| End Game Screen | When all guess attempts have been used and the hidden thinker has not been identified | The correct answer is displayed | Works as expected |

<details><summary>Screenshot</summary>
<img src="docs/incorrectScreen.png">
</details>

7.  A scoreboard to track the frequency of correct answers, providing a clear record of successful guesses. 

| **Feature**          | **Action**                                                                            | **Expected Result**                                             | **Actual Result** |
| -------------------- | ------------------------------------------------------------------------------------- | --------------------------------------------------------------- | ----------------- |
| Scoreboard | Correctly guess the hidden thinker | The amount of correct guesses is saved on the scoreboard displayed on both the main game and end game section | Works as expected |

<details><summary>Screenshot</summary>
<img src="docs/scoreboard1.png">
<img src="docs/scoreboard2.png">
</details>

8. Clear Game Understanding and navigation: Ensuring users easily comprehend the game mechanics for a seamless and enjoyable experience.

| **Feature**        | **Action**                                                  | **Expected Result**             | **Actual Result** |
| ------------------ | ----------------------------------------------------------- | ------------------------------- | ----------------- |
| Simple navigation buttons | 1. User wants to return to the start screen during game play to change difficulty setting 2. Upon end of game user wants to quit/ or play again. | 1. "back" button returns user to start screen 2.  User can choose to either "play again" or "quit" by pressing the relevant button on the end game screen  | Works as expected |

<details><summary>Screenshot</summary>
<img src="docs/backbutton1.png">
<img src="docs/quitbutton.png">
</details>

9. Self-Challenge Capability: Providing users with the opportunity to change the difficulty setting and enhance their skills while playing.

| **Feature**    | **Action**                                                           | **Expected Result**                               | **Actual Result** |
| -------------- | -------------------------------------------------------------------- | ------------------------------------------------- | ----------------- |
| Difficulty select buttons  | Select preferred difficulty using the options of easy, medium and difficult buttons| Attempts left will adjust accordingly (easy=8, medium=6 hard=4) | Works as expected |

<details><summary>Screenshot</summary>
<img src="docs/levelselect1.png">
<img src="docs/level2.png">
<img src="docs/level3.png">
<img src="docs/level4.png">
</details>

10. Full Responsiveness: Designing the game to adapt effortlessly to various screen sizes and devices, ensuring accessibility for all users.

| **Feature**  | **Action**                               | **Expected Result**       | **Actual Result** |
| ------------ | ---------------------------------------- | ------------------------- | ----------------- |
| Responsive design used throughout project | Change device or screen size | Displays correctly without layout issues | Works as expected |

<details><summary>Screenshot</summary>
<img src="docs/galaxy fold.png">
<img src="docs/ipad pro.png">
<img src="docs/iphone SE.png">
<img src="docs/iphone_se_landscape.png">
<img src="docs/iphone12_landscape.png">
<img src="docs/nesthub.png">
<img src="docs/surfaceduo.png">
<img src="docs/surfacepro7.png">
</details>

11. The user to be directed to a custom 404 error page upon entering a non-existent URL, eliminating the need to rely on the browser's back button.

| **Feature**                      | **Action**                                           | **Expected Result**                        | **Actual Result** |
| -------------------------------- | ---------------------------------------------------- | ------------------------------------------ | ----------------- |
| 404 error page | Page cannnot be found |  Directs user back to the game via 404 error page if they type a url that doesnt exist| Works as expected |

<details><summary>Screenshot</summary>
<img src="docs/404test.png">
</details>


## Bugs

| Bug                                                                                                                                         | Fix                                                                                    |
| ------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| Initial rendering of reviews.html failed with a cursor object error.  | The problem arose from using 'reviews.pub_name' to access database information. However, 'reviews' represents the entire cursor object retrieved from MongoDB, while 'pub_name' is an attribute of each individual document (review) within the cursor. Changing 'reviews' to 'review' in the iteration loop resolved the error.   | 

 Side navbar mobile function not working, 404 error on js file being returned  | A simple typo had caused this error, the Javascript folder had been named 'jss'. Correcting it to 'js', resolved the issue and the scripts.js file was able to be located and executed    | 



Encountered a type error while attempting to implement a visual star rating system based on the users rating.   | The issue stemmed from comparing a string to an integer, resulting in a TypeError. Resolution involved converting the rating to an integer using the int() function before comparison, thereby rectifying the issue."   | 

Resolved an issue where the food bowl icon failed to display in the review card main panel.  | The problem stemmed from a typo in the MongoDB naming pairs, where 'dog_meals=True' was incorrectly written as 'dog_meals=:True'. By removing the erroneous '=', the fontawesome food bowl icon now displays correctly.  | 

After implementing a for loop in the get_pubs application to fetch and render reviews associated with pub IDs, only pubs were displayed on the homepage without any reviews |   To address this, debugging statements were integrated into the route function, revealing that although both pubs and reviews were retrieved from the database, there were no reviews associated with pub IDs. A thorough examination of the MongoDB collections highlighted a data type discrepancy: the reviews collection utilized "pub_id" as a string, while the pubs collection employed ObjectId. This mismatch prevented proper association between pubs and reviews.

Resolution: To resolve the issue, code was added to convert ObjectId to a string format when retrieving data from the pubs collection. This adjustment ensured compatibility between the pub IDs in both collections, enabling accurate linkage between pubs and their associated reviews. With the data type mismatch rectified, the reviews were successfully associated with the corresponding pubs, allowing them to be displayed on the homepage as intended.   | 

Issue around displaying user_rating within the reviews visually as stars, despite converting to integers within the write_review route there was still a type error being displayed.  |  It appears that the issue is not with the conversion of user_rating to an integer in the route function but rather with how it's being used in the template. The error message indicated that a string object cannot be interpreted as an integer, which suggests that user_rating is still a string when it's being used in the template. Further investigation revealed that the error specifically occured on the line where user_rating was being used in the range function.
This was resolved by adding |int after review.user_rating, which ensured that user_rating was intepreted as an integer before being used in the range function.   | 


After creating the Flask route for editing reviews, an issue arose where the edit_review.html template failed to render. No error messages were displayed, and upon introducing print statements to the route for debugging, it became apparent that the route wasn't being called at all.Further investigation revealed a simple error in the edit_review.html template. The "Edit" button was not enclosed within a form element, preventing the GET request to the edit_review URL from being sent.   | Correcting this oversight by ensuring the "Edit" button was appropriately placed within a form element with the method set to "GET" enabled the Flask route to handle the GET request effectively, resulting in the expected rendering of the edit_review.html template






             |

## Deployment

### GitHub Pages

The website was deployed using GitHub Pages by following these steps:

1. In the GitHub repository navigate to the Settings tab
2. On the left hand menu select Pages
3. For the source select Branch: main
4. Once saved, GitHub will refresh and your website will be publishd from GitHub repository
5. The link to your published website will appear: "Your site is published at https://amegeddon.github.io/The-Thinker-Game/"

### Forking the GitHub Repository

1. Go to the GitHub repository
2. Click on Fork button in top right corner

### Making a Local Clone

1. Go to the GitHub repository
2. Locate the Code button above the list of files and click it
3. Highlight the "HTTPS" button to clone with HTTPS and copy the link
4. Open Git Bash
5. Change the current working directory to the one where you want the cloned directory
6. Type git clone and paste the URL from the clipboard ($ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY)
7. Press Enter to create your local clone

## Credits

### Images

- arrow used on back button was taken from [Fontawesome](https://fontawesome.com/)
- The four images used all come from Adobe Stock images and have been licensed for use [Adobe Stock Images](https://stock.adobe.com/uk)
- Images edited to remove background and resized using adobe Photoshop 


### Code

- [Instructions Modal](https://getbootstrap.com/docs/5.1/components/modal) was built using the Bootstrap v5.1.3 documentation
- https://codepen.io/cathydutton/pen/JjpxMm was used for guidance only in putting together the basic guessing game.
- For direction regarding readme structure and markdown formatting I referred to (https://aleksandracodes.github.io/CI_PP2_SunshineGuessing) by Aleksandra. 
-  [w3schools](https://www.w3schools.com/js/js_timing.asp) was consulted to target media query at mobiles in landscape orientation. 

## Acknowledgements

Thanks in plentiful supply for everyone who has put up with me cursing javascript. 

- to my mentor Richard for reminding me at every mentor meeting that Javascript is brilliant
- and to everyone else that I have hounded into playing the game and giving me feedback
- finally, thanks to the slack community for their encouragement and advice. 
