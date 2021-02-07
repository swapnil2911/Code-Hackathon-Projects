import React, {useState, useEffect} from 'react';
import {authMethods} from '../firebase/authmethod'

export const firebaseAuth = React.createContext()

const AuthProvider = (props) => {
  const initState = {email: '', password: ''}
  const [inputs, setInputs] = useState(initState)
  const [errors, setErrors] = useState([])
  const [token, setToken] = useState(null)
  const [email, setEmail] = useState(null)

  useEffect(()=>{
    const tkn = localStorage.getItem('token')
    const eml = localStorage.getItem('email')

    if(tkn)
      setToken(tkn)
    
    if(eml)
      setEmail(eml)
  },[])


  const handleSignup = () => {

    // middle man between firebase and signup 
    console.log('handleSignup')
    // calling signup from firebase server
    authMethods.signup(inputs.email, inputs.password,setErrors ,setToken, setEmail)
    console.log(errors, token)
  }
  const handleSignin = () => {
    //changed to handleSingin
    console.log('handleSignin!!!!')
    // made signup signin
    authMethods.signin(inputs.email, inputs.password, setErrors, setToken, setEmail)
    console.log(errors, token)
  }

  const handleSignout = () => {
    authMethods.signout(setErrors, setToken, setEmail)
  }

  return (
    <firebaseAuth.Provider
    value={{
      //replaced test with handleSignup
      handleSignup,
      handleSignin,
      token,
      inputs,
      setInputs,
      errors,
      handleSignout,
    }}>
      {props.children}
    </firebaseAuth.Provider>
  );
};

export default AuthProvider;