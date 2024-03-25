print("Check sum calcuator")
n = int(input("Enter no. of frames:"))
l = []
sum = ""
for i in range(n):
  l.append(input(f"Enter frame {i+1}:"))
if n<=0:
  print("No frames to check")
elif n==1:
  checksum = "".join([str(int(not int(bit))) for bit in l[0]])
  print("Check sum:", checksum)
else:
  for i in range(1, n):
    print(" ", l[i - 1])
    print("+", l[i])
    print("-----------")
    sum = str(bin(int(l[i - 1], 2) + int(l[i], 2)))[2:]
    l[i] = ((len(l[0])-len(sum))*"0")+sum
    print(" ", sum)
    print()
  
    if len(str(l[0])) < len(str(sum)):
      print(" ", sum[1:])
      print("+", (len(str(l[i])) - 3) * " ", "1")
      print("-----------")
      sum = str(bin(int("1", 2) + int(sum[1:], 2)))[2:]
      l[i] = ((len(l[0])-len(sum))*"0")+sum
      print(" ", sum)
      print()
  checksum=((len(l[0])-len(sum))*"0")+sum
  checksum = "".join([str(int(not int(bit))) for bit in checksum])
  print("Check sum:", checksum)
print("Receiver code : ")
