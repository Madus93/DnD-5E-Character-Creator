import dnd_dict, dnd_skills, dnd_language, dnd_magic,dnd_class
# These are all of the features and flavor text for the races, backgrounds,
# and classes that would be too lengthy to put in the main program


def dragonborn_features():
    feature = """Draconic Ancestry. You are distantly related to a particular kind of dragon. Choose a type of dragon from the below list; this determines the damage and area of your breath weapon, and the type of resistance you gain.
Dragon Color 	Damage Type 	Breath Weapon
Black 	Acid 	5' by 30' line (DEX save)
Blue 	Lightning 	5' by 30' line (DEX save)
Brass 	Fire 	5' by 30' line (DEX save)
Bronze 	Lightning 	5' by 30' line (DEX save)
Copper 	Acid 	5' by 30' line (DEX save)
Gold 	Fire 	15' cone (DEX save)
Green 	Poison 	15' cone (CON save)
Red 	Fire 	15' cone (DEX save)
Silver 	Cold 	15' cone (CON save)
White 	Cold 	15' cone (CON save)

• Breath Weapon. You can use your action to exhale destructive energy. It deals damage in an area according to your ancestry. When you use your breath weapon, all creatures in the area must make a saving throw, the type of which is determined by your ancestry. The DC of this saving throw is 8 + your Constitution modifier + your proficiency bonus. A creature takes 2d6 damage on a failed save, and half as much damage on a successful one. The damage increase to 3d6 at 6th level, 4d6 at 11th, and 5d6 at 16th level. After using your breath weapon, you cannot use it again until you complete a short or long rest. HBInstead, you may use your breath weapon a number of times equal to your Constitution modifier. You regain expended uses on a short or long rest."""
    dnd_dict.character_dict.get("features").append(feature)

def dwarf_hill_features():

    feature = """• Darkvision. Accustomed to life underground, you have superior vision in dark and dim conditions. You can see in dim light within 60 feet of you as if it were bright light, and in darkness as if it were dim light. You can't discern color in darkness, only shades of gray.

• Dwarven Resilience. You have advantage on saving throws against poison, and you have resistance against poison damage.

• Stonecunning. Whenever you make an Intelligence (History) check related to the origin of stonework, you are considered proficient in the History skill and add double your proficiency bonus to the check, instead of your normal proficiency bonus.
• Dwarven Toughness. Your hit point maximum increases by 1, and it increases by 1 every time you gain a level."""
    dnd_dict.character_dict.get("features").append(feature)

def dwarf_mountain_features():

    feature = """• Darkvision. Accustomed to life underground, you have superior vision in dark and dim conditions. You can see in dim light within 60 feet of you as if it were bright light, and in darkness as if it were dim light. You can't discern color in darkness, only shades of gray.

• Dwarven Resilience. You have advantage on saving throws against poison, and you have resistance against poison damage.

• Stonecunning. Whenever you make an Intelligence (History) check related to the origin of stonework, you are considered proficient in the History skill and add double your proficiency bonus to the check, instead of your normal proficiency bonus."""
    dnd_dict.character_dict.get("features").append(feature)

def elf_features():

    feature = """• Darkvision. Accustomed to twilit forests and the night sky, you have superior vision in dark and dim conditions. You can see in dim light within 60 feet of you as if it were bright light, and in darkness as if it were dim light. You can't discern color in darkness, only shades of gray.

• Fey Ancestry. You have advantage on saving throws against being charmed, and magic can't put you to sleep.

• Trance. Elves do not sleep. Instead they meditate deeply, remaining semi-conscious, for 4 hours a day. The Common word for this meditation is "trance". While meditating, you dream after a fashion; such dreams are actually mental exercises that have become reflexive after years of practice. After resting in this way, you gain the same benefit a human would from 8 hours of sleep."""
    dnd_dict.character_dict.get("features").append(feature)



def gnome_forest_features():

    feature = """• Darkvision. Accustomed to life underground, you have superior vision in dark and dim conditions. You can see in dim light within 60 feet of you as if it were bright light, and in darkness as if it were dim light. You can't discern color in darkness, only shades of gray.

• Gnome Cunning. You have advantage on all Intelligence, Wisdom, and Charisma saves against magic

• Natural Illusionist. You know the Minor Illusion cantrip. Intelligence is your spellcasting modifier for it.

• Speak with Small Beasts. Through sound and gestures, you may communicate simple ideas with Small or smaller beasts."""
    dnd_dict.character_dict.get("features").append(feature)

def gnome_rock_features():

    feature = """• Darkvision. Accustomed to life underground, you have superior vision in dark and dim conditions. You can see in dim light within 60 feet of you as if it were bright light, and in darkness as if it were dim light. You can't discern color in darkness, only shades of gray.

• Gnome Cunning. You have advantage on all Intelligence, Wisdom, and Charisma saves against magic
• Artificer's Lore. Whenever you make an Intelligence (History) check related to magical, alchemical, or technological items, you can add twice your proficiency bonus instead of any other proficiency bonus that may apply.

• Tinker. You have proficiency with artisan tools (tinker's tools). Using those tools, you can spend 1 hour and 10 gp worth of materials to construct a Tiny clockwork device (AC 5, 1 hp). The device ceases to function after 24 hours (unless you spend 1 hour repairing it to keep the device functioning), or when you use your action to dismantle it; at that time, you can reclaim the materials used to create it. You can have up to three such devices active at a time. When you create a device, choose one of the following options:

Clockwork Toy. This toy is a clockwork animal, monster, or person, such as a frog, mouse, bird, dragon, or soldier. When placed on the ground, the toy moves 5 feet across the ground on each of your turns in a random direction. It makes noises as appropriate to the creature it represents.

Fire Starter. The device produces a miniature flame, which you can use to light a candle, torch, or campfire. Using the device requires your action.

Music Box. When opened, this music box plays a single song at a moderate volume. The box stops playing when it reaches the song's end or when it is closed.

At your DM's discretion, you may make other objects with effects similar in power to these. The Prestidigitation cantrip is a good baseline for such effects."""
    dnd_dict.character_dict.get("features").append(feature)


def half_elf_features():

    feature = """• Darkvision. Thanks to your elven heritage, you have superior vision in dark and dim conditions. You can see in dim light within 60 feet of you as if it were bright light, and in darkness as if it were dim light. You can't discern color in darkness, only shades of gray.

• Fey Ancestry. You have advantage on saving throws against being charmed, and magic can't put you to sleep."""
    dnd_dict.character_dict.get("features").append(feature)

def halfling_lightfoot_features():

    feature = """• Lucky. When you roll a 1 on an attack roll, ability check, or saving throw, you can reroll the die. You must use the new result, even if it is a 1.

• Brave. You have advantage on saving throws against being frightened.

• Nimble. You can move through the space of any creature that is of a size larger than yours.

• Naturally Stealthy. You can attempt to hide even when you are only obscured by a creature that is at least one size larger than you."""
    dnd_dict.character_dict.get("features").append(feature)


def halfling_stout_features():

    feature = """• Lucky. When you roll a 1 on an attack roll, ability check, or saving throw, you can reroll the die. You must use the new result, even if it is a 1.

• Brave. You have advantage on saving throws against being frightened.

• Nimble. You can move through the space of any creature that is of a size larger than yours.

• Stout Resilience. You have advantage on saving throws against poison, and you have resistance to poison damage."""
    dnd_dict.character_dict.get("features").append(feature)


def half_orc_features():

    feature = """• Darkvision. Thanks to your orc blood, you have superior vision in dark and dim conditions. You can see in dim light within 60 feet of you as if it were bright light, and in darkness as if it were dim light. You can't discern color in darkness, only shades of gray.

• Menacing. You gain proficiency in the Intimidation skill.

• Relentless Endurance. When you are reduced to 0 hit points but not killed outright, you can drop to 1 hit point instead. You can't use this feature again until you finish a long rest.

• Savage Attacks. When you score a critical hit with a melee weapon attack, you can roll one of the weapon's damage dice one additional time and add it to the extra damage of the critical hit."""
    dnd_dict.character_dict.get("features").append(feature)


