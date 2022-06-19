import pandas as pd
import datetime as dt

class validation:

    def __init__(self) -> None:
        pass
     
    # method used to validate data
    def validate(self,data: pd.DataFrame) -> bool:
        
        self.dataframe=data

        if self.dataframe.empty:
            return False

        if pd.Series(self.dataframe["PLAYED AT"]).is_unique:
            pass
        else:
            return False

        if self.dataframe.isnull().values.any():
            return False
     
        today = dt.datetime.now()
        yesterday = today - dt.timedelta(days=1)
        timestamps = self.dataframe["TIME STAMP"].tolist()

        for timestamp in timestamps:
            if str(yesterday)[0:10]!=timestamp:
                return False
            
        return True
        
