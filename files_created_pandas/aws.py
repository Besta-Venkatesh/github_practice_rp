import boto3,os
import pandas as pd 
s3_client= boto3.client('s3')
s3= boto3.resource('s3')

objectdf= s3_client.get_object(Bucket='myfirstbucketinpython',Key='indian_patient_data_clinic1.csv') 
RentalsreadDf=pd.read_csv(objectdf['Body'])
print(RentalsreadDf)


