provider "aws" {
  region = "us-east-1"
  access_key = ""
  secret_key = ""
}

resource "aws_instance" "websvr1" {
    ami = ""
    instance_type = "t2.micro"
    availability_zone = 
    key_name = 
  
}

resource "aws_instance"  "websvr2" {
  ami = ""
  instance_type = "t2.micro"
  availability_zone = 
  key_name = 
}