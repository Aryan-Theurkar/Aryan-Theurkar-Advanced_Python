import gc

class Demo:
    def __init__(self):
        self.ref = None

# Create objects
a = Demo()
b = Demo()

# Create circular reference
a.ref = b
b.ref = a

print("Before Garbage Collection:")
print("Garbage Objects:", len(gc.garbage))

# Delete objects
del a
del b

# Automatic Garbage Collection
print("Collected:", gc.collect())

# Memory Information
print("Garbage Collection Count:", gc.get_count())

# Disable automatic collection
gc.disable()
print("Automatic GC Disabled")

# Manual collection
print("Manual Collection:", gc.collect())

# Enable automatic collection
gc.enable()
print("Automatic GC Enabled")
