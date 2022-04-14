from flask import Flask, jsonify
import pandas as pd

movies_data = pd.read_csv('final.csv')

app = Flask(__name__)

# extracting important information from dataframe


# variables to store data


# method to fetch data from database


# /movies api


# /like api


# /dislike api


# /did_not_watch api


if __name__ == "__main__":
  app.run()