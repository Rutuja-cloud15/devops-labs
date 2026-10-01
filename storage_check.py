def find_server_pair(storage_sizes, target):
   
#Use two loops
    for i in range(len(storage_sizes)):
        for j in range(i + 1, len(storage_sizes)):
           if storage_sizes[i] + storage_sizes[j] ==target:
                return[i,j]
    return[]

servers = [10,20,40,80,100]
target_needed = 60

result = find_server_pair(servers, target_needed)
if result:
   print("Matching pair found at index positions:", result)
   print("The server capacities are:", servers[result[0]], "GB and", servers)
else:
   print("No two servers can combine to hit the target.")


