# Вариант 1
def knapsack(C, weight, cost, n):
    K = [[0 for x in range(C + 1)] for x in range(n + 1)]
    for i in range(n + 1):
        for w in range(C + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif weight[i - 1] <= w:
                K[i][w] = max(cost[i - 1][0] + K[i - 1][w - weight[i - 1]], K[i - 1][w])
            else:
                K[i][w] = K[i - 1][w]
    return K


items = {'в': (3, 25),
         'п': (2, 15),
         'б': (2, 15),
         'а': (2, 20),
         'и': (1, 5),
         'н': (1, 15),
         'т': (3, 20),
         'о': (1, 25),
         'ф': (1, 15),
         'д': (1, 10),
         'к': (2, 20),
         'р': (2, 20)
         }

backpack = {}

Y = []
X = []
for key in items:
    Y.append([items[key][1], key])
    X.append(items[key][0])

C = 8
n = len(Y)
K = knapsack(C, X, Y, n)

w, i, all_weight = C, n, 0
res = K[n][C]
while i > 0 and res > 0:
    if res != K[i - 1][w]:
        backpack[Y[i - 1][1]] = [Y[i - 1][0], X[i - 1]]
        items.pop(Y[i - 1][1])
        all_weight += X[i - 1]
        res -= Y[i - 1][0]
        w -= X[i - 1]
    i -= 1

L = 0
for key in backpack:
    for k in range(backpack[key][1]):
        if L == 2:
            print("\b\b")
            L = 0
        print(key, end=', ')
        L += 1

start = 15
s = 0
for key in items:
    s += items[key][1]

result = K[n][C] - s + start
print("Итоговые очки выживания: ", result)


