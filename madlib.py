# Jesuit History and Mission
jesuit_history = "The Society of Jesus, also known as the Jesuits, is a religious order founded by Saint Ignatius of Loyola in the 16th century. Jesuits are known for their dedication to education, missionary work, and social justice."

# Verbs
minrangev = int(2)
verb = input("Enter 2 verbs (separated by a space): ")
verbs = verb.split()
while len(verbs) < minrangev:
    verb = input("Enter 2 verbs (separated by a space): ")
    verbs = verb.split()
verbf = verbs[0:2]

# Past Tense Verb
minrangepv = int(1)
verbp = input("Enter a past tense verb: ")
verbps = verbp.split()
while len(verbps) < minrangepv:
    verbp = input("Enter a past tense verb: ")
    verbps = verbp.split()
verbpf = verbps[0:1]

# Verbs Ending in ING
minrangeving = int(5)
verbing = input("Enter 5 verbs ending in 'ing' (separated by spaces): ")
verbings = verbing.split()
while len(verbings) < minrangeving:
    verbing = input("Enter 5 verbs ending in 'ing' (separated by spaces): ")
    verbings = verbing.split()
verbingf = verbings[0:5]

# Singular Nouns
minrangesn = int(12)
snoun = input("Enter 12 nouns (separated by spaces): ")
snouns = snoun.split()
while len(snouns) < minrangesn:
    snoun = input("Enter 12 nouns (separated by spaces): ")
    snouns = snoun.split()
snounf = snouns[0:12]

# Plural Noun
minrangepn = int(1)
pnoun = input("Enter a plural noun: ")
pnouns = pnoun.split()
while len(pnouns) < minrangepn:
    pnoun = input("Enter a plural noun: ")
    pnouns = pnoun.split()
pnounf = pnouns[0:1]

# Adjectives
minrangea = int(20)
adj = input("Enter 20 adjectives (separated by spaces): ")
adjs = adj.split()
while len(adjs) < minrangea:
    adj = input("Enter 20 adjectives (separated by spaces): ")
    adjs = adj.split()
adjf = adjs[0:20]

# Names
minrangena = int(2)
name = input("Enter 2 names (separated by spaces): ")
names = name.split()
while len(names) < minrangena:
    name = input("Enter 2 names (separated by spaces): ")
    names = name.split()
namesf = names[0:2]

# Breaking the story down into their sentences
sentence0 = f"Once upon a time in a {adjf[0]} faraway land, there lived a group of {snounf[0]} Jesuits who were known for their {adjf[1]} intelligence and {adjf[2]} dedication."
sentence1 = f"They were {verbingf[0]} tirelessly to spread the message of {snounf[1]} knowledge and {snounf[2]} enlightenment."
sentence2 = f"One day, a {adjf[3]} and {adjf[4]} young Jesuit named {namesf[0]} set out on a(n) {adjf[5]} mission."

# Combining sentences into paragraphs
paragraph0 = sentence0 + " " + sentence1 + " " + sentence2

sentence3 = f"He was tasked with {verbingf[1]} to a remote {snounf[3]} island, known as {namesf[1]}, to establish a {adjf[6]} mission there."
paragraph1 = sentence3

sentence4 = f"As he embarked on his journey, he faced many {adjf[7]} challenges, from treacherous {pnounf[0]} to {adjf[8]} storms at sea."
sentence5 = f"But his unwavering {snounf[4]} faith and {snounf[5]} determination kept him going. He knew that the people on the island were in need of {snounf[6]} guidance and {adjf[9]} support."
paragraph2 = sentence4 + " " + sentence5

sentence6 = f"Upon arriving on the island, {namesf[0]} was greeted by {adjf[10]} villagers who were curious about the {snounf[7]} teachings he had to offer."
sentence7 = f"He began {verbingf[2]} with the locals, sharing stories and {verbingf[3]} about the wonders of the {snounf[8]} Jesuit Mission."
paragraph3 = sentence6 + " " + sentence7

sentence8 = f"The Jesuits worked together with the islanders to build a {adjf[11]} chapel where they could {verbf[0]} pray and {verbf[1]} meditate."
sentence9 = f"They also set up a {adjf[12]} school where the children could receive a {adjf[13]} Jesuit education."
paragraph4 = sentence8 + " " + sentence9

sentence10 = f"Over time, the island transformed into a place of {adjf[14]} harmony and {snounf[9]} unity."
sentence11 = f"The Jesuits had successfully {verbpf[0]} the people with their {adjf[15]} wisdom, and the islanders had embraced their {snounf[10]} teachings."
paragraph5 = sentence10 + " " + sentence11

# More sentences and paragraphs
sentence12 = f"{namesf[0]} returned to his homeland, knowing that he had made a {adjf[16]} difference in the lives of the islanders."
sentence13 = f"The Jesuits continued their {adjf[17]} mission, spreading {snounf[11]} enlightenment wherever they went."
paragraph6 = sentence12 + " " + sentence13

# Add even more sentences and paragraphs to reach 100 lines
# ...

# Combine all paragraphs to create the full story
story = paragraph0 + "\n" + paragraph1 + "\n" + paragraph2 + "\n" + paragraph3 + "\n" + paragraph4 + "\n" + paragraph5 + "\n" + paragraph6 + "\n"

# Print the complete story
print(story)
