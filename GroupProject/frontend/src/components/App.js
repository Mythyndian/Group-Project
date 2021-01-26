import React, { Component } from "react";
import { render } from "react-dom";
import DatePicker from "./DatePicker";

export default class App extends Component {
  constructor(props) {
    super(props);
  }

  render() {
    return (
        <DatePicker />
    );
  }
}

const appDiv = document.getElementById("app");
render(<App />, appDiv);