def tiefling_features():

    feature = """• Darkvision. Thanks to your infernal heritage, you have superior vision in dark and dim conditions. You can see in dim light within 60 feet of you as if it were bright light, and in darkness as if it were dim light. You can’t discern color in darkness, only shades of gray.

• Hellish Resistance. You have resistance to fire damage.

• Infernal Legacy. You know the Thaumaturgy cantrip. Once you reach 3rd level, you can cast the Hellish Rebuke spell once as a 2nd-level spell. Once you reach 5th level, you can also cast the Darkness spell once. You must finish a long rest to cast these spells again with this trait. Charisma is your spellcasting ability for these spells."""
    dnd_dict.character_dict.get("features").append(feature)


def acolyte_features():
    feature = """Feature: Shelter of the Faithful

As an acolyte, you command the respect of those who share your faith, and you can perform the religious ceremonies of your deity. You and your adventuring companions can expect to receive free healing and care at a temple, shrine, or other established presence of your faith, though you must provide any material components needed for spells. Those who share your religion will support you (but only you) at a modest lifestyle.

You might also have ties to a specific temple dedicated to your chosen deity or pantheon, and you have a residence there. This could be the temple where you used to serve, if you remain on good terms with it, or a temple where you have found a new home. While near your temple, you can call upon the priests for assistance, provided the assistance you ask for is not hazardous and you remain in good standing with your temple."""

    dnd_dict.character_dict.get("features").append(feature)

def anthropologist_features():
    feature = """Feature: Cultural Chameleon

Before becoming an adventurer, you spent much of your adult life away from your homeland, living among people different from your kin. You came to understand these foreign cultures and the ways of their people, who eventually treated you as one of their own. One culture had more of an influence on you than any other, shaping your beliefs and customs. Choose a race whose culture you've adopted.
Feature: Adept Linguist

You can communicate with humanoids who don't speak any language you know. You must observe the humanoids interacting with one another for at least 1 day, after which you learn a handful of important words, expressions, and gestures – enough to communicate on a rudimentary level."""

    dnd_dict.character_dict.get("features").append(feature)

def archeologist_features():

    feature = """Feature: Dust Digger

Prior to becoming an adventurer, you spent most of your young life crawling around in the dust, pilfering relics of questionable value from crypts and ruins. Though you managed to sell a few of your discoveries and earn enough coin to buy proper adventuring gear, you have held onto an item that has great emotional value to you. Roll on the Signature Item table to see what you have, or choose an item from the table.
d8 	Signature Item
1 	10-foot pole
2 	Medallion
3 	Crowbar
4 	Shovel
5 	Hat
6 	Sledgehammer
7 	Hooded lantern
8 	Whip
Feature: Historical Knowledge

When you enter a ruin or dungeon, you can correctly ascertain its original purpose and determine its builders, whether those were dwarves, elves, humans, yuan-ti, or some other known race. In addition, you can determine the monetary value of art objects more than a century old."""

    dnd_dict.character_dict.get("features").append(feature)

def charlatan_features():
    feature = """Feature: Favorite Schemes

Every charlatan has an angle they use in preference to other schemes. Choose a favorite scam or roll on the table below.
d6 	Scam
1 	I cheat at games of chance.
2 	I shave coins or forge documents.
3 	I insinuate myself into people's lives to prey on their weakness and secure their fortunes.
4 	I put on new identities like clothes.
5 	I run sleight-of-hand cons on street corners.
6 	I convince people that worthless junk is worth their hard-earned money.
Feature: False Identity

You have created a second identity that includes documentation, established acquaintances, and disguises that allow you to assume that persona. Additionally, you can forge documents including official papers and personal letters, as long as you have seen an example of the kind of document or the handwriting you are trying to copy."""

    dnd_dict.character_dict.get("features").append(feature)

def city_watch_features():
    feature = """Feature: Watcher's Eye

Your experience in enforcing the law, and dealing with lawbreakers, gives you a feel for local laws and criminals. You can easily find the local outpost of the watch or a similar organization, and just as easily pick out the dens of criminal activity in a community, although you're more likely to be welcome in the former locations rather than the latter."""

    dnd_dict.character_dict.get("features").append(feature)

def cloistered_scholar_features():
    feature = """Feature: Library Access

Though others must often endure extensive interviews and significant fees to gain access to even the most common archives in your library, you have free and easy access to the majority of the library, though it might also have repositories of lore that are too valuable, magical, or secret to permit anyone immediate access.

You have a working knowledge of your cloister's personnel and bureaucracy, and you know how to navigate those connections with some ease.

Additionally, you are likely to gain preferential treatment at other libraries across the Realms, as professional courtesy shown to a fellow scholar."""

    dnd_dict.character_dict.get("features").append(feature)

def criminal_features():
    feature = """Feature: Criminal Specialty

There are many kinds of criminals, and within a thieves' guild or similar criminal organization, individual members have particular specialties. Even criminals who operate outside of such organizations have strong preferences for certain kinds of crimes over others. Choose the role you played in your criminal life, or roll on the table below.
d8 	Specialty
1 	Blackmailer
2 	Burglar
3 	Enforcer
4 	Fence
5 	Highway robber
6 	Hired killer
7 	Pickpocket
8 	Smuggler
Feature: Criminal Contact

You have a reliable and trustworthy contact who acts as your liaison to a network of other criminals. You know how to get messages to and from your contact, even over great distances; specifically, you know the local messengers, corrupt caravan masters, and seedy sailors who can deliver messages for you."""

    dnd_dict.character_dict.get("features").append(feature)

def entertainer_features():

    feature = """Feature: Entertainer Routines

A good entertainer is versatile, spicing up every performance with a variety of different routines. Choose one to three routines or roll on the table below to define your expertise as an entertainer.
d10 	Entertainer Routine
1 	Actor
2 	Dancer
3 	Fire-eater
4 	Jester
5 	Juggler
6 	Instrumentalist
7 	Poet
8 	Singer
9 	Storyteller
10 	Tumbler
Feature: By Popular Demand

You can always find a place to perform, usually in an inn or tavern but possibly with a circus, at a theater, or even in a noble's court. At such a place, you receive free lodging and food of a modest or comfortable standard (depending on the quality of the establishment), as long as you perform each night. In addition, your performance makes you something of a local figure. When strangers recognize you in a town where you have performed, they typically take a liking to you."""

    dnd_dict.character_dict.get("features").append(feature)

