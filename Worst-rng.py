import random as ran

Aura = [
    'Cool',
    'Wow',
    'Great',
    'Founded',
    'StarCommon',
    'starrare'
]
print('-----------------------------------')
print('Worst-rng')
print('Present By Gemcast [Gemcast Copyright]')
print('Update[Game is On website!]')
print('type w to random')
print('-----------------------------------')
while True :
    a = input('>>>')
    if a == "w":
       print(ran.choice(Aura))
    else:
        print('[Error]:Wrong Type must be lowcase letter w')
