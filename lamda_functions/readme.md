Sample Lambda functions authored from scratch by me.


1.  ebs_volume_check.py
    -This lambda function has been authored from scratch using python3.8 as it's runtime.
    -It employs boto3 to modify EBS volumes that do comply with a set policy to only provision gp3 type volumes. 
    -We use Cloudwatch events to monitor EBS volumes that are provisioned; if EBS type is not gp3, lambda function modifies volumes as needed.
    -A cloudwatch rule is created and attached to lambda to invoke this function.
    -Logstreams are monitored to see when lambda function has been invoked.

