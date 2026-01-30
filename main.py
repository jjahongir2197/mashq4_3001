class Movie:
    def __init__(self, title, seats, price):
        self.title = title
        self.seats = seats
        self.price = price

    def sell_ticket(self, qty):
        if qty <= self.seats:
            self.seats -= qty
            return qty * self.price
        return 0


class Cinema:
    def __init__(self):
        self.movies = []
        self.cash = 0

    def add_movie(self, movie):
        self.movies.append(movie)

    def show_movies(self):
        for i, m in enumerate(self.movies):
            print(i, m.title, "| Joy:", m.seats)

    def sell(self, index, qty):
        cost = self.movies[index].sell_ticket(qty)
        if cost:
            self.cash += cost
            print("Chipta sotildi:", cost)
        else:
            print("Joy yetarli emas")

    def report(self):
        print("Daromad:", self.cash)


cinema = Cinema()

while True:
    print("\n1.Film 2.Sotish 3.Hisobot 0.Exit")
    c = input(">>> ")

    if c == "1":
        cinema.add_movie(Movie(input("Film: "), int(input("Joy: ")), int(input("Narx: "))))
    elif c == "2":
        cinema.sell(int(input("Index: ")), int(input("Soni: ")))
    elif c == "3":
        cinema.report()
    elif c == "0":
        break
