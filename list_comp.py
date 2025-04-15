import random

# list_1 = []
# for i in range(1,11):
#     for a in range(1,11):
#         bob = random.randint(1,100)
#         if bob%2 == 0:
#             list_1.append(bob**2)
#             a = a+1
# print(list_1)
# list_2 = []
# for b in range(1,11):
#     list_2 = [random.randint(1,100)**2 for c in range(1,11)]
#     print(list_2)
# list_3 = []
# list_3 = [c**2 for c in [random.randint(1,100) for d in range(1,6)] if c%2==1]
# print(list_3)

[print([c**2 for c in [random.randint(1, 100) for _ in range(1, 6)] if c % 2 == 0]) for _ in range(1, 11)]
