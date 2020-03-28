## Puppet


### Puppet Types
  
      1. Master-Slave
      2. Stand Alone

### Puppet resource Types

      1. Built-In / Core  -> Puppet team will maintain and Develop.
      2. Defined          -> Edit the default resource and do customization on that.
      3. Custom           -> Write from scratch with Ruby language.

### Commands

  - Check the puppet code
  
    `puppet parser validate`
  
  - Test the puppet code
  
    `puppet apply --noop`
  
  - Run the puppet code
  
    `puppet apply`
    
    
 ## Puppet Resource
 
 ### Create a User ( create_user.pp )
 
       user { "anand":
        ensure => "present",
        uid    => "1011",
        shell  => "/bin/sh",
       }
       
### Create a File inside a new folder

        file { "/root/anand":
          ensure => "directory",
          }

        file { "/root/anand/test.txt":
          ensure   => "present",
          owner    => "anand",
          group    => "anand",
          mode     => "755",
          content  => "Hello Anand !! This is Puppet code learning",
         }
         
### Install a Package

        package { "httpd":
          ensure   => "present",
         }

        service { "httpd":
          ensure  => "running",
         }


## Puppet Classes

      Puppet classes are collection of puppet resources bundle to gether as a single unit.
