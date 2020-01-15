import React, { Component } from "react";
import Modal from "./components/Modal";
import axios from "axios";
import { BrowserRouter as Router, Route, Switch } from "react-router-dom";
import Branch from "./components/Branch";
import Login from "./components/accounts/login";
import Register from "./components/accounts/register";
import Header from "./components/layout/header";
import PrivateRoute from "./components/common/PrivateRoute";
import { Provider } from 'react-redux';
import store from "./store";
import { loadUser } from './actions/auth';

class App extends Component {
  componentDidMount() {
    store.dispatch(loadUser());
  };

  render() {
    return(
      <Provider store={store}>
        <Router>
          <Header/>
          <Switch>
          <PrivateRoute exact path="/" component={Branch}/>
          <Route exact path="/login" component={Login}/>
          <Route exact path="/register" component={Register}/>
          </Switch>
        </Router>
      </Provider>
      
    );
    
  };
}

export default App;