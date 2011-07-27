#!/usr/local/bin/python2.7

from pylsf import lsf

print '\n Hosts in cluster: ', lsf.get_host_names(), '\n'

print '{0:15s} {1:10s} {2:10s} {3:5s} {4:4s}'.format('Hostname', 'Type',
                                                     'Model', 'Cores', 'Load')


for info in lsf.get_host_info():

    c = lsf.new_intp()
    hostLoad = lsf.ls_loadofhosts('hname=' + info.hostName, c, 0, None, None,
                                  0)
    if hostLoad is not None:
        load = lsf.floatp_value(hostLoad.li)
        if load >= 65535:
            load = -1
    else:
        load = -1

    print '{0:15s} {1:10s} {2:10s} {3:5d} {4:4.2f}'.format(info.hostName,
                                                           info.hostType,
                                                           info.hostModel,
                                                           info.cores,
                                                           load)

    if info.nRes > 0:
        print '+--> Resources:', info.resources
