#! C:\Users\lpres\anaconda3\python.exe

import os
import datetime
import pandas as pd
import csv

csvFile = "C:/Users/lpres/dbno/data/WF7333raw.csv"
csvFout = "C:/Users/lpres/dbno/data/WF7333.csv"
df = pd.DataFrame()


def init():
    print("===== dbnPgm1 =====")
    # Display Script file
    scriptDirName = os.path.dirname(__file__)
    scriptBaseName = os.path.basename(__file__)
    print("Script  :", scriptDirName+"/" + scriptBaseName)

    # Display Current date and time
    now = datetime.datetime.now()
    print("RunTime :", now.strftime("%Y-%m-%d %H:%M:%S"), '\n')


def CleanseWf7333():
    print("csvFile: ", csvFile)
    df = pd.read_csv(csvFile, header=None)
    df.columns = ["Date", "Amount", "X", "Y", "Details"]
    df = df.drop(["X", "Y"], axis=1)
    # df['Date'] = pd.to_datetime(df['Date'], format='%m/%d/%Y')
    df = df.sort_values(by=['Date'])
    df["Source"] = "WF7333"
    #df["Amount"] = df["Amount"].abs()
    df["AcctCode"] = ""
    print(df)
    header = ["Source", "AcctCode", "Date", "Amount", "Details"]
    df.to_csv(csvFout, columns=header, index=False)


init()
CleanseWf7333()
