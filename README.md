TweetPyGit
==========
*Update your Twitter account with the last Git commit. Written in Python as a Django command.*

Requirements: 
----
* [Tweepy](https://github.com/tweepy/tweepy)
* [GitPython](https://github.com/gitpython-developers/GitPython)

How to use
----
Copy file to django_app/management/commands path

In the script file change **CONSUMER_KEY** and **CONSUMER_SECRET**:

     CONSUMER_KEY = "#######################################" # Your CONSUMER_KEY
     CONSUMER_SECRET = "####################################" # Your CONSUMER_SECRET
     
Also don't forget to change the path of your Git repository:

    # Git repository path
    git_path = '/path/to/your/repository/'
     
     
Run as a Django command:

    python manage.py tweet_new_commit

**Not Django user ?** It's easy to clear the file to get working example. Only delete Django 'extra lines' you don't understand. Try it:)

Contacts:
----
* Twitter - [@UnforbiddenYet](https://twitter.com/UnforbiddenYet)

Thanks:
----
You can thank me using my site :  [Dilis.me](http://dilis.me). It's simple and powerful to-do manager.
    
      

	
