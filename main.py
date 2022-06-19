#imports needed
import requests
import pandas as pd
import datetime as dt
from token_file import Token
from load_file import Load
from validate_file import validation
from send_mail import Mail

#main function
if __name__ == "__main__":
    print()

    #important attributes
    TOKEN_OBJECT = Token()
    TOKEN = TOKEN_OBJECT.get_token()
    HEADERS = {
        "Accept":"application/json",
        "Content-Type":"application/json",
        "Authorization":"Bearer {token}".format(token=TOKEN)
    }
    TODAY = dt.datetime.now()
    YESTERDAY = TODAY - dt.timedelta(days=1)
    YESTERDAY_TIME_STAMP = int(YESTERDAY.timestamp())*1000
    LOADER = Load()
    Validation = validation()
    mail = Mail()
    message="\n"

    #extracting data
    message += "Data extraction is done!\n"
    REQUEST = requests.get("https://api.spotify.com/v1/me/player/recently-played?after={time}".format(time=YESTERDAY_TIME_STAMP),headers=HEADERS)
    RESULT = REQUEST.json()
    SONG_NAME=[]
    ARTIST_NAME=[]
    PLAYED_AT=[]
    TIME_STAMP=[]

    # transforming data
    for song in RESULT["items"]:
        SONG_NAME.append(song["track"]["name"])
        ARTIST_NAME.append(song["track"]["album"]["artists"][0]["name"])
        PLAYED_AT.append(song["played_at"])
        TIME_STAMP.append(song["played_at"][0:10])

    SONG_DICT={
            "SONG NAME":SONG_NAME,
            "ARTIST NAME":ARTIST_NAME,
            "PLAYED AT":PLAYED_AT,
            "TIME STAMP":TIME_STAMP
        }
    SONG_DF = pd.DataFrame(SONG_DICT)
    print(SONG_DF)
    
    # validating and loading data
    if Validation.validate(SONG_DF)==True:
        message += "Data validation is done!\n"
        try:
            LOADER.load_data(SONG_DF)
            message += "Data successfully loaded into the database!\n"
        except:
            message += "Data already exists in the database!\n"
    else:
        if SONG_DF.empty:
            message += "No songs listened to!\n"
        else:
            message += "Data is invalid!\n"
    print(message)
    
    # confirmation mail
    mail.sendMail(message)
            
            
            
            
            
            
    
