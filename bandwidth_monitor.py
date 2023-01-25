import psutil

def get_network_info():
    # Get network usage statistics
    net_io_counters = psutil.net_io_counters()
    # Get the number of bytes sent
    bytes_sent = net_io_counters.bytes_sent
    # Get the number of bytes received
    bytes_recv = net_io_counters.bytes_recv
    # Return the number of bytes sent and received
    return (bytes_sent, bytes_recv)

def monitor_bandwidth():
    # Get the initial number of bytes sent and received
    initial_bytes_sent, initial_bytes_recv = get_network_info()
    # Wait for 1 second
    time.sleep(1)
    # Get the final number of bytes sent and received
    final_bytes_sent, final_bytes_recv = get_network_info()
    # Calculate the difference in bytes sent and received
    bytes_sent_per_sec = final_bytes_sent - initial_bytes_sent
    bytes_recv_per_sec = final_bytes_recv - initial_bytes_recv
    # Print the bandwidth usage
    print("Sent: {} bytes/s | Received: {} bytes/s".format(bytes_sent_per_sec, bytes_recv_per_sec))

# Monitor the bandwidth usage every second
while True:
    monitor_bandwidth()
