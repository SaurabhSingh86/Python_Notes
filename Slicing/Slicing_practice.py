s = "Sky is no limit"
                    # interpreter execution start_index => step_size => end_index => step_size =>end .... till the end
# Sky
print(s[:3])
print(s[-15:-12])
print(s[-15:3])

# is
print(s[4:6])
print(s[-11:-9])
print(s[4:-9])
print(s[-11:6])

# no
print(s[7:9])
print(s[7:-6])
print(s[-8:-6])
print(s[-8:9])

# limit
print(s[10:])
print(s[-5:])

# Entire list
print(s[::])
print(s[:])

# Reverse Entire list
print(s[::-1])

# o/p => 'tmlo iyS'
print(s[::-2])
