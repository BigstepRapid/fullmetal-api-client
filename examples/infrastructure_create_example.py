import sys
import os.path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from initialize_python_client import BSIClient

bsi = BSIClient.init()

strInfrastructureName = "infrastructure-label"

strUserID = "your_login_email@goes.here"

# select the datacenter where the infrastructure will be created
dictDatacenters = bsi.datacenters()
datacenter =  dictDatacenters[next(iter(dictDatacenters))]

# setting up the infrastructure object parameter
dictInfrastructureCreateParams = {
    "infrastructure_label" : strInfrastructureName,
    "datacenter_name" : datacenter.datacenter_name
}

dictInfrastructure = bsi.infrastructure_create(strUserID, dictInfrastructureCreateParams, None)

# the operation needs to be deployed in order for hardware to be provisioned and software installed