def far_traveler_features():
    feature = """Feature: Why Are You Here?

A far traveler might have set out on a journey for one of a number of reasons, and the departure from his or her homeland could have been voluntary or involuntary. To determine why you are so far from home, roll on the table below or choose from the options provided. The following section, discussing possible homelands, includes some suggested reasons that are appropriate for each location.
d6 	Reason
1 	Emissary
2 	Exile
3 	Fugitive
4 	Pilgrim
5 	Sightseer
6 	Wanderer
Feature: Where Are You From?

NOTE: You do not have to use this if you are making your own world. If you are,
feel free to create your own setting.

The most important decision in creating a far traveler background is determining your homeland. The places discussed here are all sufficiently distant from the North and the Sword Coast to justify the use of this background.

Evermeet. The fabled elven islands far to the west are home to elves who have never been to Faerun. They often find it a harsher place than they expected when they do make the trip. If you are an elf, Evermeet is a logical (though not mandatory) choice for your homeland.

Most of those who emigrate from Evermeet are either exiles, forced out for committing some infraction of elven law, or emissaries who come to Faerun for a purpose that benefits elven culture or society.

Halruaa. Located on the southern edges of the Shining South, and hemmed in by mountains all around, the magocracy of Halruaa is a bizarre land to most in Faerun who know about it. Many folk have heard of the strange skyships the Halruaans sail, and a few know of the tales that even the least of their people can work magic.

Halruaans usually make their journeys into Faerun for personal reasons, since their government has a strict stance against unauthorized involvement with other nations and organizations. You might have been exiled for breaking one of Halruaa's many byzantine laws, or you could be a pilgrim who seeks the shrines of the gods of magic.

Kara-Tur. The continent of Kara-Tur, far to the east of Faerûn, is home to people whose customs are unfamiliar to the folk of the Sword Coast. If you come from Kara-Tur, the people of Faerûn likely refer to you as Shou, even if that isn't your true ethnicity, because that's the blanket term they use for everyone who shares your origin.

The folk of Kara-Tur occasionally travel to Faerûn as diplomats or to forge trade relations with prosperous merchant cartels. You might have come here as part of some such delegation, then decided to stay when the mission was over.

Mulhorand. From the terrain to the architecture to the god-kings who rule over these lands, nearly everything about Mulhorand is a lien to someone from the Sword Coast. You likely experienced the same sort of culture shock when you left your desert home and traveled to the unfamiliar climes of northern Faerûn. Recent events in your homeland have led to the abolition of slavery, and a corresponding increase in the traffic between Mulhorand and the distant parts of Faerûn.

Those who leave behind Mulhorand's sweltering deserts and ancient pyramids for a glimpse at a different life do so for many reasons. You might be in the North simply to see the strangeness this wet land has to offer, or because you have made too many enemies among the desert communities of your home.

Sossal. Few have heard of your homeland, but many have questions about it upon seeing you. Humans from Sossal seem crafted from snow, with alabaster skin and white hair, and typically dressed in white.

Sossal exists far to the northeast, hard up against the endless ice to the north and bounded on its other sides by hundreds of miles of the Great Glacier and the Great Ice Sea. No one from your nation makes the effort to cross such colossal barriers without a convincing reason. You must fear something truly terrible or seek something incredibly important.

Zakhara. As the saying goes among those in Faerûn who know of the place, "To get to Zakhara, go south. Then go south some more." Of course, you followed an equally long route when you came north from your place of birth. Though it isn't unusual for Zakharans to visit the southern extremes of Faerûn for trading purposes, few of them stray as far from home as you have.

You might be traveling to discover what wonders are to be found outside the deserts and sword-like mountains of your homeland, or perhaps you are on a pilgrimage to understand the gods that others worship, so that you might better appreciate your own deities.

The Underdark. Though your home is physically closer to the Sword Coast than the other locations discussed here, it is far more unnatural. You hail from one of the settlements in the Underdark, each of which has its own strange customs and laws. If you are a native of one of the great subterranean cities or settlements, you are probably a member of the race that occupies the place but you might also have grown up there after being captured and brought below when you were a child.

If you are a true Underdark native, you might have come to the surface as an emissary of your people, or perhaps to escape accusations of criminal behavior (whether warranted or not). If you aren't a native, your reason for leaving "home" probably has something to do with getting away from a bad situation.
Feature: All Eyes on You

Your accent, mannerisms, figures of speech, and perhaps even your appearance all mark you as foreign. Curious glances are directed your way wherever you go, which can be a nuisance, but you also gain the friendly interest of scholars and others intrigued by far-off lands, to say nothing of everyday folk who are eager to hear stories of your homeland.

You can parley this attention into access to people and places you might not otherwise have, for you and your traveling companions. Noble lords, scholars, and merchant princes, to name a few, might be interested in hearing about your distant homeland and people."""

    dnd_dict.character_dict.get("features").append(feature)

def folk_hero_features():
    feature = """Feature: Defining Event

You previously pursued a simple profession among the peasantry, perhaps as a farmer, miner, servant, shepherd, woodcutter, or gravedigger. But something happened that set you on a different path and marked you for greater things. Choose or randomly determine a defining event that marked you as a hero of the people.
d10 	Defining Event
1 	I stood up to a tyrant's agents.
2 	I saved people during a natural disaster.
3 	I stood alone against a terrible monster.
4 	I stole from a corrupt merchant to help the poor.
5 	I led a militia to fight off an invading army.
6 	I broke into a tyrant's castle and stole weapons to arm the people.
7 	I trained the peasantry to use farm implements as weapons against a tyrant's soldiers.
8 	A lord rescinded an unpopular decree after I led a symbolic act of protect against it.
9 	A celestial, fey, or similar creature gave me a blessing or revealed my secret origin.
10 	Recruited into a lord's army, I rose to leadership and was commended for my heroism.
Feature: Rustic Hospitality

Since you come from the ranks of the common folk, you fit in among them with ease. You can find a place to hide, rest, or recuperate among other commoners, unless you have shown yourself to be a danger to them. They will shield you from the law or anyone else searching for you, though they will not risk their lives for you. """

    dnd_dict.character_dict.get("features").append(feature)

def gladiator_features():
    feature = """Feature: Entertainer Routines

A good entertainer is versatile, spicing up every performance with a variety of different routines. Choose one to three routines or roll on the table below to define your expertise as an entertainer.
d10 	Entertainer Routine
1 	Actor
2 	Dancer
3 	Fire-eater
4 	Jester
5 	Juggler
6 	Instrumentalist
7 	Poet
8 	Singer
9 	Storyteller
10 	Tumbler
Feature: By Popular Demand

You can always find a place to perform, usually in an inn or tavern but possibly with a circus, at a theater, or even in a noble's court. At such a place, you receive free lodging and food of a modest or comfortable standard (depending on the quality of the establishment), as long as you perform each night. In addition, your performance makes you something of a local figure. When strangers recognize you in a town where you have performed, they typically take a liking to you.\nA gladiator is as much an entertainer as any minstrel or circus performer trained to make the arts of combat into a spectacle the crowd can enjoy. This kind of flashy combat is your entertainer routine, though you might also have some skills as a tumbler or actor. Using your By Popular Demand feature, you can find a place to perform in any place that features combat for entertainment-perhaps a gladiatorial arena or secret pit fighting club. You can replace the musical instrument in your equipment package with an inexpensive but unusual weapon, such as a trident or net."""

    dnd_dict.character_dict.get("features").append(feature)

def guild_artisan_features():
    feature = """Feature: Guild Business

Guilds are generally found in cities large enough to support several artisans practicing the same trade. However, your guild might instead be a loose network of artisans who each work in a different village within a larger realm. Work with your DM to determine the nature of your guild. You can select your guild business from the Guild Business table or roll randomly.
d8 	Guild Business
1 	Alchemists and apothecaries
2 	Armorers, locksmiths, and finesmiths
3 	Brewers, distillers, and vintners
4 	Calligraphers, scribes, and scriveners
5 	Carpenters, roofers, and plasterers
6 	Cartographers, surveyors, and chart-makers
7 	Cobblers and shoemakers
8 	Cooks and bakers
9 	Glassblowers and glaziers
10 	Jewelers and gemcutters
11 	Leatherworkers, skinners, and tanners
12 	Masons and stonecutters
13 	Painters, limners, and sign-makers
14 	Potters and tile-makers
15 	Shipwrights and sailmakers
16 	Smiths and metal-forgers
17 	Tinkers, pewterers, and casters
18 	Wagon-makers and wheelwrights
19 	Weavers and dyers
20 	Woodcarvers, coopers, and bowyers

As a member of your guild, you know the skills needed to create finished items from raw materials (reflected in your proficiency with a certain kind of artisan's tools), as well as the principles of trade and good business practices. The question now is whether you abandon your trade for adventure, or take on the extra effort to weave adventuring and trade together.
Feature: Guild Membership

As an established and respected member of a guild, you can rely on certain benefits that membership provides. Your fellow guild members will provide you with lodging and food if necessary, and pay for your funeral if needed. In some cities and towns, a guildhall offers a central place to meet other members of your profession, which can be a good place to meet potential patrons, allies, or hirelings.

Guilds often wield tremendous political power. If you are accused of a crime, your guild will support you if a good case can be made for your innocence or the crime is justifiable. You can also gain access to powerful political figures through the guild, if you are a member in good standing. Such connections might require the donation of money or magic items to the guild's coffers.

You must pay dues of 5 gp per month to the guild. If you miss payments, you must make up back dues to remain in the guild's good graces."""

    dnd_dict.character_dict.get("features").append(feature)

