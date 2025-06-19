
# def is_palindrome(s):
#     if len(s) <= 1:
#         return True
#     new_s = s.lower()
#     reversed_s = new_s[::-1]
#     return new_s == reversed_s
#
#
# print(is_palindrome("radar"))
# print(is_palindrome(""))
# print(is_palindrome("hello"))
#
# def is_palindrome_adv(s):
#     if len(s) <= 1:
#         return True
#     low_s = s.lower()
#     clear_s = [char for char in low_s if char.isalnum()]
#     clear_s = "".join(clear_s)
#     reversed_s = clear_s[::-1]
#     return reversed_s == clear_s
#
# def save_pal_to_file(text, filename):
#     words = text.split()
#     palindromes = [word for word in words if is_palindrome_adv(word)]
#     try:
#         with open(filename, "w") as file:
#             for word in palindromes:
#                 file.write(word + "\n")
#     except IOError as e:
#         print(f"{e} error occurred")
#
# def read_pal_from_file(filename):
#     try:
#         with open(filename, "r") as file:
#             content = [line.strip() for line in file.readlines()]
#             palindromes = [word for word in content if is_palindrome_adv(word)]
#             return palindromes
#     except (FileNotFoundError, IOError) as e:
#         print(f"Error {e} occurred")
#         return []

# import numpy as np
# def average_array(numbers):
#     if not numbers:
#         return 0
#     try:
#         arr = np.array(numbers)
#         meann = np.mean(arr)
#         return meann
#     except (ValueError, TypeError) as e:
#         print(f"Error {e}")
#         return None

# def filter_above_mean(numbers):
#     if not numbers:
#         return []
#     try:
#         arr = np.array(numbers)
#         meann = np.mean(arr)
#         new_arr = arr[arr > meann].tolist()
#         return new_arr
#     except (TypeError, ValueError) as e:
#         print("Smth went wrong cause {e}")
#         return None
#
# numbers = [1, 2, 3, 4, 5]
# print(filter_above_mean(numbers))

# def normalize_array(numbers):
#     if not numbers:
#         return []
#     try:
#         arr = np.array(numbers)
#         mean = np.mean(arr)
#         below_mean_count = sum(1 for x in arr if x < mean)
#         print(f"Numbers below mean ({mean}): {below_mean_count}")
#         min_arr = np.min(arr)
#         max_arr = np.max(arr)
#         normalized = (arr - min_arr)/(max_arr - min_arr)
#         if max_arr == min_arr:
#             return [0] * len(numbers)
#         else:
#             return normalized.tolist()
#     except (TypeError, ValueError) as e:
#         print(f"Error {e} has occurred")
#
# numbers = [3,4,6,7,9,10,12]
# print(normalize_array(numbers))

# import pandas as pd

# def filter_above_av_price(filename, column):
#     try:
#         content = pd.read_csv(filename)
#         mean = content[column].mean()
#         filtered = content[content[column] > mean]
#         return filtered
#     except (FileNotFoundError, KeyError) as e:
#         print(f"Error occurred: {e}")
#         return None

# def group_by_mean(filename, group_column, value_column):
#     try:
#         dataFrame = pd.read_csv(filename)
#         mean = dataFrame.groupby(group_column)[value_column].mean()
#         result = mean.reset_index()
#         return result
#     except (FileNotFoundError, TypeError) as e:
#         print(f"Error {e}")
#         return None

# def filter_and_sort(filename, column, threshold):
#     try:
#         df = pd.read_csv(filename)
#         filtered_df = df[df[column] > threshold]
#         count_rows = 0
#         for _ in filtered_df.iterrows():
#             count_rows += 1
#         sorted_df = filtered_df.sort_values(by=column, ascending = False)
#         print(sorted_df, count_rows)
#         return sorted_df
#     except (FileNotFoundError, KeyError) as e:
#         print (f"Error {e} occurred")
#         return None

# def Fibonacci(n):
#     num1 = 1
#     num2 = 1
#     for x in range(2, n):
#         next_num = num1 + num2
#         yield next_num
#         num1 = num2
#         num2 = next_num

# from collections import Counter

# def most_common_chars(text):
#     if not text:
#         print(f"{text}: string is empty")
#         return {}
#     count_chars = Counter(text)
#     most_common = count_chars.most_common(2)
#     result = {char: count for char, count in most_common}
#     unique = set(text)
#     unique_count = 0
#     for _ in unique:
#         unique_count += 1
#     print(f"Number of unique characters:{unique_count}")
#     return result

# from collections import deque
# def is_palindrome(s):
#     s = s.lower()
#     # удаляем неалфавитно-цифровые символы
#     s =''.join(char for char in s if char.isalnum())
#     if not s:
#         return True
#     deq_s = deque(s)
#     while len(deq_s) > 1:
#         left = deq_s.popleft()
#         right = deq_s.pop()
#         if left != right:
#             return False
#         else:
#             return True

# import argparse
# parser = argparse.ArgumentParser(description = "Cкрипт для повторения заданной пользователем строки")
# parser.add_argument("string", type = str, help = "Строка для повторения")
# parser.add_argument("n", type = int, help = "Количество повторений строки")
# arguments = parser.parse_args()
# if arguments.n < 0:
#     print("Number is negative")
# else:
#    repeat = arguments.string * arguments.n
#    print(repeat)

# import itertools
# all_teams = ["Team A", "Team B", "Team C", "Team D"]
# if len(all_teams) < 2:
#     print("Not enough teams")
# else:
#     combin = itertools.combinations(all_teams, 2)
#     for team1, team2 in combin:
#         print(f"{team1} vs {team2}")

import statistics
# data1 = [1, 2, 3, 4, 5]
# data2 = [2, 4, 6, 8, 10]
# mean1 = statistics.mean(data1)
# mean2 = statistics.mean(data2)
# var1 = statistics.variance(data1)
# var2 = statisctics.variance(data2)

# import random
# broski = []
# for x in range(1000):
#     roll = random.randint(1,6)
#     broski.append(roll)
# mean = statistics.mean(broski)
# st_otklonenie = statistics.stdev(broski)
# print(f"Среднее значение от 1000 бросков кубика:{mean}")
# print(f"Стандартное отклонение:{st_otklonenie}")


# data = [1,2,3,4,5]
# if not data:
#     print("Список пуст")
# else:
#     mean = statistics.mean(data)
#     st_dev = statistics.stdev(data)
#     if st_dev == 0:
#         print("Деление на ноль невозможно")
#         z_scores = [0] * len(data)
#     else:
#         z_scores = [(x - mean) / st_dev for x in data]
#         print(f"Нормализированные данные: {[round (z, 2) for z in z_scores]}")

from fractions import Fraction
import math
fractions = [Fraction(1, 2), Fraction(1, 3)]
if not fractions:
    print("Error, check the fractions")
    fractions = [0]
else:
    denominators = [f.denominator for f in fractions]






