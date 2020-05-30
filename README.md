[![Build Status](https://travis-ci.org/sw1ckham/cte-ecommerce.svg?branch=master)](https://travis-ci.org/sw1ckham/cte-ecommerce)

CTE-Ecommerce

<p>CTE-ecommerce is fully responsive </p>

## Table of contents

[**Project Goals**](#project-goals)

[**User Goals**](#user-goals)

[**Business Goals**](#user-goals)

[**Developer Goals**](#user-goals)

[**User Stories**](#user-stories)

[**Design Choices**](#design-choices)

[**Wireframes**](#wireframes)

[**Features**](#features)

[**Technologies used**](#technologies-used)

[**Testing**](#testing)

[**Deployment**](#deployment)

[**Credits**](#credits)

### Business Goals

* Increase social media traffic
* Showcase all artwork in organised albums
* Provide a contact point for customers, fans or collaborators to contact
* Increase sales of certain products

### Developer Goals

* Provide a clean design to highlight the business owners artwork
* Implement simple navigation around the site for ease of use
* Create a short 3 step process to purchasing a product
* Create responsive galleries of the business owners artwork
* Provide a secure way for users to pay for their products.
* Create fast loading time by compressing images, without affecting the quality of images. 

### User Goals

* Browse all of the Artists work available
* Securely purchase an item if possible
* Find relevant social media accounts

### User Stories

As a user I want

* Have a clear Registration option to become a user of the site
* Be able to Log In as a returning user
* To know how many products are in my cart at all times
* Find contact information about the Artist
* Find the Artists social media accounts
* Be able to view the site on all possible screen sizes
* Once added a product to the cart, be able to navigate back to the shopping page easily.
* Once in the Checkout, are able to navigate back to your cart without using the back button. 

### Design Choices

CTE ecommerce is dark themed with splashes of light green colour throughout. The minimilistic approach suits the needs of the owner of the site, emphasing his colourful art work with a dark background.
The site is simple and clean, the users main needs for the site are observing and Artists art work with thought to maybe purchasing a print, there's no need for any other clutter in the background.

1. Buttons
* All buttons have the same stylings. I chose a bright green to compliment the theme throughout the site, and nice transition increasing the scale to improve the user experience. 

2. [Font](https://fonts.google.com/specimen/Montserrat+Alternates?sidebar.open&query=Montserrat+Alternates)
* Montserrat Alternates - I chose this as the font throughout the site because it is unique to a lot of your other site in an Artistic way, but is also clearly ledgeable.

3. Icons
* I have used an Icon in place of the cart/shopping trolley header, also amend buttons in the cart.

4. Forms
* All forms are uniform and styled with green backgrounds for nice design. 

5. Product Panels
* The product panels are transparent other than the image of the art work. The description is hidden, accessible via a plus icon. This effect is again, to pay as much attention to 
the art itself and keep the site clean and uncluttered. 

6. Footer & Navbar
* Dark backgrounds and white text, keeping to the website theme I chose a light green hover transition on the social icons. 

7. Background images as front page
* Due to the owner of the sites request, the desktop and mobile homepage will be a digital piece of art work made by the owner himself. He wants to keep 
the initial view very simple and just a piece of his work.

### Wireframes

### Features

* Back to the top button on a large screen
* Instagram plug in
* Sending an email from the About page
* Add to Cart
* Adjust Cart items
* Checkout with Stripe payments
* Password Change 

### Features left to Implement

* I need to implement a feature that allows the user to edit their information after registering with us, this is good practise, but at the moment not a nessecity as they use a seperate form to
pay for their products and the address can be different each time to deliver too. 
* I will be implementing a price changing feature. The price will not be visible until you pick a size of a print, then the price will be dependant on the size chosen.
* I will be implementing a feature to sign up to a regular email show caseing new pieces of art. 
* I will be creating a Cart Model so when the user logs out, their shopping cart will be saved. I will also be able to implement the cart 

### Technologies used

* HTML
* CSS3
* JavaScript
* jQuery

* [Django](https://www.djangoproject.com/)
* [Bootstrap 4](https://getbootstrap.com/)

* [Font Awesome](https://fontawesome.com/)
* [Google Fonts](https://fonts.google.com/)

* Python
* [Heroku](https://dashboard.heroku.com/)
* [Postgres SQL]()
* [GitHub](https://github.com/sw1ckham/cte-ecommerce)

## Requirement files

1. boto3==1.13.12 - The Amazon Web Services (AWS) Software Development Kit (SDK) for Python. 
2. botocore==1.16.12 - The foundation for the AWS-CLI command line utilities.
3. dj-database-url==0.5.0 - Config method that returns a Django database connection dictionary with all the data in your URL. 
4. Django==1.11.28 - Python Framework
5. django-forms-bootstrap==3.1.0 - Django forms library with helps to work with HTML forms. 
6. django-multiselectfield==0.1.12 - Allows user to select multiple options from the choices provided in the model. 
7. django-resized==0.3.11 - Resizes the image uploaded by the user to a max-height and max-width
8. django-storages==1.9.1 - Provides a variety of storage backends in a single library. 
9. docutils==0.15.2 -  Modular system for processing documentation into useful formats
10. gunicorn==20.0.4 - A Python WSGI HTTP Server for UNIX
11. heroku==0.1.4 - Software to run our app on
12. jmespath==0.10.0 - Allows you to declaratively specify how to extract elements from a JSON document
13. Pillow==5.4.1 - Support for opening, manipulating, and saving different image file formats
14. psycopg2==2.8.5 - PostgreSQL database adaptor. 
15. python-dateutil==2.8.1 - Is an extension to the standard datetime module
16. pytz==2020.1 - Direct translation of the Olson timezone database, and changes to the timezone definitions need to be made to this source.
17. s3transfer==0.3.3 - Python library for managing Amazon S3 transfers
18. stripe==1.84.0 - Payment system API

### Testing

All testing was carried out on all screen devices, Google Chrome, FireFox and Internet Explorer.

* [HTML W3C Validation Service](https://validator.w3.org/)

1. Error: Element head is missing a required instance of child element title.
2. Warning: Consider adding a lang attribute to the html start tag to declare the language of this document.
3. Error: Non-space characters found without seeing a doctype first. Expected <!DOCTYPE html>.
4. Error: Bad value {% url 'register' %} for attribute href on element a: Illegal character in path segment: { is not allowed.
5. Error: Stray doctype.
* Took out unnecessary DOCTYPE. 
6. Error: Bad value myModal{{ forloop.counter }} for attribute id on element div: An ID must not contain whitespace.
7. Error: The aria-labelledby attribute must point to an element in the same document.
* Changed label name to the correct label so they match. 
8. Error: Bad value {{ MEDIA_URL }}{{ art.image }} for attribute src on element img: Illegal character in path segment: { is not allowed.
9. Warning: The type attribute is unnecessary for JavaScript resources.
* Deleted type attributes
10. Warning: The form role is unnecessary for element form.
* Deleted role = form. 
11. Error: Stray end tag span.
* Deleted stray span

* [CSS W3C Validation Service](https://jigsaw.w3.org/css-validator/)

1. 714	.panel-default	Value Error : padding none is not a padding value : none
* Fixed - Changed to 0.
2. 746	.panel-info > .panel-heading	Value Error : border-color none is not a border-color value : none
* Fixed - Deleted as border: 0 now. 
3. CSS W3C Validation also picked up that the vendor extentions provided by Auto Prefixer were unknown. 

* [JSHint](https://jshint.com/)

1. Pointed out unnecessary semi-colon, deleted. 

## Manual Testing 

Carried out by myself, and two other third parties. 

1. Login
* Error when put in the wrong username/password.

2. Registration
* Error when passwords don't match
* Error when email doesn't include @ and .co.uk/.com
* Error when email isn't unique
* Error when username isn't correct 

3. Social Links
* Click on the facebook and twitter icon, both open in a new window.

4. Reset passwork functionality
* You can reset your password, are sent a confirmation messafe

5. Test all user stories
* All points made in the user stories were verified by myself and two other parties. 

6. Art panels
* All photos are able to be viewed in larger size, in a modal, on all screen sizes. 
* All toggle buttons to show product description are below the image on all screen sizes. 

7. You are able to edit the quantity of your product in the cart. 

## Bugs found during Testing

1. Error messages on register and login pages were same colour as background - could not see!
* Solution - Styled default error messages in custom.css

## Bugs found during developement

1. No Quantity auto fill
* [Solution](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input/number) 
* If you were to add a product to the cart without specifying a quantity of that product. You would get a 404 error. This is because there is no 
default value rendered. I added value="1" to my input html which stopped the problem. 

2. White space coming up on the right, as a margin around my body.
* [Solution](https://stackoverflow.com/questions/4617872/white-space-showing-up-on-right-side-of-page-when-background-image-should-extend)

3. User was able to refresh success.html and redo form submission which would throw a stripe error as it is trying to take the payment again, but the cart is empty as they already paid.
* Solution - had to redirect users back to an empty cart page with a 'Success your payment has gone through message'.

## Continous Testing

I have used [Travis-CI](https://travis-ci.org/github/sw1ckham/cte-ecommerce) 

* At the beginning of Travis testing I had problems due to the version of 'Pillow' I was using and forgetting to update my requirements.txt.
Since updating the Pillow version and my requirements.txt the builds have been passing every time. 

* [![Build Status](https://travis-ci.org/sw1ckham/cte-ecommerce.svg?branch=master)](https://travis-ci.org/sw1ckham/cte-ecommerce)

### Deployment 





## Acknowledgements

### Media

* All images belong to the Artist Cormac Thomas Eddery. 
* Content was written by the developer Sophie Wickham and Cormac Eddery. 

### Code  
 1. Wanted to add more input fields when a User registers, the default Django User Model only allows 'Username' 'Password1' 'Password2'
 * [Solution](https://dev.to/coderasha/create-advanced-user-sign-up-view-in-django-step-by-step-k9m)
 2. Editing the Django error message so it pops up as an alert and then disappears. 
 * [Solution](https://www.youtube.com/watch?v=VIx3HD2gRWQ)
 3. Got code for modals off bootstrap site
 * [Solution](https://getbootstrap.com/docs/4.0/components/modal/#large-modal)
 4. Code from Stackoverflow to create a active nav link option
 * [Solution](https://stackoverflow.com/questions/25044370/make-clicked-tab-active-in-bootstrap)
 5. Horizontally center modal images
 * [Solution](https://stackoverflow.com/questions/37950121/how-can-i-put-bootstrap-modal-in-horizontally-center)
 6. How to render content over a background image
 * [Solution](https://css-tricks.com/text-blocks-over-image/)
 7. Vertical alignment using flexbox
 * [Solution](https://philipwalton.github.io/solved-by-flexbox/demos/vertical-centering/)
 8. Carousel on About page
 * [Solution](https://bootsnipp.com/snippets/xBdN)

## Credits

* Thank you very much to my mentor Spencer for all his help, also Student Care Tutors Hayley, Stephen, Xavier and Tim. Having you guys there throughout was
a great support and I am very grateful.

* A shout out to George and Cormac who meticulously tested the site before submission. 


 