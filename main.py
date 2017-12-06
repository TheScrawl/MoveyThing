r4 = ['.','.','.','.','.']
r3 = ['.','.','.','.','.']
r2 = ['.','.','.','.','.']
r1 = ['.','.','.','.','.']
r0 = ['x','.','.','.','.']

rows = [r0, r1, r2, r3, r4]

playerX = 0
playerY = 0

print(r4)
print(r3)
print(r2)
print(r1)
print(r0)

def move():
	global playerX
	global playerY
	choice = input(str('> '))
	if choice == 'w':
		try:
			rows[playerY][playerX] = '.'
			playerY = playerY + 1
			rows[playerY][playerX] = 'x'
		except IndexError:
			playerY = 0
			rows[playerY][playerX] = 'x'

	if choice == 's':
		try:
			rows[playerY][playerX] = '.'
			playerY = playerY - 1
			rows[playerY][playerX] = 'x'
		except IndexError:
			playerY = 4
			rows[playerY][playerX] = 'x'

	if choice == 'a':
		try:
			rows[playerY][playerX] = '.'
			playerX = playerX - 1
			rows[playerY][playerX] = 'x'
		except IndexError:
			playerX = 4
			rows[playerY][playerX] = 'x'

	if choice == 'd':
		try:
			rows[playerY][playerX] = '.'
			playerX = playerX + 1
			rows[playerY][playerX] = 'x'
		except IndexError:
			playerX = 0
			rows[playerY][playerX] = 'x'

	print(r4)
	print(r3)
	print(r2)
	print(r1)
	print(r0)
	move()
move()

