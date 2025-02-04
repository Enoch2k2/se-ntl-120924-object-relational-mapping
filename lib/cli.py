from pet import Pet
from owner import Owner
import ipdb

from helpers import clear, pause, line_space, invalid_choice

class Cli:
  def start(self):
    clear()
    print("=======================================")
    print("|| Welcome to the Flatiron Pet Shop! ||")
    print("=======================================")
    line_space()
    pause()

    self.menu()

  def menu(self):
    clear()
    print("===================")
    print("|| Pet Shop Menu ||")
    print("===================")
    line_space()
    print("1. List All Owners")
    print("2. Create Owner")
    print("3. Select Owner")
    print("4. Delete Owner")
    print("'exit' to exit program")
    line_space()
    self.menu_selection()
  
  def menu_selection(self):
    user_input = input("Enter Selection: ")
    if user_input == "1":
      self.list_owners()
      line_space()
      pause()
      self.menu()
    elif user_input == "2":
      self.create_owner()
      line_space()
      pause()
      self.menu()
    elif user_input == "3":
      self.select_owner()
      line_space()
      pause()
      self.menu()
    elif user_input == "4":
      self.delete_owner()
      line_space()
      pause()
      self.menu()
    elif user_input == "exit":
      clear()
      print("Goodbye, have a great day!")
      line_space()
      pause()
      clear()
      exit()
    else:
      invalid_choice()
      self.menu()

  def owner_menu(self, owner):
    clear()
    print("=============")
    print(f"|| {owner.name} Menu ||")
    print("=============")
    line_space()
    print(f"1. {owner.name} Details")
    print(f"2. {owner.name} Adopt Pet")
    print(f"3. {owner.name} UnAdopt Pet")
    print("4. All Pets")
    print("5. Select Pet")
    print("'back' to go back to main menu")
    line_space()
    self.owner_menu_selection(owner)
  
  def owner_menu_selection(self, owner):
    user_input = input("Enter Selection: ")
    if user_input == "1":
      self.select_owner_details(owner)
      line_space()
      pause()
      self.owner_menu(owner)
    elif user_input == "2":
      print("Owner Adopt")
      line_space()
      pause()
      self.owner_menu(owner)
    elif user_input == "3":
      print("Owner UnAdopt")
      line_space()
      pause()
      self.owner_menu(owner)
    elif user_input == "4":
      print("View All Pets")
      line_space()
      pause()
      self.owner_menu(owner)
    elif user_input == "5":
      print("Select Pet")
      line_space()
      pause()
      self.owner_menu(owner)
    elif user_input == "back":
      clear()
      print("Going back to main menu")
    else:
      invalid_choice()
      self.owner_menu(owner)
  
  def list_owners(self):
    clear()
    print("====================")
    print("|| Listing Owners ||")
    print("====================")

    for owner in Owner.all():
      self.print_owner(owner)

  def print_owner(self, owner):
    line_space()
    print(f'Name: {owner.name}')
    print(f'ID: {owner.id}')
    line_space()
    print("--------------")

  def create_owner(self):
    clear()
    print("==================")
    print("|| Create Owner ||")
    print("==================")
    line_space()
    try:
      owner_name = input("Enter Name For Owner: ")
      owner = Owner.create(name=owner_name)
      clear()
      print(f'{owner.name} was successfully created')
    except Exception as err:
      clear()
      print(err)

  def delete_owner(self):
    clear()
    print("====================")
    print("||  Delete Owner  ||")
    print("====================")
    line_space()
    user_input = input("Enter ID: ")
    owner = Owner.find_by_id(user_input)
    if owner:
      owner.delete()
      clear()
      print(f"{owner.name} has been deleted")
    else:
      clear()
      print("Owner doesn't exist")
  
  def select_owner(self):
    clear()
    print("====================")
    print("||  Select Owner  ||")
    print("====================")
    line_space()
    user_input = input("Enter ID: ")
    owner = Owner.find_by_id(user_input)
    if owner:
      self.owner_menu(owner)
    else:
      clear()
      print("Owner doesn't exist")
  
  def select_owner_details(self, owner):
    clear()
    print("====================")
    print(f"||  {owner.name} Details  ||")
    print("====================")
    line_space()
    print(f'Name: {owner.name}')
    print(f'ID: {owner.id}')
    line_space()
    print("-----Pets-----")
    self.print_owner_pets(owner)

  def print_owner_pets(self, owner):
    line_space()
    for pet in owner.pets:
      self.print_pet_details(pet)

  def print_pet_details(self, pet):
    print(f'Name: {pet.name}')
    print(f'Species: {pet.species}')
    print(f'ID: {pet.id}')
    line_space()
    print("----------------")

    