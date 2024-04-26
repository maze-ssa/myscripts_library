import subprocess

source_dir = '/home/adm-ssa/aws_folder'
dest_dir = '/home/adm-ssa/on-premise_folder'

cmd = f"rclone copy {source_dir} {dest_dir} --no-traverse"
subprocess.run(cmd, shell=True)
