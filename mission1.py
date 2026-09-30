name = "SRE"
print("Hello, there!")
print(name)

server_status = "good"
if server_status == "broken":
     print("Alert! Call the Devops!")
else:
     print("Running smoothly")

for server_id in range(1,6):
   if server_id == 3:
       print("Server 3 is crashed")
   else:
       print("Server", server_id, "is healthy") 

for num in range(1,21):
   if num % 3 == 0 and num % 5 == 0:
        print("DevOps")
   elif num % 5 == 0:
        print("Ops")
   elif num % 3 == 0:
        print("Dev")
   else:
        print(num)
