#!/usr/bin/python

# Simple multi-person chat server
#
# Grant Cohoe
# Camp Fitch Computer Camp 2013

# Load modules
import socket,select,sys

# Set the host and port that we are binding to
host = "0.0.0.0"
port = 31337

# Create the socket object and give it certain parameters 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Bind the socket object to the host and port
s.bind((host, port))
# Set the socket to listen mode and specify the number of connections to queue up
s.listen(5)
# Accept an initial connection from a client
conn, addr = s.accept()
# Print when we got a connection
print "New connection from: "+str(addr)

# Set up a list of sockets that we are going to use to push data around
input_sockets = [s, sys.stdin, conn]

# Main loop. Listen for messages, print them, accept them, and more!
while True:
	# Generate a list of sockets that have data ready for us, are ready for data from us, or errored
	inputready, outputready, exceptready = select.select(input_sockets, input_sockets, [])

	# Store the last message sent to prevent duplication
	prev_msg = ""

	# Loop over each socket and do something depending on its state
	for sock in inputready:
		# This is a new connection
		if sock == s:
			# Create a connection and address variable from the socket connection
			client, address = s.accept()
			# Add them to the socket list
			input_sockets.append(client)
			print "New connection from: "+str(address)
		# Message from the server to the clients
		elif sock  == sys.stdin:
			# Get the line from the server window
			stuff = sys.stdin.readline()
			# Get rid of the EOL character
			stuff.rstrip()
			# Exit the server if "exit" appears
			if stuff == "exit":
				break
			# Print the server message to the clients
			for socke in outputready:
				# Make sure this is a socket and not stdin, also that there is actually a message
				if socke != sys.stdin and stuff:
					try:
						# If the new messasge is not the previous message (duplicate)
						if stuff != prev_msg:
							# Print the message to the clients!
							socke.send(stuff)
					except:
						# Something bad happened
						print "ERROR-STDIN: "+stuff
			# Prevent message duplication
			prev_msg = stuff
		# Message from a client to everyone else
		else:
			# Get the data from the socket
			data = sock.recv(1024)
			# Remove the EOL character
			data.rstrip()
			# If there is actually data
			if data:
				# The client would like to exit
				if data == "exit":
					# Cleanly close the socket
					print "Closing connection"
					sock.close()
					# Remove it from the list of connections
					input_sockets.remove(sock)
					break
				else:
					# For all remaining connections, print their message
					for socke in outputready:
						# Can't print to stdin and do not want to print to themselves. 
						if socke != sys.stdin and socke != sock:
							try:
								# Print to the sockets if there is a new message
								if data != prev_msg:
									# Send to socket
									socke.send(data)
							except:
								# Something bad happened
								print "ERROR-SEND: "+data
						# Print to the server
						elif socke == sys.stdin:
							if data != prev_msg:
								# Print to the server
								print "DATA-SYS: " + data
							else:
								print "DUPLICATE MESSAGE SYS: "+data
					# Set the previous message
					prev_msg = data
			# No data. Terminate the connection.
			else:
				# Close the socket
				print "Closing connection"
				sock.close()
				# Remove it from the list of connections
				input_sockets.remove(sock)
