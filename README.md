<h2>sent email</h2>
This app performs the functions of sending email. Fill out the form and select the time when the email should be sent. <br>
The application is written using the Django 2.0.5 framework. <br>
<b>********************************************************</b><br>
Sending letters is realized with the help of Gmail. <br>
If you use Gmail, you must also allow access on the page: https://myaccount.google.com/lesssecureapps <br>
You also need to click on the link: https://accounts.google.com/DisplayUnlockCaptcha <br>
<b>********************************************************</b><br>
Note:<br>
<li>this code is configured for deploy on Heroku.</li> <br>
<li>'mysite/settings.py/: in 'EMAIL_HOST_USER' enter your Gmail; in 'ALLOWED_HOSTS' enter your Heroku domain.</li> <br> <li>'sendmes/views.py/': in 't', enter your Gmail in the 'send_mail' function arguments.</li> <br>
