import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import Home from './Components/Home/Home';
import Table from './Components/Table/Table';

function App() {
 const currentPath = window.location.pathname;

  return (
    <Router>
      <div className="App">
        <Table />
      </div>
    </Router>
  );
}

export default App;
