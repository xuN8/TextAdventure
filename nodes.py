from classes import *

##-- 1 --##
go_outside = Node(
  "",
  "It's a cloudy day.\nYou're starving, but you don't feel like going home to eat.",
  "You scan your surroundings and catch sight of a new restaurant that just opened recently.\nYou've never been there before."
)

stay_outside = Node(
  "Stay outside",
  "You shrug it off like a champ and remain outside.",
  "The scent of delicious food taunts you, tempting you to give in."
)

go_inside = Node(
  "Go inside",
  "You Naruto-ran through the door with blinding speed.",
  "You enter the waiting room and see a row of chairs."
)

##-- 2 --##
waiter = "waitress"
waiter_he = "she"
waiter_him = "her"
waiter_name = "Lucianne"
waiter_last = "Humphrey"
waiter_greet = 'Before long, the %s comes up to you\n"Hello, my name is %s and I will be taking care of you for today. Follow me right this way :)"\nYour eyes widen in shock. No, this can\'t be happening. It has to be a coincidence... The %s doesn\'t seem to notice your surprise and continues talking. "How many?"' %(waiter, waiter_name, waiter)

sit = Node(
  "Set yo bum on dat chair",
  "You sat yo bum on dat chair like a boss, the cushion is very uncomfortable.",
  waiter_greet
)

stand = Node(
  "Remain standing",
  "You walk to the corner and stare at your phone.",
  waiter_greet
)

##-- 3 --##
give_waiter_sass = Node(
  "Act sassy",
  '"How many does it look like to you, huh?"',
  '%s seems taken aback but immediately composes %sself.\n"Alright, so just one. Right this way please! :D"' %(waiter_him, waiter_him)
)

ignore_waiter = Node(
  "Ignore " + waiter_name,
  "You spit on the pristine tile floor and pretend you didn't hear.\nHuh, seems like someone already patooied in the same spot.",
  'The waiter looks oddly offended.\n"Helllooo? Can you hear me?? Talk to me please. :((("'
)

give_waiter_sarcasm = Node(
  "Act sarcastic",
  '"Oh yeah, I have like FOUR kids in the car and not to mention my parents are coming soon and also my fifth uncle twice removed...\nSo like a 60-seat table would be *FAAntaStic* if you\'ve got one"',
  '%s is somehow unphased and actually seems charmed by your reply, much to your annoyance.\n"table for 60, huh? I\'ve dealt with bigger. Follow me ;)"' %waiter_name
)

reply_to_waiter = Node(
  "Respond like a normal person",
  "Uh, it's just me.",
  '"Execellent! Right this way! :D"'
)

interrogate_waiter = Node(
  "Interrogate %s for %s last initial" %(waiter_name, waiter_him),
  '"Ok WHAT\'S your last initial you ugly potato?\nIf it\'s H I swear..."',
  f'"Yeah, it\'s {waiter_last[0:3]}-... {waiter_last[0]}.\nWhy would you want to know?"\nBefore you can answer {waiter_he} shrugs and gestures you to follow her.\nOh no, it\'s real.'
)

##-- 4 --##
follow_waiter = Node(
  "Follow " + waiter_name,
  "You roll your eyes and start shuffling behind the %s since she probably knos da wae,\nor at least better than Knuckles." %waiter,
  "The %s leads you down the hallway into the dining room.\nIt appears moderately busy, but there is still a vacant table left.\n%s stops suddenly and makes an exaggerated gesture towards it." %(waiter, waiter_name)
)

stay_in_waiting_room = Node(
  "Keep yo bum on dat chair or uh, keep yo fet on da flor... whatever ur doing rn",
  "You just stay put like the rude person that you are.\n%s keeps walking for a bit until %s realizes that you're still there.\n%s flips out and Mr. Bailey-jogs back looking childishly upset" %(waiter_name, waiter_he, waiter_he),
  '"Um, follow me please?"'
)

##-- 5 --##
accept_table = Node(
  "Accept table",
  '"Looks ok... I guess"\nYou flick one of the tacky wooden chairs and it wobbles slightly due to the uneven legs.',
  '"Fantasic!\nNow have a seat like a good person and look at the menu, ok?\nI\'ll be back in a moment to take your order."'
)

refuse_table = Node(
  "Refuse table",
  '"Naw man, what even is this excuse for a table?\nHave you even seen that chair?\nIt looks like a distressed giraffe was trying to do the dumb "R-O-C-K" jumping jacks\nonly to die cringing from Fonville screaming "wHerE\'s mY sUPeRsUiT?"!\nHow am I supposed to sit on that???"',
  '%s frowns.\n"Sorry, but there aren\'t any other tables left, you\'ll have to take this one."' %waiter_name
)

