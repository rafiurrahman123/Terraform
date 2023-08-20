#Project Variable
variable "location" {
  type = string
  description = "The location of the Deployment"
  default= "East US"
}

variable "rsgname" {
  type = string
  description = "Resource Group name"
  default= "terraform-mainRG-001"
}

variable "stgactname" {
  type = string
  description = "Storage Account name"
}
