
// add useContext
import React, { useState,useContext } from "react";
import { firebaseAuth } from "../provider/authprovider";
import { withRouter } from "react-router-dom";
import firebase from 'firebase';
import {Col, Row ,Form,Button} from 'react-bootstrap';
import { Link } from "react-router-dom";
import './Sign.css';
const Signup = (props) => {
  const { handleSignup, inputs, setInputs, errors } = useContext(firebaseAuth);

  const [email, setEmail] = useState("")

  // const [email,setEmail]=useState('');
  // const [password,setPassword]=useState('');
  //const [passwordConfirmation,setPasswordConfirmation]=useState('');
  //const [signupError,setSignupError]= useState('')
 // const formisValid = () => password === passwordConfirmation;

  const submitSignup = async(e) => {
        e.preventDefault();

        //if (!formisValid()) {
          //  setSignupError({ signupError: 'Password do not match!' });
        //}
        //wait to signup 
        await handleSignup()
        //push home
        props.history.push('/')
    }
  const handleChange = (e) => {
    const { name, value } = e.target;
    console.log(inputs);
    setInputs((prev) => ({ ...prev, [name]: value }));
  };

  const handleChange1 = (e) => {
    console.log(e.target.name)
    setEmail(e.target.value)
  }

  return (
    <div>
      <Row>
        <Col lg={{ span: 6, offset: 4 }} xs={{ span: 12 }}>
          <div className="auth-wrapper">
            <div className="auth-inner">
              <Form onSubmit={submitSignup}>
                <h3>Sign Up</h3>
                <Form.Group controlId="formBasicEmail">
                  <Form.Label>Email address</Form.Label>
                  <Form.Control
                    type="email"
                    placeholder="Enter email"
                    value={inputs.email}
                    name="email"
                    onChange={handleChange}
                  />
                </Form.Group>

                <Form.Group controlId="formBasicPassword">
                  <Form.Label>Password</Form.Label>
                  <Form.Control
                    type="password"
                    placeholder="Password"
                    value={inputs.password}
                    name="password"
                    onChange={handleChange}
                  />
                </Form.Group>
                <Button variant="primary" type="submit">
                  Submit
                </Button>
              </Form>
              
              <p className="forgot-password text-right">
                Already registered ? <Link to="/signin">login</Link>
              </p>
            </div>
          </div>
        </Col>
      </Row>
    </div>
  );
};

export default withRouter(Signup);
