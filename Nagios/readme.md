## Nagios Login 

http://13.233.39.202/nagios/

	Username : nagiosadmin

	pass: anand





###Reference Files

https://www.itzgeek.com/how-tos/linux/centos-how-tos/monitor-remote-linux-system-with-nagios-3.html

https://www.itzgeek.com/how-tos/linux/centos-how-tos/monitor-remote-linux-system-with-nagios-3.html



-----------------------------------------------
define host{

use                            linux-server

host_name                      ec2-18-224-184-35.us-east-2.compute.amazonaws.com

alias                          Nagios-Slave

address                        18.224.184.35

max_check_attempts             5

check_period                   24x7

notification_period            24x7    

notification_interval          30        

}

define service{
    use            generic-service    ; Inherit values from a template
    host_name      ec2-18-224-184-35.us-east-2.compute.amazonaws.com  
    service_description    SSH   
    check_command        check_ssh
	notifications_enabled 0
    }
	
define service{
        use                             local-service         ; Name of service template to use
        host_name                       ec2-18-224-184-35.us-east-2.compute.amazonaws.com
        service_description             Current Users
        check_command                   check_local_users!20!50
        }
		
define service{
        use                             local-service         ; Name of service template to use
        host_name                       ec2-18-224-184-35.us-east-2.compute.amazonaws.com
        service_description             Total Processes
        check_command                   check_local_procs!250!400!RSZDT
        }
		
		
define service{
    use            generic-service    ; Inherit values from a template
    host_name      ec2-18-224-184-35.us-east-2.compute.amazonaws.com  
    service_description    Uptime   
    check_command        check_snmp!-C public -o sysUpTime.0
    }
	
  
-------------------------------------------------------------------------------

define host{

use                            linux-server

host_name                      ip-172-31-46-100.us-east-2.compute.internal

alias                          Nagios-Slave

address                        172.31.46.100

max_check_attempts             5

check_period                   24x7

notification_period            24x7

notification_interval          30

}

define service{
    use            generic-service    ; Inherit values from a template
    host_name      ip-172-31-46-100.us-east-2.compute.internal
    service_description    SSH
    check_command        check_ssh
        notifications_enabled 0
    }

define service{
        use                             local-service         ; Name of service template to use
        host_name                       ip-172-31-46-100.us-east-2.compute.internal
        service_description             Current Users
        check_command                   check_local_users!20!50
    }

define service{
        use                             local-service         ; Name of service template to use
        host_name                       ip-172-31-46-100.us-east-2.compute.internal
        service_description             Total Processes
        check_command                   check_local_procs!250!400!RSZDT
    }


-----------------------------------------------------------------------


###############################################################################
# LOCALHOST.CFG - SAMPLE OBJECT CONFIG FILE FOR MONITORING THIS MACHINE
#
#
# NOTE: This config file is intended to serve as an *extremely* simple
#       example of how you can create configuration entries to monitor
#       the local (Linux) machine.
#
###############################################################################




###############################################################################
###############################################################################
#
# HOST DEFINITION
#
###############################################################################
###############################################################################

# Define a host for the local machine

define host{
        use                     linux-server            ; Name of host template to use
                                                        ; This host definition will inherit all variables that are defined
                                                        ; in (or inherited by) the linux-server host template definition.
        host_name               localhost
        alias                   localhost
        address                 127.0.0.1
        }


define host{
        use                     linux-server            ; Name of host template to use
                                                        ; This host definition will inherit all variables that are defined
                                                        ; in (or inherited by) the linux-server host template definition.
        host_name               ip-172-31-36-221.ec2.internal
        alias                   Nagios-Main
        address                 172.31.36.221
}

define host{
        use                     linux-server            ; Name of host template to use
                                                        ; This host definition will inherit all variables that are defined
                                                        ; in (or inherited by) the linux-server host template definition.
        host_name               ip-172-31-43-139.ec2.internal
        alias                   Nagios-Slave
        address                 172.31.43.139
}

###############################################################################
###############################################################################
#
# HOST GROUP DEFINITION
#
###############################################################################
###############################################################################

# Define an optional hostgroup for Linux machines

define hostgroup{
        hostgroup_name  linux-servers ; The name of the hostgroup
        alias           Linux Servers ; Long name of the group
        members         localhost     ; Comma separated list of hosts that belong to this group
        }



###############################################################################
###############################################################################
#
# SERVICE DEFINITIONS
#
###############################################################################
###############################################################################


# Define a service to "ping" the local machine

define service{
        use                             local-service         ; Name of service template to use
        host_name                       localhost
        service_description             PING
        check_command                   check_ping!100.0,20%!500.0,60%
        }


# Define a service to check the disk space of the root partition
# on the local machine.  Warning if < 20% free, critical if
# < 10% free space on partition.

define service{
        use                             local-service         ; Name of service template to use
        host_name                       localhost
        service_description             Root Partition
        check_command                   check_local_disk!20%!10%!/
        }


define service{
        use                             local-service         ; Name of service template to use
        host_name                       ip-172-31-36-221.ec2.internal
        service_description             PING
        check_command                   check_ping!1.0,20%!100.0,60%

}
define service{
        use                             local-service         ; Name of service template to use
        host_name                       ip-172-31-36-221.ec2.internal
        service_description             Total Processes
        check_command                   check_local_procs!100!200!RSZDT

}

# Nagios Slave

define service{
        use                             local-service         ; Name of service template to use
        host_name                       ip-172-31-43-139.ec2.internal
        service_description             PING
        check_command                   check_ping!100.0,20%!500.0,60%

}
define service{
        use                             local-service         ; Name of service template to use
        host_name                       ip-172-31-43-139.ec2.internal
        service_description             Total Processes
        check_command                   check_local_procs!100!200!RSZDT

}

# Define a service to check the number of currently logged in
# users on the local machine.  Warning if > 20 users, critical
# if > 50 users.

define service{
        use                             local-service         ; Name of service template to use
        host_name                       localhost
        service_description             Current Users
        check_command                   check_local_users!20!50
        }


# Define a service to check the number of currently running procs
# on the local machine.  Warning if > 250 processes, critical if
# > 400 users.

define service{
        use                             local-service         ; Name of service template to use
        host_name                       localhost
        service_description             Total Processes
        check_command                   check_local_procs!250!400!RSZDT
        }



# Define a service to check the load on the local machine.

define service{
        use                             local-service         ; Name of service template to use
        host_name                       localhost
        service_description             Current Load
        check_command                   check_local_load!5.0,4.0,3.0!10.0,6.0,4.0
        }



# Define a service to check the swap usage the local machine.
# Critical if less than 10% of swap is free, warning if less than 20% is free

define service{
        use                             local-service         ; Name of service template to use
        host_name                       localhost
        service_description             Swap Usage
        check_command                   check_local_swap!20!10
        }



# Define a service to check SSH on the local machine.
# Disable notifications for this service by default, as not all users may have SSH enabled.

define service{
        use                             local-service         ; Name of service template to use
        host_name                       localhost
        service_description             SSH
        check_command                   check_ssh
        notifications_enabled           0
        }



# Define a service to check HTTP on the local machine.
# Disable notifications for this service by default, as not all users may have HTTP enabled.

define service{
        use                             local-service         ; Name of service template to use
        host_name                       localhost
        service_description             HTTP
        check_command                   check_http
        notifications_enabled           0
        }

