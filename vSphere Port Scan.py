import socket, struct, platform

#region Global Variables

blocked_ports = []
open_ports = []

#Set the default timeout value to two seconds
socket.setdefaulttimeout(2)

#endregion

def port_check(ports, ip_address, vsphere_object):


    for element in ports:
        v_port = int(element)
        #connect to the ports
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((ip_address,v_port))
        if result == 0:
            open_ports.append(v_port)
        else:
           blocked_ports.append(v_port)

    print(vsphere_object + ' (' + ip_address + ')' + ' may experience issues due to the following being blocked:')
    print('')

    for i in blocked_ports:
        for key, value in ports.items():
         if str(i) == key:
            print '- '+ str(value) + '' + ' (Port ' + str(i) + ')'
    print('')

    #Reset the block ports list back to zero
    del blocked_ports[:]

def esxi__increase_ip():

    # x.x.x.x string -> integer
    ip2int = lambda ipstr: struct.unpack('!I', socket.inet_aton(ipstr))[0]
    # x.x.x.x string -> integer
    int2ip = lambda n: socket.inet_ntoa(struct.pack('!I', n))


    #Convert the first IP address to an integer
    esxi_initial_int = ip2int(esxi_input.initial_ip)

    #Second host IP Address Address
    esxi_increase_int = (esxi_initial_int + 1)
    esxi_increase_ip = int2ip(esxi_increase_int)
    esxi_input.ip.append(esxi_increase_ip)

def vcenter_input():

    while True:
        try:
            print''
            vcenter_input.ip = raw_input('Please enter the vCenter IP Address: ')
            print('')
            # Check for a valid IP Address
            socket.inet_aton(vcenter_input.ip)
        # if not a valid ip show the following error
        except socket.error:
            print ''
            print('*** Error: Please enter a valid IP Address ***')
            print ''
        else:
            break

def esxi_input():


    while True:
        print('')
        esxi_input.hosts = raw_input('Enter the number of ESXi hosts you would like to check: ')
        # Verify that the user enters a 1 digit organization code
        if len(esxi_input.hosts) > 1 or esxi_input.hosts.isdigit() == False:
            print('')
            print(' *** Error: Please enter a valid number ***')
            print('')
            continue
        #user successfully entered a organization code name
        else:
            break

    #region ESXi Port Scan
    if int(esxi_input.hosts) >= 1:

        while True:
            try:
                print''
                esxi_input.initial_ip = raw_input('Please enter the starting ESXi Host IP Address: ')
                # Check for a valid IP Address
                socket.inet_aton(esxi_input.initial_ip)
            # if not a valid ip show the following error
            except socket.error:
                print ''
                print('*** Error: Please enter a valid IP Address ***')
                print ''
            else:
                break

    #create the list that will house all of the ESXi IP Address
    esxi_input.ip = []

    #Add the first user defined ESXi Host IP Address to the list
    esxi_input.ip.append(esxi_input.initial_ip)

    #region Define the variables that allow us to increase an IP






    #endregion

def executing_script():
    print('')
    print('*** Executing script. This may take several minutes.... ***')
    print('')




print('')
print('The following vSphere objects are currently supported:')
print('')
print('- vCenter 5.x')
print('- ESXi 5.x')
print('')

while True:
    object_to_scan = raw_input('Which object would you like to scan (vCenter, ESXi, Both): ').lower()
    if object_to_scan not in ['vcenter', 'esxi', 'both']:
        print('')
        print('*** Error: Please enter "vCenter", "ESXi" , or "Both". ***')
        print('')
        continue
    else:
        break

if object_to_scan == 'vcenter':
    esxi_input.hosts = 0
    vcenter_input()
    executing_script()
elif object_to_scan == 'esxi':
    esxi_input()
    executing_script()
else:
    vcenter_input()
    esxi_input()
    executing_script()


#region vCenter

