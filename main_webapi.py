from distutils.log import debug
from os import environ
from webapi import app

if __name__=="__main__":
    app.run(host="0.0.0.0",debug="True", port=8092)