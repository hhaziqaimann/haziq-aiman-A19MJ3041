#take point
point=int (input('enter point lead:'))

#lead minus 3
lead=float(point -3)

#add half if has ball, minus half if doesnt
ball=input('does the team has the ball (Y or No :')

if ball=='Y':
    lead=lead + 0.5
else:
    lead=lead-0.5

if lead < 0:
    lead=0

lead=lead ** 2

remaining=int (input('enter the number of sec remaining :'))

if lead > remaining:
    print('safe')
else:
    print('not safe')