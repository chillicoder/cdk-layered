from aws_cdk import (
    aws_ec2 as ec2,
    core as cdk
)

# For consistency with other languages, `cdk` is the preferred import name for
# the CDK's core module.  The following line also imports it as `core` for use
# with examples from the CDK Developer's Guide, which are in the process of
# being updated to use `cdk`.  You may delete this import if you don't need it.
from aws_cdk import core


class VpcStack(cdk.Stack):

    def __init__(self, scope: cdk.Construct, construct_id: str, cidr, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        self.vpc = ec2.Vpc(
            self, "ThisVpc",
            cidr=str(cidr),
            max_azs=2
        )

        core.CfnOutput(
            self,"Output",
            value=self.vpc.vpc_id
        )
