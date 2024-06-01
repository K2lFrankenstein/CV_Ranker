
import {initializeApp} from "https://www.gstatic.com/firebasejs/10.12.1/firebase-app.js";
import { getAuth, GoogleAuthProvider, onAuthStateChanged , signInWithRedirect,getRedirectResult } from "https://www.gstatic.com/firebasejs/10.12.1/firebase-auth.js";


var firebaseConfig = {
  "apiKey": "AIzaSyAYUO3JcjV2CK1UDOvudj4Nmzm-kqDs-X0",
  "authDomain": "randomsearch-b73d9.firebaseapp.com",
  "projectId": "randomsearch-b73d9",
  "storageBucket": "randomsearch-b73d9.appspot.com",
  "messagingSenderId": "1071038864705",
  "appId": "1:1071038864705:web:f46274c1f3bc860ea3d5c0",
  "measurementId": "G-GNRVY5H2B2",
  
};





// const app = initializeApp(firebaseConfig);
// const auth = getAuth(app);
// auth.languageCode = 'en';
// const provider = new GoogleAuthProvider();


// provider.setCustomParameters({
//     prompt: 'consent'  // This ensures the user is prompted to select an account and give consent again
// });



// export async function decon(){

//     console.log('Google sign-in button clicked.');
//     signInWithRedirect(auth, provider);

//     console.log("redirect done");

    
//     await getRedirectResult(auth)
    // .then((result) => {
    //     console.log(0);
    //     if (result !== null) {
            
    //         console.log(1);
            
    //             try {
    //                 console.log(2);
    //                 const credential = GoogleAuthProvider.credentialFromResult(result);
    //                 const user = result.user;
    //                 console.log(user);
            
    //                 // Send data to backend
    //                 const response =  fetch('/login/', {
    //                     method: 'POST',
    //                     headers: {
    //                         'Content-Type': 'application/json',
    //                         'X-CSRFToken': '{{ csrf_token }}',  // Make sure to include CSRF token
    //                     },
    //                     body: JSON.stringify({ User: user }),
    //                 });
            
    //                 console.log(response);
            
    //                 const data =  response.json();
    //                 console.log('Success:', data);
            
    //                 // const textDangerElement = document.getElementById("text-danger");
    //                 // textDangerElement.innerHTML = data;
            
    //                 window.location.href = '../dashboard/';
    //             } catch (error) {
    //                 console.error('Error sending token to backend:', error);
            
    //                 const textDangerElement = document.getElementById("text-danger");
    //                 textDangerElement.innerHTML = error;
    //             }
           
            
    //         // Usage example:
    //         // handleLogin(result);
        

                
    //     }

    //     else{

    //         console.log("whtf");
            
    //     }
    // })
    // .catch((error) => {
    //     console.error('Error during sign-in:', error);
    //     const textDangerElement = document.getElementById("text-danger");
    //     textDangerElement.innerHTML = error;
    // });

// };
    // const googlelogin_btn = document.getElementById("googleSignIn");

    // googlelogin_btn.addEventListener("click", function () {
        


        
    // });

const app = initializeApp(firebaseConfig);
const auth = getAuth(app);
auth.languageCode = 'en';
const provider = new GoogleAuthProvider();
provider.setCustomParameters({
    prompt: 'consent'  // This ensures the user is prompted to select an account and give consent again
});
    

          
document.addEventListener("DOMContentLoaded", function () {
    const googlelogin_btn = document.getElementById("googleSignIn");

    googlelogin_btn.addEventListener("click", function () {
        console.log('Google sign-in button clicked.');
        signInWithRedirect(auth, provider);
    });

    // Listen for changes in the user's authentication state
    auth.onAuthStateChanged(function (user) {
        if (user) {
            // User is signed in
            // console.log('User:', user);

            // Send data to backend
            fetch('/login/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': '{{ csrf_token }}',  // Make sure to include CSRF token
                },
                body: JSON.stringify({ User: user }),
            })
            .then(response => {
                // console.log(response);
                return response.json();
            })
            .then(data => {
                // console.log('Success:', data);
                window.location.href = '../dashboard/';
            })
            .catch((error) => {
                console.error('Error sending token to backend:', error);
                const textDangerElement = document.getElementById("text-danger");
                textDangerElement.innerHTML = error;
            });
        } else {
            // User is signed out
            console.log('User is signed out');
        }
    });
});






// Eorking code for single timelogin





// const app = initializeApp(firebaseConfig);
// const auth = getAuth(app);
// auth.languageCode = 'en';
// const provider = new GoogleAuthProvider();
// provider.setCustomParameters({
//     prompt: 'consent'  // This ensures the user is prompted to select an account and give consent again
// });

// document.addEventListener("DOMContentLoaded", async function () {
//     const googlelogin_btn = document.getElementById("googleSignIn");

//     googlelogin_btn.addEventListener("click", function () {
//         console.log('Google sign-in button clicked.');
//         signInWithRedirect(auth, provider);
//     });

    
//     await getRedirectResult(auth)
//         .then((result) => {
//             if (result !== null) {
                
//                 const credential = GoogleAuthProvider.credentialFromResult(result);
//                 const user =  result.user;
//                 console.log(user);

//                 // Send data to backend
//                 fetch('/login/', {
//                     method: 'POST',
//                     headers: {
//                         'Content-Type': 'application/json',
//                         'X-CSRFToken': '{{ csrf_token }}',  // Make sure to include CSRF token
//                     },
//                     body: JSON.stringify({ User: user }),
//                 })
//                 .then(response => {

//                     console.log(response);
//                     response.json()})

//                 .then(data => {
//                     console.log('Success:', data);

//                     // const textDangerElement = document.getElementById("text-danger");
//                     // textDangerElement.innerHTML = data;

//                     window.location.href = '../dashboard/';
//                 })
//                 .catch((error) => {
//                     console.error('Error sending token to backend:', error);

//                     const textDangerElement = document.getElementById("text-danger");
//                     textDangerElement.innerHTML = error;

//                 });
//             }
//         })
//         .catch((error) => {
//             console.error('Error during sign-in:', error);
//             const textDangerElement = document.getElementById("text-danger");
//             textDangerElement.innerHTML = error;
//         });
// });





// export { googlebutton };