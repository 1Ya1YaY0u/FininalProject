import malware
import psutil


# status = malware.Malware().main()
# print(status)
pids = psutil.pids()
pname = []
for pid in pids:
    ps = psutil.Process(pid)
    pname.append(ps.name())
# print(ps)
# print(ps.name())
# input()
# print(pname)
# if psutil.Process().name() in pname:
if pname.count(psutil.Process().name()) > 1:
    print(pname.count(psutil.Process().name()))
    print("0")
else:
    print("1")
input()
