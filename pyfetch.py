from cpuinfo import get_cpu_info
import platform
import os
import subprocess
import linecache
import re
import distro
import psutil

product = "product"

# Allow commands to run in SHELL
os.path.expandvars("$PATH")

# Get CPU info
cpuInfo = get_cpu_info()['brand_raw']
# Get GPU info
os.path.expandvars("$PATH")
lshw = subprocess.Popen(("lshw", "-C", "display"), stderr=subprocess.DEVNULL, stdout=subprocess.PIPE)
output = subprocess.check_output(("tee", "gpu.txt"), stdin=lshw.stdout)
preGpuName = linecache.getline("gpu.txt", 3)
gpuName = re.sub("       product: ", "", preGpuName)
# Get Memory info
memory = psutil.virtual_memory()[2]
# Get System & Host info
mSys = platform.uname()
host = mSys.node
kernelSystem = platform.platform()
distro = distro.name()


# Print result
print("OS:", distro)
print()
print(f"Host:", host)
print()
print("Kernel:", kernelSystem)
print()
print("CPU:", cpuInfo)
print()
print("GPU:", gpuName)
print("Memory % Used:", memory)