def guild_merchant_features():
    feature = """Instead of an artisans' guild, you might belong to a guild of traders, caravan masters, or shopkeepers. You don't craft items yourself but earn a living by buying and selling the works of others (or the raw materials artisans need to practice their craft). Your guild might be a large merchant consortium (or family) with interests across the region. Perhaps you transported goods from one place to another, by ship, wagon, or caravan, or bought them from traveling traders and sold them in your own little shop. In some ways, the traveling merchant's life lends itself to adventure far more than the life of an artisan."""

    dnd_dict.character_dict.get("features").append(feature)

def haunted_one_features():
    feature = """Feature: Harrowing Event

Prior to becoming an adventurer, your path in life was defined by one dark moment, one fateful decision, or one tragedy. Now you feel a darkness threatening to consume you, and you fear there may be no hope of escape. Choose a harrowing event that haunts you, or roll one on the Harrowing Events table.
d10 	Harrowing Event
1 	A monster that slaughtered dozens of innocent people spared your life, and you don’t know why.
2 	You were born under a dark star. You can feel it watching you, coldly and distantly. Sometimes it beckons you in the dead of night.
3 	An apparition that has haunted your family for generations now haunts you. You don’t know what it wants, and it won’t leave you alone.
4 	Your family has a history of practicing the dark arts. You dabbled once and felt something horrible clutch at your soul, whereupon you fled in terror.
5 	An oni took your sibling one cold, dark night, and you were unable to stop it.
6 	You were cursed with lycanthropy and later cured. You are now haunted by the innocents you slaughtered.
7 	A hag kidnapped and raised you. You escaped, but the hag still has a magical hold over you and fills your mind with evil thoughts.
8 	You opened an eldritch tome and saw things unfit for a sane mind. You burned the book, but its words and images are burned into your psyche.
9 	A fiend possessed you as a child. You were locked away but escaped. The fiend is still inside you, but now you try to keep it locked away.
10 	You did terrible things to avenge the murder of someone you loved. You became a monster, and it haunts your waking dreams.
Feature: Heart of Darkness

Those who look into your eyes can see that you have faced unimaginable horror and that you are no stranger to darkness. Though they might fear you, commoners will extend you every courtesy and do their utmost to help you. Unless you have shown yourself to be a danger to them, they will even take up arms to fight alongside you, should you find yourself facing an enemy alone."""

    dnd_dict.character_dict.get("features").append(feature)

def hermit_features():
    feature = """Feature: Life of Seclusion

What was the reason for your isolation, and what changed to allow you to end your solitude? You can work with your DM to determine the exact nature of your seclusion, or you can choose to roll on the table below to determine the reason behind your seclusion.
d8 	Life of Seclusion
1 	I was searching for spiritual enlightenment.
2 	I was partaking of communal living in accordance with the dictates of a religious order.
3 	I was exiled for a crime I didn't commit.
4 	I retreated from society after a life-altering event.
5 	I needed a quiet place to work on my art, literature, music, or manifesto.
6 	I needed to commune with nature, far from civilization.
7 	I was the caretaker of an ancient ruin or relic.
8 	I was a pilgrim in search of a person, place, or relic of spiritual significance.
Feature: Discovery

The quiet seclusion of your extended hermitage gave you access to a unique and powerful discovery. The exact nature of this revelation depends on the nature of your seclusion. It might be a great truth about the cosmos, the deities, the powerful beings of the outer planes, or the forces of nature. It could be a site that no one else has ever seen. You might have uncovered a fact that has long been forgotten, or unearthed some relic of the past that could rewrite history. It might be information that would be damaging to the people who or consigned you to exile, and hence the reason for your return to society.

Work with your DM to determine the details of your discovery and its impact on the campaign."""

    dnd_dict.character_dict.get("features").append(feature)


def inquisitor_features():
    feature = """Feature: Legal Authority

As an inquisitor of the church, you have the authority to arrest criminals. In the absence of other authorities, you are authorized to pass judgment and even carry out sentencing. If you abuse this power, however, your superiors in the church might strip it from you."""

    dnd_dict.character_dict.get("features").append(feature)

def investigator_features():
    feature = """Feature: Watcher's Eye

Your experience in enforcing the law, and dealing with lawbreakers, gives you a feel for local laws and criminals. You can easily find the local outpost of the watch or a similar organization, and just as easily pick out the dens of criminal activity in a community, although you're more likely to be welcome in the former locations rather than the latter."""


    dnd_dict.character_dict.get("features").append(feature)

def knight_features():
    feature = """Feature: Position of Privilege

Thanks to your noble birth, people are inclined to think the best of you. You are welcome in high society, and people assume you have the right to be wherever you are. The common folk make every effort to accommodate you and avoid your displeasure, and other people of high birth treat you as a member of the same social sphere. You can secure an audience with a local noble if you need to.\nVariant Feature: Retainers

If your character has a noble background, you may select this background feature instead of Position of Privilege.

You have the service of three retainers loyal to your family. These retainers can be attendants or messengers, and one might be a majordomo. Your retainers are commoners who can perform mundane tasks for you, but they do not fight for you, will not follow you into obviously dangerous areas (such as dungeons), and will leave if they are frequently endangered or abused."""


    dnd_dict.character_dict.get("features").append(feature)

def marine_features():
    feature = """Feature: Hardship Endured

Hardship in your past has forged you into an unstoppable living weapon. This hardship is essential to you and is at the heart of a personal philosophy or ethos that often guides your actions. You can roll on the following table to determine this hardship or choose one that best fits your character.
d6 	Hardship
1 	You hid underwater to avoid detection by enemies and held your breath for an extremely long time. Just before you would have died, you had a revelation about your existence.
2 	You spent months enduring thirst, starvation, and torture at the hands of your enemy, but you never broke.
3 	You enabled the escape of your fellow soldiers, but at great cost to yourself. Some of your past comrades may think you're dead.
4 	No reasonable explanation can explain how you survived a particular battle. Every arrow and bolt missed you. You slew scores of enemies single-handedly and led your comrades to victory.
5 	For days, you hid in the bilge of an enemy ship, surviving on brackish water and foolhardy rats. At the right moment, you crept up to the deck and took over the ship on your own.
6 	You carried an injured marine for miles to avoid capture and death.
Feature: Steady

You can move twice the normal amount of time (up to 16 hours) each day before being subject to the effect of a forced march (see "Travel Pace" in chapter 8 of the Player's Handbook). Additionally, you can automatically find a safe route to land a boat on shore, provided such a route exists."""

    dnd_dict.character_dict.get("features").append(feature)

