from nodes import *

# BEGINNING
responses_to_waiter = (
  give_waiter_sass,
  ignore_waiter,
  give_waiter_sarcasm,
  reply_to_waiter,
  interrogate_waiter
)

# Give the same options for each response to the waiter's greeting
follow_or_stay = (
  follow_waiter,
  stay_in_waiting_room.choices(
    follow_waiter,
    # Create a loop to force player to follow the waiter
    ignore_waiter.choices(ignore_waiter, follow_waiter)
  )
)
for response in responses_to_waiter:
  response.choices(*follow_or_stay)


go_outside.choices(
  stay_outside.choices(
    go_inside,
    stay_outside
  ),
  go_inside. choices(
    sit.choices(*responses_to_waiter),
    stand.choices(*responses_to_waiter)
  )
)

# DINING ROOM
follow_waiter.choices(
  # Force player to accept the table
  refuse_table.choices(
    accept_table.choices(
      look_at_menu.choices(
        order_now,
        order_later.choices(order_later, order_now)
      ),
      look_at_phone.choices(look_at_phone, look_at_menu),
      play_with_knives.choices(
        run_to_another_table.choices(
          play_with_knives,
          obey.choices(accept_table)
        ),
        obey
      )
    )
  ),
  accept_table
)

reactions_to_getting_caught = (
  defense_mode.choices(accept_defeat_and_take_food),
  accept_defeat_and_take_food
)

order_now.choices(
  do_activities_on_kids_menu.choices(*reactions_to_getting_caught),
  play_on_phone.choices(*reactions_to_getting_caught)
)

accept_defeat_and_take_food.choices(
  reject_food.choices(
    accept_food,
    order_now
  ),
  accept_food.choices(
    eat.choices(
      keep_eating.choices(
        keep_eating, 
        finish_eating
      ),
      finish_eating.choices(
        pay.choices(
          give_tip.choices(leave_restaurant),
          no_tip.choices(give_tip)
        ),
        no_pay.choices(pay)
      )
    )
  )
)