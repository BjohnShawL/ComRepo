import React, { Component } from 'react';
import './App.css';
import { CONFIG } from './config'
import { Card, CardDeck } from 'react-bootstrap'

class App extends Component {



  constructor() {
    super();
    this.state = {
      tags: []
    }
  };

  componentDidMount() {

    fetch(`${CONFIG.API_BASE_URL}/tags`).then(
      results => results.json()
    ).then(returnedTags => this.setState({ tags: returnedTags.data }))

  }

  cardBuilder(){
    return(this.state.tags.map((tag, index) =>
    <Card key={index} bg='success'>
      <Card.Body>
        <Card.Title>{tag.name}</Card.Title>
        <Card.Subtitle>-embodied by {tag.character}</Card.Subtitle>
        <Card.Text>
          {tag.description}
        </Card.Text>
  <Card.Footer>{tag.current_use} out of {tag.max_use} uses remaining</Card.Footer>
      </Card.Body>
    </Card>))
    
  }

  render() {
    console.log(this.state.tags);
    const tagsArray = this.state.tags.map((tag, index) => <li key={index}>{tag.name} {tag.character} {tag.current_use} {tag.max_use}</li>);
    const tagsCards = this.cardBuilder()
    return (
      <div className="App">
        
        <br></br>
        {/* <ul>
        {tagsArray}
      </ul> */}
        <CardDeck>
          {tagsCards}
        </CardDeck>

      </div>

    );
  }
}
export default App;
