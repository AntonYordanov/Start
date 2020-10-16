total_steps = 0
steps_home = 0

while total_steps < 10000:
    line = input()

    if line == 'Going home':
        steps_home = int(input())
        total_steps += steps_home
        break
    else:
        additional_steps = int(line)
        total_steps += additional_steps

steps_difference = total_steps - 10000

if total_steps >= 10000:
    print(f'Goal reached! Good job!')
    print(f'{steps_difference} steps over the goal!')
else:
    print(f'{abs(steps_difference)} more steps to reach goal.')