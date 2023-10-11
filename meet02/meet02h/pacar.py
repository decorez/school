class Pacar:

    def __init__(self, nama, umur, kelamin):
        
        self.nama = nama
        self.kelamin = kelamin
        self.umur = umur

    def menyapa(self):

        print(f'Hai, nama saya {self.nama} umur saya {self.umur} saya seorang {self.kelamin}')

    def bernyanyi(self, title='my heart will go on'):
        print(f'saya akan bernanyi bersama kamu lagunya {title}')

    def mengagumi(self, type='ganteng'):
        print(f'saya mengakui bahwa kamu {type}')

pacar_pertama_oscar = Pacar('cindi', '9', 'wanita')
pacar_kedua_oscar = Pacar('stela', '10', 'wanita')
pacar_ketiga_oscar = Pacar('fikri', '21', 'pria')

pacar_pertama_oscar.menyapa()
pacar_pertama_oscar.bernyanyi()
pacar_pertama_oscar.mengagumi()
pacar_kedua_oscar.menyapa()
pacar_pertama_oscar.bernyanyi('indonesia raya')
pacar_ketiga_oscar.menyapa()
pacar_kedua_oscar.mengagumi('keren')
pacar_pertama_oscar.bernyanyi('garuda pancasila')
pacar_ketiga_oscar.mengagumi('pemberani')