chosen_letter = input("Which letter do you want to count? ")
my_sentence = "My gosh, what a beautiful Monday morning this is."
def m_word_count(my_sentence):
  count = 0
  for count_word in my_sentence:
    if count_word == chosen_letter:
      count += 1
  return count
print("Chosen letter: " + chosen_letter)
print("Count: " + str(m_word_count(my_sentence)))