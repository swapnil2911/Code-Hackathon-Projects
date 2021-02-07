
import React, {useContext, Component } from 'react';
import './Sign.css';
import { firebaseAuth } from "../provider/authprovider";
import { Link } from "react-router-dom";
import {Col, Row } from 'react-bootstrap';

const Signin = () => {


  const {handleSignin, inputs, setInputs, errors} = useContext(firebaseAuth)
  
  const handleSubmit = (e) => {
    e.preventDefault()
    console.log('handleSubmit')
    handleSignin()
    
  }
  const handleChange = e => {
    const {name, value} = e.target
    console.log(inputs)
    setInputs(prev => ({...prev, [name]: value}))
  }

  return (
    <div>
    <Row>
    <Col lg = {{span:6,offset:4}} xs = {{span:12}}>
    <div className="auth-wrapper">
      <div className="auth-inner">
    
    <form onSubmit={handleSubmit}>
      <h3>Log In</h3>

      <div className="form-group">
          <label>Email address</label>
          <input type="email" name="email" className="form-control" placeholder="Enter email" value={inputs.email} onChange={handleChange}/>
      </div>

      <div className="form-group">
          <label>Password</label>
          <input type="password" name="password" className="form-control" placeholder="Enter password" value={inputs.password} onChange={handleChange}/>
      </div>

      <button type="submit" className="btn btn-primary btn-block">Submit</button>
      <p className="forgot-password text-right">
          Didn't <Link to='/signup' >sign up?</Link>
      </p>
      {errors.length > 0 ? errors.map(error => <p style={{color: 'red'}}>{error}</p> ) : null}
    </form>
    </div>
    </div>
    </Col>
    </Row>
    </div>
  );
};

export default Signin;