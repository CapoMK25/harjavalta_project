import React, { Component } from "react";
import { render } from "react-dom";

export default class App extends Component {
  constructor(props) {
    super(props);
  }

  render() {
    return (
      <div>
        <HomePage/>
      </div>
    );
  }
}

const appDiv = document.getElementById("root");
render(<App/>, appDiv);