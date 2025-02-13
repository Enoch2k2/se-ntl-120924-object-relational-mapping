from pet import Pet
from owner import Owner

from helpers import clear, pause, line_space, invalid_choice
from simple_term_menu import TerminalMenu
from rich import print
import ipdb

class Cli:
  def start(self):
    clear()
    print("[bold magenta]=======================================[/bold magenta]")
    print("[bold magenta]||[/bold magenta] [bright_cyan]Welcome to the Flatiron Pet Shop![/bright_cyan] [bold magenta]||[/bold magenta]")
    print("[bold magenta]=======================================[/bold magenta]")
    line_space()
    pause()

    self.menu()

  def menu(self):
    clear()
    print("===================")
    print("|| Pet Shop Menu ||")
    print("===================")
    line_space()
    # print("1. List All Owners")
    # print("2. Create Owner")
    # print("3. Select Owner")
    # print("4. Delete Owner")
    # print("'exit' to exit program")
    options = ["List All Owners", "Create Owner", "Select Owner", "Delete Owner", "Exit Program"]
    terminal_menu = TerminalMenu(options, menu_highlight_style=("fg_blue",))
    menu_entry_index = terminal_menu.show()
    if menu_entry_index != None:
      self.menu_selection(menu_entry_index)
    else:
      self.menu()

  
  def menu_selection(self, user_input):
    if user_input == 0:
      self.list_owners()
      line_space()
      pause()
      self.menu()
    elif user_input == 1:
      self.create_owner()
      line_space()
      pause()
      self.menu()
    elif user_input == 2:
      self.select_owner()
      line_space()
      pause()
      self.menu()
    elif user_input == 3:
      self.delete_owner()
      line_space()
      pause()
      self.menu()
    elif user_input == 4:
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
      self.adopt_pet(owner)
      line_space()
      pause()
      self.owner_menu(owner)
    elif user_input == "3":
      self.unadopt_pet(owner)
      line_space()
      pause()
      self.owner_menu(owner)
    elif user_input == "4":
      self.print_pets()
      line_space()
      pause()
      self.owner_menu(owner)
    elif user_input == "5":
      self.select_pet_details()
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

  def adopt_pet(self, owner):
    clear()
    print("====================")
    print(f"||  {owner.name} Adopt Pet  ||")
    print("====================")
    line_space()
    try:
      pet_name = input("Enter Pet Name: ")
      pet_species = input("Enter Pet Species: ")
      pet = Pet.create(name=pet_name, species=pet_species)
      pet.owner = owner
      clear()
      print(f'{pet.name} has been adopted')
    except Exception as error:
      clear()
      print(error)

  def unadopt_pet(self, owner):
    clear()
    print("====================")
    print(f"||  {owner.name} Unadopt Pet  ||")
    print("====================")
    line_space()
    pet_id = input("Enter Pet ID here: ")
    try:
      found_pets = [pet for pet in owner.pets if pet.id == int(pet_id)]
      if len(found_pets) > 0:
        pet = found_pets[0]
        pet.delete()
        clear()
        print(f'{pet.name} has been unadopted')
      else:
        clear()
        print('Pet does not belong to you')
    except:
      clear()
      print("Something went wrong, try again")

  def print_pets(self):
    clear()
    print("====================")
    print("|| Listing Pets ||")
    print("====================")
    for pet in Pet.all():
      line_space()
      self.print_pet_details(pet)

  def select_pet_details(self):
    clear()
    print("====================")
    print("|| Pet Details ||")
    print("====================")
    line_space()
    pet_id = input("Enter Pet ID Here: ")
    try:
      found_pets = [pet for pet in Pet.all() if pet.id == int(pet_id)]
      if len(found_pets) > 0:
        pet = found_pets[0]
        clear()
        print("----------------")
        self.selected_pet_details(pet)
      else:
        clear()
        print('Pet doesn\'t exist')
    except:
      clear()
      print("Something went wrong, try again")

  def selected_pet_details(self, pet):
    line_space()
    print("Pet Info")
    line_space()
    self.print_pet_details(pet)
    line_space()
    print("Pet Owner Info")
    line_space()
    # ipdb.set_trace()
    if pet.owner:
      print(f'Owner: {pet.owner.name}')
      print(f'Owner ID: {pet.owner.id} ')
    else:
      print('Pet not adopted')
    line_space()
    print("----------------")
