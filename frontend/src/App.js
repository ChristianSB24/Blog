import React, { Component } from 'react'; 
import axios from 'axios';

class App extends Component {
  state = {
    posts: []
  };
// new
  componentDidMount() {
    this.getPosts();
  }
// new
  getPosts() {
    axios
      .get('https://immense-shelf-24544.herokuapp.com/')
      .then(res => {
        this.setState({ posts: res.data });
      })
      .catch(err => {
        console.log(err);
      });
    }
    render() {
      return (
        <div>
          {this.state.posts.map(item => (
            <div key={item.id}>
              <h1>{item.title}</h1>
              <span>{item.entry}</span>
        </div>
      ))}
    </div>
    );
  }
}
export default App;