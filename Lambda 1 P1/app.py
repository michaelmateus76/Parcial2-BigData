import requests
import boto3
import time

bucket="punto1parcial"

def handler(event,context):

	localtime=time.localtime()
	
	s3 = boto3.resource('s3')
	getHTMLNewspaper("Avianca","https://query1.finance.yahoo.com/v7/finance/download/AVHOQ?period1=1634601600&period2=1634688000&interval=1d&events=history&includeAdjustedClose=true",localtime,bucket,s3)
	getHTMLNewspaper("Ecopetrol","https://query1.finance.yahoo.com/v7/finance/download/EC?period1=1634774400&period2=1634860800&interval=1d&events=history&includeAdjustedClose=true",localtime,bucket,s3)
	getHTMLNewspaper("GrupoAval","https://query1.finance.yahoo.com/v7/finance/download/AVAL?period1=1634774400&period2=1634860800&interval=1d&events=history&includeAdjustedClose=true",localtime,bucket,s3)
	getHTMLNewspaper("CementosArgos","https://query1.finance.yahoo.com/v7/finance/download/CMTOY?period1=1634774400&period2=1634860800&interval=1d&events=history&includeAdjustedClose=true",localtime,bucket,s3)

	
	return {
			"status_code":200
		}

def getHTMLNewspaper(name, url,localtime,bucketname,s3):	
	headers = {'User-Agent': 'Mozilla'}
	r = requests.get(url, headers=headers)
	filepath="/tmp/"+name+".csv"
	f = open(filepath,"w")
	f.write(r.text)
	f.close()
	data={
		'file':filepath,
		'bucket':bucketname,
		'path':'stocks/company='+name+'/year='+str(localtime.tm_year)+'/month='+str(localtime.tm_mon)+'/day='+str(localtime.tm_mday)+'/'+str(localtime.tm_hour)+str(localtime.tm_min)+str(localtime.tm_sec)+'page.csv'
	}
	s3.meta.client.upload_file(data['file'],data['bucket'] , data['path'])