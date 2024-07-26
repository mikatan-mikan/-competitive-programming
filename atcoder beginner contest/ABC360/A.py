s = input()

m_ = s.find("M")
r_ = s.find("R")

if r_ < m_:
    print("Yes")
else:
    print("No")