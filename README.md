# sentimentscore - Sentiment Analysis with GNL API

Instructions on how to use the script that extracts keywords and key phrases from a website using the Google Cloud Natural Language API:

First, you will need to have a Google Cloud account and create a project.

1. Go to the Google Cloud Console and enable the Natural Language API for your project.

2.  Create credentials for your project, such as an API key or a service account. You will need these credentials to authenticate with the API.

5. Install the Google Cloud SDK on your computer, which will allow you to interact with the API using the command line.

4.  Once you have the SDK set up, you can use the following command to set the credentials for your project:

```gcloud auth application-default login```

6. Install the google-cloud-language python library by running this command in your terminal:

```pip install google-cloud-language```

7. Replace https://www.example.com/posts with the url of the website you want to extract keywords and key phrases from.

8. Run the script by executing the command python your_file_name.py

9. The script will return a list of keywords sorted by their salience scores and a list of key phrases sorted by their confidence scores.


## Notes
Please note that you will need to have a valid internet connection to access the Google Cloud Natural Language API. Also, you should check the usage limits and pricing for the API to avoid any unexpected charges.
