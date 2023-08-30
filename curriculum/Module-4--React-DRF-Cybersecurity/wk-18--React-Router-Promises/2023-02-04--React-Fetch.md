Saturday, February 4, 2022
=====================
### Video Resources from Previous Cohorts
- [Videos](https://www.youtube.com/channel/UCASZ7zW_Egu0T4KG3YEdGfw/playlists)

### Lecture Topics
- Promises
- Fetch API


## News Site III
Today, we are going to continue on with [news-site-III](https://github.com/deltaplatoonew/news-site-III) repo. Just like we saw with News Site I and II, we will be moving much of the code from yesterday's [news-site-II](https://github.com/deltaplatoonew/news-site-II).

First, let's review some terms to get us all on the same page.

**React Component**: A piece of reusable code that returns markup. Each React Component has its own own state and behaviors. A page can consist of one or more React Components. For us, we have a news site that has many components. Our home page has an ArticleList Component that renders a number of ArticleTeaser Components that render Article Components.

**State**: State is a global Javascript Object (or Python Dictionary if you still think in that way) on a particular React Component. It basically keeps track of how things are in that particular Component (e.g., On vs. Off, Selected vs. Not Selected, number of times clicked, etc.). State is private, meaning that it's scoped within a component.

**Props**: Parameters that you pass from a parent Component to a child Components. When you instantiate a new Component on the page, it may or may not take `props`. `props` and `state` are very different!

Now that we've gotten on the same page, let's move forward.

# Where AJAX Fails
Up to this point, we've been building our website using static data that exists within our app. Let's first grab our completed `news-site-II` and keep it nearby. We'll need it soon. We have been importing our News from `/data/news.json` and passing it into our ArticleList component. That's okay for right now, but we want to have dynamic data being fetched from an API. In a typical full stack web development team, you will have a frontend and backend developer working together to figure out data. The frontend developer will talk with the backend dev to go over what type of data structure is being returned and how to best move forward. Long story short - the backend developers provide the data, the frontend developers consume it.

Today's challenge isn't going to be a ton of React. Instead it's mostly using AJAX to get some data from an external source / web service and bring that back into our app to be presented in a React Component - once we get our data from the external source, we will put it in our HomePage and ArticleList components.

To understand this better, we have to talk about `promises` in Javascript. Let's start off first with a review of AJAX. AJAX stands for Asynchronous Javascript And XML. You make a request from a web page using AJAX and if it's successful, it does something. If it is not successful, we do something else. Here's a basic implementation of AJAX:

```javascript
$.ajax('https://jsonip.com', {
  success: function(data) {
    console.log(data);
  },
  error: function() {
    alert('something went wrong')
  }
})
```

This is not a terrible way to fetch data and do something with it. The original purpose of AJAX was just meant to grab data from widgets and then bring it back to your page. As the Internet grew, however, it became a bit more unmanageable. Here's a hypothetical example if Facebook were a single page app and they were using AJAX:

```javascript
$.ajax('https://www.facebook.com/login', {
  success: function(data) {
    // Login Successful - show home screen
  },
  error: function() {
    alert('something went wrong')
  }
})
```

While it may seem simple enough, this is probably not what's going on behind the scenes. There are probably a ton of other AJAX calls that would occur. You'd log in, hit the home screen, and then probably have some posts loaded via AJAX, maybe some photos, some statuses, etc. Your code might look more like a nightmare like this:

```javascript
$.ajax('https://www.facebook.com/login', {
  success: function(data) {
    // Login Successful - show home screen
    $.ajax('https://www.facebook.com/posts', {
      // Posts loaded
      $.ajax('https://www.facebook.com/posts/photos', {
        success: function(data){
          // Photos loaded
          $.ajax('https://www.facebook.com/posts/statuses', {
            success: function(data){
              // Statuses loaded
              $.ajax('https://www.facebook.com/posts/comments', {
                success: function(data){
                  // Comments loaded
                  $.ajax('https://www.facebook.com/posts/likes', {
                    success: function(data){
                      // Likes loaded
                    },
                    error: alert('something went wrong with likes')
                  })
                },
                error: alert('something went wrong with comments')
              })
            },
            error: alert('something went wrong with statuses')
          })
        },
        error: alert('something went wrong with photos')
      })
    }),
    error: function() {
      alert('sorry, error with posts')
    }
  },
  error: function() {
    alert('something went wrong')
  }
})
```

As you can begin to see with the AJAX calls above, it's beginning to form what's called the `JS Christmas Tree of Doom` or `Javascript Hell`. It's very difficult to read and isn't read top to bottom. Instead, it's read from outside to inside. It's like a Quintin Tarantino movie. This, however, is how the web used to be written.

# Promises
Moving onto `promises`, let's pretend that your house is a website and that you want to buy new carpets for your living room. There was a period of time when hardwood was all the rage but I think people are moving back towards carpet. Take a look at the code below:

```javascript
// Buying furnishings for your house off the Internet is asynchronous
function getNewCarpetsForLivingRoom(){
  $.ajax('Buy carpet online', {
    // When you purchase anything online (in our case it's carpet), you provide your money and it's out of your hands. You now just wait.
    success: function(data){
      // Carpet was delivered
      placeCarpetInLivingRoom;
      say('I love my new carpet');
    },
    error: function() {
      callCustomerService;
    }
  });
}
```

That's old code using `AJAX`. In today's modern web development world, we use `fetch` - it's a bit simpler and gets all of the code in one place:

```javascript
fetch('buildHouse')
  .then(return fetch('frame house')) // fires off when the house is built
  .then(return fetch('hvac & electricity'))
  // this allows us to have asynchronous code that reads top to bottom
```

In JS, there is a concept called `promises` that allow us to make calls to web services. It looks a little something like this:

```javascript
new Promise(function() {
  // when you create a Promise, you pass in a callback function
  // the callback function will return something at some point in the future
})
```

In the real world, let's say you are buying a house or a condo for the first time. Unless you are super baller and should not be here at Code Platoon, you probably don't have 1-3 hundred thousand dollars in the bank to pay for it out of pocket. You will likely take a mortgage out. You go to a bank and they provide a Promise to you that they will loan you, say $200,000. You then go to someone selling their house and you can say that a Bank is Promising you $200,000. You can make a contract with a seller at that point that says you will have money in the bank to pay them for their home at some point in the future.

JS Promises promise a value of something in the future. Let's build a house using Promises:
```javascript
function buildFoundation() {
  return new Promise(function(resolve, reject) {
    setTimeout(function(){ // setting a timer here that the promise will resolve in 1000 milliseconds
      resolve();
    }, 1000);
  });
}

buildFoundation().then(function() { // here, we are relying on the Promise of the foundation being built. After that, we'll console log below
  console.log('Foundation Built')
})
```

If you run this in the console, you should see `Foundation Built` show up. Continuing on, let's create a bunch of promises to create our house:

```javascript
function buildFoundation() {
  return new Promise(function(resolve, reject) {
    setTimeout(function(){ // setting a timer here that the promise will resolve in 1000 milliseconds
      console.log('foundation built')
      resolve();
    }, 1000);
  });
}

function buildFrame() {
  return new Promise(function(resolve, reject) {
    setTimeout(function(){ // setting a timer here that the promise will resolve in 2000 milliseconds
      console.log('frame built')
      resolve();
    }, 2000);
  });
}

function buildHVAC() {
  return new Promise(function(resolve, reject) {
    setTimeout(function(){ // setting a timer here that the promise will resolve in 3000 milliseconds
      console.log('hvac built')
      resolve();
    }, 3000);
  });
}

function buildElectric() {
  return new Promise(function(resolve, reject) {
    setTimeout(function(){ // setting a timer here that the promise will resolve in 2500 millisecond
      console.log('electric built')
      resolve();
    }, 2500);
  });
}

// now we can call things to occur in a specific order:
buildFoundation()
  .then(buildFrame())
  .then(buildHVAC())
  .then(buildElectric())
```

Run this in your console! Does it do what you expect? Uh oh - we have a bug! It appears that the Electric is being run before the HVAC! Let's fix it:

```javascript
buildFoundation()
  .then(() => buildFrame())
  .then(() => buildHVAC())
  .then(() => buildElectric())
```

Now we get what we want to see. When in doubt, always use fat arrow functions.


# Fetch
Let's talk about the `fetch` API to retrieve things from web resources. It's pre-built in to your console and is a bunch of chained promises together:

```javascript
fetch('http://localhost:3000/api') // first, make a request to localhost or wherever
  .then((response) => response.json()) // then, get the response object and turn it into json
  .then((json) => console.log(json)) // then, get the response (json) and then console log it out
```

Let's actually make a request to our API (built into our `news-site-iii`). When you run `npm run start` today, we have your regular web server and an API that is running on port 3001. If you hit `3001/api/articles`, you get the list of articles back. If you hit `3001/api/articles/2`, you will get the specific article in that list. Go back to the console and make a fetch request to that endpoint. You will get a Promise, followed by an Object. You will also need to turn off insecure scripts to load it up (the icon next to the URL bar).


Challenges
----------
* [News Site III](https://github.com/deltaplatoonew/react-news-site-iii)
For today's challenge, you will create a Javascript module that calls out to the API. We've stubbed this out in `ArticlesAPI.js` - you need to write the code that goes in here (you will not need to explicitly create Promises).
