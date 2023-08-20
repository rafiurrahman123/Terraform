terraform {
  required_providers {
    azurerm = {
      source = "hashicorp/azurerm"
      version = "3.70.0"
    }
  }
}

provider "azurerm" {
  skip_provider_registration = "true"
  features {} 
}

#build azure resource group
resource "azurerm_resource_group" "terraform-mainRG-001" {
  name = var.rsgname
  location = var.location
  
}

resource "azurerm_virtual_network" "mainnetwork" {
  name = "mainnetwork"
  location = azurerm_resource_group.terraform-mainRG-001.location
  resource_group_name = azurerm_resource_group.terraform-mainRG-001.name
  address_space = ["10.0.0.0/16"]
}

#build devsubnet and link to mainnetwork virtual network
resource "azurerm_subnet" "devsubnet" {
  name = "dev-subnet"
  resource_group_name = azurerm_resource_group.terraform-mainRG-001.name
  address_prefixes = ["10.0.1.0/24"]
  virtual_network_name = azurerm_virtual_network.mainnetwork.name
}

#build testsubnet and link to mainnetwork virtual network
resource "azurerm_subnet" "testsubnet" {
  name = "test-subnet"
  resource_group_name = azurerm_resource_group.terraform-mainRG-001.name
  address_prefixes = ["10.0.2.0/24"]
  virtual_network_name = azurerm_virtual_network.mainnetwork.name
}

resource "azurerm_storage_account" "storageaccountname" {
  name                     = var.stgactname
  resource_group_name      = azurerm_resource_group.terraform-mainRG-001.name
  location                 = azurerm_resource_group.terraform-mainRG-001.location
  account_tier             = "Standard"
  account_replication_type = "GRS"

  tags = {
    environment = "staging"
  }
}