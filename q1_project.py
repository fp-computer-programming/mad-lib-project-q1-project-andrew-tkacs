#Author: Andrew Tkacs

# Jesuit History and Mission Madlib Project

print("Welcome to the Jesuit History and Mission Madlib!")

# empty lists for different word types

verbs = []
verbps = []
verbings = []
snouns = []
pnouns = []
adjs = []
names = []

# Verbs

print("Enter 2 verbs (separated by a space):")
verbs_input = input()
if len(verbs_input.split()) == 2:
    verbs = verbs_input.split()
else:
    print("Please enter exactly 2 verbs.")

# Past Tense Verb

print("Enter a past tense verb:")
verbp = input()
if verbp.endswith("ed"):
    verbps.append(verbp)
else:
    print("Please enter a verb in the past tense (ending with 'ed').")

# Verbs Ending in ING

print("Enter 5 verbs ending in 'ing' (separated by spaces):")
verbings_input = input()
if len(verbings_input.split()) == 5:
    verbings = verbings_input.split()
else:
    print("Please enter exactly 5 verbs ending in 'ing'.")

# Singular Nouns

print("Enter 12 nouns (separated by spaces):")
snouns_input = input()
if len(snouns_input.split()) == 12:
    snouns = snouns_input.split()
else:
    print("Please enter exactly 12 nouns.")

# Plural Noun

print("Enter a plural noun:")
pnoun = input()
if pnoun.endswith("s"):
    pnouns.append(pnoun)
else:
    print("Please enter a plural noun (ending with 's').")

# Adjectives

print("Enter 20 adjectives (separated by spaces):")
adjs_input = input()
if len(adjs_input.split()) == 20:
    adjs = adjs_input.split()
else:
    print("Please enter exactly 20 adjectives.")

# Names

print("Enter 2 names (separated by spaces):")
names_input = input()
if len(names_input.split()) == 2:
    names = names_input.split()
else:
    print("Please enter exactly 2 names.")

# Generate the story if all inputs are valid

if (verbs and verbps and verbings and snouns and pnouns and adjs and names):
    sentence0 = f"Once upon a time in a {adjs[0]} faraway land, there lived a group of {snouns[0]} Jesuits who were known for their {adjs[1]} intelligence and {adjs[2]} dedication."
    sentence1 = f"They were {verbings[0]} tirelessly to spread the message of {snouns[1]} knowledge and {snouns[2]} enlightenment."
    sentence2 = f"One day, a {adjs[3]} and {adjs[4]} young Jesuit named {names[0]} set out on a(n) {adjs[5]} mission."

    paragraph0 = sentence0 + " " + sentence1 + " " + sentence2

    sentence3 = f"He was tasked with {verbings[1]} to a remote {snouns[3]} island, known as {names[1]}, to establish a {adjs[6]} mission there."
    paragraph1 = sentence3

    sentence4 = f"As he embarked on his journey, he faced many {adjs[7]} challenges, from treacherous {pnouns[0]} to {adjs[8]} storms at sea."
    sentence5 = f"But his unwavering {snouns[4]} faith and {snouns[5]} determination kept him going. He knew that the people on the island were in need of {snouns[6]} guidance and {adjs[9]} support."
    paragraph2 = sentence4 + " " + sentence5

    sentence6 = f"Upon arriving on the island, {names[0]} was greeted by {adjs[10]} villagers who were curious about the {snouns[7]} teachings he had to offer."
    sentence7 = f"He began {verbings[2]} with the locals, sharing stories and {verbings[3]} about the wonders of the {snouns[8]} Jesuit Mission."
    paragraph3 = sentence6 + " " + sentence7

    sentence8 = f"The Jesuits worked together with the islanders to build a {adjs[11]} chapel where they could {verbs[0]} pray and {verbs[1]} meditate."
    sentence9 = f"They also set up a {adjs[12]} school where the children could receive a {adjs[13]} Jesuit education."
    paragraph4 = sentence8 + " " + sentence9

    sentence10 = f"Over time, the island transformed into a place of {adjs[14]} harmony and {snouns[9]} unity."
    sentence11 = f"The Jesuits had successfully {verbps[0]} the people with their {adjs[15]} wisdom, and the islanders had embraced their {snouns[10]} teachings."
    paragraph5 = sentence10 + " " + sentence11

    sentence12 = f"{names[0]} returned to his homeland, knowing that he had made a {adjs[16]} difference in the lives of the islanders."
    sentence13 = f"The Jesuits continued their {adjs[17]} mission, spreading {snouns[11]} enlightenment wherever they went."
    story = paragraph0 + "\n" + paragraph1 + "\n" + paragraph2 + "\n" + paragraph3 + "\n" + paragraph4 + "\n" + paragraph5 + "\n"

    # Print Story w/ inputs for user

    print("Here's your Jesuit History and Mission Madlib:")
    print(story)
else:
    print("Some inputs were invalid. Please make sure to follow the instructions and try again.")