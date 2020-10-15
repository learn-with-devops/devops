## BackUp and Restore

- Many nunmber of ways to take backup of DataBase.

        - Generate the backup using mysqldump utility
        - Generate Incremental backups using Binary Log
        - Generate backups using the Replication of Slaves
        
### Generate the backup using mysqldump utility
------

- Taking Backup of Single DataBase

        mysqldump -u <user> -p <Database> > /opt/mysql_backup/Employee_backup.sql
        
        Ex: 
            mysqldump -u root -p Employee > /opt/mysql_backup/Employee_backup.sql 
            
- Encrypt that DataBase for security purpouse with openSSL.
        
        openssl enc -aes-256-cbc -in /opt/mysql_backup/Employee_backup.sql -out /opt/mysql_backup/Employee_backup_encrypted.file

        Note : 
        - It will ask for Password and enter that. 
        - Remove main backup file.
            rm -rf /opt/mysql_backup/Employee_backup.sql
            
- For Testing purpouse Drop your database in MYSQL DB.
        
        drop database Employee;

- Now Decrypt the encrypted file with openSSL.

        openssl enc -aes-256-cbc -d -in  /opt/mysql_backup/Employee_backup_encrypted.file > /opt/mysql_backup/Employee_backup.sql
        
- Restore the decrypted file to Database.

        mysql -u root -p Employee < /opt/mysql_backup/Employee_backup.sql 
        
-----

#### Taking Backup of Multiple Databases.

        sudo mysqldump -u [user] -p [database_1] [database_2] [database_etc] > [filename].sql
    
### Taking Backup for entire Database.

        mysqldump -u root -p --all-databases > /opt/mysql_backup/total_backup.sql