def mercenary_features():
    feature = """NOTE: if you are making your own setting, you do not have to use these location names.\nFeature: Mercenaries of the North

Countless mercenary companies operate up and down the Sword Coast and throughout the North. Most are small-scale operations that employ a dozen to a hundred folk who offer security services, hunt monsters and brigands, or go to war in exchange for gold. Some organizations, such as the Zhentarim, Flaming Fist, and the nation of Mintarn have hundreds or thousands of members and can provide private armies to those with enough funds. A few organizations operating in the North are described below.

The Chill. The cold and mysterious Lurkwood serves as the home of numerous groups of goblinoids that have banded together into one tribe called the Chill. Unlike most of their kind, the Chill refrain s from raiding the people of the North and maintains relatively good relations so that they can hire them selves out as warriors. Few city-states in the North are willing to field an army alongside the Chill, but several are happy to quietly pay the Chill to battle the Uthgardt, ores, trolls of the Evermoors, and other threats to civilization.

Silent Rain. Consisting solely of elves, Silent Rain is a legendary mercenary company operating out of Evereska. Caring little for gold or fame, Silent Rain agrees only to jobs that either promote elven causes or involve destroying ores, gnolls, and the like. Prospective employers must leave written word (in Elvish) near Evereska, and the Silent Rain sends a representative if interested.

The Bloodaxes. Founded in Sundabar nearly two centuries ago, the Bloodaxes were originally a group of dwarves outcast from their clans for crimes against the teachings of Moradin Soulforger. They began hiring out as mercenaries to whoever in the North would pay them. Since then the mercenary company has broadened its membership to other races , but every member is an exile, criminal, or misfit of some sort looking for a fresh start and a new family among the bold Bloodaxes.
Feature: Mercenary Life

You know the mercenary life as only someone who has experienced it can. You are able to identify mercenary companies by their emblems, and you know a little about any such company, including the names and reputations of its commanders and leaders, and who has hired them recently. You can find the taverns and festhalls where mercenaries abide in any area, as long as you speak the language. You can find mercenary work between adventures sufficient to maintain a comfortable lifestyle."""

    dnd_dict.character_dict.get("features").append(feature)

def noble_features():
    feature = """Feature: Position of Privilege

Thanks to your noble birth, people are inclined to think the best of you. You are welcome in high society, and people assume you have the right to be wherever you are. The common folk make every effort to accommodate you and avoid your displeasure, and other people of high birth treat you as a member of the same social sphere. You can secure an audience with a local noble if you need to.\nVariant Feature: Retainers

If your character has a noble background, you may select this background feature instead of Position of Privilege.

You have the service of three retainers loyal to your family. These retainers can be attendants or messengers, and one might be a majordomo. Your retainers are commoners who can perform mundane tasks for you, but they do not fight for you, will not follow you into obviously dangerous areas (such as dungeons), and will leave if they are frequently endangered or abused."""

    dnd_dict.character_dict.get("features").append(feature)

def outlander_features():
    feature = """Feature: Origin

You've been to strange places and seen things that others cannot begin to fathom. Consider some of the distant lands you have visited, and how they impacted you. You can roll on the following table to determine your occupation during your time in the wild, or choose one that best fits your character.
d10 	Origin
1 	Forester
2 	Trapper
3 	Homesteader
4 	Guide
5 	Exile or outcast
6 	Bounty hunter
7 	Pilgrim
8 	Tribal nomad
9 	Hunter-gatherer
10 	Tribal marauder
Feature: Wanderer

You have an excellent memory for maps and geography, and you can always recall the general layout of terrain, settlements, and other features around you. In addition, you can find food and fresh water for yourself and up to five other people each day, provided that the land offers berries, small game, water, and so forth."""

    dnd_dict.character_dict.get("features").append(feature)

def pirate_features():
    feature = """Feature: Ship's Passage

When you need to, you can secure free passage on a sailing ship for yourself and your adventuring companions. You might sail on the ship you served on, or another ship you have good relations with (perhaps one captained by a former crewmate). Because you're calling in a favor, you can't be certain of a schedule or route that will meet your every need. Your DM will determine how long it takes to get where you need to go. In return for your free passage, you and your companions are expected to assist the crew during the voyage.\nVariant Sailor: Pirate

You spent your youth under the sway of a dread pirate, a ruthless cutthroat who taught you how to survive in a world of sharks and savages. You've indulged in larceny on the high seas and sent more than one deserving soul to a briny grave. Fear and bloodshed are no strangers to you, and you've garnered a somewhat unsavory reputation in many a port town.

If you decide that your sailing career involved piracy, you can choose the Bad Reputation feature below instead of the Ship's Passage feature.
Variant Feature: Bad Reputation

If your character has a sailor background, you may select this background feature instead of Ship's Passage.

No matter where you go, people are afraid of you due to your reputation. When you are in a civilized settlement, you can get away with minor criminal offenses, such as refusing to pay for food at a tavern or breaking down doors at a local shop, since most people will not report your activity to the authorities."""

    dnd_dict.character_dict.get("features").append(feature)

def sage_features():
    feature = """Feature: Specialty

To determine the nature of your scholarly training, roll a d8 or choose from the options in the table below.
d8 	Specialty
1 	Alchemist
2 	Astronomer
3 	Discredited academic
4 	Librarian
5 	Professor
6 	Researcher
7 	Wizard's apprentice
8 	Scribe
Feature: Researcher

When you attempt to learn or recall a piece of lore, if you do not know that information, you often know where and from whom you can obtain it. Usually, this information comes from a library, scriptorium, university, or a sage or other learned person or creature. Your DM might rule that the knowledge you seek is secreted away in an almost inaccessible place, or that it simply cannot be found. Unearthing the deepest secrets of the multiverse can require an adventure or even a whole campaign."""

    dnd_dict.character_dict.get("features").append(feature)

def sailor_features():
    feature = """Feature: Ship's Passage

When you need to, you can secure free passage on a sailing ship for yourself and your adventuring companions. You might sail on the ship you served on, or another ship you have good relations with (perhaps one captained by a former crewmate). Because you're calling in a favor, you can't be certain of a schedule or route that will meet your every need. Your DM will determine how long it takes to get where you need to go. In return for your free passage, you and your companions are expected to assist the crew during the voyage."""

    dnd_dict.character_dict.get("features").append(feature)

def soldier_features():
    feature = """Feature: Specialty

During your time as a soldier, you had a specific role to play in your unit or army. Roll a d8 or choose from the options in the table below to determine your role:
d8 	Specialty
1 	Officer
2 	Scout
3 	Infantry
4 	Cavalry
5 	Healer
6 	Quartermaster
7 	Standard bearer
8 	Support staff (cook, blacksmith, or the like)
Feature: Military Rank

You have a military rank from your career as a soldier. Soldiers loyal to your former military organization still recognize your authority and influence, and they defer to you if they are of a lower rank. You can invoke your rank to exert influence over other soldiers and requisition simple equipment or horses for temporary use. You can also usually gain access to friendly military encampments and fortresses where your rank is recognized."""

    dnd_dict.character_dict.get("features").append(feature)

def spy_features():
    feature = """Feature: Criminal Specialty

There are many kinds of criminals, and within a thieves' guild or similar criminal organization, individual members have particular specialties. Even criminals who operate outside of such organizations have strong preferences for certain kinds of crimes over others. Choose the role you played in your criminal life, or roll on the table below.
d8 	Specialty
1 	Blackmailer
2 	Burglar
3 	Enforcer
4 	Fence
5 	Highway robber
6 	Hired killer
7 	Pickpocket
8 	Smuggler
Feature: Criminal Contact

You have a reliable and trustworthy contact who acts as your liaison to a network of other criminals. You know how to get messages to and from your contact, even over great distances; specifically, you know the local messengers, corrupt caravan masters, and seedy sailors who can deliver messages for you.\nVariant Criminal: Spy

Although your capabilities are not much different from those of a burglar or smuggler, you learned and practiced them in a very different context: as an espionage agent. You might have been an officially sanctioned agent of the crown, or perhaps you sold the secrets you uncovered to the highest bidder."""

    dnd_dict.character_dict.get("features").append(feature)


def urban_bounty_hunter_features():
    feature = """Feature: Ear to the Ground

You are in frequent contact with people in the segment of society that your chosen quarries move through. These people might be associated with the criminal underworld, the rough-and-tumble folk of the streets, or members of high society. This connection comes in the form of a contact in any city you visit, a person who provides information about the people and places of the local area."""

    dnd_dict.character_dict.get("features").append(feature)

