# NewsAppDjango
This is a Django app that allows potential trip planners to respond to news and events. It uses NewsAPI and PredictHQ API to fetch data related to News and Events respectively. I have absolutely zero prior experience using Django and very minimal experience with HTML/CSS/JavaScript. Had to learn Django from scratch and then code it within 4 days. Hope you like my efforts.

How it Works
-----------
### 1. Login and Home Page
The trip curator needs to have a registered account with us. The app first validates the user, logs the user in or allows the user to sign up for an account. Post account creation and login, the user is taken to the global news homepage wwith latest global news articles fetched from major media houses. The home button on the top left corner can take the user back to this page whenever needed

### 2. Search Functionality
On the top of the page there is a search bar that allows the user to search for a specific place/event/person, etc. to fetch latest news and events related to that topic. The search results have a tab to toggle between news and key events

### 3. My Location
While signing up, the trip curator is asked for his/her location in addition to other standard fields. This location indicates the primary location that has been assigned to the curator (i.e. this user is responsible for handling all news/events related to that particular location). The drop down right next to the welcome text on the top of the page will allow the user to view 'My Location' page that will quickly give the results corresponding to his/her paerticular location eliminating the need for manual searching

### 4. Add Item to Pending List
This app also comes with the functionality to allow a user to track and manage news/events assigned to him/her. Clicking the '+' button next to an item will add it to the user's account.

### 5. Manage Your Tasks
On the account options dropdown there is an option for the user to view 'My Tasks'. Here, the user can view his/her tasks and mark the addressed ones as completed so that they don't show up in the pending tasks list

Installation Instructions
-----------
First, clone this repo to your machine
`git clone https://github.com/isdapro/NewsAppDjango.git `

Next, create and start a virtual environment
`virtualenv env --no-site-packages`
`activate`

Ensure you are at the correct level (you may have to do the following)
`cd NewsAppDjango\NewsApp `

Install the project dependencies
`pip install -r requirements.txt`

Modify the .env.example file after obtaining the required APIs and rename it to .env

Migrate the app and then start the server
`python manage.py migrate`
`python manage.py runserver`

Open `localhost:8000` on your machine to view the app!