##-- 6 --##
menu = '''
  APPETIZERS:
  Rotten Flesh
  Rick Roll
  Tide Pods
  Paimon
  SPAM
  Berries and Cream
  Tweaks Bar
  Pog Chips

  MEALS:
  Papas Fritas Mezclada con Pollo
  Sushi Viejo en Halado
  Sweet Madame
  Vegan Vegetarian Kosher Non-GMO Gluten-Free Fat-Free Hormone-Free Low-Cholersterol Free-Range Gourmet Burger
  Green Eggs and Ham

  DRINKS:
  Black Coffee Slurpee
  Watermelon Switch
  La Croix
  Fat Free Chocolate Milk
  Low Fat Milk
  Bloxy-Cola
'''

look_at_menu = Node(
  "Look at big boi menu",
  "You settle down and open up the menu.",
  "You finish reading the menu, satisfied with your decision.\nYou glance up from the table and see that the %s is back." %waiter,
  lambda: real_print(menu)
)

look_at_phone = Node(
  "Look at your phone",
  "Just to mess with %s, you look at your phone instead." %waiter_him,
  "%s pretends not to notice and walks away.\nThank Bazuki, %s's gone.\nYou check your Discord for messages but there are none.\nMight want to look at that menu by now..." %(waiter_name, waiter_he)
)

play_with_knives = Node(
  "Play with those shiny pointy things on the table",
  f"You jump onto the table and immediately grab the knives.\nYou wave them around dangerously while making pirate noises, causing the {waiter} step to back a little.",
  f"{waiter_name} gives you a stern look, like a mother trying to scold her children.\nWell, they are quite sharp, so you might want to be careful with those..."
)

##-- 7 --##
def include_result(string, text_node):
  string += ''.join(text_node.get_result())

order_now = Node(
  "Order now",
  "You slam your fist on the table as you demand your entrees.",
  "%s visibily flinches at each fist-slam and seems like %s is about to faint.\n%s frantically scribbles down your order and runs off.\nIt's just a matter of time before the food arrives." %(waiter_name, waiter_he, waiter_he),
  # include_result,
  # execution,
  # look_at_menu
)

order_later = Node(
  "Order later",
  '"Go away, bozo. I\'m not done looking."\nYou start making cryptic hand motions and gestures as if to ward off the devil.',
  'The %s backs off, buying you some more time to yourself.\nAfter some time, %s comes back.' %(waiter, waiter_he)
)

obey = Node(
  f"Stop messing with {waiter_name}",
  "Rembering the sacred oath of Kelso's Choices,\nthou finalee giveths in to thou's reprehensible deeds like a good lad.",
  f"The {waiter} smiles weakly,\nclearly exhausted from working her facial muscles so much.\nYou follow {waiter_name} back to your table without resistance."
)

##-- 8 --##
run_to_another_table = Node(
  "Run and hide at another table",
  f'Without warning, you launch youself off the table, knives spinning in slow-motion behind you.\nBefore Ms. Trombetta can recite "In Lak\'ech Tú eres mi otro yo,"\nyou yeet yourself arcoss the room to another table.\n{waiter_name} trails behind via the ancient art of Mr. Bailey jog,\nbut it is no use; you are just too fast.',
  "You hide behind the people sitting there,\ncatching a glimpse of even more shiny pointy things."
)

do_activities_on_kids_menu = Node(
  "Do activities on the kid's menu",
  f"Since you don't have anything better to do, you get to work on the kid's menu.\nAt first you find it insulting that {waiter_name} would include such a thing that was clearly designed for clueless under-developed youth,\nbut even the adults have to entertain themselves somehow...",
  f"Right before you could finish the final cross-word puzzle,\n{waiter_name} walks in on you. Oh no.\nYou frantically scramble to grab all the endless expanse of activity sheets and broken crayons as {waiter_name}'s ridiculous grin grows wider and wider than that of the Chesire Cat - but alas, it is no use.\nYou were caught in 4k."
)

play_on_phone = Node(
  "Play on your phone",
  'You bust out your phone. What should you play? You think for a moment, but the answer is all too obvious. Calculator app for life. The numbers just get bigger and bigger as you spam operations at insane speeds.\n13, 69, 5417... 8000... 3.14e100...\nAnd then, as always, it comes to the dreaded end. The final straw. The last stand. You slowly lower your trembling finger, anticipation rising like a storm. Sparks fly. The ground begins to shake. Your face grows numb. You begin to scream. And then... you push the button.\nERROR\n"LET\'S GOOOOOOOOOO!!!\n You set your phone on the table in triumph. Best. Game. Ever.',
  f"You look behind you and see a ridiculous grin on {waiter_name}'s face.\nThe {waiter} was there the whole time, watching you.\nYou narrow your eyes in fury. What a creep."
)

