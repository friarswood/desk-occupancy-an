# project
import os
from occupancy.director import Director
from dotenv import load_dotenv
load_dotenv()

# Fill in from the Service Account and Project:
USERNAME   = os.getenv("DT_SVC_KEY")
PASSWORD   = os.getenv("DT_SVC_SECRET")
PROJECT_ID = os.getenv("DT_PROJECT")

# url base and endpoint
API_URL_BASE  = "https://api.disruptive-technologies.com/v2"


if __name__ == '__main__':

    # initialise Director instance
    d = Director(USERNAME, PASSWORD, PROJECT_ID, API_URL_BASE)

    # iterate historic events
    d.run_history()

    # stream realtime events
    d.run_stream(n_reconnects=5)

