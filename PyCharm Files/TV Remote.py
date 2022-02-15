import time
import random


class TV_Remote():
    def __init__(self, TV_Status = "Off", Volume = "50", Channel_List = "Sony SAB", Channel_Name = "Sony SAB"):
        print("Creating the Remote...")
        time.sleep((2))

        self.TV_Status = TV_Status
        self.Volume = Volume
        self.Channel_List = Channel_List
        self.Channel_Name = Channel_Name
    def TV_ON(self):

        if self.TV_Status == "ON":
            print("TV is already on")

        else:
            print("TV is turning ON...")
            time.sleep((1))
            print("TV is turned ON")
            self.TV_Status = "ON"

    def TV_OFF(self):

        if self.TV_Status == "ON":
            print("Tv is already OFF...")

        else:
            print("TV is turning off...")
            time.sleep((1))
            print("TV is turned off...")


    def Volume(self):


        while True:

            answer = input("For increasing the volume Type : '-' \nFor Decreasing the volume type: '+' \nFor exit type : 'Exit'...")


            if answer == "-":

                if self.Volume != 0:
                 self.Volume -= 1
                print("Volume: ", self.Volume)


            elif answer == "+":

                 if self.Volume != 100:
                  self.Volume += 1
                  print("Volume: ", self.Volume)


            else:
                print("Volume is adjusted...")


    def Add_Channel(self,Channel_Name):

        print("Adding Channel...")
        time.sleep((2))

        self.Channel_List.append(Channel_Name)
        print("Channel added..")

    def Random_Channel(self):

        Random = random.randint(0,len(self.Channel_List)-1)

        self.Channel_Name = self.Channel_List[Random]

        print("You are watching now", self.Channel_Name)


    def __len__(self):
        return len(self.Channel_List)


    def __str__(self):
        return "TV status: {} \n TV Volume: {} \nChannel list: {} \nWatching Channel: {} ".format(self.TV_Status,self.Volume,self.Channel_List,self.Channel_Name)

Remote_1 = TV_Remote()



print("""

1.Turn On The TV
2.Turn Off The Tv
3.Adjust Volume Channel
4.Add Channel
5.Open Random
6. Quit

""")

while True:

    Answer_1 = int(input("Pls enter the no. here "))


     if Answer_1 == 1:
         Remote_1.TV_ON()

     elif Answer_1 == 2:
          Remote_1.TV_OFF()

     elif Answer_1 == 3:
        Remote_1.Volume()























