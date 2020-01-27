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
    ex: aws configure --profile terraform_user.  ## terraform_user is created from IAM with Admin access
 
 ## Terraform Commands 
 
  - Initialize the terraform
    
        terraform init
        
  - Arrange the terraform configuration file in proper format 
  
        terraform fmt
        
  - Run your script as DRY RUN mode.
  
        terraform plan
        
  - Provision your script 
  
        terraform apply
        
  - Update your existing infrastructure.
   
        terraform apply
        
  - Destroy your Infrastructure
  
        terraform destroy
        
  - Terraform Console
  
        terraform console
        
  - Sample configuration to craete a EC2_Server
  
        provider "aws" {
        profile = "terraform_user"
              region = "eu-west-1"
        }
        resource "aws_instance" "my-ec2-ins" {
          ami     = "ami-02df9ea15c1778c9c"
          instance_type = "t2.micro"

          tags = {
            Name = "terraform_anand"
          }
        }


## Variable Declaration

  - String declaration
  
        variable "myvar" {
          type = "string"
          default = "Hello Platform"
      }
      
      Run : 
      
        - terraform console
        - var.myvar.  or "${var.myvar}"
        
  - 