if object_to_scan in ['vcenter', 'both']:


    #region Ports required for vCenter 5.x
    vcenter_5 = {'25': 'Email notifications',
                 '53': 'DNS lookups',
                 '80': 'direct HTTP connections',
                 '80': 'DPM with IPMI (iLO/BMC) ASF Remote Management and Control Protocol',
                 '88': 'AD Authentication',
                 '135': 'Linked Mode',
                 '161': 'SNMP Polling',
                 '162': 'SNMP Trap Send',
                 '389': 'LDAP port number for the Directory Services for the vCenter Server group',
                 '443': 'Used to listen for connections from the vSphere Client',
                 '443': 'vCenter Agent. Host DPM with HP iLO Remote Management and Control Protocol',
                 '623': 'DPM and IPMI (iLO/BMC) ASF Remote Management and Control Protocol',
                 '902': 'Used to send data to managed hosts',
                 '902': 'Managed hosts send a regular heartbeat to the vCenter Server system',
                 '902': 'Host access to other hosts for migration and provisioning',
                 '1024': 'Bi-directional RPC communication on dynamic TCP ports',
                 '1433': 'vCenter Microsoft SQL Server Database',
                 '1521': 'vCenter Oracle Database',
                 '5988': 'CIM Transactions over HTTPs',
                 '7500': 'Linked Mode, Java Discovery Port',
                 '8005': 'Internal Communication Port',
                 '8006': 'Internal Communication Port',
                 '8009': 'AJP Port',
                 '8080': 'VMware Virtual Center Management Web Services',
                 '8083': 'Internal Service Diagnostics',
                 '8085': 'Internal Service Diagnostics/SDK',
                 '8086': 'Internal Communication Port',
                 '8087': 'Internal Service Diagnostics',
                 '8089': 'SDK Tunneling Port',
                 '8443': 'VMware Virtual Center Management Web Services',
                 '9443': 'vSphere Web Client Access',
                 '10109': 'Inventory Service Linked Mode Communication',
                 '10443': 'Inventory Service HTTPS',
                 '51915': 'Web service used to add host to AD domain'}


    #endregion

    #set the vsphere_object_ip_address to the vcenter IP for proper identification in the port check function


    port_check(vcenter_5, vcenter_input.ip, 'vCenter')

#endregion

#region ESXi

#region Ports required for ESXi 5.x
esxi_5 = {'22': 'SSH Server',
      '53': 'DNS Client',
      '68': 'DHCP Client',
      '80': 'Redirect Web Browser to HTTPS Server (443)',
      '88': 'PAM Active Directory Authentication - Kerberos',
      '111': 'NFS Client - RPC Portmapper',
      '123': 'NTP Client',
      '161': 'SNMP Polling',
      '162': 'SNMP Trap Send',
      '389': 'PAM Active Directory Authentication - Kerberos',
      '427': 'CIM Service Location Protocol (SLP)',
      '443': 'VI / vSphere Client to ESXi/ESX Host management connection',
      '443': 'Host to host VM migration provisioning',
      '445': 'PAM Active Directory Authentication',
      '464': 'PAM Active Directory Authentication - Kerberos',
      '514': 'Remote syslog logging',
      '902': 'Host access to other hosts for migration and provisioning',
      '902': 'vSphere Client access to virtual machine consoles(MKS)',
      '902': '(UDP) Status update (heartbeat) connection from ESXi to vCenter Server',
      '1024': 'Bi-directional communication on TCP/UDP porsts is required between the ESXi host and the AD Domain Controller',
      '2049': 'Transactions from NFS storage devices',
      '3260': 'Transactions to iSCSI storage devices',
      '5900': 'RFP protocol which is used by management tools such as VNC',
      '5988': 'CIM transactions over HTTP',
      '5989': 'CIM XML transactions over HTTPS',
      '8000': 'Requests from vMotion',
      '8100': 'Traffic between hosts for vSphere Fault Tolerance (FT)',
      '8182': 'Traffic between hosts for vSphere High Availability (HA)',
      '8200': 'DVS Port Information',
      '8301': 'DVS Portion Information',
      '8302': 'Internal Communication Port'}
#endregion

if esxi_input.hosts > 0:


    for x in range((int(esxi_input.hosts) - 1)):

        esxi__increase_ip()

    for index, vsphere_object_ip_address in enumerate(esxi_input.ip):

     port_check(esxi_5, vsphere_object_ip_address, 'ESXi')

#endregion



#determine if user is running Windows to keep terminal open

if platform.system() == 'Windows':

    raw_input('To exit hit enter:')































