# Example file for Advanced Python by Joe Marini
# Formatting output strings

# Basic formatting - center(), ljust(), rjust()
withdh = 40
print("Centered".center(withdh, '-'))
print("Left Aligned".ljust(withdh, '.'))
print("Right Aligned".rjust(withdh, '.'))

# Formatting strings with format specification codes
# Format spec is: [[fill]align][sign]["z"]["#"]["0"][width][grouping_option]["."precision][type]
val1 = 1234.5678
val2 = 10987.65
val3 = 12.99
val4 = -280.7

print(f"{val1}")
print(f"{val2}")
print(f"{val3}")
print(f"{val4}")
print()
# Specify a precision and type
# After the colon we can specify format options

print(f"{val1:.2f}")
print(f"{val2:.2e}")
print(f"{val3:.2f}")
print(f"{val4:.2f}")
print()

# Use alignment and width and leading zeros
# < is left align, > is right align, ^ is centered
# spacify width after alignment symbol


print(f"{val1:>010.2f}") # leading zeros
print(f"{val2:>10.2f}")
print(f"{val3:^10.2f}")
print(f"{val4:^10.2f}")
print()
# Use a grouping option and +/- signs

print(f"{val1:>+10.2f}") 
print(f"{val2:>+10.2f}")
print(f"{val3:^+10.2f}")
print(f"{val4:^+10.2f}")
print()
# just negative numbers with sign
print(f"{val1:>-10.2f}") 
print(f"{val2:>-10.2f}")
print(f"{val3:^-10.2f}")
print(f"{val4:^-10.2f}")
print()

#spefiying the grouping option with comma

print(f"{val1:>-10,.2f}") 
print(f"{val2:>-10,.2f}")
print(f"{val3:^-10,.2f}")
print(f"{val4:^-10,.2f}")
print()
# Insert a fill character that is not a leading zero

print(f"{val1:_>-10,.2f}") 
print(f"{val2:_>-10,.2f}")
print(f"{val3:_^-10,.2f}")
print(f"{val4:_^-10,.2f}")
print()

# Create format specifiers dynamically
width = 10
precision = 2

format_spec = f"{123.456:{width}.{precision}f}"
print(format_spec)
print()

format_spec = "{val:{width}.{precision}f}".format(val=123.456, width=width, precision=precision)
print(format_spec)

