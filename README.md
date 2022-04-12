<h1 align="center">Maeve's Bags</h1>

View the repository in GitHub [here](https://github.com/MaeveHughes/Maeves-Bags)

View the live project [here] ()

# Project Overview

Maeve's Bags was built as the 5th milestone project as part of Code Institute's Full Stack Software Software Development course. The full stack application uses a Django framework, HTML, CSS, Javascript and Python. 

Maeve's Bags is an ecommerce web application for customers seeking to purchase bags online. Visitors to the site would be able to browse all products by sorting, searching and by the various bag categories. Visitors can also register for an account to view past orders and contact the company with any queries.

Please note that the website is for educational purposes only. Stripe's credit card payment functionality is active but remains in a "test mode" so that no payments will be taken. Please do not enter any personal credit/debit card numbers whilst using the site. 

When testing this app, to make a payment, the following details should be used:

* Card number: 4242 4242 4242 4242
* CVC: any three numbers
* Date: any future date
* ZIP Code: any five numbers

# Contents

1. [User Experience (UX)](#user-experience-(ux))
    - [Strategy](#strategy)
    - [Scope](#scope)
    - [Structure](#structure)
    - [Skeleton](#skeleton)
    - [Surface](#surface)
2. [Information Architecture](#information-architecture)
    - [Database](#database)
    - [Data Model](#data-model)
3. [Technologies Used](#technologies-used)
4. [Testing](#testing)
5. [Deployment](#deployment)
    - [Local Deployment](#local-deployment)
    - [Deployment to Heroku](#deployment-to-heroku)
    - [Storing Static Files with AWS](#storing-static-files-with-aws)
    - [Connecting Stripe to Heroku](#connecting-stripe-to-heroku)
6. [Credits](#credits)
    - [Code](#code)
    - [Media](#media)
    - [Blog Credits](#blog-credits)
7. [Acknowledgments](#acknowledgments)

# User Experience (UX)

## Strategy

### User Stories

#### Viewing & Navigation
1. As a first time user, I would like to instinctively know what the website is offering. 
2. As a first time user, I would like to view a list of bags.
3. As a first time user, I want to be able to view individual bag details.
4. As a first time user, I want to be able to easily view the total of my purchases at any time.
5. As a first time user, I want to be able to contact the business with any queries I may have. 

#### Registration & User Accounts
6. As a site user, I want to be able to easily register for an account.
7. As a site user, I want to be able to easily login or logout.
8. As a site user, I want to be able to easily recover my password in case I forget.
9. As a site user, I want to be able to receive email confirmation after registering. 
10. As a site user, I want to have a personalised user profile.

#### Sorting & Searching
11. As a site user, I want to be able to sort the list of available bags.
12. As a site user, I want to be able to sort a specific category of bag.
13. As a site user, I want to be able to sort multiple categories of bags simultaneously.
14. As a site user, I want to be able to search for a product by name or description.
15. As a site user, I want to be able to easily see what I have searched for and the number of results.

#### Purchasing & Checkout
16. As a purchasing user, I want to be able to easily select the quantity of a bags when purchasing it / them.
17. As a purchasing user, I want to be able to view items in my bag to be purchsed.
18. As a purchasing user, I want to be able to adjust the quantity of individual items in my bag.
19. As a purchasing user, I want to be able to easily enter my payment information.
20. As a purchasing user, I want to be able to feel my personal and payment information is safe and secure.
21. As a purchasing user, I want to be able to view an order confirmation and checkout.
22. As a purchasing user, I want to receive an email confirmation after checking out.

#### Admin & Store Management
23. As a site owner, I want to be able to add, edit and remove products from the site easily. 
24. As a site owner, I want access to an admin section to view and manage orders. 

## Scope

The key features of the website were developed based on the user stories.

### For any site user: 

- Home page, with striking image of a fashionable person holding a handbag on their arm which quickly helps users to understand the purpose of the site.

- Products Page, where users can view all the products or products based on filtering criteria. 

- Product Detail Page, detailing information about the product. From here users can add products to their bags or decide to return to the products page.

- Shopping Bag page, where users can see what products have been added to their bag and adjust the quantity as needed.

- Checkout page, allowing users to purchase products. 

- Confirmation page, allowing users to see a confirmation of their order.

- Contact Page, where users can view the contact details for the company and contact the company using the contact form.

- Sign Up Page, where users can register to become a registered user.

### For registered users: 

All of the above plus: 

- Profile Page, where users can update their default delivery information allowing for ease at checkout. 

- Order History, from the profile page, users can see the previous orders they have made. 

- Log Out Page, where users can log out of their account. 

### For Site Admin:

All of the above plus: 

- Site management page, where admin users can add, edit and delete products.

## Structure

This website has 10 custom built pages and 14 (not all are used) account operations Django Allauth pages. The navbar at the top of the screen gives users access to the most important pages at all times.

#### Pages

**Accessible to all users**

* Header and navigation bar - The brang name is on the top left corner with a link to home page. Visible only on large screens. The navbar consists of the products navigation menu, with sorting or filtering possibilities. My account dropdown list of options for register and login. When registered, the dropdown list contains profile and logout links. There is a search bar for looking after products by name or key words in description. Bag icon with link to your bag list items and the total price of the selected order. The mobile navbar has the same search and cart links, however rather than links to the products, there is a collapsible side nav which is triggered by a burger menu. 

* Home - The landing page of the site, with striking image of a fashionable woman holding a handbag on their arm and a informative statement outlining "The new collections are here for Spring | Summer 2022", followed by a shop now button. This is sitting on a marble background image. This gives first time visitors a nice welcome.

* Products - This is a list of all products when clicking on the shop now button on the home page, clicking on a category in the navbar, or performing a search. There is a sorting option for prices and rating in ascending or descending way. The layout of the products page is similar to that of the Boutique Ado walkthrough project by displaying 4 products in a row on extra large screens, 3 on large screens, 2 on medium and small devices and 1 on extra small screen sizes. Basic product information is displayed below the product image (product name, price and a view product details button). As there may be a large amount of products displayed on a page, I have added a back to top button which appears when the user scrolls to the bottom of the page. I have deliberately put this at the bottom of the page so the focus is not drawn away from the products.

* Product Detail - When choosing one specific product, a new page opens that contains the chosen product, its details, input quantity option and a button to add it to bag. Admin users are also able to edit and delete products using the icons featured in this section. Products can be added to the bag by clicking the add to bag button. Users can return to an all products view by clicking the "Continue Shopping" button.

* Cart - A user purchases an item by adding it to the cart. The Cart is the users digital shopping cart, containing all products the user has added to it and their details, including the chosen quantity. Each product from the bag contains its name, image, price, quantity selected and the subtotal which is price multiplied by quantity. The user has the option to update each products quantity or remove it (this is only currently available on desktop view). The grand total with delivery included is displayed and two buttons: one to proceed to checkout and one to go back and shop more. If a user does not meet the free delivery threshold a helpful message will be displayed to let them know what they need to spend in order to qualify for free delivery. If the user has no items in the shopping bag, a message is displayed to the user to let them know this and a button to take the user to the all products page is displayed.

* Checkout - The checkout page features a form for the user to fill in, with name, email, phone number, delivery address. The checkout page contains the payment form from Stripe that takes: card number, CVC, expiry date and ZIP code. The page includes an order summary , as a table with products name, images (images are links that will take the user back to the product details page for that product details)quantity selected, subtotal. Also, the delivery costs, grand total and a button that redirects to bag for adjusting it if needed. From the checkout page, if user is authenticated, they can save their details to their My Profile so they are prefilled for the next order. 

* Order Confirmation - The page shows when a payment has successfully been made and an order confirmation will be displayed to the user. The confirmation will also be sent to the given email address during checkout. If the order was successful, the cart will be emptied. In the confirmation, the user can view the items order, the quantity, an order number, grand total and delivery details. At the bottom of the page their is a link back to the products to encourage users to purchse more items.

* Sign In - The page gives users the ability to log into the site by using a form. Users have to provide their username and password. There is two buttons at the bottom of the page: One to log in and one back to the home page.

* Sign Up - The page gives users the ability to register by using a form. Users have to provide their email address, email address confirmation, username, password and password confirmation. There is two buttons at the bottom of the page: One to register and one back to the login page.

* Contact - A simple contact form that is sent to the site owner and the page also includes the companys contact details. The form is sent by email to the site owner. Contact messages can be located on the site administration page (for superusers only).


**Accessible to signed in users**

* My Profile - Each user can access their own personal profile to view order history and the users billing and shipping details is here. A message to inform the user that this is a past order confirmation is displayed to avoid confusion.

* Sign Out - The page gives users the ability to log out of the site. There is two buttons at the bottom of the page: One to log in and one back to the products page.

* Other accounts operations pages such as Forgot Password.

**Accessible to Admin users**

* Add Product - This is where admin users can add new products to the website. Admin users have to fill out a form with the following details: name, sku, price, category, rating, description and also have the option to upload an image. If the admin user decides not to use an image it will use the default image. At the end of the form there is two buttons: one to add product and the other to cancel which will bring the user back to the admin page.

* Edit Product - The page for admin users to edit or delete products. In order to access this page the admin user will have to open a particular product and select the buttons edit or delete. If the user decides to edit a product they have the option to edit the following details: name, sku, price, category, rating, description and image. If the user clicks on the delete button the product is automatically deleted.


#### Pages provided by Django

These pages are provided by the Allauth package of the Django framework, but are customised by me to fit in with the rest of the site. Read more about Allauth [here](https://django-allauth.readthedocs.io/en/latest/)

* Sign Up - where users can register for an account on the site.

* Sign in - Registered users can log accessing their personal info etc by signing in.

* Sign Out - Registered users can log out of the site.

* Various pages for email verification and password reset, etc.


#### Features left to implement
* An option for users to leave a review /rating on each product.
* A welcome or discount offer for new customers, such as 20% off their first order, to encourage more registrations.
* Additional payment options such as Apple Pay or Paypal for ease of purchasing.


## Skeleton

Below you can find the links for my wireframes, showing how I would like the pages to be structured, and how the site will appear on different device sizes. 

The wireframes have been created using moqups and show for Desktop, iPad and iPhone. 

- Home Page
    - [Desktop](documentation/wireframes/HomePageDesktopWireframe.png)
    - [iPad](documentation/wireframes/HomePageIPadWireframe.png)
    - [iPhone](documentation/wireframes/HomePageIPhoneWireframe.png)
- All Products Page
    - [Desktop](documentation/wireframes/ProductsDesktopWireframe.png)
    - [iPad](documentation/wireframes/)
    - [iPhone](documentation/wireframes/)
- View Product Page
    - [Desktop](documentation/wireframes/ProductDetailsDesktopWireframe.png)
    - [iPad](documentation/wireframes/)
    - [iPhone](documentation/wireframes/)
- Basket Page
    - [Desktop](documentation/wireframes/BagDesktopWireframe.png)
    - [iPad](documentation/wireframes/)
    - [iPhone](documentation/wireframes/)
- Checkout Page
    - [Desktop](documentation/wireframes/CheckoutDesktopWireframe.png)
    - [iPad](documentation/wireframes/)
    - [iPhone](documentation/wireframes/)
- Confirmation Page
    - [Desktop](documentation/wireframes/OrderSummaryDesktopWireframe.png)
    - [iPad](documentation/wireframes/)
    - [iPhone](documentation/wireframes/)
- Contact Us Page
    - [Desktop](documentation/wireframes/ContactDesktopWireframe.png)
    - [iPad](documentation/wireframes/)
    - [iPhone](documentation/wireframes/)


