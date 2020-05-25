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
* Create a form for users to contact the business owners
* Create responsive galleries of the business owners artwork
* Provide a secure way for users to pay for their products and provide a confirmation email

### User Goals

* Browse all of the Artists work available
* Securely purchase an item if possible
* Find relevant social media accounts

### User Stories

As a user I want

* Have a clear Registration option to become a user of the site
* Be able to Log In as a returning user
* To know how many products are in my cart at all times
* Change the size of my chosen product in my cart and the quantity of that product I want to buy
* Find contact information about the Artist
* Find the Artists social media accounts
* Be able to view the site on all possible screen sizes
* Once added a product to the cart, be able to navigate back to the shopping page easily

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


### Testing

All testing was carried out on all screen devises, Google Chrome, FireFox and Internet Explorer.

* [HTML W3C Validation Service](https://validator.w3.org/)

* [CSS W3C Validation Service](https://jigsaw.w3.org/css-validator/)

## Testing user stories

## Manual Testing 

Carried out by myself, and two other third parties. 

## Bugs found during Testing

## Bugs found during developement

1. No Quantity auto fill
* [Solution](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input/number) If you were to add a product to the cart without specifying a quantity of that product. You would get a 404 error. This is because there is no 
default value rendered. I added value="1" to my input html which stopped the problem. 

2. White space coming up on the right, as a margin around my body.
* [Solution](https://stackoverflow.com/questions/4617872/white-space-showing-up-on-right-side-of-page-when-background-image-should-extend)

## Continous Testing

### Deployment 

## Acknowledgements

### Media

* All images belong to the Artist Cormac Thomas Eddery. 
* Content was written by the developer Sophie Wickham and Cormac Eddery. 

### Code  
 1. Wanted to add more input fields when a User registers, the default Django User Model only allows 'Username' 'Password1' 'Password2'
 * [Solution](https://dev.to/coderasha/create-advanced-user-sign-up-view-in-django-step-by-step-k9m)
 2. Editing the Django error message so it pops up as an alert and then disappears. 
 *[Solution](https://www.youtube.com/watch?v=VIx3HD2gRWQ)

## Credits

* Thank you very much to my mentor Spencer for all his help, also Student Care Tutors Hayley, Stephen, Xavier and Tim. Having you guys there throughout was
a great support and I am very grateful.

* A shout out to George and Cormac who meticulously tested the site before submission. 


 