MAXDOTS = 50
MINDOTS = 1

dotschar = "."
endstring = "|"


def moreStars():
    looping = MINDOTS
    for x in range(MINDOTS, MAXDOTS):
        print(dotschar * x + endstring)
        looping += 1


def lessStars():
    stars = MAXDOTS
    for x in range(MINDOTS, MAXDOTS):
        if stars >= MINDOTS:
            stars -= 1
            print(dotschar * stars + endstring)


moreStars()
lessStars()
