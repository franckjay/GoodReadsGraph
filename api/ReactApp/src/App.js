import React from "react";
import './App.css';
import { Container } from "semantic-ui-react";
import { BookEntry } from "./components/BookEntry";
import { GrabBook } from "./components/GrabBook";

function App() {
  return (
    <div className="App">
      <Container style={{marginTop: 40}}>
          <BookEntry/>
          <GrabBook/>
        </Container>
    </div>
  );
}
export default App;
