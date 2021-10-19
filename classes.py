'''
Example Node go_outside:
...
1: Stay inside
2: Go outside
2
You went outside
You see a restaurant
1: Go inside
2: Stay outside
1

go_outside = Node(
  menu = "Go outside",
  execution = "You went outside",
  prompt = "You see a restaurant",
  children = [go_inside, stay_outside]
)
'''
class Node:

  def __init__(self, menu, execution, prompt, callback=None, *args):
    self.menu = menu
    self.execution = execution
    self.prompt = prompt
    self.callback = callback
    self.children = []
    self.args = args

  def execute(self):
    if self.callback:
      print("CALLBACK")
      print(self.args)
      self.callback(*self.args)

    # Print output text
    print("%s\n%s\n" %(self.execution, self.prompt))

    children = self.children or []
    if len(children) > 0:
      # Add options to menu
      menu = ""
      for i in range(len(children)):
        menu += str(i+1) + ": " + children[i].menu + "\n"

      # Make sure the user entered a valid input
      try:
        # Get input
        choice = input(menu)

        # Process input
        if choice:
          index = int(choice)-1
          children[index].execute()
      except:
        print("Oh noes, I think you messed up. Otra vez?")
        self.execute()
    else:
      print("The End")

  def choices(self, *args):
    self.children = list(args)
    return self   # So that this function can be nested in decision tree

class TextNode(Node):
  def __init__(self, menu, execution, prompt, text_prompt):
    super().__init__(menu, execution, prompt)
    self.text_prompt = text_prompt
    self.result = []
  
  def execute(self):
    try:
      menu_directions = '\nType the entrees you want separated by commas. (Ex: "Rotten Flesh,Sweet Madame,La Croix)\n'
      self.result = list(input(self.text_prompt + menu_directions).split(","))
    except:
      self.execute()
    super().execute()
  
  def get_result(self):
    return self.result