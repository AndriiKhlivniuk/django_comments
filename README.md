# django_comments

<h1>Start the project</h1>
<ol>
  <li>Navigate to the folder django_comments</li>
  <li>Run command "pip install -r requirements.txt" to install all requirements for the project</li>
  <li>To start the appliaction run "python manage.py runserver"</li>
</ol> 
<br>
<h1>Application usage</h1>
<ol>
  <li>Navigate to http://127.0.0.1:8000/comments_app/ in your browser, this will be the main page of the app</li>
  <li>To add the comment click "Add comment lin on top of the page", fill the form and solve the capcha and click submit button</li>
  <li>Click the "All comments" link on the top of the page and this will bring you to the main page with all the comments created</li>
  <li>To leave comment for the main comment fill the form under the query that you want to comment and click submit </li>
</ol> 
<br>

<h1>Run app in Docker</h1>
<ol>
  <li>Navigate to the folder django_comments</li>
  <li>Run command "docker build -t comments_app . " this will build "comments_app" image</li>
  <li>To start the appliaction in docker run "docker run -p 8000:8000 comments_app"</li>
  <li>Navigate to http://127.0.0.1:8000/comments_app/ in your browser</li>
</ol> 