// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
    apiKey: "AIzaSyC-G9XcoCE6itDSM1tB_q4W4LuxlooFy7M",
    authDomain: "sigma-ab9fc.firebaseapp.com",
    projectId: "sigma-ab9fc",
    storageBucket: "sigma-ab9fc.firebasestorage.app",
    messagingSenderId: "790510874863",
    appId: "1:790510874863:web:cfd6c9cea4e886842feb1a",
    measurementId: "G-QT7LDYZWW9"
  };
  
  firebase.initializeApp(firebaseConfig);
  const auth = firebase.auth();
  const db = firebase.firestore();
  const storage = firebase.storage();
  
  function signUp() {
    const email = document.getElementById("signup-email").value;
    const password = document.getElementById("signup-password").value;
  
    auth.createUserWithEmailAndPassword(email, password)
      .then((userCredential) => {
        const user = userCredential.user;
        return db.collection("users").doc(user.uid).set({
          email: user.email,
          createdAt: new Date()
        });
      })
      .then(() => {
        document.getElementById("status").innerText = "Signed up and data saved!";
      })
      .catch(error => {
        document.getElementById("status").innerText = error.message;
      });
  }
  
  function login() {
    const email = document.getElementById("login-email").value;
    const password = document.getElementById("login-password").value;
  
    auth.signInWithEmailAndPassword(email, password)
      .then(() => {
        document.getElementById("status").innerText = "Login successful!";
      })
      .catch(error => {
        document.getElementById("status").innerText = error.message;
      });
  }
  