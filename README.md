# Workbench-Django-Comments
Comment API using the Django REST Framework that allows users to submit comments associated with the below content URLs, or retrieve a list of comments associated with a content URL.

Content URLs
/low-altitude-launch
/planetary-motion
/pop-quiz


1) All requests should go through the Django REST Framework.
**Complete**

2) A Create (POST) end point should take the following fields and save them to the database: IP, Username, Comment, content URL.
**Complete**

3) A List (GET) end point would take a content URL and return a list of all previously submitted comments matching that content URL.
**Complete**

4) Any IP Address adding more than 2 comments (POST) in 1 minute should have that request rejected and be locked out for 5 minutes.

5) Any Comment that is an exact duplicate of an existing comment posted within the last 24 hours should be rejected and the originating IP Address should be locked out for 1 minute. (POST)

6) The API should use a rate limiter to prevent the user from making more than 20 requests (POST and GET) per minute.
**Complete**

7) Please use a sqlite database. 
**Complete**

8) You do not need to use authenticated users. The username field can be set manually.
**Complete**

9) IP Addresses can be manually submitted in a field with the POST and GET requests, since this is a dev environment and all IPs would be the same.
**Complete**

