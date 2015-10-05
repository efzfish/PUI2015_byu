import csv
import json
import sys
import urllib2

if __name__=='__main__':
    url = 'http://api.prod.obanyc.com/api/siri/vehicle-monitoring.json?key=%s&VehicleMonitoringDetailLevel=calls&LineRef=%s' % (sys.argv[1],sys.argv[2])
    request = urllib2.urlopen(url)
    metadata = json.loads(request.read())
    bus = metadata['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']

    with open(sys.argv[3], 'wb') as csvFile:
        writer = csv.writer(csvFile)
        headers = ['Latitude', 'Longitude','Stop Name','Stop Status']
        writer.writerow(headers)
        
        for i in bus:
            latitude = i['MonitoredVehicleJourney']['VehicleLocation']['Latitude']
            longitude = i['MonitoredVehicleJourney']['VehicleLocation']['Longitude']
            stopname = i['MonitoredVehicleJourney']['MonitoredCall']['StopPointName']
            stopstatus = i['MonitoredVehicleJourney']['MonitoredCall']['Extensions']['Distances']['PresentableDistance']
        
            writer.writerow([latitude, longitude, stopname, stopstatus])