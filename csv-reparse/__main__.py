import csv


# sorting class that reverses the order of a collection
class Reversor:
    def __init__(self, obj):
        self.obj = obj

    def __eq__(self, other):
        return other.obj == self.obj

    def __lt__(self, other):
        return other.obj < self.obj


emoji = """
anarchoCommunismFlag
flag_eo
queerAnarchyFlag
star33
starAngry
starAutismCreature
starAwkwardHeh
starAYAYARRR
starBlush
starBlushRelieved
starConfused
starCrazyEyes
starCry2
starCry3
starCry4
starCry5
starDespair
starEhehe
starEmpatheticHeart
starEnthusiasticThumbsUp
starEw
starExcited
starExcited2
starFemGothFingerguns
starGiggle
starGiggle2
starGiggle3
starGiggleCat
starGrin
starHanaBlank
starHappyHeart
starHappySmile
starHeadPat
starHiding
starHmm
starHugComfort
starHugLove
starHype
starHype2
starKittyAww
starLaugh
starLewd
starLove
starLove2
starMelt
starNoseBoop
starNotLikeThis
starNotLikeThis2
starOhISee
starOhoho
starOuchie
starPinkHeart
starPirate
starPlead
starPluralHeart
starPoke
starReceiveHeadpats
starReceiveHug
starRofl
starSad
starSad2
starSadBunny
starScream
starShock
starShrug
starShrug2
starShyHeart
starSigh
starSmile
starSmug
starSmug2
starSmug3
starSmug4
starSneaky
starSpaceBottle
starSparkles
starSparkles2
starStonks
starSweat
starSweat2
starThink
starThisIsFine
starThisTrans
starThumbsUp
starTooTiredToUseWords
starTransHeartSparkling
starUgh
starUncomfortableLaugh
starUwah
starUwah2
starWave
starWhat
starWhat2
starWhatTheFlippinFlappinFuck
starWoah
starWoah
starWoah2
starWow
starYay
starYayBoobs
"""


if __name__ == '__main__':
    # convert to dictionary with default value 0, removing blank items
    stats = dict([(k, 0)
                 for k in filter(lambda k: k.strip(), emoji.splitlines())])
    with open('emoji_votes.csv') as csvfile:
        csvfile = csv.reader(csvfile, delimiter=',')
        next(csvfile)  # skip header row
        for row in csvfile:
            # pick the last column, split on semicolons, only keep non-blank items
            picks = [x for x in row[-1:][0].split(';') if x]
            for pick in picks:
                # increment count, create if it doesn't exist
                stats[pick] = stats.get(pick, 0)+1
            # sort list by count descending and name ascending
            sorted_list = sorted(list(stats.items()),
                                 key=lambda tup: (Reversor(tup[1]), tup[0]))
        # find the length of the longest string
        max_len = len(max([k for k, v in sorted_list], key=len))
        # pad results for easy reading
        for k, v in sorted_list:
            print(f'{k.ljust(max_len)} {v}')
