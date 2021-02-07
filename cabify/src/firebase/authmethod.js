import firebaseconfig from './firebaseIndex'
import firebase from 'firebase'

export const authMethods = {
  // firebase helper methods go here... 
  signup: (email, password, setErrors,setToken, setEmail) => {
    firebase.auth().createUserWithEmailAndPassword(email,password) 
      //make res asynchonous so that we can make grab the token before saving it.
      .then( async res => {
        const userObj={
          email:res.user.email
        }
        firebase.
         firestore().
         collection('users')
          .doc(email)
         .set(userObj);
        const token = await Object.entries(res.user)[5][1].b
        //set token to localStorage 
        await localStorage.setItem('token', token)
        await localStorage.setItem('email', res.user.email)

        setEmail(email)
        setToken(token)
        //grab token from local storage and set to state. 
          console.log(res)
        })
        .catch(err => {
        setErrors(prev => ([...prev, err.message]))
      })
    },
  signin: (email, password, setErrors, setToken, setEmail) => {
    //change from create users to...
    firebase.auth().signInWithEmailAndPassword(email, password) 
      //everything is almost exactly the same as the function above
      .then( async res => {
        const token = await Object.entries(res.user)[5][1].b
          //set token to localStorage 
          await localStorage.setItem('token', token)
          await localStorage.setItem('email', res.user.email)

          setEmail(email)      
          setToken(window.localStorage.token)
        })
        .catch(err => {
          setErrors(prev => ([...prev, err.message]))
        })
      },
      //no need for email and password
      signout: (setErrors, setToken, setEmail) => {
      // signOut is a no argument function
    firebase.auth().signOut().then( res => {
      //remove the token
      localStorage.removeItem('token')
      localStorage.removeItem('email')
        //set the token back to original state
        setToken(null)
        setEmail(null)
    })
    .catch(err => {
      //there shouldn't every be an error from firebase but just in case
      setErrors(prev => ([...prev, err.message]))
      //whether firebase does the trick or not i want my user to do there thing.
        localStorage.removeItem('token')
        
          setToken(null)
            console.error(err.message)
    })
    },
  }