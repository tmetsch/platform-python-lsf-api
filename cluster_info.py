from pylsf import lsf

print '\n Hosts in cluster: ', lsf.get_host_names(), '\n'

print '{0:10s} {1:10s} {2:10s} {3:5s}'.format('Hostname', 'Type', 'Model', 'Cores')
   
for info in lsf.get_host_info():
    print '{0:10s} {1:10s} {2:10s} {3:5d}'.format(info.hostName, info.hostType,  info.hostModel, info.cores)
    print '+--> Resources:', info.resources

print '\n\n'

for load in lsf.get_host_load():
    print lsf.intp_value(load.status)  
    print load.hostName, load.li, load.status
