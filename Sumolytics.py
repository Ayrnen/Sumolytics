# Wrestler class
class Rikishi:
    # Static variable counting all created Rikishi
    count = 0
    # Name, Letter Rank, Maegashira Number, East/West, Country of Origin
    def __init__(self, name, rank, number, cardinal, nationality):
        self.name = name
        self.rank = rank
        self.number = number,
        self.cardinal = cardinal
        self.nationality = nationality
        self.division = 'Makuuchi'
        self.wins = 0
        self.losses = 0
    # Every time new Rikishi is initialized the static variable count +=1
        Rikishi.count += 1
    # Don't know why this is static but that's what they used in StackOverflow
    @staticmethod
    def getCount():
        return Rikishi.count
    # Takes W/L and increases wins or losses variables accordinly
    def record(result):
        if upper(self, result) == 'W':
            self.wins +=1
        if upper(result) == 'L':
            self.losses +=1

    def getName(self):
        return self.name

# Test for my Rikishi static variable "count" - IT WORKS
# a = Rikishi('Takakeisho', 'Ozeki', 'N/A', 'West', 'Japan')
# print(a.getCount())
# b = Rikishi('Shoudai', 'Ozeki', 'N/A', 'West', 'Japan')
# print(b.getCount())
# print(a.getCount())
# print(Rikishi.getCount())

# Tournament Class
class Honbasho:
    # First day of tournament, city, stadium name
    def __init__(self, date, city, stadium):
        self.startDate = date
        self.city = city
        self.stadium = stadium
        # list of dayMatches (nested list) - should have a length of 15
        self.allMatches = []
        # list of Shiai classes to be stored into all matches and then reset
        self.dayMatches = []
        # tracks day of tournament and increments accordingly - might place a cap of 15
        self.day = 0

        # create dataframe and default values for tournament value

    # Function allowing for a more abstract creation of Shiais
    def newMatch(self, high, low, winner, technique, seconds, monoii, controversial):
        self.dayMatches.append(Shiai(tournament, high, low, winner, technique, seconds, monoii, controversial))

    # To be run at the end of each day, priming class for next day
    def endDay(self):
        self.allMatches.insert(day, dayMatches)
        self.dayMatches = []
        self.day +=1
        if self.day > 15:
            endHonBasho()
    def endHonBasho():
        pass
        # save everything from shiai into new DataFrame
        # append DataFrame to csv file and save csv file
        # save rikishi wins/losses into dataFrame
        # reset rikishi wins/losses to 0


# Match Class
class Shiai:
    #leftmost wrestler, rightmost wrestler, winner's name, match length, controversial result?, judge intervention?
    def __init__(self, left, right, winner, technique, seconds, controversial = False, monoii = False):
        self.high = left
        self.low = right
        self.winner = winner
        self.technique = technique
        self.length = seconds
        self.controversial = controversial
        self.monoii = monoii
        self.rematch = False
        self.same = False

    # more abstraction
    def __swap(self):
        holder = self.high
        self.high = self.low
        self.low = holder

    # probably useless function but this will make sure that the higher ranked wrestler always has the "higher / leftmost" position
    # if they are the same rank this will not change the order
    def order(self):
        if self.high.getNumber() < self.low.getNumber():
            pass
        elif self.high.getNumber() > self.low.getNumber():
            self.__swap()

        elif self.high.getNumber() == self.low.getNumber():
            if self.high.getRank() == self.low.getRank():
                if self.high.getCardinal() == self.low.getCardinal():
                    self.same = True
                elif self.high.getCardinal() == 'E':
                    pass
                else:
                    self.__swap()


            elif self.high.getRank() == 'Y':
                pass
            elif self.high.getRank() == 'K':
                pass

            elif self.high.getRank() == 'O':
                if self.low.getRank() == 'Y':
                    swap()
                else:
                    pass

            elif self.high.getRank() == 'S':
                if self.low.getRank() == 'Y' or self.low.getRank() == 'O':
                    self.__swap()
                else:
                    pass


### Skip first line
### Turn abbreviations to full words

# Rikishi text file Reader
def RikishiReader():
    import pandas as pd
    df = pd.read_csv(r'C:\Users\Aymen\Desktop\Sumolytics\RikishiSample.txt')

    # Make names title case
    df['name'] = df['name'].str.title()

    # Show full rank name
    df.loc[df['rank'] == 'M', 'rank'] = 'Maegashira'
    df.loc[df['rank'] == 'K', 'rank'] = 'Komusubi'
    df.loc[df['rank'] == 'S', 'rank'] = 'Sekiwake'
    df.loc[df['rank'] == 'O', 'rank'] = 'Ozeki'
    df.loc[df['rank'] == 'Y', 'rank'] = 'Yokozuna'

    # Show full cardinal name
    df.loc[df['cardinal'] == 'E', 'cardinal'] = 'East'
    df.loc[df['cardinal'] == 'W', 'cardinal'] = 'West'

    # Show full nationality name
    df.loc[df['nationality'] == 'JP', 'nationality'] = 'Japan'
    df.loc[df['nationality'] == 'MN', 'nationality'] = 'Mongolia'
    df.loc[df['nationality'] == 'BG', 'nationality'] = 'Bulgaria'
    df.loc[df['nationality'] == 'BR', 'nationality'] = 'Brazil'
    df.loc[df['nationality'] == 'GE', 'nationality'] = 'Georgia'

    # Make column names title case
    df.columns = df.columns.str.title()

    # print(df)
    return df
def RikishiInit(df):
    rikishis = []
    for name in df['Name']:
        rikishis.append(Rikishi(
        df.loc[df['Name'] == name, 'Name'],
        df.loc[df['Name'] == name, 'Rank'],
        df.loc[df['Name'] == name, 'Number'],
        df.loc[df['Name'] == name, 'Cardinal'],
        df.loc[df['Name'] == name, 'Nationality'])
        )

df = RikishiReader()
RikishiInit(df)

# Tourament text file reader
def HonbashoReader():
    import pandas as pd
    from datetime import datetime

    df = pd.read_csv(r'C:\Users\Aymen\Desktop\Sumolytics\TournamentSample.txt')
    df['date'][0] = datetime.strptime(str(df['date'][0]), "%d/%m/%y")

    df['city'] = df['city'].str.title()
    df['stadium'] = df['stadium'].str.title()
    df.columns =  df.columns.str.title()

    print(df)
    return df
# df = HonbashoReader()

# Match text file reader
def ShiaiReader():
    import pandas as pd
    df = pd.read_csv(r'C:\Users\Aymen\Desktop\Sumolytics\MatchSample.txt')

    df['left'] = df['left'].str.title()
    df['right'] = df['right'].str.title()
    df['winner'] = df['winner'].str.title()
    df['technique'] = df['technique'].str.title()
    df.columns= df.columns.str.title()

    print(df)
    return df
# df = ShiaiReader()
