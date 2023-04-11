# This is an automatically generated code sample.
# To make this code sample work in your Oracle Cloud tenancy,
# please replace the values for any parameters whose current values do not fit
# your use case (such as resource IDs, strings containing ‘EXAMPLE’ or ‘unique_id’, and
# boolean, number, and enum parameters with values not fitting your use case).

import oci
from datetime import datetime

# Create a default config using DEFAULT profile in default location
# Refer to
# https://docs.cloud.oracle.com/en-us/iaas/Content/API/Concepts/sdkconfig.htm#SDK_and_CLI_Configuration_File
# for more info
config = oci.config.from_file()


# Initialize service client with default config file
core_client = oci.core.ComputeClient(config)


# Send the request to service, some parameters are not required, see API
# doc for more info
update_instance_response = core_client.update_instance(
    instance_id="ocid1.instance.oc1.iad.anuwcljtctshpiyc7xzbvt622arxiv3oj755nwpdp2e4fzumbxbbqyal5dwa",
    update_instance_details=oci.core.models.UpdateInstanceDetails(
        shape="VM.Standard.E3.Flex",
        shape_config=oci.core.models.UpdateInstanceShapeConfigDetails(
            ocpus=4.0,
            memory_in_gbs=64.0,
            baseline_ocpu_utilization="BASELINE_1_1"),
    ))

# Get the data from response
print(update_instance_response.data)
