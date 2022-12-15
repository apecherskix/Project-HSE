import random
import time
class Duude:
    def __init__(self, name):
        print( 'Вы создали пацанчика!')
        self.name = name
        self.damage = 25
        self.maxhp = 150
        self.danger = 0
        self.money = 50
        self.energy=100
        self.hp = self.maxhp
        self.hard = 0
    def fight(self):
        d = random.randint(1, 5)
        if self.danger >= 2.5 and self.hp==self.maxhp and self.energy>=40:
             if self.damage>=d*(3+self.hard):
                print( self.name + " подрался на стрелке! Проверьте здоровье срочно, необходим смачный перекус!")
                self.hp -= (self.maxhp//6)*d
                self.money += random.randint(5, 15)
                self.danger = 0
                self.energy -= 40
                self.hard+=1
             else:
                print( "Братанчик, не повезло же тебе! Так поколотили, даже мать родная не узнает. Лучше повысь свой урон, слабых на районе не любят! И проверь статы, здоровье тебе смачно подпортили!")
                self.hp==d*self.maxhp//5
                self.money-=self.money//6*d
        else:
            print( "Пока нельзя драться! Но скоро будет стрелка, надо позависать на райончике. Увеличьте ваши статы!")

    def eat(self):
        if  self.hp > 2*self.maxhp//3 and self.hp <= self.maxhp:
            print( self.name + " сыт, лучше пойти на турнички!")
        elif self.hp <= (self.maxhp * 2/3) and self.money>=20:
            self.hp += self.maxhp//3
            print( "Шашлычок в желудке! " + self.name + " доволен и кайфует!")
            self.energy+=15
            self.money-=20
            if self.hp>self.maxhp:
                self.hp=self.maxhp
        else:
            print( "Поел бы, да за душой ни гроша. Порка бы как-нибудь подзаработать немного деньжат")

    def train(self):
        print( "Локация: Турнички. \nТут ,братки, собралась вся элита райончика. Нажмите: 1 - начать трешу; 2 - просто посмотреть")
        c=input()
        if c == '1':
            print( "Тренировка не бесплатная, необходимо 30 монет! У вас монет: ", self.money, "\nНажмите: 1 - заплатить; 2 - слиться")
            b=input()
            if b == '1' and self.money>=30 and self.energy>=30:
                self.money -= 30
                self.maxhp += 12
                self.damage += 5
                self.energy -= 30
                self.danger += 1.25
                print( "Вы получили +12 к hp(чтобы было максимальное здоровье, надо покушать или поспать) и +5 к урону")
            else:
                print( 'Да уж... Братки разочарованны в тебе. Повысь свои характеристики и перестань, наконец, жмотиться!')
        elif c == '2':
            print( "Вы посмотрели как тренируются крутые ребята района. Ваш урон повысился")
    def sleep(self):
        self.energy=100
        self.hp+=self.maxhp//3
        if self.hp>self.maxhp:
            self.hp=self.maxhp
        print('Ваш пацанчик успешно дрыхнет после тяжелого дня. Он проснется через 15 секунд')
        for i in range (1,5):
            time.sleep(3)
            print('спать осталось '+str(15-i*3)+' sec')
    def work(self):
        if  self.hp>=self.maxhp//3 and self.energy>=50:
            self.money+=25
            self.hp-=self.maxhp//3
            self.energy-=50
            print( "Ваш пацанчик успешно поработал на стройке и заработал 25 рублей. Ну а че, дома тоже кому-то надо строить. Проверьте статы, здоровье и энергия были понижены.")
    def condition(self):
        print( "Состояние вашего пацанчика!", "\nИмя - " + self.name + "\nМонеты ---> ", self.money, "\nЗдоровье --> ", self.hp,"\nУрон ---> ", self.damage, "\nУровень опасности ---> ", self.danger, '\nЭнергия ---> ', self.energy)
name = input('Введите имя пацанчика: ')
dude = Duude(name)
while True:
    print('Введите:\n1 - посмотреть характеристики пацанчика \n2 - пойти потренить \n3 - подраться \n4 - похавать \n5- пойти на стройку \n6-поспать часок-другой')
    a = input()
    if a == '1':
        dude.condition()
    elif a == '2':
        dude.train()
    elif a == '3':
        dude.fight()
    elif a == '4':
        dude.eat()
    elif a=='5':
        dude.work()
    elif a=='6':
        dude.sleep()
    else:
        break