##-- 9 --##
defense_mode = Node(
  "Activate defense mode",
  'Ye can\'t have this, naw.\nYeh lower yer head and clench yer fists, dark shadows forming \'round yer eyes.\n"What yeh just saw... wers a lie.\nYour eyebawls be playin\' tricks on you, ya hear?\nDirty tricks.\nDirtier theen a lunch tray. Dirtier theen teh underside ofa desk.\nDIRTiER THAN TeH wORDS THAT WIlL COME OUT o\' MAH MoUTH iF Ah sEE YOU DO tHaT AG\'IN...\nunderstand?"',
  f'{waiter_name} just smirks. "Yeah, suuuuuurre ;)"'
)

accept_defeat_and_take_food = Node(
  "Accept defeat and take the food",
  f'You let out a sigh.\nWhatever, it\'s not like you have anything to lose.\n{waiter_name} wouldn\'t dare to use that against you... right?\nYou sigh once again.\n"Just give me the food, doofus."',
  f"{waiter_name} giggles and hands over your order."
)

##-- 9 --##
reject_food = Node(
  "Channel your inner Karen",
  f'You stare at the dishes.\nThere are all distgusting.\nFilthy.\nGarbage.\nYou resist the urge to gag.\nFigures, anything that {waiter_name} touches is instantly trash.\nYour eye twitches. Your hair... what\'s happening to it?\nWhy did your clothes just change out of nowhere?\nWithout warning, you grab the plates and slam them on the floor.\nThey shatter. Food spills everywhere, soiling the floor and even your mittens - no pie for you.\n"where. Is. tHE. MANAGER!"',
  f'You force the {waiter} into a headlock until {waiter_he} speaks with a rasp.\n"Ms. Kelly\'s out, but I can tell chef Vance to make something else for you."\nYour heart skips a beat. Those names...'
)

accept_food = Node(
  "Accept food",
  'You grudgingly take the lame excuse for food with a sneer.\n"Mark my words..."',
  "The food doesn't look all that bad.\nSeems like they got the order right."
)

##-- 10 --##
eat = Node(
  "Dig in like it'z chik'n din",
  "You take a few spoonfuls and shove them into your mouth.",
  "There's still more left."
)

keep_eating = Node(
  "Keep eatin' like yer hart's a beatn'",
  "It's not over yet, you've still got room. You wolf down a few more mouthfuls.",
  "Ugh, it seems endless."
)

finish_eating = Node(
  "Stawp gobblin' cuz yer belly's a-wobblin'",
  "Your belly is indeed a-wobblin' so you squeeze in one last bite before you explode.",
  f"Just in the nick of time, {waiter_name} returns with your paycheck.\nGolly, it's like they have security cameras in here er somethin'..."
)

##-- 11 --##
pay = Node(
  f"Surrender your shillings to redcoat {waiter_name}",
  "You reach into your purse and produce a handful of shillings.\nYou slap them on the table and slide them over.",
  f'And just like that, the {waiter} robs you of your month\'s worth of earings,\ncounting them all with a stinginess not unlike that of Scrooge McDuck.\n{waiter_name} looks up with the slyness of a fox.\n"Would you care to give a *totally* optional tip?"'
)

no_pay = Node(
  "Up and leave without paying",
  f"And just like that, you attempt to walk out.\n{waiter_name} follows you, but you quicken your pace.",
  f"Just as you exit through the door, {waiter_name} catches up and trips you, rendering you immobile.\nOh well, that's karma for ya."
)

##-- 12 --##
give_tip = Node(
  "Give tip",
  "You grit your teeth as you reach deep into the dark depths of your pockets.\nYour arm slowly sinks deeper and deeper until only your shoulder is left.\nHow your pocket is that big, you have no idea.\nAfter grabbing blindly at thin air, your hand brushes against a few spare coins.\nBingo.",
  f"Your arm resurfaces and you hand over the tip.\nThe {waiter} greedily snatches it from your palm, satisfied." 
)

no_tip = Node(
  "No tip",
  f'The {waiter} frowns.\n"So you can\'t even spare a penny?\nJust a little something to show us your immense gratitude for our outstanding services?\nWe work really hard here at the restaurant you know... "',
  f"You open your mouth to object,\nbut {waiter_name} whips out a Nerf, placing you at gunpoint.\nSo much for \"optional.\""
)

##-- 13 --##
leave_restaurant = Node(
  "Skedaddle",
  f"{waiter_name} hands you your reciept and sees you out the door.",
  'As you walk back home, you think to yourself,\n"What a wacko restaurant, definitely not going back there again..."'
)