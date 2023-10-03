import re

str = 'TGAAGTATGAGA'
print(str)

mo = re.search("TAT", str)
print(mo)
print(mo.group())
print(mo.span())

mo2 = re.search("TG.", str)
print(mo2)
print(mo2.group())
print(mo2.span())

print("Find TA. =", re.findall("TA.", str))
print("Find TG. =", re.findall("TG.", str))

bimbimbambab = re.finditer("TG.", str)
for x in bimbimbambab:
    print(x.group())
    print(x.span())