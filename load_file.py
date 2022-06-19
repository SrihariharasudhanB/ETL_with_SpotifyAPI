# imports needed
import mysql.connector
import pandas as pd

QUERY1 = """
    CREATE TABLE IF NOT EXISTS etl_project1 (
        song_name VARCHAR(200),
        artist_name VARCHAR(200),
        played_at VARCHAR(200),
        time_stamp VARCHAR(200),
        PRIMARY KEY (played_at)
    );
"""

QUERY2="""
INSERT INTO etl_project1 VALUES(
    '{s_name}',
    '{a_name}',
    '{p_at}',
    '{t_stamp}'
);
"""

HOST="< YOUR HOST NAME >"
DB="< YOUR DB NAME >"
USER="< YOUR USER NAME >"
PASSWORD="< YOUR PASSWORD >" 

class Load:
    
    CONNECTOR = mysql.connector.connect(host=HOST,username=USER,password=PASSWORD,database=DB)
    CURSOR = CONNECTOR.cursor()
    
    def __init__(self) -> None:
        pass

    def load_data(self,DATA: pd.DataFrame):
        
        self.CURSOR.execute(QUERY1)
        
        self.DATA=DATA
        size=self.DATA.__len__()

        for i in range(0,size):
            self.CURSOR.execute(QUERY2.format(
                s_name = str(self.DATA["SONG NAME"][i]).replace("'","''"),
                a_name = str(self.DATA["ARTIST NAME"][i]).replace("'","''"),
                p_at = str(self.DATA["PLAYED AT"][i]).replace("'","''"),
                t_stamp = str(self.DATA["TIME STAMP"][i]).replace("'","''")
            ))
        self.CONNECTOR.commit()

        self.CURSOR.close()
        self.CONNECTOR.close()
