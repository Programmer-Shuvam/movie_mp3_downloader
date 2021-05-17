pi = 'Global pi'


def outer():
	# global pi
    pi = "outer pi"

    def inner():

        # global pi
pi = 'inner pi'
        print(pi)

    inner()
	print(pi)


outer()
print(pi)

def len(a):

print('This is user defined', a)

len(pi)
