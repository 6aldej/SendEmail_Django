<h2>Sent email app</h2>
This app performs the functions of sending email. Fill out the form and select the time when the email should be sent. <br>
The application is written using the Django 2.0.5 framework. <br>
<b>********************************************************</b><br>
Sending letters is realized with the help of Gmail. <br>
If you use Gmail, you must also allow access on the page: https://myaccount.google.com/lesssecureapps <br>
You also need to click on the link: https://accounts.google.com/DisplayUnlockCaptcha <br>
<b>********************************************************</b><br>
<h3>Note:</h3><br>
<li>this code is configured for deploy on Heroku.</li> <br>
<li>'mysite/settings.py/: in <b>'EMAIL_HOST_USER'</b> enter your Gmail; in <b>'ALLOWED_HOSTS'</b> enter your Heroku domain.</li> <br> <li>'sendmes/views.py/': in 't', enter your Gmail in the <b>'send_mail'</b> function arguments.</li> <br>
