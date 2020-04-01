
# Welcome to Uncle Jib's!

## The Snow Sports Specialists

Here at Uncle Jib's we are a family run retailers who love snow and everything to do with it. We will get you the right equipment
We are all about the experience here at Uncle Jib's and want to bring you the very best experience when using our site. We hope you 
all enjoy browsing and hope to see you again soon.



## why was this site created?
Uncle Jib's webshope has been designed and built by Libby Winfield as a final project for the Code Institute Full Stack Web Development 
Diploma. The purpose of this shopping site is to allow for new customers to shop on a safe and secure site in order to shop for the latests
snowboards and equipment. Specifically aimed at customers who enjoy being outdoors in the snowy mountains looking for the highest quality 
and stylist snowbaords to suit their riding needs.

## UX

#### Business Goals
The goals for Uncle Jib's website on a buiness front are:
- Providing a professional online shop where users can easily fine their way around the site
- provide links to social Media
- products with photos/descriptions/ details


#### Visitor Goals
- find new snowboards
- browse categories of snowboards
- 

## WHAT USERS EXPECT/NEED/want
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
- order details

##DATABASE MODELS

-product MODELS

 | Name | Key in DB | Validation | Field Type |
 | --- | --- | --- | --- |
 | Title | title | max_length=250 | CharField |
 | Image 1 | image_01 | blank=True | ImageField |
 | Price | price | max_digits=6 | DecimalField |
 | Descriptions | description |  | TestField |
 | Size | size | max_length=100 | CharField |
 | Colour | colour | max_length=100 | CharField |
 | Flex | flex | max_length=100 | CharField |
 | Shape | shape | max_length=100 | CharField |
 | Board Profile | board_profile | max_length=100 | CharField |




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
- **Django** as a python framework.
- **AWS S3** Bucket to store images which are entered into the database.
- **Stripe** as a payment platform.
- **Heroku** for deployment
- **Pillow** as a python library for processing images.
- **Git** as version control.
- **Github** to allow storing and sharing the project remotely.
- **Whitenoise** allows the web app to have its own static files.
- **Boto3** to enable management and 
- **Sqlite3** for a development database.
- **Bootstrap** to provide simple structure to th website and making it mobile responsive.
- **Font Awesome** to provide the icons for the site.
- **Google Fonts** to style we websites fonts.
- **JQuery** as DOM manipulation.
- **HTML**
- **CSS**
- **Java** Script
- **Python**
- **Gitpod** was used to develop the entire site.



## Testing

The code below will delete the migrations due to an occuring error which occured multiple
 times. In order to migrate my files, I had to delete migrations and remigrate them 
 to the products model.py.
`find . -path "*/migrations/*.py" -not -name "__init__.py" -delete`
`find . -path "*/migrations/*.pyc"  -delete `  
`python manage.py migrate UncleJibs zero`

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

### Content
- The text for section Y was copied from the [Wikipedia article Z](https://en.wikipedia.org/wiki/Z)

### Media
- Logo created by me online at www.designevo.com

### Acknowledgements

- I received inspiration for this project from multiple shopping sites such as ridestore.com, absolute-snow.com and many more.
- 


