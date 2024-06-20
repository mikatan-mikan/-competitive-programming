n = int(input())

st = set()

ans = 0

for i in range(n):
    tmp = input()
    r_tmp = tmp[::-1]
    if tmp not in st and r_tmp not in st:
        ans += 1
    st.add(tmp)
    st.add(r_tmp)

print(ans)