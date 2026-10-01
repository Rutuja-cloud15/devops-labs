aws_ec2_instance = {
"instance_id": "i-0987sfee",
"instance_type" : "t2.micro",
"status" : "stopped",
"public_ip" : "54.210.43.8" }

print("--- AWS CONSOLE SIMULATOR ---")
print("Current Server State:", aws_ec2_instance["status"])

#Changing the state
print("\nBooting up instance", aws_ec2_instance["instance_id"],"...")
aws_ec2_instance["status"]= "running"

print("Server is now:", aws_ec2_instance["status"].upper())
print("Your application is live at http://" + aws_ec2_instance["public_ip"] + ":80")