def urchin_features():

    feature = """Feature: City Secrets

You know the secret patterns and flow to cities and can find passages through the urban sprawl that others would miss. When you are not in combat, you (and companions you lead) can travel between any two locations in the city twice as fast as your speed would normally allow."""

    dnd_dict.character_dict.get("features").append(feature)


#Player classes
def artificer_features():
    feature = """
Optional Rule: Firearm Proficiency

If your Dungeon Master uses the rules on firearms in chapter 9 of the Dungeon Master's Guide and your artificer has been exposed to the operations of such weapons, your artificer is proficient with them.
Magical Tinkering

At 1st level, you learn how to invest a spark of magic in objects that would otherwise be mundane. To use this ability, you must tinker’s tools, or other artisan’s tools in hand. You then touch a Tiny nonmagical object as an action and give it one of the following magical properties of your choice:

    The object sheds bright light in a 5-foot radius and dim light for an additional 5 feet.
    Whenever tapped by a creature, the object emits a recorded message that can be heard up to 10 feet away. You utter the message when you bestow this property on the object, and the recording can be no more than 6 seconds long.
    The object continuously emits your choice of an odor or a nonverbal sound (wind, waves, chirping, or the like). The chosen phenomenon is perceivable up to 10 feet away.
    A static visual effect appears on one of the object’s surfaces. This effect can be a picture, up to 25 words of text, lines and shapes, or a mixture of these elements, as you like.

The chosen property lasts indefinitely. As an action, you can touch the object and end the property early.

You can give the magic of this feature to multiple objects, touching one object each time you use the feature, and a single object can bear only one of the properties at a time. The maximum number of objects you can affect with the feature at one time is equal to your Intelligence modifier (minimum of one object). If you try to exceed your maximum, the oldest property immediately ends, and then the new property applies.
"""

    dnd_dict.character_dict.get("features").append(feature)


def barbarian_features():
    feature = """
Rage

In battle, you fight with primal ferocity. On your turn, you can enter a rage as a bonus action.

While raging, you gain the following benefits if you aren't wearing heavy armor:

    You have advantage on Strength checks and Strength saving throws.
    When you make a melee weapon attack using Strength, you gain a bonus to the damage roll that increases as you gain levels as a barbarian, as shown in the Rage Damage column of the Barbarian table.
    You have resistance to bludgeoning, piercing, and slashing damage.

If you are able to cast spells, you can't cast them or concentrate on them while raging.

Your rage lasts for 1 minute. It ends early if you are knocked unconscious or if your turn ends and you haven't attacked a hostile creature since your last turn or taken damage since then. You can also end your rage on your turn as a bonus action.

Once you have raged the number of times shown for your barbarian level in the Rages column of the Barbarian table, you must finish a long rest before you can rage again."""


    dnd_dict.character_dict.get("features").append(feature)


def druid_features():
    feature = """Druidic

You know Druidic, the secret language of druids. You can speak the language and use it to leave hidden messages. You and others who know this language automatically spot such a message. Others spot the message's presence with a successful DC 15 Wisdom (Perception) check but can't decipher it without magic."""
    dnd_dict.character_dict.get("features").append(feature)



def monk_features():
    feature = """
Unarmored Defense

Beginning at 1st level, while you are wearing no armor and not wielding a shield, your AC equals 10 + your Dexterity modifier + your Wisdom modifier.
Martial Arts

At 1st level, your practice of martial arts gives you mastery of combat styles that use unarmed strikes and monk weapons, which are shortswords and any simple melee weapons that don't have the two-handed or heavy property.

You gain the following benefits while you are unarmed or wielding only monk weapons and you aren't wearing armor or wielding a shield:

    You can use Dexterity instead of Strength for the attack and damage rolls of your unarmed strikes and monk weapons.

    You can roll a d4 in place of the normal damage of your unarmed strike or monk weapon. This die changes as you gain monk levels, as shown in the Martial Arts column of the Monk table.

    When you use the Attack action with an unarmed strike or a monk weapon on your turn, you can make one unarmed strike as a bonus action. For example, if you take the Attack action and attack with a quarterstaff, you can also make an unarmed strike as a bonus action, assuming you haven't already taken a bonus action this turn.

Certain monasteries use specialized forms of the monk weapons. For example, you might use a club that is two lengths of wood connected by a short chain (called a nunchaku) or a sickle with a shorter, straighter blade (called a kama). Whatever name you use for a monk weapon, you can use the game statistics provided for the weapon on the Weapons page.
"""
    dnd_dict.character_dict.get("features").append(feature)

def paladin_features():
    feature = """ Divine Sense

The presence of strong evil registers on your senses like a noxious odor, and powerful good rings like heavenly music in your ears. As an action, you can open your awareness to detect such forces. Until the end of your next turn, you know the location of any celestial, fiend, or undead within 60 feet of you that is not behind total cover. You know the type (celestial, fiend, or undead) of any being whose presence you sense, but not its identity (the vampire Count Strahd von Zarovich, for instance). Within the same radius, you also detect the presence of any place or object that has been consecrated or desecrated, as with the Hallow spell.

You can use this feature a number of times equal to 1 + your Charisma modifier. When you finish a long rest, you regain all expended uses.
Lay on Hands

Your blessed touch can heal wounds. You have a pool of healing power that replenishes when you take a long rest. With that pool, you can restore a total number of hit points equal to your paladin level x 5.

As an action, you can touch a creature and draw power from the pool to restore a number of hit points to that creature. up to the maximum amount remaining in your pool.

Alternatively, you can expend 5 hit points from your pool of healing to cure the target of one disease or neutralize one poison affecting it. You can cure multiple diseases and neutralize multiple poisons with a single use of Lay on Hands, expending hit points separately for each one.

This feature has no effect on undead and constructs.
"""

    dnd_dict.character_dict.get("features").append(feature)


def ranger_features():
    feature = """
Favored Enemy

Beginning at 1st level, you have significant experience studying, tracking, hunting, and even talking to a certain type of enemy commonly encountered in the wilds.

Choose a type of favored enemy: beasts, fey, humanoids, monstrosities, or undead. You gain a +2 bonus to damage rolls with weapon attacks against creatures of the chosen type. Additionally, you have advantage on Wisdom (Survival) checks to track your favored enemies, as well as on Intelligence checks to recall information about them.

When you gain this feature, you also learn one language of your choice, typically one spoken by your favored enemy or creatures associated with it. However, you are free to pick any language you wish to learn.
Natural Explorer

You are a master of navigating the natural world, and you react with swift and decisive action when attacked. This grants you the following benefits:

• You ignore difficult terrain.

• You have advantage on initiative rolls.

• On your first turn during combat, you have advantage on attack rolls against creatures that have not yet acted.

In addition, you are skilled at navigating the wilderness. You gain the following benefits when traveling for an hour or more:

• Difficult terrain doesn’t slow your group’s travel.

• Your group can’t become lost except by magical means.

• Even when you are engaged in another activity while traveling (such as foraging, navigating, or tracking), you remain alert to danger.

• If you are traveling alone, you can move stealthily at a normal pace.

• When you forage, you find twice as much food as you normally would.

• While tracking other creatures, you also learn their exact number, their sizes, and how long ago they passed through the area.
"""

    dnd_dict.character_dict.get("features").append(feature)


def rogue_features():
    feature = """
Sneak Attack

Beginning at 1st level, you know how to strike subtly and exploit a foe's distraction. Once per turn, you can deal an extra 1d6 damage to one creature you hit with an attack if you have advantage on the attack roll. The attack must use a finesse or a ranged weapon.

You don't need advantage on the attack roll if another enemy of the target is within 5 feet of it, that enemy isn't incapacitated, and you don't have disadvantage on the attack roll.

The amount of the extra damage increases as you gain levels in this class, as shown in the Sneak Attack column of the Rogue table.
Thieves' Cant

During your rogue training you learned thieves' cant, a secret mix of dialect, jargon, and code that allows you to hide messages in seemingly normal conversation. Only another creature that knows thieves' cant understands such messages. It takes four times longer to convey such a message than it does to speak the same idea plainly.

In addition, you understand a set of secret signs and symbols used to convey short, simple messages, such as whether an area is dangerous or the territory of a thieves' guild, whether loot is nearby, or whether the people in an area are easy marks or will provide a safe house for thieves on the run.
"""

    dnd_dict.character_dict.get("features").append(feature)

