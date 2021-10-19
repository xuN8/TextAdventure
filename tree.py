from nodes import *

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

# Main tree
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

follow_waiter.choices(
  # Force player to accept the table
  refuse_table.choices(
    accept_table.choices(
      look_at_menu.choices(
        order_now,
        order_later.choices(order_later, order_now)
      ),
      look_at_phone.choices(look_at_phone, look_at_menu)
    )
  ),
  accept_table
)