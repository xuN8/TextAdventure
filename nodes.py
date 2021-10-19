from classes import *

##-- 1 --##
go_outside = Node(
  "Go outside",
  "You went outside",
  "You see a restaurant"
)

stay_outside = Node(
  "Stay outside",
  "You shrug it off like a champ and remain outside",
  "The scent of delicious food taunts you, tempting you to give in"
)

go_inside = Node(
  "Go inside",
  "You Naruto-ran through the door with blinding speed",
  "You enter the waiting room and see a row of chairs"
)

##-- 2 --##
waiter = "waitress"
waiter_pronoun = "she"
waiter_pronoun2 = "her"
waiter_name = "Lucianne"
waiter_last_initial = "H"
waiter_greet = 'Before long, the %s comes up to you\n"Hello, my name is %s and I will be taking care of you for today. Follow me right this way :)"\n Your eyes widen in shock. No, this can\'t be happening. It has to be a coincidence... The %s doesn\'t seem to notice your surprise and continues talking. "How many?"' %(waiter, waiter_name, waiter)

sit = Node(
  "Set yo bum on dat chair",
  "You sat yo bum on dat chair like a boss, the cushion is very uncomfortable",
  waiter_greet
)

stand = Node(
  "Remain standing",
  "You walk to the corner and stare at your phone",
  waiter_greet
)

##-- 3 --##
give_waiter_sass = Node(
  "Act sassy",
  '"How many does it look like to you, huh?"',
  '%s seems taken aback but immediately composes %sself.\n"Alright, so just one. Right this way please! :D"' %(waiter_pronoun2, waiter_pronoun2)
)

ignore_waiter = Node(
  "Ignore " + waiter_name,
  "You spit on the pristine tile floor and pretend you did'nt hear. Huh, seems like someone already patooied in the same spot.",
  'The waiter looks oddly offended.\n"Helllooo? Can you hear me?? Talk to me please. :((("'
)

give_waiter_sarcasm = Node(
  "Act sarcastic",
  '"Oh yeah, I have like FOUR kids in the car and not to mention my parents are coming soon and also my fifth uncle twice removed... So like a 60-seat table would be *FAAntaStic* if you\'ve got one"',
  '%s is somehow unphased and actually seems charmed by your reply, much to your annoyance.\n"table for 60, huh? I\'ve dealt with bigger. Follow me ;)"' %waiter_name
)

reply_to_waiter = Node(
  "Respond like a normal person",
  "Uh, it's just me.",
  '"Execellent! Right this way! :D"'
)

interrogate_waiter = Node(
  "Interrogate %s for %s last initial" %(waiter_name, waiter_pronoun2),
  '"Ok WHAT\'S your last initial you ugly potato? If it\'s H I swear..."',
  '"Yeah, it\'s Hum-... H. Why would you want to know?" Before you can answer %s shrugs and gestures you to follow her. Oh no, it\'s real.' %waiter_pronoun
)

##-- 4 --##
follow_waiter = Node(
  "Follow " + waiter_name,
  "You roll your eyes and start shuffling behind the %s since she probably knos da wae, or at least better than Knuckles." %waiter,
  "The %s leads you down the hallway into the dining room. It appears moderately busy, but there is still a vacant table left. %s stops suddenly and makes an exaggerated gesture towards it." %(waiter, waiter_name)
)

stay_in_waiting_room = Node(
  "Keep yo bum on dat chair or uh, keep yo fet on da flor... whatever ur doing rn",
  "You just stay put like the rude person that you are. %s keeps walking for a bit until %s realizes that you're still there. %s flips out and Mr. Bailey-jogs back looking chilishly upset" %(waiter_name, waiter_pronoun, waiter_pronoun),
  '"Um, follow me please?"'
)

##-- 5 --##
accept_table = Node(
  "Accept table",
  '"Looks ok... I guess"\nYou flick one of the tacky wooden chairs and it wobbles slightly due to the uneven legs.',
  '"Fantasic! Now have a seat like a good person and look at the menu, ok? I\'ll be back in a moment to take your order."'
)

refuse_table = Node(
  "Refuse table",
  '"Naw man, what even is this excuse for a table? Have you even seen that chair? It looks like a distressed giraffe was trying to do the dumb "R-O-C-K" jumping jacks only to die cringing from Fonville screaming "wHerE\'s mY sUPeRsUiT?"! How am I supposed to sit on that???"',
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

  MEALS:
  Papas Fritas Mezclada con Pollo
  Sushi Viejo en Halado
  Sweet Madame
  Vegan Vegetarian Kosher Non-GMO Gluten-Free Fat-Free Hormone-Free Low-Cholersterol Free-Range Gourmet Burger
  Green Eggs and Ham

  DRINKS:
  Watermelon Switch
  La Croix
  Fat Free Chocolate Milk
  Low Fat Milk
'''

look_at_menu = TextNode(
  "Look at big boi menu",
  "You finish reading the menu, satisfied with your decision.",
  "You glance up from the table and see that the %s is back." %waiter,
  "You plop yourself down and grab the worn, oily menu from the table." + menu
)

look_at_phone = Node(
  "Look at your phone",
  "Just to mess with %s, you look at your phone instead." %waiter_pronoun2,
  "%s pretends not to notice and walks away. Thank Bazuki, %s's gone.\nYou check your Discord for messages but there are none.\nMight want to look at that menu by now..." %(waiter_name, waiter_pronoun)
)

##-- 7 --##
def include_result(string, text_node):
  string += ''.join(text_node.get_result())

order_now = Node(
  "Order now",
  "You slam your fist on the table as you demand your entrees.",
  "%s visibily flinches at each fist-slam and seems like %s is about to faint. %s frantically scribbles down your order and runs off." %(waiter_name, waiter_pronoun, waiter_pronoun),
  # include_result,
  # execution,
  # look_at_menu
)

order_later = Node(
  "Order later",
  '"Go away, bozo. I\'m not done looking." You start making odd hand motions and gestures as if to ward off evil spirits.',
  'The %s backs off, buying you some more time to yourself.\nAfter some time, %s comes back.' %(waiter, waiter_pronoun)
)

