class Gun:

    def __init__(self, model):

        self.model = model
        self.bullet_cout = 0

    def add_bullet(self, count):

        self.bullet_cout += count

    def shoot(self):

        if self.bullet_cout <= 0:

            print("[%s] is empty..." % self.model)

            return

        self.bullet_cout -= 1

        print("[%s] shot...[%d]" % (self.model,self.bullet_cout))


class Soldier:

    def __init__(self, name):

        self.name = name
        self.gun = None

    def fire(self):

        if self.gun is None:

            print("[%s] doesn't have a gun..." % self.name)

            return

        print("ahahahahah")

        self.gun.add_bullet(50)

        self.gun.shoot()


ak47 = Gun("Ak47")

# ak47.add_bullet(50)
# ak47.shoot()

xusanduo = Soldier("xusanduo")
xusanduo.gun = ak47
xusanduo.fire()

print(xusanduo.gun)



