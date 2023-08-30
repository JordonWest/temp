Monday, February 6, 2022
=====================
### Video Resources from Previous Cohorts
- [Videos](https://www.youtube.com/channel/UCASZ7zW_Egu0T4KG3YEdGfw/playlists)

### Lecture Topics
- React Lifecycle Methods


# Review: Component Lifecycle
The following is a review of the "Component Lifecycle" for React. Below we are start with a component in its natural state:

```javascript
import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';

class App extends Component {
  render() {
    return (
      <div className="App">
        <div className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
          <h2>Welcome to React</h2>
        </div>
        <p className="App-intro">
          To get started, edit <code>src/App.js</code> and save to reload.
        </p>
      </div>
    );
  }
}

export default App;
```

Our component could also have a `constructor` that allows us to add `state` and/or `props`:

```javascript
import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';

class App extends Component {
  state = {
    articles: []
  }

  render() {
    return (
      <div className="App">
        <div className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
          <h2>Welcome to React</h2>
        </div>
        <p className="App-intro">
          To get started, edit <code>src/App.js</code> and save to reload.
        </p>
      </div>
    );
  }
}

export default App;
```

You may or may not have seen `componentDidMount()` show up in your code:
```javascript
import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';

class App extends Component {
  state = {
    articles: []
  }

  componentDidMount() {}

  render() {
    return (
      <div className="App">
        <div className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
          <h2>Welcome to React</h2>
        </div>
        <p className="App-intro">
          To get started, edit <code>src/App.js</code> and save to reload.
        </p>
      </div>
    );
  }
}

export default App;
```

`ComponentDidMount` is one of the [lifecycle methods](https://reactjs.org/docs/react-component.html#the-component-lifecycle) that comes built into React Components. These lifecycle methods basically allow you to hook into a component at that specific point in their "life" to achieve various things. This [image](https://cdn-images-1.medium.com/max/2000/1*XcGM-8E_hGl4fpAr9wJIsA.png) demonstrates the complete lifecycle of a React Component. At the top at the 12 o'clock position is a Component's birth: `willMount`, and the death is at 10 o'clock: `willUnmount`. Most of the time, you'll only use a couple of these lifecycle methods: `componentDidMount` and `componentWillReceiveProps`.

`componentDidMount` is most commonly used when you call out to your API. `componentWillReceiveProps` is fired when something happens with a parent component and it cascades down to the children to change the props. When `render` is fired, that is the point when a component is `mounted`.

Today, as you continue to wire up the `ArticlesAPI` JS module and connect to the API from your Components, you will want to use `componentDidMount` and `componentDidUpdate` for that (please see the example in the `readme` to help you).


Challenges
----------
* [News Site IV](https://github.com/deltaplatoonew/react-news-site-iv)
