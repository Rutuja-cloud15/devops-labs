import sys

# sys.argv[0] is always the name of the script itself
# sys.argv[1] will be the action command we pass in !

if len(sys.argv) < 2:
     print("Usage:python3 control_panel.py [start|stop|status]")
     sys.exit()
action = sys.argv[1]

if action == "start":
    print("Starting all cloud applications")
elif action =="stop":
    print("Shutting down servers safely")
elif action =="status":
    print("Checking system status: All systems nominal.")
else:
    print("Unknown command!")

