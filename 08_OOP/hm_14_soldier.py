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


ak47 = Gun("Ak47")
ak47.add_bullet(50)
ak47.shoot()


