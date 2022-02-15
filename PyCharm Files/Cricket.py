with open("Cricket_Rcb.txt", "r") as Cricket_Rcb:
    Wicket_Keeper = list()
    Batsmen = list()
    Bowler = list()

    for row in Cricket_Rcb:
        row = row[:-1]
        row_Elements = row.split(",")

        if row_Elements[1] == "Wicket_Keeper":
            Wicket_Keeper.append(row + "\n")

        elif row_Elements[1] == "Batsmen":
            Batsmen.append(row + "\n")

        else:
            Bowler.append(row + "\n")

        with open("Wicket_Keeper.txt","w") as Wicket_Keeper_F:
            for i in Wicket_Keeper:
                Wicket_Keeper_F.write(i)

        with open("Batsmen.txt","w") as Batsmen_F:
            for i in Batsmen:
                Batsmen_F.write(i)

        with open("Bowler","w") as Bowler_F:
            for i in Bowler:
                Bowler_F.write(i)
