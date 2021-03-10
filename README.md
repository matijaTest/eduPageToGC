# eduPageToGC

### This is a simple python script for mapping all of your future homeworks to your google calendar using https://github.com/ivanhrabcak/edupage-api

### Setup

- Clone this repo
- Go to https://developers.google.com/calendar/overview and create your credentials.json file
- Add that file to your project directory
- In the console you can now run `py mapToGC.py`
- If you get any errors in mapToGC.py change `SCOPES = ['https://www.googleapis.com/auth/calendar']` to `SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']` then run command above and after change this line back to original
- If problems persist delete credentials.json file and all should work.
