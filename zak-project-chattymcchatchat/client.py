# Import the nessary libraries
import socket
import string
import select
import sys

# Socket variable declaration
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(2)

# Connect to server. Change this for remote servers.
s.connect(("10.0.0.165", 1356))

# A prompt asking client to enter something.
sys.stdout.write(">")
sys.stdout.flush()

while 1:
    # These are the possible events.
    # sys.stdin --> Client has typed something through keyboard.
    # s --> Server has send a new message by some other client you.
    streams = [sys.stdin, s]

    # Moniter both the streams simultaneously for inputs.
    readable, writable, err = select.select(streams, [], [])

    # If server has sent something, readable will fill up.
    for sock in readable:
        if sock == s:

            # Receive data in our variable. Check if it is empty.
            data = sock.recv(1024)
            if not data:
                sys.exit()
            else:

                # Write data to stdout and give client prompt back.
                sys.stdout.write(data)
                sys.stdout.write(">")
                sys.stdout.flush()

        # No, its not the server. Our client has typed something in.
        else:

            # Read message. Send it to server. Give prompt back to client.
            msg = sys.stdin.readline()
            s.send(msg)
            sys.stdout.write(">")
            sys.stdout.flush()

