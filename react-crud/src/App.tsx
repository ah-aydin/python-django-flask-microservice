import React from 'react';
import './App.css';
import Nav from './components/Nav';
import Sidemenu from './components/Sidemenu';
import Products from './product_service/products';

import { BrowserRouter as Router, Route} from 'react-router-dom';

function App() {
  return (
    <div className="App">
      <Nav />
      <div className="container-fluid">
        <div className="row">
          <Sidemenu/>

          <main className="col-md-9 ms-sm-auto col-lg-10 px-md-4">
            <Router>
              <Route path="/product_service/products" component={Products}/>
            </Router>
          </main>
        </div>
      </div>
    </div>
  );
}

export default App;
