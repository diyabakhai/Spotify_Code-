class Songs:
    flag = 0
    soulful, acoustic, workout, party,Artist1,Artist2,Artist3,Artist4 = [], [], [], [], [], [], [], []
    create_playlist=[]
    pole = 0

    def hindi(self):
        print("Enter the genre\n")
        a = int(input("1.Soulful \n2.Acoustic \n3.Workout \n4.Party \n"))
        if a == 1:
            self.soulful = ['Shayad', 'Dil Na Jaaneya', 'Thoda Thoda Pyaar ', 'Hawaayein', 'Bhula Dunga',
                       'Tune jo Na kaha', 'Kaise Bataoon ', 'Mere Bina', 'Tum hi ho', 'Humdard']
            for i in range(len(self.soulful)):
                print(f"{i}. {self.soulful[i]}")
            self.Artist1 = ['Arijit Singh', 'Rochak Kohli', 'Stebin Ben', 'Arijit Singh', 'Darshan Raval',
                       'Mohit Chauhan', 'Atif Aslam', 'Nikhil DSouza', 'Arijit Singh', 'Arijit Singh']
            self.flag = 1
            self.pole = 1
            self.options()
        elif a == 2:
            self.acoustic = ['Tum Se Hi(Reprise)', 'Bin Tere', 'Meri Tum Ho', 'Kabira(Encore)', 'Jeena Jeena',
                        'Sham', 'Iktaara', 'Channa Mereya', 'Tujh Ko Jo Paaya', 'Dancing in The Sun']
            for i in range(len(self.acoustic)):
                print(f"{i}. {self.acoustic[i]}")
            self.Artist2 = ['Ankit Tiwari & Alia Bhatt', 'Armaan Malik', 'Pritam', 'Pritam', 'Atif Aslam',
                       'Amit Trivedi & Nikhil DSouza', 'Amit Trivedi', 'Pritam and Arjit Singh', 'Pritam and Mohit Chauhan', 'Sharvi Yadav']
            self.flag = 2
            self.pole = 2
            self.options()
        elif a == 3:
            self.workout = ['Apna Time Aayega', 'Bang Bang', 'Rock on', 'Bhaag Milka Bhaag',
                       'Shor Machega', 'Ud-daa Punjab', 'Parinda', 'Besabriya', 'Sadda Hak', 'Ziddi Dil']
            for i in range(len(self.workout)):
                print(f"{i}. {self.workout[i]}")
            self.Artist3 = ['Ranveer Singh & DIVINE', 'Neeti Mohan & Benny Dayal', 'Farhan Akhtar', 'Siddharth Mahadevan',
                       'Honey Singh', 'Amit Trivedi & Vishal Dadlani', 'Saina', 'Armaan Malik', 'Mohit Chauhan', 'Vishal Dadlani']
            self.flag = 3
            self.pole = 3
            self.options()
        elif a == 4:
            self.party = ['Kar Gayi Chull', 'Coca Cola', 'Prada', 'Badtameez Dil', 'Tareefan',
                     'The Disco Song', 'Nachde Ne Saare', 'Saturday Saturday', 'Befikra', 'Illegal Weapon']
            for i in range(len(self.party)):
                print(f"{i}. {self.party[i]}")
            self.Artist4 = ['Badshah & Amaal Malik', 'Tony & Neha Kakkar', 'The Doorbean & Shreya Sharma', 'Pritam, Benny Dayal & Shefali Alvares',
                       'Badshah & QARAN', 'Vishal-Shekhar & Benny Dayal', 'Jaleen Royal & Harshdeep Kaur', 'Badshah', 'Meet Bros & Aditi Singh Sharma', 'Garry Sandhu ']
            self.flag = 4
            self.pole= 4
            self.options()
        else:
            print("Invalid Input. Run Again!")
            self.hindi()

    def createPlaylist(self):
        cp1 = int(input("Enter the Song to be added in customized Playlist\n"))
        if self.flag == 1:
            self.create_playlist.append(self.soulful[cp1])
            opt = int(input("\n1: Continue to add Songs\n2: Display Playlist and exit\n"))
            if opt == 1:
                self.hindi()
            elif opt == 2:
                self.printplaylist()
        elif self.flag == 2:
            self.create_playlist.append(self.acoustic[cp1])
            opt = int(input("\n1: Continue to add Songs\n2: Display Playlist and exit\n"))
            if opt == 1:
                self.hindi()
            elif opt == 2:
                self.printplaylist()
        elif self.flag == 3:
            self.create_playlist.append(self.workout[cp1])
            opt = int(input("\n1: Continue to add Songs\n2: Display Playlist and exit\n"))
            if opt == 1:
                self.hindi()
            elif opt == 2:
                self.printplaylist()
        elif self.flag == 4:
            self.create_playlist.append(self.party[cp1])
            opt = int(input("\n1: Continue to add Songs\n2: Display Playlist and exit\n"))
            if opt == 1:
                self.hindi()
            elif opt == 2:
                self.printplaylist()
    def printplaylist(self):
        print("The Songs in Your playlist are:-")
        for i in range(len(self.create_playlist)):
            print(f'{i}. {self.create_playlist[i]}')    
    def dispArtist(self):
        b = int(input("Enter the song of your choice\n"))
        if self.pole==1:
            print(f"Name: {self.soulful[b]}\nArtist: {self.Artist1[b]}\n")
        elif self.pole==2:
            print(f"Name: {self.acoustic[b]}\nArtist: {self.Artist2[b]}\n")
        elif self.pole==3:
            print(f"Name: {self.workout[b]}\nArtist: {self.Artist3[b]}\n")
        elif self.pole==4:
            print(f"Name: {self.party[b]}\nArtist: {self.Artist4[b]}\n")
        self.options()
    def options(self):
        x=int(input("Select 1: View Artist\n2: Create Playlist "))
        if x==1:
            self.dispArtist()
        elif x==2:
            self.createPlaylist()

    def english(self):
        print("Enter the genre\n")
        m = int(input("1.Soulful \n2.Acoustic \n3.Workout \n4.Party\n")) 
        if m == 1:
            self.soulful1 = ['Willow', 'Lover', 'Modern loneliness', 'Who', 'Dusk till Dawn', 'As you Are','Soon You will Get Better', 'Tightrope', 'betty', 'All of Me']
            for j in range(len(self.soulful1)): print(f"{j}. {self.soulful1[j]}")
            self.ArtistE1 = ['Taylor Swift','Taylor Swift', 'Lauv', 'Lauv', 'Zayn Malik Ft. Sia', 'The Weekend', 'Taylor Swift', 'Zayn Malik','Taylor Swift','John Legend']
            self.flag = 5
            self.pole = 5 
            self.options()
        elif m == 2:
            self.acoustic1 = ['Death By A Thousand Cuts', 'I Dont Wanna Live', 'Trampoline', 'tRuTh', 'Afterglow','Let her Go', 'The Heart of Life', 'You are the reason','She will be Loved', 'Photograph']
            for j in range(len(self.acoustic1)): print(f"{j}. {self.acoustic1[j]}")
            self.ArtistE2 = ['Taylor Swift', 'Zayn Malik', 'Zayn Malik', 'Taylor Swift','Ed Sheeran', 'Passenger','John Mayer', 'Leona Lewis', 'Maroon 5', 'Ed Sheeran' ]
            self.flag = 6
            self.pole = 6 
            self.options()
        elif m == 3:
            self.workout1 = ['Like I would', 'Are you ready for it', 'Bad Blood', 'Party Monster','I dont care', 'My Oh My','Raising Hell','Blood, Sweat & Tears','Don’t Stop the Music','Mic Drop (Steve Aoki Remix)' ]
            for j in range(len(self.workout1)): print(f"{j}. {self.workout1[j]}")
            self.ArtistE3 = ['Zayn Malik', 'Taylor Swift','Taylor Swift', 'The Weekend','Ed Sheeran Ft. Justin Bieber','Camilla Cabello Ft. Da Baby','Kesha feat. Big Freedia','Ava Max','Rihanna','BTS' ]
            self.flag = 7
            self.pole = 7 
            self.options()
        elif m == 4:
            self.party1 = ['Blinding Lights', 'Starboy', '22', 'ME!', 'We Are Never Getting Back Together', 'Shake It Off','Cheap Thrills', 'I Wanna Dance with Somebody','We Found Love','Billie Jean']
            for j in range(len(self.party1)): print(f"{j}. {self.party1[j]}")
            self.ArtistE4 = ['The Weekend', 'The Weekend', 'Taylor Swift', 'Taylor Swift','Taylor Swift','Taylor Swift','Sia','Whitney Houston','Rihanna','Michael Jackson']
            self.flag = 8
            self.pole = 8 
            self.options()
        else:
            print("Invalid Input. Run Again!") 
            self.english()

    def options(self):
        x=int(input("Select \n1: View Artist\n2: Create Playlist\n "))
        if x==1:
            self.dispArtist() 
        elif x==2:
            self.createPlaylist() 
        else:
            print("Invalid Input. Run Again!") 
            self.options()


if __name__ == '__main__':
    song = Songs()
    mopt=int(input("1: Hindi Songs\n2: English Songs"))
    if mopt==1:
        song.hindi()
    if mopt==2:
        song.english()