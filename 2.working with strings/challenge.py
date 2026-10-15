# Convert the messy phone number
# into a clean number format with only digits

# # "+49 (176) 123-4567"

no ="+49 (176) 123-4567"
print(no.replace("+","").replace("(","").replace(")","").replace("-","").replace(" ",""))