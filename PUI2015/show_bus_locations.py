import json
import sys
import urllib2

if __name__=='__main__':
    url = 'http://api.prod.obanyc.com/api/siri/vehicle-monitoring.json?key=%s&VehicleMonitoringDetailLevel=calls&LineRef=%s' % (sys.argv[1],sys.argv[2])
    request = urllib2.urlopen(url)
    metadata = json.loads(request.read())
    busnum = len(metadata['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'])
    print 'Bus Line : %s' % (sys.argv[1])
    print 'Number of Active Buses : %s' % (busnum)
    for i in range(busnum):
        print 'Bus %s is at latitude %s and longitude %s' % (i,metadata['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][i]['MonitoredVehicleJourney']['VehicleLocation']['Latitude'],metadata['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][i]['MonitoredVehicleJourney']['VehicleLocation']['Longitude'])


