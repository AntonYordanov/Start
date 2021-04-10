# from collections import deque
#
#
# def addition(n):
#     return str(n)
#
# first_line = input().split(', ')
# second_line = input().split(', ')
# dec = deque(first_line)
# decpower = deque(second_line)
# decpower.reverse()
#
# Palm = 0
# Crossett = 0
# Willow = 0
#
# while not(Palm>=3 and Willow>=3 and Crossett>=3) or len(dec)>0 or len(decpower)>0:
#     if len(dec)==0 or len(decpower)==0:
#         break
#     firework = int(dec.popleft())
#     power = int(decpower.popleft())
#     if firework<=0:
#         decpower.insert(0,str(power))
#         continue
#     if power<=0:
#         dec.insert(0, str(firework))
#         continue
#     check = firework + power
#     if check % 3 == 0 and check % 5 != 0:
#         Palm = Palm + 1
#     elif check % 5 == 0 and check % 3 != 0:
#         Willow = Willow + 1
#     elif check % 3 == 0 and check % 5 == 0:
#         Crossett = Crossett + 1
#     else:
#         firework=firework-1
#         if firework > 0:
#             dec.append(firework)
#         while not(Palm>=3 and Willow>=3 and Crossett>=3) or len(dec)>0 or len(decpower)>0:
#             firework = int(dec.popleft())
#             check = firework + power
#             if check % 3 == 0 and check % 5 != 0:
#                 Palm = Palm + 1
#                 break
#             elif check % 5 == 0 and check % 3 != 0:
#                 Willow = Willow + 1
#                 break
#             elif check % 3 == 0 and check % 5 == 0:
#                 Crossett = Crossett + 1
#                 break
#             else:
#                 firework = firework - 1
#                 if firework>0:
#                     dec.append(firework)
#
# if Palm>=3 and Willow>=3 and Crossett>=3:
#     print('Congrats! You made the perfect firework show!')
# else:
#     print('Sorry. You can’t make the perfect firework show.')
# if len(dec)>0:
#     any=dec[0]
#     if len(dec)>1:
#         listm = list(dec)
#
#         any=', '.join(map(addition,listm))
#     print(f'Firework Effect left: {any}')
# if len(decpower)>0:
#     any=decpower[0]
#     if len(decpower)>1:
#         decpower.reverse()
#         listm=list(decpower)
#
#         any=', '.join(map(addition,listm))
#     print(f'Explosive Power left: {any}')
#
# print(f'Palm Fireworks: {Palm}')
# print(f'Willow Fireworks: {Willow}')
# print(f'Crossette Fireworks: {Crossett}')

from collections import deque


def stock_availability(invlist: list,typed:str,*params):
    if typed=='delivery':
        for x in params:
            invlist.append(x)
    elif typed=='sell':
        if len(params)==0:
            invlist.pop(0)
        for x in params:
            if str(x).isnumeric():
                del invlist[:x]
            else:
                invlist= list(filter(lambda y: y != x,invlist))
    return invlist

