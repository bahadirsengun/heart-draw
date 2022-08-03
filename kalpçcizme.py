import turtle as ciz

def cizim(kalp, kalem, arkaplan):
    ciz.bgcolor(arkaplan)
    ciz.pensize(1)

    def curve():
        for i in range(200):
            ciz.right(1)
            ciz.forward(1)

    ciz.speed(0)
    ciz.color(kalem, kalp)

    ciz.begin_fill()
    ciz.left(140)
    ciz.forward(111.65)
    curve()

    ciz.left(120)
    curve()
    ciz.forward(111.65)
    ciz.end_fill()
    ciz.hideturtle()
    ciz.done()

while True:
    secin = input("İstediğiniz Renkte Kalp Çizdirmek İçin--1 \n"
                  "Çıkış Yapmak İçin ise--q \n"
                  "Seçiminizi Yapınız = ")
    if secin.lower() == "q":
        break
    elif secin == "1":
        kalp = input("\n Kalbin Rengini Giriniz : ")
        kalem = input("Kalemin Rengini Giriniz : ")
        arkaplan = input("Arka Plan TRengini Belirkleyiniz : ")

        try:
            cizim(kalp, kalem, arkaplan)1
                        print("\n---------\n")
        except:
            print("}n-----Düzgün Bir Renk Kombinasyonu Giriniz-----\n")
    else:
        print("\n -----Düzgün Bir Seçim Yapnızız----- \n")