def knowledge_cleric_feature():
    feature = """Blessings of Knowledge

At 1st level, you learn two languages of your choice. You also become proficient in your choice of two of the following skills: Arcana, History, Nature, or Religion.

Your proficiency bonus is doubled for any ability check you make that uses either of those skills."""
    dnd_dict.character_dict.get("player_class").append("Knowledge Domain")
    dnd_dict.character_dict.get("features").append(feature)
    dnd_language.double_language()
    added_spells = ['Command','Identify']
    dnd_dict.character_dict.get("first_level").append(added_spells)
# Used to double the proficiency of the ability check
    new_prof = (dnd_skills.prof_bonus * 2)
    i = 1
    while i < 3:
# If the player is proficient in all of these skills, pass.
        if dnd_skills.skills_dict['arcana']==dnd_class.RaceStats.stat_bonus(dnd_dict.character_dict['Stats']['intelligence']['mod'],dnd_skills.prof_bonus) and dnd_skills.skills_dict['history']==dnd_class.RaceStats.stat_bonus(dnd_dict.character_dict['Stats']['intelligence']['mod'],dnd_skills.prof_bonus) and dnd_skills.skills_dict['nature']==dnd_class.RaceStats.stat_bonus(dnd_dict.character_dict['Stats']['intelligence']['mod'],dnd_skills.prof_bonus) and dnd_skills.skills_dict['religion']==dnd_class.RaceStats.stat_bonus(dnd_dict.character_dict['Stats']['intelligence']['mod'],dnd_skills.prof_bonus):
            i+=2
            break
        else:
            while True:
                print(f'{i}/2')
                choice1 = input("Select the skill you want proficiency in:\n1) Arcana\n2) History\n3) Nature\n4) Religion\nEnter your Selection: ")
                if choice1 =='1':
                    if dnd_skills.skills_dict['arcana']==dnd_dict.character_dict['Stats']['intelligence']['mod']:
                        arc_mod = dnd_dict.character_dict['Stats']['intelligence']['mod']
                        updated_arc = dnd_class.RaceStats.stat_bonus(arc_mod, new_prof)
                        dnd_skills.skills_dict['arcana']=updated_arc
                        i+=1
                        break
                    elif dnd_skills.skills_dict['arcana']>dnd_dict.character_dict['Stats']['intelligence']['mod']:
                        print("Already proficient")
                        continue

                if choice1 =='2':
                    if dnd_skills.skills_dict['history']==dnd_dict.character_dict['Stats']['intelligence']['mod']:
                        his_mod = dnd_dict.character_dict['Stats']['intelligence']['mod']
                        updated_his = dnd_class.RaceStats.stat_bonus(his_mod, new_prof)
                        dnd_skills.skills_dict['history']=updated_his
                        i+=1
                        break
                    elif dnd_skills.skills_dict['history']>dnd_dict.character_dict['Stats']['intelligence']['mod']:
                        print("Already proficient")
                        continue

                if choice1 =='3':
                    if dnd_skills.skills_dict['nature']==dnd_dict.character_dict['Stats']['intelligence']['mod']:
                        nat_mod = dnd_dict.character_dict['Stats']['intelligence']['mod']
                        updated_nat = dnd_class.RaceStats.stat_bonus(nat_mod, new_prof)
                        dnd_skills.skills_dict['nature']=updated_nat
                        i+=1
                        break
                    elif dnd_skills.skills_dict['nature']>dnd_dict.character_dict['Stats']['intelligence']['mod']:
                        print("Already proficient")
                        continue

                if choice1 =='4':
                    if dnd_skills.skills_dict['religion']==dnd_dict.character_dict['Stats']['intelligence']['mod']:
                        rel_mod = dnd_dict.character_dict['Stats']['intelligence']['mod']
                        updated_rel = dnd_class.RaceStats.stat_bonus(rel_mod, new_prof)
                        dnd_skills.skills_dict['religion']=updated_rel
                        i+=1
                        break
                    elif dnd_skills.skills_dict['religion']>dnd_dict.character_dict['Stats']['intelligence']['mod']:
                        print("Already proficient")
                        continue

                else:
                    print("Invalid Selection")
                    continue

def life_cleric_feature():
    feature = """Bonus Proficiency

When you choose this domain at 1st level, you gain proficiency with heavy armor.
Disciple of Life

Also starting at 1st level, your healing spells are more effective. Whenever you use a spell of 1st level or higher to restore hit points to a creature, the creature regains additional hit points equal to 2 + the spell's level."""
    added_spells = ['Bless','Cure Wounds']
    dnd_dict.character_dict.get("first_level").append(added_spells)
    dnd_dict.character_dict.get("player_class").append("Life Domain")
    dnd_dict.character_dict.get("features").append(feature)
    armor_prof = ['Heavy Armor']
    dnd_dict.character_dict.get("Armor_Prof").append(armor_prof)

def light_cleric_feature():
    feature = """Bonus Cantrip

When you choose this domain at 1st level, you gain the Light cantrip if you don't already know it.
Warding Flare

Also at 1st level, you can interpose divine light between yourself and an attacking enemy. When you are attacked by a creature within 30 feet of you that you can see, you can use your reaction to impose disadvantage on the attack roll, causing light to flare before the attacker before it hits or misses. An attacker that can't be blinded is immune to this feature.

You can use this feature a number of times equal to your Wisdom modifier (a minimum of once). You regain all expended uses when you finish a long rest."""

    added_spells = ['Burning Hands', 'Faerie Fire']
    dnd_dict.character_dict.get("first_level").append(added_spells)
    dnd_dict.character_dict.get("player_class").append("Light Domain")
    dnd_class.RaceStats.pass_repeat_function(dnd_dict.character_dict.get("cantrip"),'Light')
    dnd_dict.character_dict.get("features").append(feature)

def nature_cleric_feature():
    feature = """Acolyte of Nature

At 1st level, you learn one cantrip of your choice from the druid spell list. You also gain proficiency in one of the following skills of your choice: Animal Handling, Nature, or Survival.
Bonus Proficiency

Also at 1st level, you gain proficiency with heavy armor."""
    added_spells = ['Animal Friendship', 'Speak with Animals']
    dnd_dict.character_dict.get("first_level").append(added_spells)
    dnd_dict.character_dict.get("player_class").append("Life Domain")
    dnd_dict.character_dict.get("player_class").append("Nature Domain")
    dnd_dict.character_dict.get("features").append(feature)
    armor_prof = ['Heavy Armor']
    dnd_dict.character_dict.get("Armor_Prof").append(armor_prof)

