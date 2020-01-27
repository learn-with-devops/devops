## About Terraform:

- It is An Infrastructure as a Code ( IAC )

- Terraform is a tool for developing, changing and versioning infrastructure safely and efficiently. 
Terraform can manage existing and popular service providers as well as custom in-house solutions. 
Terraform is the first multi-cloud immutable infrastructure tool that was introduced to the world by **HashiCorp**,
released three years ago, and written in **Go**. 

## Installation of terraform: 

- wget https://releases.hashicorp.com/terraform/0.11.11/terraform_0.11.11_linux_amd64.zip
- export PATH=/root/terraform/:$PATH (or) PATH=${PATH}:/root/terraform

## Supports

It support any kind of cloud for provisining your infrastructure.

  - AWS
  - Azure
  - GoogleCloud
  - openStack
  - VM's etc...
  
## Configuration file

It supports two kind of configuration files

  - .tf files
  - .tf.json files

  Note : Terraform will download the required plugins based on provider name specified in the configuration file. 

## SetUp with AWS 

Create a IAM user with admin access and configure in Linux/Windows/Mac Server.

  - aws configure --profile <profile_name>
