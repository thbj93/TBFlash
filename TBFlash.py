import os
from pathlib import Path
import openpyxl


if not os.path.exists(Path.home() / 'TBFlash' / 'collection.xlsx'):
	if not os.path.exists(Path.home() / 'TBFlash'):
		os.mkdir(Path.home() / 'TBFlash')
	wb = openpyxl.Workbook()
	ws = wb.active
	ws['A1'] = 'Question'
	ws['B1'] = 'Answer'
	wb.save(Path.home() / 'TBFlash' / 'collection.xlsx')

wb = openpyxl.load_workbook(Path.home() / 'TBFlash' / 'collection.xlsx')
ws = wb.active

def print_menu():
	print()
	print("MENU")
	print("1. Add flashcard")
	print("2. Quiz")
	print("3. Show flashcards")
	print("9. Exit")
	print()

def add_card():
	print('NEW CARD')
	new_row = ws.max_row + 1
	question = input('Type question: ')
	answer = input('Type answer: ')
	ws.cell(row=new_row, column=1).value = question
	ws.cell(row=new_row, column=2).value = answer
	wb.save(Path.home() / 'TBFlash' / 'collection.xlsx')
	print()


def run_quiz():
	print('QUIZ - ', ws.max_row - 1, 'questions total')
	for q in range(2, ws.max_row+1):
		print('Question: ', ws['A' + str(q)].value)
		user_answer = input('Your answer: ')
		print('The correct answer is: ', ws['B' + str(q)].value)
		print()

def show_cards():
	print('SHOW CARDS')
	if ws.max_row <= 1:
		print('No cards to show.')
	print()
	for q in range(2, ws.max_row+1):
		print('Q: ', ws.cell(row=q, column=1).value)
		print('A: ', ws.cell(row=q, column=2).value)
		print()

print_menu()
menu_choice = 0

while menu_choice != 9:
	menu_choice = int(input("Menu choice: "))
	print()
	if menu_choice == 1:
		add_card()
		print_menu()
	elif menu_choice == 2:
		run_quiz()
		print_menu()
	elif menu_choice == 3:
		show_cards()
		print_menu()
	elif menu_choice != 9:
		print("Invalid option, please try again.")
		print()