# If the player is proficient in all of these skills, pass.
    if dnd_skills.skills_dict['animal_handling']==dnd_class.RaceStats.stat_bonus(dnd_dict.character_dict['Stats']['wisdom']['mod'],dnd_skills.prof_bonus) and dnd_skills.skills_dict['nature']==dnd_class.RaceStats.stat_bonus(dnd_dict.character_dict['Stats']['intelligence']['mod'],dnd_skills.prof_bonus) and dnd_skills.skills_dict['survival']==dnd_class.RaceStats.stat_bonus(dnd_dict.character_dict['Stats']['wisdom']['mod'],dnd_skills.prof_bonus):
        pass
    else:
        while True:
            choice = input("Choose the skill you want proficiency in:\n1) Animal Handling\n2) Nature\n3) Survival\nEnter your selection: ")
            if choice=='1':
                if dnd_skills.skills_dict['animal_handling']==dnd_dict.character_dict['Stats']['wisdom']['mod']:
                    anm_mod = dnd_dict.character_dict['Stats']['wisdom']['mod']
                    updated_anm = dnd_class.RaceStats.stat_bonus(anm_mod,dnd_skills.prof_bonus)
                    dnd_skills.skills_dict['animal_handling']=updated_anm
                    break
                elif dnd_skills.skills_dict['animal_handling']>dnd_dict.character_dict['Stats']['wisdom']['mod']:
                    print("Already Proficient")
                    continue
            elif choice=='2':
                if dnd_skills.skills_dict['nature']==dnd_dict.character_dict['Stats']['intelligence']['mod']:
                    nat_mod = dnd_dict.character_dict['Stats']['intelligence']['mod']
                    updated_nat = dnd_class.RaceStats.stat_bonus(nat_mod,dnd_skills.prof_bonus)
                    dnd_skills.skills_dict['nature']=updated_nat
                    break
                elif dnd_skills.skills_dict['nature']>dnd_dict.character_dict['Stats']['intelligence']['mod']:
                    print("Already Proficient")
                    continue
            elif choice=='3':
                if dnd_skills.skills_dict['survival']==dnd_dict.character_dict['Stats']['wisdom']['mod']:
                    sur_mod = dnd_dict.character_dict['Stats']['wisdom']['mod']
                    updated_sur = dnd_class.RaceStats.stat_bonus(sur_mod,dnd_skills.prof_bonus)
                    dnd_skills.skills_dict['survival']=updated_sur
                    break
                elif dnd_skills.skills_dict['survival']>dnd_dict.character_dict['Stats']['wisdom']['mod']:
                    print("Already Proficient")
                    continue
            else:
                print("Invalid Selection")
                continue

def tempest_cleric_feature():
    feature = """Bonus Proficiencies

At 1st level, you gain proficiency with martial weapons and heavy armor.
Wrath of the Storm

Also at 1st level, you can thunderously rebuke attackers. When a creature within 5 feet of you that you can see hits you with an attack, you can use your reaction to cause the creature to make a Dexterity saving throw. The creature takes 2d8 lightning or thunder damage (your choice) on a failed saving throw, and half as much damage on a successful one.

You can use this feature a number of times equal to your Wisdom modifier (a minimum of once). You regain all expended uses when you finish a long rest."""
    added_spells = ['Fog Cloud', 'Thunderwave']
    dnd_dict.character_dict.get("first_level").append(added_spells)
    dnd_dict.character_dict.get("player_class").append("Tempest Domain")
    armor_prof = ['Heavy Armor']
    weapon_prof = ['Martial Weapons']
    dnd_dict.character_dict.get("Weapon_Prof").append(weapon_prof)
    dnd_dict.character_dict.get("Armor_Prof").append(armor_prof)
    dnd_dict.character_dict.get("features").append(feature)

def trickery_cleric_feature():
    feature = """Blessing of the Trickster

Starting when you choose this domain at 1st level, you can use your action to touch a willing creature other than yourself to give it advantage on Dexterity (Stealth) checks. This blessing lasts for 1 hour or until you use this feature again."""
    added_spells = ['Charm Person', 'Disguise Self']
    dnd_dict.character_dict.get("first_level").append(added_spells)
    dnd_dict.character_dict.get("player_class").append("Trickery Domain")
    dnd_dict.character_dict.get("features").append(feature)

def war_cleric_feature():
    feature = """Bonus Proficiency

At 1st level, you gain proficiency with martial weapons and heavy armor.
War Priest

From 1st level, your god delivers bolts of inspiration to you while you are engaged in battle. When you use the Attack action, you can make one weapon attack as a bonus action.

You can use this feature a number of times equal to your Wisdom modifier (a minimum of once). You regain all expended uses when you finish a long rest."""
    added_spells = ['Divine Favor', 'Shield of Faith']
    dnd_dict.character_dict.get("first_level").append(added_spells)
    dnd_dict.character_dict.get("player_class").append("War Domain")
    armor_prof = ['Heavy Armor']
    weapon_prof = ['Martial Weapons']
    dnd_dict.character_dict.get("Weapon_Prof").append(weapon_prof)
    dnd_dict.character_dict.get("Armor_Prof").append(armor_prof)
    dnd_dict.character_dict.get("features").append(feature)

def draconic_sorcerer_feature():
    feature = """Dragon Ancestor

At 1st level, you choose one type of dragon as your ancestor. The damage type associated with each dragon is used by features you gain later.
Draconic Ancestry
Dragon Color 	Damage Type
Black 	Acid
Blue 	Lightning
Brass 	Fire
Bronze 	Lightning
Copper 	Acid
Gold 	Fire
Green 	Poison
Red 	Fire
Silver 	Cold
White 	Cold

You can speak, read, and write Draconic. Additionally, whenever you make a Charisma check when interacting with dragons, your proficiency bonus is doubled if it applies to the check.
Draconic Resilience

As magic flows through your body, it causes physical traits of your dragon ancestors to emerge. At 1st level, your hit point maximum increases by 1 and increases by 1 again whenever you gain a level in this class.

Additionally, parts of your skin are covered by a thin sheen of dragon-like scales. When you aren't wearing armor, your AC equals 13 + your Dexterity modifier."""
    dnd_dict.character_dict.get("player_class").append("Draconic Bloodline")
    dnd_dict.character_dict.get("features").append(feature)

def wild_magic_sorcerer_feature():
    feature = """Wild Magic Surge

Starting when you choose this origin at 1st level, your spellcasting can unleash surges of untamed magic. Immediately after you cast a sorcerer spell of 1st level or higher, the DM can have you roll a d20. If you roll a 1, roll on the Wild Magic Surge table to create a random magical effect.
Tides of Chaos

Starting at 1st level, you can manipulate the forces of chance and chaos to gain advantage on one attack roll, ability check, or saving throw. Once you do so, you must finish a long rest before you can use this feature again.

Any time before you regain the use of this feature, the DM can have you roll on the Wild Magic Surge table immediately after you cast a sorcerer spell of 1st level or higher. You then regain the use of this feature."""
    dnd_dict.character_dict.get("player_class").append("Wild Magic")
    dnd_dict.character_dict.get("features").append(feature)

def archfey_warlock_feature():
    feature = """Fey Presence

Starting at 1st level, your patron bestows upon you the ability to project the beguiling and fearsome presence of the fey. As an action, you can cause each creature in a 10-foot cube originating from you to make a Wisdom saving throw against your warlock spell save DC. The creatures that fail their saving throws are all charmed or frightened by you (your choice) until the end of your next turn.

Once you use this feature, you can't use it again until you finish a short or long rest."""
    dnd_dict.character_dict.get("player_class").append("Archfey Patron")
    dnd_dict.character_dict.get("features").append(feature)
    dnd_magic.archfey_warlock_magic()

def fiend_warlock_feature():
    feature = """Dark One's Blessing

Starting at 1st level, when you reduce a hostile creature to 0 hit points, you gain temporary hit points equal to your Charisma modifier + your warlock level (minimum of 1)."""
    dnd_dict.character_dict.get("player_class").append("Fiend Patron")
    dnd_dict.character_dict.get("features").append(feature)
    dnd_magic.fiend_warlock_magic()

def goo_warlock_feature():
    feature = """Awakened Mind

Starting at 1st level, your alien knowledge gives you the ability to touch the minds of other creatures. You can telepathically speak to any creature you can see within 30 feet of you. You don't need to share a language with the creature for it to understand your telepathic utterances, but the creature must be able to understand at least one language."""
    dnd_dict.character_dict.get("player_class").append("Great Old One Patron")
    dnd_dict.character_dict.get("features").append(feature)
    dnd_magic.goo_warlock_magic()

