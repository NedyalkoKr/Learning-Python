from random import choice

aliens = []
colors = ['green', 'blue', 'red', 'yellow', 'pink', 'orange', 'purple', 'black', 'white']
blood = [i for i in range(1, 101)]
speed = ['slow', 'medium', 'fast', 'ultrafast']

# create 30 new aliens
for i in range(0, 30):
    new_alien = {
        # choose a random color, bools and speed for each alien
        'color': choice(colors),
        'blood': choice(blood),
        'speed': choice(speed),
    }
    aliens.append(new_alien)

for alien in aliens:
    print(alien)

for alien in aliens:
    if alien['color'] == 'green' and alien['speed'] == 'slow':
        alien['points'] += 10
        print(alien)

print(f"Total number of aliens: {len(aliens)}")