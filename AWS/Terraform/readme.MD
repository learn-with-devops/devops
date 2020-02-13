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
    
        terraform init.  ( Terraform will download the required plugins based on provider name specified in the configuration file )
        
  - Arrange the terraform configuration file in proper format 
  
        terraform fmt
        
  - Run your script as DRY RUN mode.
  
        terraform plan
        
        Note : Store the dryrun mode output like below
               terraform plan -out out.terraform
        
  - Provision your script 
  
        terraform apply.      // terrafor apply --auto-approve ( for auto creating the ec2 )
        
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
        
### Note

        [root@ip-172-31-31-8 ec2_demo]# cat ~/.aws/config 
        [default]
        region = eu-west-1
        [profile terraform_user]
        region = eu-west-1
        [root@ip-172-31-31-8 ec2_demo]# cat ~/.aws/credentials 
        [default]
        aws_access_key_id = AKIAJHO7C627BHFOAMOA
        aws_secret_access_key = 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
        [terraform_user]
        aws_access_key_id = AKIAXSB5ISV5RWIQFB26
        aws_secret_access_key = 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

## Variable Types

### Simple Variable types

    - String 
    - Number
    - Boolean
    
### Complex types

    - List
    - Set
    - Map 
    - Object
    - Tuple
    

## Variable Declaration

  - String declaration
  
        variable "myvar" {
          type = "string"
          default = "Hello Platform"
      }
      
      Run : 
      
        - terraform console
        - var.myvar.  or "${var.myvar}"
        
  - Map Declaration
  
        variable "mymap" {
          type = map(string)
          default = {
        mykey = "my value"
          }
        }
      Run :
      
        - var.mymap
        - var.mymap["mykey"] or "${var.mymap["mykey"]}"
        
  - List Declaration
  
        variable "mylist" {
          type = list
          default = [1,2,3]
        }
        
       Run:
       
         - var.mylist
         - var.mylist[1]
         - element(var.mylist, 1)
         - slice(var.mylist, 0, 2)
  
     
## Starting from scrach

### EC2 Instace Creation with direct process

        provider "aws" {
            region = "eu-west-1"
        }

        resource "aws_instance" "httpd" {
            count   =  2
            ami              = "ami-0ff760d16d9497662"
            instance_type    = "t2.micro"
            key_name         = "Anand-Mac-Ireland"
            monitoring       = true
            vpc_security_group_ids = ["sg-0635bbd6766f3cab1"]
            subnet_id        =  "subnet-e7257faf"
            tags = {
                Name = "apache-test"
                Env  = "test"
            }
        }
        
### EC2 creation with Variables and See the Output with Output Variable

                provider "aws" {
                    region = "${var.region_name}"
                }

                variable "instance_count" {
                    default = "1"
                }

                variable "ami_types" {
                    type = map(string)
                    default = {
                        "eu-west-1" = "ami-0ff760d16d9497662"
                        "eu-east-2" = "ami-0ff760d16d9497663"
                        "eu-west-3" = "ami-0ff760d16d9497662"
                    }
                }

                variable "region_name" {
                    default = "eu-west-1"
                }

                variable "instance_type" {
                    default = "t2.micro"
                }

                variable "monitoring" {
                    default = "true"
                }

                variable "tags" {
                    type = map(string)
                    default = {
                        "name" = "apache-test"
                        "env" = "test"
                    }
                }

                resource "aws_instance" "httpd" {
                    count            = "${var.instance_count}"
                    ami              = "${lookup(var.ami_types,var.region_name)}"
                    instance_type    = "${var.instance_type}"
                    key_name         = "Anand-Mac-Ireland"
                    monitoring       = "${var.monitoring}"
                    vpc_security_group_ids = ["sg-0635bbd6766f3cab1"]
                    subnet_id        = "subnet-e7257faf"
                    tags = "${var.tags}"
                }

                output "instance_ip" {
                    value = "${aws_instance.httpd.*.public_ip}"
                }


                // TAGS DECLARATION WITH LIST
                // variable "instance_tags" {
                //  type = "list"
                //  default = ["Terraform-1", "Terraform-2"]
                // }

                // tags = {
                //    Name  = "${element(var.instance_tags, count.index)}"
                //    Batch = "5AM"
                //  }

        Note : 
        
            ## See the Output
            
            terraform output
            
