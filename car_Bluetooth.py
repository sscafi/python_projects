import bluetooth

# The MAC address of the car's Bluetooth device
car_address = "00:11:22:33:44:55"

# Create a socket object for Bluetooth communication
socket = bluetooth.BluetoothSocket(bluetooth.RFCOMM)

# Establish a connection with the car's Bluetooth device on channel 1
socket.connect((car_address, 1))

# Send a message to the car
socket.send("Hello, car!")

# Receive a response from the car
response = socket.recv(1024)
print("Response from car: " + response)

# Close the Bluetooth socket
socket.close()
