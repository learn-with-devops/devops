## Vault

      Secure, store and tightly control access to tokens, passwords, certificates, encryption keys 
      for protecting secrets and other sensitive data using a UI, CLI, or HTTP API.
      
## Installation  of Vault

      ###  I am using a CentOS 7 EC2, 
      ###  I am following https://learn.hashicorp.com/vault/getting-started/install

            wget https://releases.hashicorp.com/vault/1.0.3/vault_1.0.3_linux_amd64.zip
            
      ### Unzip the Vault
            
            unzip vault_1.0.3_linux_amd64.zip

      ### I am copying vault binarry 
            
            cp vault /usr/bin/vault

      ### Install command-line completion
      
            vault -autocomplete-install
      
      ###  Reload shell
      
            exec $SHELL

      ### Start Vault server
      
            vault server -dev
      

## Vault CLI Operations

      - Start by setting the environment variable.
            
            export VAULT_ADDR=’http://127.0.0.1:8200’
            
      - 
