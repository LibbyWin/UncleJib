
# Welcome to Uncle Jib's!

## The Snow Sports Specialists

Here at Uncle Jib's we are a family run retailers who love snow and everything to do with it. We will get you the right equipment
We are all about the experience here at Uncle Jib's and want to bring you the very best experience when using our site. We hope you 
all enjoy browsing and hope to see you again soon.

Uncle Jib's webshope has been designed and built by Libby Winfield as a final project for the Code Institute Full Stack Web Development 
Diploma. The purpose of this shopping site is to allow for new customers to shop on a safe and secure site in order to shop for the latests
snowboards and equipment. Specifically aimed at customers who enjoy being outdoors in the snowy mountains looking for the highest quality 
and stylist snowbaords to suit their riding needs.

## UX

#### Business Goals
- online professional shop
- provide links to social Media
- products with photos/descriptions/ details


#### Visitor Goals
- find new snowboards
- browse categories of snowboards
- 

WHAT USERS EXPECT/NEED/want
-
-
-
-
-
- 



## DESIGN CHOICE

- fonts

- icons

- colours


## wireframes

- add links

## Pages

- home page
- products 
- cart 
- categories
- search
- about
- delivery
- returns
- contact
- FAQs
- register
- login
- logout
- accounts
- checkout
- terms and conditions

## furture features

- favourites
- email a customer when order is being processed
- dicount
- sales
- newsletter
- subscribe
- 

##DATABASE MODELS

-product MODELS

 | Name | Key in DB | Validation | Field Type |
 | --- | --- | --- | --- |
 | Title | title | max_length=250 | CharField |
 | Image 1 | image_01 | blank=True | ImageField |
 | Image 2 | image_02 | blank=True, null=True | ImageField |
 | Image 3 | image_03 | blank=True, null=True | ImageField |
 | Price | price | max_digits=6 | DecimalField |
 | Descriptions | description |  | TestField |
 | Size | size | max_length=100 | CharField |
 | Colour | colour | max_length=100 | CharField |
 | Gender | gender | max_length=100 | CharField |
 | Year | year | max_length=100 | CharField |
 | Flex | flex | max_length=100 | CharField |
 | Shape | shape | max_length=100 | CharField |
 | Rider Profile | rider_profile | max_length=100 | CharField |
 | Board Profile | board_profile | max_length=100 | CharField |
 | Condition | condition | max_length=100 | CharField |



##CHECKOUT MODELS

| Title | Key in DB | Validation | Field Type |
|---|---|---|---|
|  Full Name | full_name  |  max_length=50 | CharField  |
| Phone Number | phone_number  |  max_length=20 |  CharField |
| Country | country | max_length=40 |  CharField |
| Postcode | postcode | max_length=20 | CharField  |
| Town or City |  town_or_city | max_length=40 | CharField  |
| Street Address 1 | street_address1 | max_length=40 | CharField  |
| Street Address 2 | street_address2 |  max_length=40 | CharField  |
| County |  county |  max_length=40 | CharField  |
| Date | date |  default=datetime.date.today | DateField  |


## ORDERLINEITEM

| Title | Key in DB | Validation | Field Type |
|---|---|---|---|
| Order | order | Order, null=False | ForeignKey |
| Products | product | Product, null=False | ForeignKey |
| Quantity | quantity | blank=False | IntegerField |

## Technologies used
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 




Use this section to provide insight into your UX process, focusing on who this website is for, what it is that they want to achieve and how 
your project is the best way to help them achieve these things.

In particular, as part of this section we recommend that you provide a list of User Stories, with the following general structure:
- As a user type, I want to perform an action, so that I can achieve a goal.

This section is also where you would share links to any wireframes, mockups, diagrams etc. that you created as part of the design process. 
These files should themselves either be included as a pdf file in the project itself (in an separate directory), or just hosted elsewhere online 
and can be in any format that is viewable inside the browser.


## Features

In this section, you should go over the different parts of your project, and describe each in a sentence or so.
 
### Existing Features
- Feature 1 - allows users X to achieve Y, by having them fill out Z
- ...

For some/all of your features, you may choose to reference the specific project files that implement them, although this is entirely optional.

In addition, you may also use this section to discuss plans for additional features to be implemented in the future:

### Features Left to Implement
- Another feature idea

## Technologies Used

In this section, you should mention all of the languages, frameworks, libraries, and any other tools that you have used to construct this project. 
For each, provide its name, a link to its official site and a short sentence of why it was used.

- [JQuery](https://jquery.com)
    - The project uses **JQuery** to simplify DOM manipulation.


## Testing

In this section, you need to convince the assessor that you have conducted enough testing to legitimately believe that the site works well. Essentially, 
in this part you will want to go over all of your user stories from the UX section and ensure that they all work as intended, with the project providing 
an easy and straightforward way for the users to achieve their goals.

Whenever it is feasible, prefer to automate your tests, and if you've done so, provide a brief explanation of your approach, link to the test file(s) and 
explain how to run them.

For any scenarios that have not been automated, test the user stories manually and provide as much detail as is relevant. A particularly useful form for 
describing your testing process is via scenarios, such as:

1. Contact form:
    1. Go to the "Contact Us" page
    2. Try to submit the empty form and verify that an error message about the required fields appears
    3. Try to submit the form with an invalid email address and verify that a relevant error message appears
    4. Try to submit the form with all inputs valid and verify that a success message appears.

In addition, you should mention in this section how your project looks and works on different browsers and screen sizes.

You should also mention in this section any interesting bugs or problems you discovered during your testing, even if you haven't addressed them yet.

If this section grows too long, you may want to split it off into a separate file and link to it from here.

## Deployment

This section should describe the process you went through to deploy the project to a hosting platform (e.g. GitHub Pages or Heroku).

In particular, you should provide all details of the differences between the deployed version and the development version, if any, including:
- Different values for environment variables (Heroku Config Vars)?
- Different configuration files?
- Separate git branch?

In addition, if it is not obvious, you should also describe how to run your code locally.


## Credits

### Content
- The text for section Y was copied from the [Wikipedia article Z](https://en.wikipedia.org/wiki/Z)

### Media
- The photos used in this site were obtained from ...

### Acknowledgements

- I received inspiration for this project from X




LOGO CREATED BY ME ONLINE AT WWW.DESIGNEVO.COM