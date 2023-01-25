output_file="system_information.csv"

# Get CPU usage
cpu_usage=$(top -b -n1 | awk '/Cpu\(s\):/ {print $2}')

# Get RAM usage
free_memory=$(free -m | awk 'NR==2{printf "%.2f\n", $4*100/$2 }')
total_memory=$(free -m | awk 'NR==2{printf "%.2f\n", $2 }')

# Get disk usage
df -h | awk '{print $1 " " $5}' | grep -v Use > $output_file

# Append the system information to the CSV file
echo "CPU,$cpu_usage" >> $output_file
echo "RAM,$free_memory,$total_memory" >> $output_file

echo "System information exported to $output_file"
