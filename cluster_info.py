
from pylsf import lsf

print '\n Hosts in cluster: ', lsf.get_host_names(), '\n'

print '{0:20s} {1:20s} {2:29s} {3:2s}'.format('Hostname', 'Type', 'Model', 'Cores')
   
for info in lsf.get_host_info():
     print '{0:20s} {1:20s} {2:29s} {3:2d}'.format(info.hostName, info.hostType,  info.hostModel, info.cores)
    
     #print info.hostName, info.hostType, info.hostModel, info.cores

