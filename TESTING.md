# Paws & Pints Testing

<div style="text-align: right;">

[Back to README.md](README.md)

</div>

<img src="static/images/responsive.png">

[View the live project here.](https://paws-and-pints-9f68e52a491c.herokuapp.com/get_pubs)

Manual testing was performed continuously during development to ensure the functionality of various site features.

- - -

## CONTENTS

* [CODE VALIDATION](#code-validation)
  * [W3C Validator](#w3c-validator)
  * [JavaScript Validator](#javascript-validation)
  * [Python Validator](#python-validation)
  * [Lighthouse](#lighthouse)
  * [WAVE Testing](#wave-testing)
* [MANUAL TESTING](#manual-testing)
  * [Testing User Stories](#testing-user-stories)
  * [Full Testing](#full-testing)
    * [Site Wide](#site-wide)
    * [Index Home](#index-home)
    * [Register Page](#register-page)
    * [Log In Page](#log-in-page)
    * [Profile](#profile)
    * [Add Pub](#edit-profile)
    * [Manage Reviewss](#manage-reviews)
    * [404 Page](#404-page)
* [BUGS](#bugs)
  * [Solved Bugs](#solved-bugs)
  * [Known Bugs](#known-bugs)

<sup><sub>[*Back to top*](#contents)</sup></sub>

-----

## CODE VALIDATION 

### W3C Validator

The HTML on all pages of the site was validated using the W3C validator, and the CSS was also validated through the same tool. The HTML was checked by inputting the URL of the deployed site to avoid errors related to Jinja templating, while the CSS was validated via direct input.

<details><summary>Index HTML</summary>
<img src="static/images/html-home.png">
</details>

<details><summary>Register HTML</summary>
<img src="static/images/html-register.png">
</details>

<details><summary>Log In HTML</summary>
<img src="static/images/html-login.png">
</details>

<details><summary>Profile HTML</summary>
<img src="static/images/html-profile.png">
</details>

<details><summary>Add Pub HTML</summary>
<img src="static/images/add_pub.png">
</details>

<details><summary>Manage Reviews HTML</summary>
<img src="static/images/html-admin.png">
</details>


<details><summary>CSS</summary>
<img src="static/images/css-validator.png">
</details>

>Note:
> The 404 page was manually tested by inputting the code directly into the validator and no errors were found except for those related to the Jinja templating.
><details><summary>404 Error Page.</summary>
><img src="static/images/404-validator.png">
></details>

<sup><sub>[*Back to top*](#contents)</sup></sub>

-----

### Javascript Validation

[JS Hint](https://jshint.com) The JavaScript on the site was tested and no major errors were found. However, some warnings for undefined and an unused variable were flagged. The undefined variable warnings stem from code copied from Materialize, and all variables are used within HTML files.

<details><summary>Vanilla Javascript</summary>
<img src="static/images/js-validator.png">
</details>

<sup><sub>[*Back to top*](#contents)</sup></sub>

-----

### Python Validation

[CI Python Linter](https://pep8ci.herokuapp.com) has been utilized to validate Python code on the site, ensuring it complies with PEP 8 standards. Initially, this highlighted numerous whitespace errors, but these have been resolved, and the current code is now PEP 8 compliant.

<details><summary>Python</summary>
<img src="static/images/python-validator.png">
</details>

<sup><sub>[*Back to top*](#contents)</sup></sub>

-----

### Lighthouse

The Lighthouse tool in Chrome Developer Tools has been used to test performance, best practices, accessibility, and SEO. Both desktop and mobile tests have been conducted for each page.

<details><summary>Index</summary>
<img src="static/images/home-desktop.png">

<img src="static/images/home-mobile.png">
</details>

| | Performance | Accessibility | Best Practice | SEO |
| :---: | :---: | :---: | :---: | :---: |
| Desktop | 99 | 100 | 100 | 100 |
| Mobile | 90 | 100 | 100 | 100 |

<details><summary>Register</summary>
<img src="static/images/register-desktop.png"

<img src="static/images/register-mobile.png">
</details>

| | Performance | Accessibility | Best Practice | SEO |
| :---: | :---: | :---: | :---: | :---: |
| Desktop | 100 | 100 | 100| 100 |
| Mobile | 99 | 100 | 100 | 100 |

<details><summary>Log In</summary>
<img src="static/images/login-desktop.png"

<img src="static/images/login-mobile.png">
</details>

| | Performance | Accessibility | Best Practice | SEO |
| :---: | :---: | :---: | :---: | :---: |
| Desktop | 100 | 100 | 100 | 100 |
| Mobile | 98 | 100 | 100 | 100 |

<details><summary>Profile</summary>
<img src="static/images/profile-desktop.png">

<img src="static/images/profile-mobile.png">
</details>

| | Performance | Accessibility | Best Practice | SEO |
| :---: | :---: | :---: | :---: | :---: |
| Desktop | 100| 100 | 100 | 100 |
| Mobile | 98 | 100 | 100 | 100 |

<details><summary>Add Pub</summary>
<img src="static/images/add-pub-desktop.png">

<img src="static/images/add-pub-mobile.png">
</details>

| | Performance | Accessibility | Best Practice | SEO |
| :---: | :---: | :---: | :---: | :---: |
| Desktop | 100 | 100 | 100 | 100 |
| Mobile | 98 | 100 | 100 | 100 |

<details><summary>Manage Reviews</summary>
<img src="static/images/admin-desktop.png">

<img src="static/images/mobile-admin.png">
</details>

| | Performance | Accessibility | Best Practice | SEO |
| :---: | :---: | :---: | :---: | :---: |
| Desktop | 99 | 95 | 100 | 100 |
| Mobile | 91 | 95 | 100 | 100 |


> Notes for Lighthouse Testing:

>* The accessibility score is lower on the admin's Manage Reviews page due to the delete button. This button uses Materialize classes, and despite efforts, it has not been possible to adjust the red background and white text enough to provide sufficient contrast.
>
>* Performance scores on mobile devices can be improved by reducing image sizes. This can be achieved by adding a function to the photo upload Flask route that automatically resizes images upon upload.

<sup><sub>[*Back to top*](#contents)</sup></sub>

-----

### WAVE Testing

Testing with [WAVE](https://wave.webaim.org) has identified issues with the img alt tags, indicating they are duplicate and potentially insufficient. To improve accessibility, users should be able to provide their own descriptive alt text. The default "user uploaded image" is not adequate. Dynamically adding the {{pub.name}} has made the alt tag more meaningful but further work here is required. 


<sup><sub>[*Back to top*](#contents)</sup></sub>

-----

## Manual Testing

### Testing User Stories

>#### User Goals
>
>- Discover dog-friendly pubs across Anglesey and explore their amenities and services.
>- Engage with authentic reviews from fellow users to make informed decisions about pub visits.
>- Contribute to the community by adding new dog-friendly pubs and sharing personal experiences through reviews.
>- THe ability to edit their review entries to reflect updated experiences or feedback.
>- The ability to add pubs to the site and uploaded a photo to accompany the pub details. 
>- The ability for the user to delete pubs and reviews that they themselves have added.
>

>#### Site Admin Goals
>
>In addition to user goals:
>
>-  Manage pub entries and reviews seamlessly with options to edit or delete content effortlessly
>- Create an immersive and user-friendly platform with intuitive navigation, captivating visuals, and an appealing design.
>-  Ensure a seamless user experience across all devices by implementing full responsiveness, allowing the website to adapt seamlessly to different screen sizes and device types.
>- The user to be directed to a custom 404 error page upon entering a non-existent URL.

| Goal | Implementation | Image |
| :---: | :---: | :---: |
|  Discover dog-friendly pubs across Anglesey and explore their amenities and services.| Pubs are showcased in cards that reveal descriptions and reviews upon clicking. Icons highlight pub amenities, and tooltips provide detailed descriptions when hovered over | <img src="static/images/user-story1.png" style="width: 400px; height: auto;"> |
| Engage with authentic reviews from fellow users to make informed decisions about pub visits. | Reviews are displayed when clicking on a pub, with a star system visually representing the pub's rating. Additionally, each pub's location includes an average rating, also depicted with star | <img src="static/images/user-story2.png" style="width: 400px; height: auto;"> |
| Contribute to the community by adding new dog-friendly pubs and sharing personal experiences through reviews. | Users can add their own review of any of the pubs listed| <img src="static/images/user-story3.png" style="width: 400px; height: auto;"> |
| THe ability to edit their review entries to reflect updated experiences or feedback. |Users can edit their reviews directly from their profile page. | <img src="static/images/user-story4.png" style="width: 400px; height: auto;"> |
| The ability to add pubs to the site and uploaded a photo to accompany the pub details.  | Logged-in users can add a pub through the 'Add Pub' tab.|  <img src="static/images/user-story5.png" style="width: 400px; height: auto;"> |
| The ability for the user to delete pubs and reviews that they themselves have added. | Logged in users can delete their reviews and pubs from the 'Profile' tab. | <img src="static/images/user-story6.png" style="width: 400px; height: auto;"> |
| Manage pub entries and reviews seamlessly with options to edit or delete content effortlessly | Admin can edit or delete any post from the 'Manage Reviews' tab. | <img src="static/images/user-story7.png" style="width: 400px; height: auto;"> |
|  Create an immersive and user-friendly platform with intuitive navigation, captivating visuals, and an appealing design. | The site offers a simple, straightforward design that ensures ease of use, while the photo upload feature enhances its visual appeal.| <img src="static/images/user-story8.png" style="width: 400px; height: auto;"> | Ensure a seamless user experience across all devices by implementing full responsiveness, allowing the website to adapt seamlessly to different screen sizes and device types. | The site offers full responsive design. | <img src="static/images/user-story9.png" style="width: 400px; height: auto;"> | The user to be directed to a custom 404 error page upon entering a non-existent URL.| The 404 error page features a 'Home' button that directs users back to the main page when clicked | <img src="static/images/user-story10.png" style="width: 400px; height: auto;">

<sup><sub>[*Back to top*](#contents)</sup></sub>

-----

### Full Testing

Full testing was performed on the following devices:

* Laptop
  * Lenovo IDEAPAD 

* Mobile
  * iphone 12
 
 Desktop device tested the site using the following browsers:
 
 * Google Chrome
 * Mozilla Firefox
 * Microsoft Edge
 * Safari 

#### Site-Wide


| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| Navbar Links | Display different navigation bar links based on whether the user is logged out, logged in, or an admin. | View the site based on different login statuses. | Links are displayed according to each status | __PASS__ |
| Brand Logo | Directs user back to the home page | Clicked logo | Taken back to the home page | __PASS__ |


#### Index Home


| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| Search Bar operational| Returns relevant search results | Entered text | Shown correct search resuts | __PASS__ |
| Write a review link actionable (logged in) | User to be directed to 'Write a review' page | Clicked link | Taken to write review, review submitted succesfully | __PASS__ |
| Write a review link actionable (logged out) | User to be directed to 'Login' page | Clicked link | Redirected to the login page | __PASS__ |
| Register nav link actionable  | Returns sign up form | clicked link |Taken to Sign up page | __PASS__ |
| Login nav link actionable  | Returns login form | clicked link |Taken to Login page | __PASS__ |


#### Register Page


| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| Login link actionable | Redirects already registered users to the login page | Clicked link | Taken to login page | __PASS__ |
| Form validation | Error message appears to let user know they have not matched the required format | Input incorrect format | Helper text turns red and error message appears | __PASS__ |
| Username already taken  | Flash message if username is already in use | Attempt to sign up with the same username | Flash message appears | __PASS__ |
| View password Text | Password text revealed when user toggles 'show password' box | Clicks box | Password text becomes visible | __PASS__ |
| Register account | Flash message indicating registrationsuccess and user redirected to their profile | Register new account | Flash message appears and user redirected to profile | __PASS__ |


#### Log In Page


| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| View password Text | Password text revealed when user toggles 'show password' box | Clicks box | Password text becomes visible | __PASS__ |
| Flash Message: Incorrect Username or Password | Test with incorrect username and password | Flash message appears | PASS |
Log in | Flash message indicates success and redirects to profile | Enter correct login credentials | Flash message appears and redirects to profile __PASS__ |


#### Profile


| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| User Profile Accessible Only to the Logged-In User | Redirects Unauthorized Access to Login Page | Enter Incorrect Username in URL | Redirects User to Login Page | PASS |
| User Review Edit Button Functional on Profile page| Displays the user's full review with options to edit or cancel | Click the edit button | Full review details are shown |
| Edit Button on Review Page Functional | Allows input of revised details and provides a flash message | Click the edit button | Details are updated and a flash message is displayed |
| Cancel Edit Review Button Functional | Redirects User to Profile | Click Cancel Button | User Redirected to Profile | PASS |
| Delete Review Button Functional | Redirects to Confirm Deletion Page | Click Delete Button | Displays Confirm Deletion Page | PASS |
| Cancel Delete Review Button Functional | Cancels Deletion and Redirects to Profile Page | Click Cancel Button | Deletion Canceled and Redirected to Profile Page | PASS |
| Edit Pub Details Button Operational | Shows Pub form pre-filled with the user's previous input | Click the Edit button to modify pub information | Updates pub details, displays a flash message, and user directed to upload photo page | PASS |
| Edit Pub Details Button Operational | Shows Pub form pre-filled with the user's previous input | Click the Edit button to modify pub information | Updates pub details, displays a flash message, and user directed to upload photo page | PASS |
| Upload new photo button functional | Updates image and redirects user to their profile page | Click button and upload new image | Updates pub image, displays flash message and redirects to profile page | PASS |
| Continue without uploading image button | Directs user back to their profile page | Click button | User redirected to profile page | PASS |


#### Add Pub

| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| Submission Blocked if Inputs Are Left Empty | Submission of incomplete forms is blocked with an error message instructing the user to complete all required fields | Enter information in some but not all fields | An error message appears, and submission is prevented | PASS |
| Submit Button Functional | Displays upload photo page | Click the Submit Button | Upload photo page is correctly displayed | __PASS__ |
| Upload Button Functional | Returns user to their profile with a flash message | Uploads photo | Flash message appears and user is redirected to profile | __PASS__ |
| Continue Without Uploading Button Functional | Returns user to their profile page | Click the Continue Without Uploading Button | User is redirected to profile page | __PASS__ |
| get_photo flask route correctly display default image is no image is uploaded | New pub entry are given a default image of my lovely whippet dog | Adds new pub without uploading an image | Default image of lovely whippet correctly displayed | __PASS__ |


#### Manage Reviews

| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| User Must Be Logged In to Access This Page | Redirects to the login page if not authenticated | Access via direct URL entry | Redirects to login page | PASS |
| Delete Review Button Functional | Redirects to Confirm Deletion Page | Click Delete Button | Displays Confirm Deletion Page | PASS |
| Confirm Delete Review Button Functional | Review deleted, flash message displayed, and user redirected to manage reviews page | Click Confirm Deletion Button | 'Review successfully deleted' message displayed, user returned to manage reviews page | PASS |
| Cancel Delete Review Button Functional | Cancels deletion, user returned to manage reviews page | Click Cancel Button | Deletion canceled and user redirected to manage reviews page | PASS |
| Delete Pub Button Operational | Redirects to Confirm Deletion Page | Click Button | Confirm Deletion Page displayed | PASS |
| Confirm Delete Pub Button Functional | Pub deleted, flash message displayed, and user redirected to manage reviews page | Click Confirm Deletion Button | 'Pub successfully deleted' message displayed, user returned to manage reviews page | PASS |

-----

## Bugs

### Solved Bugs

| Bug                                                                                                                                         | Fix                                                                                    |
| ------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| Initial rendering of `reviews.html` failed with a cursor object error.  | The issue was caused by using `reviews.pub_name` to access database information. Since `reviews` represents the entire cursor object from MongoDB, and `pub_name` is an attribute of each individual review document, changing `reviews` to `review` in the iteration loop resolved the error. |
| Side navbar mobile function not working; 404 error on JS file being returned  | A typo in the folder name caused the issue. The folder was incorrectly named `jss` instead of `js`. Renaming it to `js` allowed the `scripts.js` file to be located and executed correctly. |
| Encountered a type error while implementing a visual star rating system based on user ratings.   | The error occurred due to comparing a string to an integer. The solution was to convert the rating to an integer using the `int()` function before comparison. |
| Resolved an issue where the food bowl icon failed to display in the review card main panel.  | The issue was due to a typo in MongoDB naming pairs: `dog_meals=True` was incorrectly written as `dog_meals=:True`. Removing the erroneous `=` corrected the display of the FontAwesome food bowl icon. |
| Issue with displaying reviews associated with pub IDs on the homepage. | Although both pubs and reviews were retrieved from the database, no reviews were associated with pub IDs due to a data type mismatch: the reviews collection used `"pub_id"` as a string, while the pubs collection used `ObjectId`. Adding code to convert `ObjectId` to a string format resolved the issue, enabling accurate linkage between pubs and reviews. |
| Issue with displaying `user_rating` visually as stars. Despite converting to integers within the `write_review` route, a type error was still present. | The problem was not with converting `user_rating` to an integer but with its usage in the template. The error message indicated that a string object could not be interpreted as an integer. Adding `|int` after `review.user_rating` in the template ensured that `user_rating` was treated as an integer before being used in the `range` function. |
| Issue with the `edit_review.html` template failing to render. | The issue was due to the "Edit" button not being enclosed within a form element, preventing the GET request from being sent. Placing the "Edit" button within a form element with the method set to "GET" resolved the issue, allowing the Flask route to handle the request and render the template correctly. |

<sup><sub>[*Back to top*](#contents)</sup></sub>

-----

### Known Bugs

| Bug                                                                 | Fix                                                                                    |
| ------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| Search Results Display Unpredictably | Despite various attempts to style the search results with CSS, they do not consistently appear at the top of the page as expected. Further investigation is needed to determine if the issue is related to the use of Materialize for card layouts. |
| Database Photos Not Deleted with Pubs | Photos stored in the database are not being removed when corresponding pubs are deleted, leading to increased storage use. This issue needs urgent attention. The current approach, which stores images as binary data, raises scalability concerns. Storing images separately via URLs could be a more efficient solution. The fact that images remain in the database even after the related pubs are deleted is not sustainable. |

<sup><sub>[*Back to top*](#contents)</sup></sub>
