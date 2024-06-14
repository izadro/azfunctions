import logging
import azure.functions as func
from azure.identity import DefaultAzureCredential
from azure.mgmt.compute import ComputeManagementClient

subscription_id = ${{SUBSCRIPTION_ID}}
resource_group_name = 'qa-allurereports-poc_group'
vm_name = 'qa-allurereports-poc'

def main(mytimer: func.TimerRequest) -> None:
    utc_timestamp = datetime.datetime.utcnow().replace(
        tzinfo=datetime.timezone.utc).isoformat()

    if mytimer.past_due:
        logging.info('The timer is past due!')

    logging.info('Python timer trigger function ran at %s', utc_timestamp)

    # Authenticate using DefaultAzureCredential
    credential = DefaultAzureCredential()
    compute_client = ComputeManagementClient(credential, subscription_id)

    # Start the VM
    async_vm_start = compute_client.virtual_machines.begin_start(resource_group_name, vm_name)
    async_vm_start.result()  # Wait for the operation to complete

    logging.info(f'Started VM {vm_name} in resource group {resource_group_name}')
