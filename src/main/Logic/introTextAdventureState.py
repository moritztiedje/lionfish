from src.main.Logic.stateMachine import ChoiceState, ForwardingState, GoBackState, AdvanceState, AttemptState, \
    GameOverState


class IntroTextAdventureState(ChoiceState):
    def __init__(self):
        super().__init__(
                "This will be the night to end all nights, whatever way this goes, you know that nothing will be the "
                "same again. People had called you a crazy nutbag, a dropout who fancied himself an arcane master, a "
                "madman, a loser, the village idiot with a love for lovecraft gone into the bizarre. Your hands "
                "tremble as they sift through the pages of the ritual book. All of your previous studies, efforts and "
                "hardships have led you to this moment, to this point in your life, where you are going to make the "
                "world a better place, once and for all, for everyone."
                "\n"
                "However, for a second, doubt flutters into your mind. Maybe you should not do this. Maybe bringing "
                "old and arcane beings into this world is not something that will make it a better place. Maybe the "
                "real reason you are considering this ritual is out of a lowly sense of hurt pride and not some great "
                "altruistic motive. What are you going to do?"
        )
        self.add_next_state(
                "Go through with it. You have a chance to make the world a better place. It would be unforgivable to "
                "falter on the verge of doing something great.",
                self.__build_go_on_state()
        )
        self.add_next_state(
                "Stop. Just stop. You are about to open a door of which you know that it is already dangerous to peek "
                "through its keyhole. Burn this book an leave this place.",
                self.__build_stop_state()
        )

    def __build_go_on_state(self):
        go_on = ChoiceState(
                "You have come this far. Why go half the way and then turn back, just because of a few bad omens, "
                "prophetic warnings and people who screamed as their eyeballs melted along the way? It is time to show "
                "the world that you are someone to be taken seriously. You begin the incantation with an insecure "
                "murmur, that soon turns into a deep and commanding bass of which you are no longer sure if it is your "
                "own or someone elses."
        )
        go_on.add_next_state("Keep singing", self.__build_keep_singing_state())
        go_on.add_next_state("Stop singing", self.__build_attempt_stop_singing_state())
        return go_on

    def __build_keep_singing_state(self):
        keep_singing = ChoiceState(
                "The song becomes louder and stranger. Excited screeching and shrieks mix themselves with the "
                "ever-rising bass. You realize that it is impossible for mutliple voices to come out of one throat, "
                "but then again, usually there is no fire burning out of a singers mouth and his feet are on the floor "
                "and not floating in the air along with the remainder of his body. An unnatural wind is gushing "
                "through the clearing, ripping and tearing at the book in your hand."
        )
        keep_singing.add_next_state("Hold on to the book.", self.__build_attempt_hold_on_state())
        keep_singing.add_next_state("Let go of the book.", self.__build_let_go_state())
        return keep_singing

    def __build_attempt_stop_singing_state(self):
        state = AttemptState("", 0.5)
        state.set_fail_state(self.__build_fail_stop_singing())
        state.set_success_state(self.__build_success_stop_singing())
        return state

    def __build_fail_stop_singing(self):
        fail_stop_singing = ForwardingState(
                "You try to force your jaw back shut, but some inevitable force rips it back open, dislocating your "
                "jaw and leaving your mouth agape, while the song rises out of your throat. ")
        fail_stop_singing.set_next_state(self.__build_keep_singing_state())
        return fail_stop_singing

    def __build_success_stop_singing(self):
        success_stop_singing = ForwardingState(
                "It takes all of the strength that your mind possesses but with a final act willpower, you force your "
                "jaw shut and snap the book closed. You feel exhausted and notice that your trousers have been stained "
                "by urine. Whatever secrets the book holds, you now have certainty that they are not of the kind that "
                "would help anyone. If you are completeley honest with yourself, you knew that before you got started, "
                "but nobody is as easily blinded by greed as a reject and a loser such as yourself. Whatever your next "
                "steps will be, you decide to burn the book there and then, before your next bout of an identity "
                "crisis starts a new apocalypse. \n")
        success_stop_singing.set_next_state(self.__build_old_age_state())
        return success_stop_singing

    def __build_stop_state(self):
        stop = ForwardingState(
                "For once in your life, you did the right thing. Like a suicidal man walking up to the edge and realising "
                "what the plunge would truly be, coming to this clearing and looking down at this book helps you to "
                "realize that it is probably a bad idea to perform milennia-old rituals that are, if your are perfectly "
                "honest with yourself, much more likely to bring about the end of the world than help it in any way. After "
                "burning the book then and there, you leave this place and whatever could have happened behind. \n"
        )
        stop.set_next_state(self.__build_old_age_state())
        return stop

    def __build_attempt_hold_on_state(self):
        state = AttemptState("", 0.25)
        state.set_fail_state(self.__build_hold_on_fail_state())
        state.set_success_state(self.__build_hold_on_success_state())
        return state

    @staticmethod
    def __build_hold_on_success_state():
        return GameOverState(
                "Despite the violent tugging and tearing of the winds, you manage to hold on to the book. It drags you up "
                "into the air and towards the center of the clearing, towards the eye of the storm. You feel it now, the "
                "fire and the way it burns. It is like the time you burned yourself on a hot stove, multiplied a "
                "hundred-fold and stretched out over an eternity. Through all of the pain your fraying mind realizes that "
                "this is, what the immeasurable agony of hellfire probably feels like, if hell even exists. In an "
                "explosion "
                "of charred meat and fire, your body explodes showering the clearing in your blood and guts. Out of the "
                "mist of your evaporating blood, strange and awful creatures appear and scurry off into the forest. They "
                "are anxious to get out of the way before their bigger siblings arrive. But none of this is your concern "
                "any more. You are dead and the world is doomed. Game Over. "
        )

    def __build_hold_on_fail_state(self):
        hold_on_fail = ForwardingState(
                "You do your best, but your muscles are no match for the violence of the winds. "
        )
        hold_on_fail.set_next_state(self.__build_let_go_state())
        return hold_on_fail

    def __build_let_go_state(self):
        return AdvanceState(
                "The book shoots out of your grasp into the center of the clearing, while the winds swirl and rise around "
                "you. It does not matter in which direction you try to run or hide, not even an ox would be a match for "
                "the winds that swoop you up and blow you around. You try grasp at the branches and the trees as you are "
                "catapulted up into the air but manage little more than taking a few leaves with you. There is a chaos of "
                "dirt, twigs and water blowing around you, you spin around your own axis and loose all feeling for up and "
                "down. For a a couple of seconds, the wind blows away the debris you can see the clearing at a dizzing "
                "distance below you, the book is still floating in its center, with tendrils of fire shooting out of it, "
                "singeing the grass and setting trees on fire. Then the debris is back and you can see and taste nothing "
                "but dirt. Seconds, minutes, hours or days go by, where you can do nothing but be shaken and shoved around "
                "by the winds."
                "\n"
                "For a while, you can feel nothing but fear and panic. At some time you reach up to your face and notice a "
                "beard has sprouted from it, which had not been there when you were still down on the ground. At another "
                "time your face feels young and clean shaven, then old and wrinkly, then strong and defined then so "
                "youthful that it comes to no surprise when you reach down in your pants and notice that your pubic hair "
                "is gone. Your body and mind change along with your age. Sometimes your clothes bulge with muscles, then "
                "they hang so loose you feel they might slip off your bony hip and fly off into the wind. At one time your "
                "mind, wit and perception are sharp enough to understand that the wind is carrying you through space and "
                "time, showing you parallel versions of yourself, people that you might have been, may become, have been "
                "or will be. At other times you are dumb as rock and struggle to gather anything but the basic notion of "
                "the wind carrying you somewhere far away. The only thing that remains untouched is your memory, as long "
                "as you are not currently drifting as an amnesiac, which also happens a few times."
                "\n"
                "At some point, one of the many versions of yourself finally breaks out of the wind, shoots towards an "
                "unknown surface of water at a sharp angle, hits it, bounces back up like a skipping stone a few times and "
                "crashes into a beach in a tangle of limbs, hair and torn clothes."
        )

    def __build_old_age_state(self):
        return GameOverState(
                "You continue to live your life, as good as you can, but at an old age you have to admit that it has "
                "been a rather pointless life of mediocrity. Maybe you did the right thing all those years ago but "
                "also maybe even the end of the world would have been preferrable to this insignificant blob of "
                "nothing. You are old now and you doubt that you have more than a few years left among the living. "
                "Maybe you wish that you had done things differently, done more with the one life than you had, but "
                "the time for wishes has gone by. All you can do now is accept the inevitable. Game Over."
        )
