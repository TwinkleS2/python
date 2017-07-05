import turtle

t = turtle.Pen()
t.shape("turtle")

reptilia = ['turtle','crocodile','iguana','chamelon']

if 'turtle' in reptilia:
	t.color('red')
	t.forward(100)

if 'lion' not in reptilia:
	t.color('yellow')
	t.forward(100)

turtle.done()

