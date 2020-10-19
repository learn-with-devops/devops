Linux booting:
-------

- It is a process to initiate a laptop or desktop with os.
- when you press the power button then internally some process is going so, that is known as booting process.
- booting process is follows some steps internally. below are the steps

      1 -- Bios -- basic input & output 
             post (power on self test)
             hardware ram,rom,cd-rom
      2 -- MBR  -- boot recorder
      3 -- GRUB -- grand united boot loader
      4 -- Kernal -- taker care of os into Ram
      5 -- INIT process
           0 halt
           1 single usermode
           2 multiuser
           3 full multiuser mode
           4 unused
           5 graphical mode
           6 reboot
      6 -- run level -- /etc/rc.d/rco.d or rc1.d
 
1)BIOS:
------
        - the first stage of booting process when you on/restart your machine the power is supplied to SMPS which converts AC to DC.
        - the DC power is supplied to all device connected to that machine such as processor, RAM, CD-ROM, mouse, keyboard, etc..
        - The most intelligent device in computer is processor(CPU).
        - when power supplied it will start running it's sequence of instructions stored in the memory.
        - The instruction it will run is to pass control to BIOS
        - in BIOS 2 operations are going
         a)POST (power on self test)
         b)selecting first boot device
        - post is process of checking H/W availability.
        - BIOS will have list of all devices.
        - In post process it will send an electric pulse to each and every device.
        - if an electric pulse is returned from that device it conclude the h/w working fine and ready for use it.
        - if it does not receive signal from that device. it will treat that device is not working.

2)MBR:
-----
        - The MBR is the first sector of the computer hard drive that tells the computer how to load the operating system, how the hard drive is partitioned.
        - A master boot record (MBR) is the 512-byte boot sector that is the first sector of a partitioned data storage device of a hard disk.

3)GRUB:
------
        - It is a multi boot loader package. that supports multiple operating systems on a computer. During boot-up, the user can select the operating system to run. if you are not specified it loads the default kernel.
 
4)KERNEL:
--------
        - kernel is the core part of the operating system. once control is given to kernel which is the control part of all your OS & act as a mediator between h/w &   s/w. 
        - kernel once loaded into RAM it always resides on RAM until the machine is shutdown.
        - once the kernel start it's operates the first thing it do is executing INIT Process. 

5)INIT:
------
        - after OS started initial process is starting. it is parent process of the all processes in Os.
        - in "/etc/inittab" in this config file we have the default initialize process is their.
        - It is the first process to start when a computer boots up, and it runs until the system shuts down
         0 halt
         1 single usermode
         2 multiuser
         3 full multiuser mode
         4 unused
         5 graphical mode
         6 reboot
 

6)RUN LEVEL:
------------
        - when the linux system is bootup, you might see various services getting started.
        - those are run level programs, executed from run level directory as defined by your runlevel
        - depending on your INIT level settings, the system executed the program from one of the following directions.

        Runlevel 0- /etc/rc.d/rc0.d/ 
          1- /etc/rc.d/rc1.d/ 
          2- /etc/rc.d/rc3.d/ 
          3- /etc/rc.d/rc3.d/ 
          4- /etc/rc.d/rc4.d/ 
          5- /etc/rc.d/rc5.d/
          6- /etc/rc.d/rc6.d/
