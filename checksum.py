print("Check sum calcuator")
s = []
r = []


def inputEl(n, frames):
  for i in range(n):
    frames.append(input(f"Enter frame{i+1}: "))


def calculate(frames):
  n = len(frames)
  result = ""
  if n <= 0:
    print("No frames to check")
  elif n == 1:
    return frames[0]
  else:
    for i in range(1, n):
      print(" ", frames[i - 1])
      print("+", frames[i])
      print("-----------")
      result = str(bin(int(frames[i - 1], 2) + int(frames[i], 2)))[2:]
      frames[i] = ((len(frames[0]) - len(result)) * "0") + result
      print(" ", frames[i])
      print()

      if len(str(frames[0])) < len(str(result)):
        print(" ", result[1:])
        print("+", (len(str(frames[i])) - 3) * " ", "1")
        print("-----------")
        result = str(bin(int("1", 2) + int(result[1:], 2)))[2:]
        frames[i] = ((len(frames[0]) - len(result)) * "0") + result
        print(" ", frames[i])
        print()
    return ((len(frames[0]) - len(result)) * "0") + result


print("\n--Enter sender frames(assuming all frames are received)--\n")
n = int(input("Enter no. of frames:"))
inputEl(n, s)
Ssum = calculate(s)
checksum = "".join([str(int(not int(bit))) for bit in Ssum])
print("Sender chechsum is:", checksum)

print("\n--Enter receiver frames details--\n")
inputEl(n, r)
Rsum = calculate(r)
print("Final checksum calculation:")
print(" ", checksum)
print("+", Rsum)
print("-----------")
final = str(bin(int(checksum, 2) + int(Rsum, 2)))[2:]
print(" ", final)
validate = "".join([str(int(not int(bit))) for bit in final])
print("Receiver checksum is:", validate)

if "1" in validate:
  print("\nError detected")
else:
  print("\nNo error detected")
