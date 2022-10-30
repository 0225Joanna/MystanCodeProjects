"""
File: boggle.py
Name: Joanna
----------------------------------------
This program finds all the words on a 4 x 4 board. Each of the board contains a letter (User will input it).
When starting to find a word, each letter must be a horizontal, vertical, or diagonal neighbor of previous one.
Besides, words must be at least four letters in length.
"""

import time

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'


def main():
	"""
	This program finds all the words on a 4 x 4 board. Each of the board contains a letter (User will input it).
	When starting to find a word, each letter must be a horizontal, vertical, or diagonal neighbor of previous one.
	Besides, words must be at least four letters in length.
	"""
	start = time.time()
	###################
	# User input
	all_letters = []
	for i in range(4):
		row = input(f'{i+1} row of letters: ')
		# creating a lst of letters in Boggle
		if input_checker(row):		# The input format is legal.
			row = row.split()
			all_letters.append(row)
		else:
			print('Illegal format')
			break
	dict_lst = read_dictionary()
	# Finding all the words in the Boggle
	boggle(all_letters, dict_lst)
	####################
	end = time.time()
	print('----------------------------------')
	print(f'The speed of your boggle algorithm: {end - start} seconds.')


def input_checker(s):
	"""
	:param s: str, the string must be consist of 4 letters and 3 space.
	:return: bool, checking the input format is legal.
	"""
	if len(s.strip()) == 7:		# 'a b c d' (4 letters + 3 space)
		for i in range(4):
			if s[i*2].isalpha():
				if i < 3: 	# i < 3 because the last space is in position 5   (i*2+1)
					if s[i*2+1] == ' ':
						return True
	return False


def boggle(all_letters, dict_lst):
	"""
	:param all_letters: lst, all the letters in the Boggle Game.
	:param dict_lst: lst, all the words in the FIlE.
	:return: This program does not return anything. Print the number of the words in the boggle.
	"""
	ans_lst = []
	# regarding each position of the letters as initial letter of the words.
	for i in range(4):
		for j in range(4):
			lst = boggle_helper(all_letters, i, j,  '', [], [], dict_lst)
			if len(lst) != 0:
				for k in range(len(lst)):
					ans_lst.append(lst[k])
	print(f'There are {len(ans_lst)} words in total.')


def boggle_helper(all_letters, previous_i, previous_j, current_str, current_lst, used_letters, dict_lst):
	"""
	:param all_letters: all_letters: lst, all the letters in the Boggle Game.
	:param previous_i: int, the position i of the previous letter.
	:param previous_j: int, the position j of the previous letter.
	:param current_str: str, recording the current string.
	:param current_lst: lst, recording the current list of the words.
	:param used_letters: lst, recording the position of the letters we have used.
	:param dict_lst: lst, all the words in the FIlE.
	:return: lst, the words in the boggle.
	"""
	# base case
	if len(current_str) >= 4:
		if current_str not in current_lst:
			if current_str in dict_lst:
				current_lst.append(current_str)
				print(f'Found \"{current_str}\"')
	for di, dj in [(-1, -1), (-1, 1), (-1, 0), (0, 1), (0, -1), (1, 1), (1, 0), (1, -1)]:
		new_i = previous_i + di
		new_j = previous_j + dj
		# choose
		if current_str == '':
			current_str += all_letters[previous_i][previous_j]
			used_letters.append(f'{previous_i}{previous_j}')
		if has_prefix(current_str, dict_lst):
			if 0 <= new_i < 4 and 0 <= new_j < 4:
				if f'{new_i}{new_j}' not in used_letters:
					current_str += all_letters[new_i][new_j]
					used_letters.append(f'{new_i}{new_j}')
					# explore
					boggle_helper(all_letters, new_i, new_j, current_str, current_lst, used_letters, dict_lst)
					# un-choose
					current_str = current_str[:-1]
					used_letters.pop()
	return current_lst


def read_dictionary():
	"""
	This function reads file "dictionary.txt" stored in FILE
	and appends words in each line into a Python list
	"""
	with open(FILE, 'r') as f:
		dict_lst = []
		for word in f:
			word = word.strip()
			if len(word) >= 4:
				dict_lst.append(word)
	return dict_lst


def has_prefix(sub_s, dict_lst):
	"""
	:param sub_s: str, the current string.
	:param dict_lst: lst, all the words in the FIlE.
	:return: bool, return True if the sub_s at the beginning of a word.
	"""
	for word in dict_lst:
		if word.startswith(sub_s):
			return True


if __name__ == '__main__':
	main()
