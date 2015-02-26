# asteroidFactory
import pygame, random

asteroid_1 = pygame.image.load("img/asteroid1.bmp")
asteroid1_frames = 19
asteroid_2 = pygame.image.load("img/asteroid3.bmp")
asteroid2_frames = 20
asteroid_3 = pygame.image.load("img/asteroid4.bmp")
asteroid3_frames = 20
asteroid_4 = pygame.image.load("img/asteroid5.bmp")
asteroid4_frames = 20
asteroid_5 = pygame.image.load("img/asteroid6.bmp")
asteroid5_frames = 20
asteroid_6 = pygame.image.load("img/asteroid7.bmp")
asteroid6_frames = 20
asteroid_7 = pygame.image.load("img/asteroid8.bmp")
asteroid7_frames = 25
	
class AsteroidFactory:
	def __init__(self):
		## variables declared here are unique to each instance
		
		self.size = 50
		self.MAX_SPEED = 5
		self.MIN_SPEED = 2

		self.counter = 0

		# whenever counter => spawnrate a new asteroid is made
		self.frameBetweenSpawns = 40

		self.asteroids = []

		# how many points to give the player when an asteroid
		# leaves the screen
		self.reward = 10
		# how much to hurt the player if they hit the asteroid
		self.damage = 20

	def spawn(self, width, image_index):
		self.counter += 1
		
		asteroid = {
		0: asteroid_1,
		1: asteroid_2,
		2: asteroid_3,
		3: asteroid_4,
		4: asteroid_5,
		5: asteroid_6,
		6: asteroid_7,
		}.get(image_index, 0)
		asteroid_frames = {
		0: asteroid1_frames,
		1: asteroid2_frames,
		2: asteroid3_frames,
		3: asteroid4_frames,
		4: asteroid5_frames,
		5: asteroid6_frames,
		6: asteroid7_frames,
		}.get(image_index, 0)
		
		if self.counter >= self.frameBetweenSpawns:
			self.asteroids.append({ 'frame': 0,
						'rect': pygame.Rect(random.randint(0, width - self.size), 0 - self.size, self.size, self.size),
						'speed': random.randint(self.MIN_SPEED, self.MAX_SPEED),
						'surface':pygame.transform.scale(asteroid, (asteroid.get_rect().width*asteroid_frames, asteroid.get_rect().height)),
						'health': 100
						})
			self.counter = 0


	def remove(self, height):
		asteroidsRemoved = 0

		for a in self.asteroids[:]:
			if a['rect'].top > height:
				self.asteroids.remove(a)
				# get points for dodging asteroids
				asteroidsRemoved += 1
			elif a['health'] <= 0:
				# no points for shooting asteroids
				self.asteroids.remove(a)

		return self.reward * asteroidsRemoved

	def move(self):
		for a in self.asteroids:
			a['rect'].move_ip(0, a['speed'])

	def draw(self, target):
		for a in self.asteroids:
			target.blit(a['surface'], a['rect'], pygame.Rect((a['frame']*(a['surface'].get_width()/self.size)),0,a['surface'].get_width()*2/self.size,a['surface'].get_height()))

	def collide_bullets(self, bullets):
		for a in self.asteroids:
			for b in bullets:
				if (b['rect']).colliderect(a['rect']):
					bullets.remove(b)
					a['health'] -= 10

	def collide_player(self, playerRect, playerHealth):
		for a in self.asteroids:
			if playerRect.colliderect(a['rect']):
				self.asteroids.remove(a)
				return playerHealth - self.damage
		return playerHealth

	def remove_all(self):
		for a in self.asteroids:
			self.asteroids.remove(a)
		self.asteroids = []
