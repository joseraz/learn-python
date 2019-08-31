print(" Hi, this is a tracker for you body status. ")

x = int(input(" Number of times you have thought about your body: "))
y = int(input(" Number of times you have gone out for a run: "))

def adonis():
    z = y - x
    print(f"\t {z}")
    print(" When this numer is positive you will feel better.")

adonis()
