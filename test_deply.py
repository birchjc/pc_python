import platform
import datetime

print("--------------------------------------------------")
print(f"Hello! This code was written on Windows.")
print(f"But right now, it is running on: {platform.node()} ({platform.system()})")
print(f"The time is: {datetime.datetime.now()}")
print("--------------------------------------------------")