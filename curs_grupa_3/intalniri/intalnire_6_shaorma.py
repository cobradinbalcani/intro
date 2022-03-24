class Shaorma:
    tip = ['Lipie', 'Farfurie', 'In palma']
    legume = True
    sos1 = None
    carne = None
    cmd = None


    def __init__(self, cerere_tip, cerere_carne):
        if cerere_tip in self.tip:
            self.cmd = cerere_tip
        else:
            print('Avem alt model mai bun.')
        self.carne = cerere_carne

        if cerere_carne in self.carne:
            self.carne = cerere_carne
        else:
            print('nu avem')

    def adauga_sos(self, cerere_sos):
        self.sos1 = cerere_sos


client1 = Shaorma('Lipie', 'pui')
client2 = Shaorma('In palma', 'arici')
print(client1.cmd, client1.carne)
print(client2.cmd, client2.carne)
client1.adauga_sos('mustar')
print(client1.sos1)

client1.suc = 'fanta'
print(client1.suc)