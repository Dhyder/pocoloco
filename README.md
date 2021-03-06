# Vintasia Galleria
## Author
* [Shaggy](https://github.com/Dhyder)

## Description
This is a Gallery Django application that allows uploading of images, showcasing and sharing via link. 

## Screenshots
![Heart](https://user-images.githubusercontent.com/86789832/143848413-317498bd-93fa-46e2-8fe4-8107b45edcdb.PNG)
![Heart](https://user-images.githubusercontent.com/86789832/143848670-53f38a0d-81e0-4c97-b06f-63659c0c0a42.PNG)

## Live Link
You can view the site at: [Heart of Vintasia](https://heartofvintasia.herokuapp.com/)

## User Story
- View different photos that interest me.
- Click a single image to expand it and view the details of that photo.
- Search under different categories.
- Copy link to the photo for sharing with my friends.
- View photos based on location they were taken


## SetUp / Installation Requirements
### Prerequisites
* Django 3.2.9
* python3.8.10
* virtualenv
* pgAdmin4
* HTML5  
* CSS3
* Javascript 
* Font Awesome
* jQuery

### Cloning
* In your terminal:

        $ git clone https://github.com/Dhyder/pocoloco.git
        $ cd pocoloco/

## Running the Application
* Creating the virtual environment

        $ virtualvenv virtual
        $ source virtual/bin/activate
 or (windows)
 
        $ source virtual/Scripts/activate

* Installing Dependencies

        $ pip install -r requirements.txt
        
* Making Migrations

        $ python manage.py makemigrations galleria
        
* Migrate

        $ python manage.py migrate

* Running the application:

        $ python3.8 manage.py runserver
        

## Testing the Application
* To run the tests for the class files:

        $ python3.8 manage.py test

## Technologies Used
* Python3.8.10
* Django3.2.9

## Known Bugs
* No known bugs at the moment
## Author's Contact Information
* For any queries, you can reach out at [desastrecaliente@gmail.com]

### MIT License:
Copyright (c) 2021 **Shaggy**
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
