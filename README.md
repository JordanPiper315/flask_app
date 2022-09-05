# Backpacking Application
A database built in postgresql with ORM in Python. Datebase is for a mobile application that will help backpackers plan and execute backpacking trips more efficiently.

## API Reference Table
| Endpoint Paths        | Methods | Parameters  |
|-----------------------|---------|-------------|
| localhost:5000/users  | GET     |             |
| localhost:5000/users  | GET     | /<int:id>   |
| localhost:5000/users  | POST    |             |
| localhost:5000/users  | DELETE  | /<int:id>   |
| localhost:5000/trips  | GET     |             |
| localhost:5000/trips  | GET     | /<int:id>   |
| localhost:5000/trips  | POST    |             |
| localhost:5000/trips  | DELETE  | /<int:id>   |
| localhost:5000/foods  | GET     |             |
| localhost:5000/foods  | GET     | /<int:id>   |
| localhost:5000/foods  | POST    |             |
| localhost:5000/foods  | DELETE  | /<int:id>   |
| localhost:5000/gear   | GET     |             |
| localhost:5000/gear   | GET     | /<int:id>   |
| localhost:5000/gear   | POST    |             |
| localhost:5000/gear   | DELETE  | /<int:id>   |
| localhost:5000/permits| GET     |             |
| localhost:5000/permits| GET     | /<int:id>   |
| localhost:5000/permits| POST    |             |
| localhost:5000/permits| DELETE  | /<int:id>   |
| localhost:5000/trails | GET     |             |
| localhost:5000/trails | GET     | /<int:id>   |
| localhost:5000/trails | POST    |             |
| localhost:5000/trails | DELETE  | /<int:id>   |

### What future improvements are in store, if any?
This is an application I really hope to build someday. I will be expanding the tables with more things like trail ratings, gear categories, as well as creating more relationships between tables and their data. I plan on implementing relationships that allow people to have their gear and their gear for each respective trip, same with food. And the ability to see your hiking buddies gear so you can make sure your packing is complimentary and there isn't any useless repetitive gear being packed for a trip. I'm sure an endless stream of potential improvements will come to my mind as I continue to build out this project.

# flask_app
