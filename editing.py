# Lets the user add, delete, update, or view words in a unit.
# Everything related to editing the vocab.

from input_validation import confirm_del_action
from file_ops import load_vocab, save_vocab, save_vocab_file


#function that adds a word to the dictionary
#def add_word(unit, word, meaning)



#function that delets a word in the dictionary
def delete_word() -> None:
    vocab = load_vocab()
    while True:
        word_to_delete = input("Which word do you want to delete? (type 'exit' to return to main menu): ").strip().lower()
        if word_to_delete == "exit":
            print("Returning to main menu.")
            return
        # checking in which units the word exists
        units_with_word = []
        for unit_name in vocab:
            for entry in vocab[unit_name]:
                if entry["word"].strip().lower() == word_to_delete:
                    units_with_word.append(unit_name)
                    break  
        if not units_with_word:
            print(f"The word '{word_to_delete}' was not found in any unit.")
            continue
        else:
            # in case the word was found in unit/s
            print(f"The word '{word_to_delete}' appears in the following unit(s): {', '.join(units_with_word)}")

            if confirm_del_action(f"Do you want to delete the word '{word_to_delete}' from these unit(s)?"):
                for unit_name in units_with_word:
                    vocab[unit_name] = [entry for entry in vocab[unit_name] if entry["word"].lower() != word_to_delete]
                save_vocab(vocab)
                print(f"The word '{word_to_delete}' was deleted from: {', '.join(units_with_word)}")
                return
            else:
                return


#function that delets a whole unit
def delete_unit() -> None:
    vocab = load_vocab()
    while True:
        unit_to_delete = input("Which unit do you want to delete? (type 'exit' to return to main menu): ").strip().lower()
        if unit_to_delete == "exit":
            print("Returning to main menu.")
            return
        if unit_to_delete not in vocab:
            print(f"'{unit_to_delete}' was not found in the dictionary.")
            continue
        else:
            # in case the unit was found in dictionary
            print(f"'{unit_to_delete}' exists in the dictionary")
        if confirm_del_action(f"Do you want to delete '{unit_to_delete}' from the dictionary?"):
            del vocab[unit_to_delete]
            save_vocab_file(vocab)
            print(f"'{unit_to_delete}' was deleted from the dictionary.")
            return
        else:
            return



#finction that shows the words and their translation from a unit
#def list_words(unit)