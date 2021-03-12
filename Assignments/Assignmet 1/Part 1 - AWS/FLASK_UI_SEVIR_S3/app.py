from flask import Flask, render_template, request, redirect, url_for, flash, \
    Response, session
from flask_bootstrap import Bootstrap
from filters import datetimeformat, file_type
from resources import get_bucket, get_buckets_list
import csv
import random
from time import time
from decimal import Decimal
import boto3
import string
import random
import os


app = Flask(__name__)
Bootstrap(app)
app.secret_key = 'secret'
app.jinja_env.filters['datetimeformat'] = datetimeformat
app.jinja_env.filters['file_type'] = file_type


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        bucket = request.form['bucket']
        session['bucket'] = bucket
        return redirect(url_for('files'))
    else:
        buckets = get_buckets_list()
        return render_template("index.html", buckets=buckets)


@app.route('/files')
def files():
    my_bucket = get_bucket()
    summaries = my_bucket.objects.all()

    return render_template('files.html', my_bucket=my_bucket, files=summaries)


@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']

    my_bucket = get_bucket()
    my_bucket.Object(file.filename).put(Body=file)

    flash('File uploaded successfully')
    return redirect(url_for('files'))


@app.route('/delete', methods=['POST'])
def delete():
    key = request.form['key']

    my_bucket = get_bucket()
    my_bucket.Object(key).delete()

    flash('File deleted successfully')
    return redirect(url_for('files'))


@app.route('/download', methods=['POST'])
def download():
    key = request.form['key']

    my_bucket = get_bucket()
    file_obj = my_bucket.Object(key).get()

    return Response(
        file_obj['Body'].read(),
        mimetype='text/plain',
        headers={"Content-Disposition": "attachment;filename={}".format(key)}
    )


@app.route('/copyfromsevir', methods=['POST'])
def copyfromsevir():
    # Connect to Boto3
    s3 = boto3.resource(
        service_name='s3',
        region_name='us-east-2')

    # Copying from S3 Public SEVIR to our bucket for analysis 

    #Import Catalog from SEVIR 
    s3 = boto3.resource('s3',region_name='us-east-2')
    copy_source = {
        'Bucket': 'sevir',
        'Key': 'CATALOG.csv'
    }
    s3.meta.client.copy(copy_source, 'kronosteam4', 'CATALOG.csv')
    print('Sucessfully Catalog has been copied to our S3 Bucket ') 

    #import SEVIR H5 FILES : 1TB all files 

    #vil2019--1
    s3 = boto3.resource('s3',region_name='us-east-2')
    copy_source = {
        'Bucket': 'sevir',
        'Key': 'data/vil/2019/SEVIR_VIL_RANDOMEVENTS_2019_0101_0430.h5'
    }
    s3.meta.client.copy(copy_source, 'kronosteam4', 'data/vil/2019/SEVIR_VIL_RANDOMEVENTS_2019_0101_0430.h5')
    print('Sucessfully vil sensor HDF5 data has been copied to our S3 Bucket ') 

    #IR069--2 
    s3 = boto3.resource('s3',region_name='us-east-2')
    copy_source = {
        'Bucket': 'sevir',
        'Key': 'data/ir069/2019/SEVIR_IR069_STORMEVENTS_2019_0701_1231.h5'
    }
    s3.meta.client.copy(copy_source, 'kronosteam4', 'data/ir069/2019/SEVIR_IR069_STORMEVENTS_2019_0701_1231.h5')
    print('Sucessfully IR069 sensor data HDF5 files has been copied to our S3 Bucket ') 

    #IR069--3
    s3 = boto3.resource('s3',region_name='us-east-2')
    copy_source = {
        'Bucket': 'sevir',
        'Key': 'data/ir069/2019/SEVIR_IR069_STORMEVENTS_2019_0701_1231.h5'
    }
    s3.meta.client.copy(copy_source, 'kronosteam4', 'data/ir069/2019/SEVIR_IR069_STORMEVENTS_2019_0701_1231.h5')
    print('Sucessfully IR069 sensor data HDF5 files has been copied to our S3 Bucket ') 

    #IR107--4
    s3 = boto3.resource('s3',region_name='us-east-2')
    copy_source = {
        'Bucket': 'sevir',
        'Key': 'data/ir107/2019/SEVIR_IR107_STORMEVENTS_2019_0701_1231.h5'
    }
    s3.meta.client.copy(copy_source, 'kronosteam4', 'data/ir107/2019/SEVIR_IR107_STORMEVENTS_2019_0701_1231.h5')
    print('Sucessfully IR107 sensor data HDF5 files has been copied to our S3 Bucket ') 

    #lght--5
    s3 = boto3.resource('s3',region_name='us-east-2')
    copy_source = {
        'Bucket': 'sevir',
        'Key': 'data/lght/2019/SEVIR_LGHT_ALLEVENTS_2019_1101_1201.h5'
    }
    s3.meta.client.copy(copy_source, 'kronosteam4', 'data/lght/2019/SEVIR_LGHT_ALLEVENTS_2019_1101_1201.h5')
    print('Sucessfully lght sensor data HDF5 files has been copied to our S3 Bucket ') 

    #vis--5
    s3 = boto3.resource('s3',region_name='us-east-2')
    copy_source = {
        'Bucket': 'sevir',
        'Key': 'data/vis/2019/SEVIR_VIS_STORMEVENTS_2019_0101_0131.h5'
    }
    s3.meta.client.copy(copy_source, 'kronosteam4', 'data/vis/2019/SEVIR_VIS_STORMEVENTS_2019_0101_0131.h5')
    print('Sucessfully vis sensor data HDF5 files has been copied to our S3 Bucket ') 

    #Nowcastingfiles--6
    s3 = boto3.resource('s3',region_name='us-east-2')
    copy_source = {
        'Bucket': 'sevir',
        'Key': 'data/vis/2019/SEVIR_VIS_STORMEVENTS_2019_0101_0131.h5'
    }
    s3.meta.client.copy(copy_source, 'kronosteam4', 'data/vis/2019/SEVIR_VIS_STORMEVENTS_2019_0101_0131.h5')
    print('Sucessfully vis sensor data HDF5 files has been copied to our S3 Bucket ') 


if __name__ == "__main__":
    app.run()
