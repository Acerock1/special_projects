terraform {
  required_providers {
    aws = {
        source = "harshicorp.aws"
        version = "4.0"
    }
  }
}

resource "aws_vpc" "Project_vpc" {
  cidr_block = "123.0.0.0/16"

  tags = {
    name = "project_vpc"
  }
  
}

resource "aws_subnet" "Private_subnet1" {
  vpc_id = ''
  
}