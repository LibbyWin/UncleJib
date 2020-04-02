
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
- Providing a professional online shop where users can easily fine their way around the site.
- There are links to all social media to provide Uncle Jib's with a brand awareness for all customers.

#### Visitor Goals
- Allows for shoppers to find the best snowboard for them, by providing descriptions and information relevant to each individual snowboard.
- Enjoy browsing for those who like to see what new products are being released.
- Ensures the users know what type of snowboarder type they are. They can choose what boarder suits their riding style and can find a suitable 
board from there.
- Buying for a trustworthy online dealer.

## WHAT USERS EXPECT/NEED/want
- The users need to be able to easily find selected items that are shown within the category on the navigation bar. 
- Having a clean and clear layout that allows user to easily navigate around the site.
- Ensure that the site is easy to use not only on a desktop view but also mobile views and tablets.
- All information and images should be layed out in a clear manor to make easy reading.
- Have a working contact page to allow for users to contact the site owner when they have any questions that need answering.
- To be able to see hwat items are within their cart.
- Allow for users to log into the site to keep their contact details and payment information.

## DESIGN CHOICE

- FONTS

### Icons
- There are many icons throughout the entire site to easily show what specific items represent. 
- - Within the footer section of the page there are two icons, Snapchat and Facebook. These two social media links lead the users 
onto those chosen platforms to allow users spread brand awarenss. 
- - There is a search icon on the navigation bar to show users that they can add anything within the search bar to find a 
specific item. 
- - On the home page, on the 'Select a Snowboard Category' there are two icons, Snowflakes and  Snowman. These icons are placed on the 
snowboard categories to add some character to the cards.  

### Colours
- Specific colours are shown and have been specifically chosen becuase they work well with each other.

- Background colour: #2c2e2f - Dark grey
- Headline colour: #2fb8ce - Light blue
- Text: #c5c5c5c - Dark white / Creme
- The use of dark white / creme on the dark grey background allows for users to easily read the text, as if white/#ffffff was chosen there 
would be a bright contrast and would strain the users eyes when viewing the site.

### Styling
- There are specific styling additions to the majrity of the buttons to allow for users to know when they are hovering on them. These buttons 
will turn from a light blue to dark blue to indicate that these will take oyu to other pages within the site. 
- Curved edges were chosen on buttons to make the site more user friendly. This is a common styling choice within bootstrap and is commonly 
used on sites such as Facebook and Instagram.


## wireframes
- All wireframes were hand drawn and were made 2/3x over to ensure I could create the best site possible wihtin the ssessed time period.
The wireframes can be found within the 'static' file under the name 'wireframes'.

## Pages

- Home Page
- Products 
- Cart 
- Categories
- Search
- About
- Delivery
- Returns
- Contact
- - 
- FAQs
- Register
- Login
- Logout
- Accounts
- Checkout


## furture features
There are many future features I would like to implement in the future to allow for a better user experience.
- Creating a 'like' system that all products will have. A user can simply 'like' a product and it be went to a wish list for future visits to 
the site.
- When a customer has purchased a snowboard from the website, an automatic email shall be sent to ensure them that theyre order is being 
requested, processed, in production and out for delievery. This will improve customer satisfaction and ease their nerve if they are a first 
time buyer. 
- When the snow seasons come to an end in early may, I would like for the site to have a sale, so users can purchase the same snowboard 
just at a lower price. 
- If a user has just signed up to the site, there will be a modal which will pop up and offer them a 10% discount on their first order to try 
and promote more sales and gain more users within the database.
- Create a newsletter for viewers that have accounts to notify them when there are specific sales on and to tell them about any new information
which they might have missed when they were last on the site.
- Allow for users to see order details once they have purchased their order. This will allow the user to ask for any alterations to their 
purchase and ask any question abot refund, exchanges and delivery information.

##DATABASE MODELS

### Product model app
Within the `products app`, the product containal all the data for the products within the site.

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




### Checkout Model
Found within the `checkout app`, shows how the form will appear on the site. 

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
- **CSS** - Much of the CSS has been used within the HTML as it was easier to import and use some of the style provided by Bootstrap.
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
`python3 manage.py runserver --run-sync` 
 - These few lines of code allowed for me to delete and reimport any migrations I needed to my project. However countless times I had to manually 
 delete the migrations folders, __pycache__, db.sqlite3 files to ensure that there was a hard reboot and reinstallation of `makemigrations` and `migrate`.

- Some testing was done within the products app to ensure that my spelling for 'products' and 'product' were caught. 

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
- The descriptions and images for the snowboard, descriptions and categories were all taken from www.absolute-snow.co.uk.
This site sells everything to do with the outdoors from hiking, wakeboarding and snowboarding. 
- Big thanks to W3Schools for alling me to understande certain concepts and use small snippets of their code to push the limits of this site.
- Big thanks to Scott Kipp for allowing me to take information form your previous MS4 and providing me with inspiration for the categories 
to products to product design for the site.
- The accounts app was taken from a previous project that we were taught and had been incorporated into this project, 
to allow me to spend more time on more inportant aspects of the site.


### Acknowledgements

- I received inspiration for this project from multiple shopping sites such as ridestore.com, absolute-snow.co.uk and many more.
- Many thanks to all the tutors at CI who helped me fix many bugs within my products/models.py file when it started to error out saying there 
was already a products table there when there wasnt. 
- Shout out to my mentor Brian Mc
- 


