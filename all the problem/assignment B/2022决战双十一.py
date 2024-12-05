n, m = map(int, input().split())
sp = [[tuple(map(int, x.split(':'))) for x in input().split()] for _ in range(n)]
qx = [[tuple(map(int, x.split('-'))) for x in input().split()] for _ in range(m)]
loop = []


def nested_loops(n, current=0, res=None):
    if not res:
        res = ['']*n
    if current == n:
        loop.append(res.copy())
        return
    for s_p in sp[current]:
        res[current] = s_p
        nested_loops(n, current + 1, res)


nested_loops(n)
ans = float('inf')
for loo in loop:
    shop = [0]*m
    price = 0
    for lo in loo:
        price += lo[1]
        shop[lo[0]-1] += lo[1]
    price -= 50*(price//300)
    for i, pr in enumerate(shop):
        q_x = qx[i]
        q_x.sort(key=lambda x: -x[1])
        for q, x in q_x:
            if pr >= q:
                price -= x
                break
    ans = min(ans, price)
print(ans)
