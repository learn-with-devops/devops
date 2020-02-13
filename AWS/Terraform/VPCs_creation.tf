# provider.tf

provider "aws" {
    region = "${var.region_name}"
}

# variables.tf

variable "vpc_cidr" {
    default = "10.80.0.0/16"
}

variable "subnets_cidr" {
    type = list
    default = ["10.80.0.0/24","10.80.1.0/24"]
}

variable "avilability_zone_subnet" {
    type = list
    default = ["eu-west-1a","eu-west-1c"]
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


# vpc.tf

resource "aws_vpc" "terra_vpc" {
    cidr_block = "${var.vpc_cidr}"
    tags = {
        name = "terra-vpc"
    }
}

resource "aws_internet_gateway" "ig_main" {
    vpc_id = "${aws_vpc.terra_vpc.id}"
    tags = {
        name = "ig_main"
    }
}

resource "aws_subnet" "terr-pub" {
    count = "${length(var.subnets_cidr)}"
    vpc_id = "${aws_vpc.terra_vpc.id}"
    cidr_block = "${element(var.subnets_cidr,count.index)}"
    availability_zone = "${element(var.avilability_zone_subnet,count.index)}"
    tags = {
        name = "subnet-$(count.index+1)"
    }
}

resource "aws_route_table" "pub-rt" {
    vpc_id = "${aws_vpc.terra_vpc.id}"
    route {
        cidr_block = "0.0.0.0/0"
        gateway_id = "${aws_internet_gateway.ig_main.id}"
    }
}

resource "aws_route_table_association" "rt-a" {
    count = "${length(var.subnets_cidr)}"
    subnet_id = "${element(aws_subnet.terr-pub.*.id,count.index)}"
    route_table_id = "${aws_route_table.pub-rt.id}"
}
