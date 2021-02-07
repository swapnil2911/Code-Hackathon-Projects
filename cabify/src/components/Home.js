import React, {useContext,useState,useEffect} from 'react';
import {firebaseAuth} from '../provider/authprovider'
import {Navbar,Nav,Form,InputGroup,Button,FormControl,Row,Col,Card,Modal,Container} from 'react-bootstrap';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faSearch } from '@fortawesome/free-solid-svg-icons'
import firebase from 'firebase';
import './HomenL.css';
const Home = (props) => {
  const { handleSignout, inputs, setInputs, errors } = useContext(firebaseAuth);
  const [show, setShow] = useState(false);

  const handleClose = () => setShow(false);
  const handleShow = () => setShow(true);
  const handelAdd =()=>{
    setShow(false);
    // console.log(adddate);
    // console.log(adddest);
    // console.log(addsrc);
    // console.log(maindate);
    if(!addsrc || !adddest|| !adddate )
    {
      setAdddst('');
      setAddsrc('');
      alert('Enter valid inputs!')
    }
    else{
      const email = localStorage.getItem('email');
      const docObject = { 
        source:addsrc,
        destination:adddest,
        date:adddate,
        email:email,
        phone:phone
      };
      firebase.firestore().collection("requests").add(docObject);
      setAdddate(new Date());
      setAdddst('');
      setAddsrc('');
     
    }
  }
  const [addsrc,setAddsrc]=useState('');
  const [adddest,setAdddst]=useState('');
  const [adddate,setAdddate]=useState(null);
  const [data,setData]=useState([])
  const [src,setSrc]=useState('');
  const [dest,setDest]=useState('');
  const [date,setDate]=useState('');
  const [datauser, setDataUser] = useState([])

  const [loaded, setLoaded] = useState(false)
  const [phone,setPhone]=useState('0000000000');
  var datausr=[];
  var data1=[]
  useEffect(()=>{
    firebase.firestore().collection("requests").get()
    .then(function(querySnapshot) {
      querySnapshot.forEach(function(doc) {
        // doc.data() is never undefined for query doc snapshots
       // data1.push(doc);
        //setData(data1);
        //console.log(doc.data());
        data1.push(doc.data());
        console.log(data1);
        

    });
    setData(data1);
    datausr=data1.filter(function(data){
      return data.email===localStorage.getItem("email");
    })

    setDataUser(datausr)
    setLoaded(true)
    console.log(datauser)

  });
  },[])
  const handleSubmit=()=>{
    //console.log(data);
    data1=data;
    console.log(data1)
    if(src!=='')
    {
      data1=data1.filter(function(data){
        return data.source===src;
      });
    }
    if(dest!=='')
    {
      data1=data1.filter(function(data){
        return data.destination===dest;
      });
    }
    if(date!='')
    {
      data1=data1.filter(function(data){
        return data.date===date;
      }); 
    }
    //console.log(data1);
    setData(data1);
  };
  //console.log(data);
  // setData(data1);
  //console.log(adddate);
  // console.log(maindate);

  if(!loaded) {
    return <div>Loading ...</div>
  }

  return (
    <div>
      <Navbar
        id="Navbar"
        className="navbar_main_container"
        bg="primary"
        variant="dark"
        expand="lg"
      >
        <Navbar.Brand className="navLinks navBrand" href="/">
          <h1>Cabify </h1>{" "}
        </Navbar.Brand>
        <Button variant="danger" onClick={handleSignout} className="ml-auto" style={{Align: 'right'}}>Signout!</Button>
      </Navbar>
      <Row>
        <Navbar className="bg-light" style={{width:"100%"}}>
          <Col lg={3} className="input-group ">
            <input
              type="text"
              className="form-control"
              placeholder="Source"
              name="srch-term"
              value={src}
              onChange={(e) => setSrc(e.target.value)}
            />
            <div className="input-group-btn">
              <button className="btn btn-default"  onClick={handleSubmit}>
                <FontAwesomeIcon icon={faSearch} />
              </button>
            </div>
          </Col>
          <Col lg={3} className="input-group ">
            <input
              type="text"
              className="form-control"
              placeholder="Destination"
              name="srch-term"
              value={dest}
              onChange={(e)=>setDest(e.target.value)}
            />
            <div className="input-group-btn">
              <button className="btn btn-default"  onClick={handleSubmit}>
                <FontAwesomeIcon icon={faSearch} />
              </button>
            </div>
          </Col>
          <Col lg={3} className="input-group">
            <input
              type="date"
              className="form-control"
              name="srch-term"
              value={date}
              onChange={(e)=>setDate(e.target.value)}
            />
            <div className="input-group-btn">
              <button className="btn btn-default"  onClick={handleSubmit}>
                <FontAwesomeIcon icon={faSearch} />
              </button>
            </div>
          </Col>
        </Navbar>
      </Row>
      <div
        className="navbar navbar-inverse navbar-static-top width-fix"
        id="navbar"
        role="navigation"
      >
      </div>
      <Container >
      <Row>
        <Col lg={{ span: 3 }} id="box2">
          <h3>MY REQUESTS</h3>
          <Button variant="dark" onClick={handleShow} className="mr-sm-5">
            Add New Request
          </Button>
          <Modal show={show} onHide={handleClose}>
            <Modal.Header closeButton>
              <Modal.Title>Travel Request</Modal.Title>
            </Modal.Header>
            <Modal.Body>
              <Form>
                <Form.Group controlId="Source">
                  <Form.Label>Source</Form.Label>
                  <Form.Control
                    type="text"
                    placeholder="Enter starting point"
                    defaultValue={addsrc}
                    onChange={(e) => setAddsrc(e.target.value)}
                  />
                </Form.Group>
                <Form.Group controlId="Destination">
                  <Form.Label>Destination</Form.Label>
                  <Form.Control
                    type="text"
                    placeholder="Enter the destination"
                    default
                    Value={adddest}
                    onChange={(e) => setAdddst(e.target.value)}
                  />
                </Form.Group>
                <Form.Group controlId="Date">
                  <Form.Label>Date</Form.Label>
                  <Form.Control
                    type="Date"
                    placeholder="Enter the date"
                    defaultValue={adddate}
                    onChange={(e) => setAdddate(e.target.value)}
                  />
                  <Form.Group controlId="Phone No:">
                  <Form.Label>Phone No:</Form.Label>
                  <Form.Control
                    type="text"
                    placeholder="Enter Phone No:"
                    defaultValue={phone}
                    onChange={(e) => setPhone(e.target.value)}
                  />
                </Form.Group>
                </Form.Group>
              </Form>
            </Modal.Body>
            <Modal.Footer>
              <Button variant="secondary" onClick={handleClose}>
                Close
              </Button>
              <Button variant="primary" onClick={handelAdd}>
                Save Changes
              </Button>
            </Modal.Footer>
          </Modal>
          {datauser.map((item) => {
              return ( 
                <Row class="myrequest">
                  <Card style={{margin:"5%"}}>
                    <div class="card-body">
                      <p className="card-title">
                        Destination: {item.destination}
                      </p>
                      <br></br>
                      <p className="card-text">Source: {item.source}</p>
                      <br></br>
                      <p className="card-text">Date: {item.date}</p>
                      <br></br>
                    </div>
                  </Card>
                </Row>
              );
          })}
        </Col>

        <Col lg={{span:7,offset:1}} xs={12}>
          {data.map((item) => {
            if (localStorage.getItem('email') !== item.email) {
              return (
                <Row>
                  <Card style={{width: "100%"}}>
                    <h5 className="card-header">Journey</h5>
                    <div class="card-body">
                      <h5 className="card-title">
                        Destination: {item.destination}
                      </h5>
                      <p className="card-text">Source: {item.source}</p>
                      <p className="card-text">Date: {item.date}</p>
                      <p className="card-text">Contact: {item.email}</p>
                      <p className="card-text">Phone No: {item.Phone}</p>
                      <a href="#" className="btn btn-primary">
                        Accept
                      </a>
                    </div>
                  </Card>
                </Row>
              );
            }
          })}
        </Col>
      </Row>
      </Container>
    </div>
  );
};

export default Home;          
       
       
       
       
       
       
       
       