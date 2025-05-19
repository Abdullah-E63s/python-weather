import pyrebase

firebaseConfig = {
  "apiKey": "AIzaSyAYBqDpBgFKJ_ZsIS7kXvJ1VVqQ85XdCSQ",
  "authDomain": "fir-course-e0d82.firebaseapp.com",
  "databaseURL": "https://fir-course-e0d82-default-rtdb.firebaseio.com",
  "projectId": "fir-course-e0d82",
  "storageBucket": "fir-course-e0d82.firebasestorage.app",
  "messagingSenderId": "107730130727",
  "appId": "1:107730130727:web:c3d9feec680387d957fb02"
}

firebase = pyrebase.initialize_app(firebaseConfig)

db = firebase.database()
auth = firebase.auth()
storage = firebase.storage()

# authentication
# logic
try:
    email = input("Enter your email: ")
    password = input("Enter your password: ")

    user = auth.sign_in_with_email_and_password(email, password)
    print("Successfully signed in!")
except:
    print("Invalid email or password please try again!")

# signup
email = input("enter your email:")
password  = input("enter your password: ")
confirm = input("please confirm your password:")

if password  == confirm:
    try:
     auth.create_user_with_email_and_password(email, password)
     print("signup successfull")
    except:
       print("signup failed, Email already exists")
else:
   print("password does not match")



