
param name string
param location string = resourceGroup().location
param tags object = {}
param prefix string
var dbserverUser = 'admin${uniqueString(resourceGroup().id)}'
@secure()
param dbserverPassword string
param dbserverDatabaseName string

module dbserver 'core/database/mysql/flexibleserver.bicep' = {
  name: name
  params: {
    name: '${prefix}-mysql'
    location: location
    tags: tags
    sku: {
      name: 'Standard_B1ms'
      tier: 'Burstable'
    }
    storage: {
      storageSizeGB: 20
    }
    version: '8.0.21'
    administratorLogin: dbserverUser
    administratorLoginPassword: dbserverPassword
    databaseNames: [ dbserverDatabaseName ]
    allowAzureIPsFirewall: true
  }
}

output dbserverDatabaseName string = dbserverDatabaseName
output dbserverUser string = dbserverUser
output dbserverDomainName string = dbserver.outputs.MYSQL_DOMAIN_NAME
