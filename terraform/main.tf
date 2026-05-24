resource "aws_security_group" "mlops_sg" {

  name = "mlops-security-group"

  ingress {

    from_port = 22
    to_port = 22
    protocol = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {

    from_port = 5000
    to_port = 5000
    protocol = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {

    from_port = 8081
    to_port = 8081
    protocol = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {

    from_port = 30007
    to_port = 30007
    protocol = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {

    from_port = 30081
    to_port = 30081
    protocol = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {

    from_port = 0
    to_port = 0
    protocol = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

resource "aws_instance" "mlops_server" {

  ami = var.ami_id

  instance_type = var.instance_type

  key_name = var.key_name

  security_groups = [
    aws_security_group.mlops_sg.name
  ]

  tags = {
    Name = "EdgeIntelliShield-MLOps"
  }

  user_data = <<-EOF
              #!/bin/bash

              sudo apt update -y

              sudo apt install docker.io -y

              sudo systemctl start docker

              sudo systemctl enable docker

              sudo apt install docker-compose -y

              EOF
}