# TAP-ENP Assignment - URL Shortener

### Running it locally

To run it locally, you can run the `flask run` command in the main directory and access the app at localhost:5000

### Build and run from Docker image

1. To build docker image, run `docker build -t smallurl .`
2. Run `docker run -d -p 5000:5000 smallurl` 
3. Access the web app at localhost:8000 (gunicorn uses port 8000)

### Hosting

The application is also hosted on: http://tap-smallurl.herokuapp.com (though there might be some cold start delays due to Heroku's dyno hibernation)

### Implemented challenges
1. **I've got style** - Simple and responsive layout
2. **Elephants never forget** - the shortened URLs are stored in a relational database
3. **Push to production** - Hosted on Heroku
4. **Tried and tested** - Wrote some unit tests
5. **I ship containers** - Containerized the application
6. Allow users to input custom alias!

### Assumption: 

- Custom alias provided can only be alphanumeric and have a maximum of 16 characters.
