# Chat client - ah

# Imports
import socket
import sys

# Check if a string contains a substring
def instr(chkstr, substr):
    return not chkstr.find(substr) == -1

# Get server ip and port to connect to from user
connect_to = raw_input("Enter a server IP to connect to: ")
# Validate input
if connect_to == "":
    print "No IP entered"
    sys.exit(0)
# Check if user entered information in ip:port format
if not instr(connect_to, ":"):
    print "Not a valid server IP"
    sys.exit(0)

# Validate input again
get_conn_info = connect_to.split(":")
if not get_conn_info[1].isdigit():
    print "Invalid port"
    sys.exit(0)
# Make a tuple out of it and try to connect to the socket
conn_tuple = get_conn_info[0], int(get_conn_info[1])
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    sock.connect(conn_tuple)
except:
    print "Could not find server"
    sock.close()
    sys.exit(0)
# After a successful connection, print that server was found
print "Found server"
# Ask for a username
username = raw_input("Enter a username: ")
# Verify that a username was entered
if username == "":
    print "No username was entered, disconnecting"
    sock.close()
    sys.exit(0)
# Send username to server
sock.sendall(username)
# Get response from server
login_response = sock.recv(1024).replace("\n", "")
# Login successful
if login_response == "Ok":
    print "Connection to server accepted"
# Login rejected
elif login_response == "Nope":
    print "Connection to server rejected"
    sock.close()
    sys.exit(0)
# Received an unknown response from the server
else:
    print "Received unknown response from server, disconnecting"
    sock.close()
    sys.exit(0)
# Print login successful
print "Logged in as {0} successfully".format(username)
# Infinite loop for sending messages
while True:
    message = raw_input("Enter a message to send: ")
    if not message == "":
        # Exception handling in case server closes connection unexpectedly
        try:
            sock.sendall(message)
        except:
            print "Server closed connection unexpectedly"
            sock.close()
            sys.exit(0)
