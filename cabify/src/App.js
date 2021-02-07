import React, {useContext, useEffect} from 'react';
import {Route, Switch, Redirect} from 'react-router-dom'
import Signup from './components/Signup'
import Signin from './components/Sign'
import './App.css';
import {firebaseAuth} from './provider/authprovider'
import Home from './components/Home';

function App() {
  const { token } = useContext(firebaseAuth)
  console.log(token)
  return (
    <>
    {/* switch allows switching which components render.  */}
      <Switch>
        {/* route allows you to render by url path */}

        <Route exact path='/' render={rProps => token === null ? <Signin /> : <Home />} />
        <Route exact path='/signin' component={Signin} />
        <Route exact path='/signup' component={Signup} />
      </Switch>
    </>
  );
}

export default App;