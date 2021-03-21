alien_0 = {
    'color': 'green',
    'points': 10,
    'x_pos': 0,
    'y_pos': 25,
    'speed': 'medium'
}

print(alien_0)
print(f"Current position: {alien_0['x_pos']}, {alien_0['y_pos']}")

alien_0['color'] = 'red'
alien_0['points'] = 0

if alien_0['speed'] == 'slow':
    x_increment = 1
    y_increment = 2
elif alien_0['speed'] == 'medium':
    x_increment = 5
    y_increment = 10    
else:
    x_increment = 10
    y_increment = 22

alien_0['x_pos'] = alien_0['x_pos'] + x_increment
alien_0['y_pos'] = alien_0['y_pos'] + y_increment

print(f"New position: {alien_0['x_pos']}, {alien_0['y_pos']}")