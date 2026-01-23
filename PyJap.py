import random
#from termcolor
#import colored


hiragana_romaji_a = {'あ': 'a',  'い': 'i',  'う': 'u',  'え': 'e',  'お': 'o',}
hiragana_romaji_ka = {'か': 'ka', 'き': 'ki', 'く': 'ku', 'け': 'ke', 'こ': 'ko'}
hiragana_romaji_sa = {'さ': 'sa', 'し': 'shi','す': 'su', 'せ': 'se', 'そ': 'so'}
hiragana_romaji_ta = {'た': 'ta', 'ち': 'chi','つ': 'tsu','て': 'te', 'と': 'to'}
hiragana_romaji_na = {'な': 'na', 'に': 'ni', 'ぬ': 'nu', 'ね': 'ne', 'の': 'no'}
hiragana_romaji_ha = {'は': 'ha', 'ひ': 'hi', 'ふ': 'fu', 'へ': 'he', 'ほ': 'ho'}
hiragana_romaji_ma = {'ま': 'ma', 'み': 'mi', 'む': 'mu', 'め': 'me', 'も': 'mo'}
hiragana_romaji_ya = {'や': 'ya',             'ゆ': 'yu',             'よ': 'yo'}
hiragana_romaji_ra = {'ら': 'ra', 'り': 'ri', 'る': 'ru', 'れ': 're', 'ろ': 'ro'}
hiragana_romaji_wa = {'わ': 'wa', 'ん': 'n', 'を': 'wo'}
hiragana_romaji_list = {
    'あ': 'a',  'い': 'i',  'う': 'u',  'え': 'e',  'お': 'o',
    'か': 'ka', 'き': 'ki', 'く': 'ku', 'け': 'ke', 'こ': 'ko',
    'さ': 'sa', 'し': 'shi','す': 'su', 'せ': 'se', 'そ': 'so',
    'た': 'ta', 'ち': 'chi','つ': 'tsu','て': 'te', 'と': 'to',
    'な': 'na', 'に': 'ni', 'ぬ': 'nu', 'ね': 'ne', 'の': 'no',
    'は': 'ha', 'ひ': 'hi', 'ふ': 'fu', 'へ': 'he', 'ほ': 'ho',
    'ま': 'ma', 'み': 'mi', 'む': 'mu', 'め': 'me', 'も': 'mo',
    'や': 'ya',             'ゆ': 'yu',             'よ': 'yo',
    'ら': 'ra', 'り': 'ri', 'る': 'ru', 'れ': 're', 'ろ': 'ro',
    'わ': 'wa',                         'を': 'wo',
    'ん': 'n'
}


katakana_romaji_a = {'ア': 'a',  'イ': 'i',  'ウ': 'u',  'エ': 'e',  'オ': 'o',}
katakana_romaji_ka = {'カ': 'ka', 'キ': 'ki', 'ク': 'ku', 'ケ': 'ke', 'コ': 'ko'}
katakana_romaji_sa = {'サ': 'sa', 'シ': 'shi','ス': 'su', 'セ': 'se', 'ソ': 'so'}
katakana_romaji_ta = {'タ': 'ta', 'チ': 'chi','ツ': 'tsu','テ': 'te', 'ト': 'to'}
katakana_romaji_na = {'ナ': 'na', 'ニ': 'ni', 'ヌ': 'nu', 'ネ': 'ne', 'ノ': 'no'}
katakana_romaji_ha = {'ハ': 'ha', 'ヒ': 'hi', 'フ': 'fu', 'ヘ': 'he', 'ホ': 'ho'}
katakana_romaji_ma = {'マ': 'ma', 'ミ': 'mi', 'ム': 'mu', 'メ': 'me', 'モ': 'mo'}
katakana_romaji_ya = {'ヤ': 'ya',             'ユ': 'yu',             'ヨ': 'yo'}
katakana_romaji_ra = {'ラ': 'ra', 'リ': 'ri', 'ル': 'ru', 'レ': 're', 'ロ': 'ro'}
katakana_romaji_wa = {'ワ': 'wa', 'ン': 'n', 'ヲ': 'wo'}
katakana_romaji_list = {
    'ア': 'a',  'イ': 'i',  'ウ': 'u',  'エ': 'e',  'オ': 'o',
    'カ': 'ka', 'キ': 'ki', 'ク': 'ku', 'ケ': 'ke', 'コ': 'ko',
    'サ': 'sa', 'シ': 'shi','ス': 'su', 'セ': 'se', 'ソ': 'so',
    'タ': 'ta', 'チ': 'chi','ツ': 'tsu','テ': 'te', 'ト': 'to',
    'ナ': 'na', 'ニ': 'ni', 'ヌ': 'nu', 'ネ': 'ne', 'ノ': 'no',
    'ハ': 'ha', 'ヒ': 'hi', 'フ': 'fu', 'ヘ': 'he', 'ホ': 'ho',
    'マ': 'ma', 'ミ': 'mi', 'ム': 'mu', 'メ': 'me', 'モ': 'mo',
    'ヤ': 'ya',             'ユ': 'yu',             'ヨ': 'yo',
    'ラ': 'ra', 'リ': 'ri', 'ル': 'ru', 'レ': 're', 'ロ': 'ro',
    'ワ': 'wa',                         'ヲ': 'wo',
    'ン': 'n'

}



japanese_writing = ""


while True:
    if japanese_writing not in ("1", "2" ):
        japanese_writing = input("1) hiragana\n2) katakana\nPlease enter your choice:> ")
    else:
        print(f"Exiting script.")
        break

if japanese_writing == "1":

    print()
    while True:
        print(f"Welcome to hiragana test please choose which one to test\n")
        print(f"1) a\n""2) ka\n""3) sa\n""4) ta\n""5) na\n""6) ha\n""7) ma\n""8) ya\n""9) ra\n""10) wa\n""11) all\n""12) q(quit)\n")
        user_choice = input("Please enter your choice: ")
        print()
        valid_choice = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"]

        if user_choice == "1":
            count = 0
            max_count = 10
            correct = 0
            wrong = 0
            while count < max_count:
                char = random.choice(list(hiragana_romaji_a.keys()))
                correct_romaji = hiragana_romaji_a[char]
                user_input = input(f"Translate {char} to romaji: ").strip().lower()
                count += 1
                if user_input == correct_romaji:
                    correct +=1
                else:
                    print(f"Wrong. The correct answer is {correct_romaji}")
                    print()
                    wrong +=1
                print(f"You have {max_count - count} attempts left")
                print()
            print(f"You have ✅ {correct} correct answers, and ❌ {wrong} wrong answers")
            print()

        elif user_choice == "2":
            count = 0
            max_count = 10
            correct = 0
            wrong = 0
            while count < max_count:
                char = random.choice(list(hiragana_romaji_ka.keys()))
                correct_romaji = hiragana_romaji_ka[char]
                user_input = input(f"Translate {char} to romaji: ").strip().lower()
                count += 1
                if user_input == correct_romaji:
                    correct +=1
                else:
                    print(f"Wrong. The correct answer is {correct_romaji}")
                    wrong +=1
                print()
                print(f"You have {max_count - count} attempts left")
            print(f"You have ✅ {correct} correct answers, and ❌ {wrong} wrong answers")
            print()

        elif user_choice == "3":
            count = 0
            max_count = 10
            correct = 0
            wrong = 0
            while count < max_count:
                char = random.choice(list(hiragana_romaji_sa.keys()))
                correct_romaji = hiragana_romaji_sa[char]
                user_input = input(f"Translate {char} to romaji: ").strip().lower()
                count += 1
                if user_input == correct_romaji:
                    correct +=1
                else:
                    print(f"Wrong. The correct answer is {correct_romaji}")
                    wrong +=1
                print()
                print(f"You have {max_count - count} attempts left")
            print(f"You have ✅ {correct} correct answers, and ❌ {wrong} wrong answers")
            print()

        elif user_choice == "4":
            count = 0
            max_count = 10
            correct = 0
            wrong = 0
            while count < max_count:
                char = random.choice(list(hiragana_romaji_ta.keys()))
                correct_romaji = hiragana_romaji_ta[char]
                user_input = input(f"Translate {char} to romaji: ").strip().lower()
                count += 1
                if user_input == correct_romaji:
                    correct +=1
                else:
                    print(f"Wrong. The correct answer is {correct_romaji}")
                    wrong +=1
                print()
                print(f"You have {max_count - count} attempts left")
            print(f"You have ✅ {correct} correct answers, and ❌ {wrong} wrong answers")
            print()

        elif user_choice == "5":
            count = 0
            max_count = 10
            correct = 0
            wrong = 0
            while count < max_count:
                char = random.choice(list(hiragana_romaji_na.keys()))
                correct_romaji = hiragana_romaji_na[char]
                user_input = input(f"Translate {char} to romaji: ").strip().lower()
                count += 1
                if user_input == correct_romaji:
                    correct +=1
                else:
                    print(f"Wrong. The correct answer is {correct_romaji}")
                    wrong +=1
                print()
                print(f"You have {max_count - count} attempts left")
            print(f"You have ✅ {correct} correct answers, and ❌ {wrong} wrong answers")
            print()

        elif user_choice == "6":
            count = 0
            max_count = 10
            correct = 0
            wrong = 0
            while count < max_count:
                char = random.choice(list(hiragana_romaji_ha.keys()))
                correct_romaji = hiragana_romaji_ha[char]
                user_input = input(f"Translate {char} to romaji: ").strip().lower()
                count += 1
                if user_input == correct_romaji:
                    correct +=1
                else:
                    print(f"Wrong. The correct answer is {correct_romaji}")
                    wrong +=1
                print()
                print(f"You have {max_count - count} attempts left")
            print(f"You have ✅ {correct} correct answers, and ❌ {wrong} wrong answers")
            print()

        elif user_choice == "7":
            count = 0
            max_count = 10
            correct = 0
            wrong = 0
            while count < max_count:
                char = random.choice(list(hiragana_romaji_ma.keys()))
                correct_romaji = hiragana_romaji_ma[char]
                user_input = input(f"Translate {char} to romaji: ").strip().lower()
                count += 1
                if user_input == correct_romaji:
                    correct +=1
                else:
                    print(f"Wrong. The correct answer is {correct_romaji}")
                    wrong +=1
                print()
                print(f"You have {max_count - count} attempts left")
            print(f"You have ✅ {correct} correct answers, and ❌ {wrong} wrong answers")
            print()

        elif user_choice == "8":
            count = 0
            max_count = 10
            correct = 0
            wrong = 0
            while count < max_count:
                char = random.choice(list(hiragana_romaji_ya.keys()))
                correct_romaji = hiragana_romaji_ya[char]
                user_input = input(f"Translate {char} to romaji: ").strip().lower()
                count += 1
                if user_input == correct_romaji:
                    correct +=1
                else:
                    print(f"Wrong. The correct answer is {correct_romaji}")
                    wrong +=1
                print()
                print(f"You have {max_count - count} attempts left")
            print(f"You have ✅ {correct} correct answers, and ❌ {wrong} wrong answers")
            print()

        elif user_choice == "9":
            count = 0
            max_count = 10
            correct = 0
            wrong = 0
            while count < max_count:
                char = random.choice(list(hiragana_romaji_ra.keys()))
                correct_romaji = hiragana_romaji_ra[char]
                user_input = input(f"Translate {char} to romaji: ").strip().lower()
                count += 1
                if user_input == correct_romaji:
                    correct +=1
                else:
                    print(f"Wrong. The correct answer is {correct_romaji}")
                    wrong +=1
                print()
                print(f"You have {max_count - count} attempts left")
            print(f"You have ✅ {correct} correct answers, and ❌ {wrong} wrong answers")
            print()

        elif user_choice == "10":
            count = 0
            max_count = 10
            correct = 0
            wrong = 0
            while count < max_count:
                char = random.choice(list(hiragana_romaji_wa.keys()))
                correct_romaji = hiragana_romaji_wa[char]
                user_input = input(f"Translate {char} to romaji: ").strip().lower()
                count += 1
                if user_input == correct_romaji:
                    correct +=1
                else:
                    print(f"Wrong. The correct answer is {correct_romaji}")
                    wrong +=1
                print()
                print(f"You have {max_count - count} attempts left")
            print(f"You have ✅ {correct} correct answers, and ❌ {wrong} wrong answers")
            print()


        elif user_choice == "11":
            count = 0
            max_count = 45
            correct = 0
            wrong = 0
            while count < max_count:
                char = random.choice(list(hiragana_romaji_list.keys()))
                correct_romaji = hiragana_romaji_list[char]
                user_input = input(f"Translate {char} to romaji: ").strip().lower()
                count += 1
                if user_input == correct_romaji:
                    correct +=1
                else:
                    print(f"Wrong. The answer is {correct_romaji}")
                    wrong +=1
                print()
                print(f"You have {max_count - count} attempts left")
            print(f"You have ✅ {correct} correct answers, and ❌ {wrong} wrong answers")
            print()

        elif user_choice == "12":
             print("Exiting")
             break
        



            

elif japanese_writing == "2":

    while True:
        print(f"Welcome to katakana test please choose which one to test\n")
        print(f"1) a\n""2) ka\n""3) sa\n""4) ta\n""5) na\n""6) ha\n""7) ma\n""8) ya\n""9) ra\n""10) wa\n""11) all\n""12) q(quit)\n")
        user_choice = input("Please enter your choice: ")
        print()
        valid_choice = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"]
        print()

        if user_choice == "1":
            count = 0
            max_count = 10
            correct = 0
            wrong = 0
            while count < max_count:
                char = random.choice(list(katakana_romaji_a.keys()))
                correct_romaji = katakana_romaji_a[char]
                user_input = input(f"Translate {char} to romaji: ").strip().lower()
                count += 1
                if user_input == correct_romaji:
                    correct +=1
                else:
                    print(f"Wrong. The correct answer is {correct_romaji}")
                    print()
                    wrong +=1
                print(f"You have {max_count - count} attempts left")
                print()
            print(f"You have ✅ {correct} correct answers, and ❌ {wrong} wrong answers")
            print()


        elif user_choice == "2":
            count = 0
            max_count = 10
            correct = 0
            wrong = 0
            while count < max_count:
                char = random.choice(list(katakana_romaji_ka.keys()))
                correct_romaji = katakana_romaji_ka[char]
                user_input = input(f"Translate {char} to romaji: ").strip().lower()
                count += 1
                if user_input == correct_romaji:
                    correct +=1
                else:
                    print(f"Wrong. The correct answer is {correct_romaji}")
                    wrong +=1
                print()
                print(f"You have {max_count - count} attempts left")
            print(f"You have ✅ {correct} correct answers, and ❌ {wrong} wrong answers")
            print()

        elif user_choice == "3":
            count = 0
            max_count = 10
            correct = 0
            wrong = 0
            while count < max_count:
                char = random.choice(list(katakana_romaji_sa.keys()))
                correct_romaji = katakana_romaji_sa[char]
                user_input = input(f"Translate {char} to romaji: ").strip().lower()
                count += 1
                if user_input == correct_romaji:
                    correct +=1
                else:
                    print(f"Wrong. The correct answer is {correct_romaji}")
                    wrong +=1
                print()
                print(f"You have {max_count - count} attempts left")
            print(f"You have ✅ {correct} correct answers, and ❌ {wrong} wrong answers")
            print()

        elif user_choice == "4":
            count = 0
            max_count = 10
            correct = 0
            wrong = 0
            while count < max_count:
                char = random.choice(list(katakana_romaji_ta.keys()))
                correct_romaji = katakana_romaji_ta[char]
                user_input = input(f"Translate {char} to romaji: ").strip().lower()
                count += 1
                if user_input == correct_romaji:
                    correct +=1
                else:
                    print(f"Wrong. The correct answer is {correct_romaji}")
                    wrong +=1
                print()
                print(f"You have {max_count - count} attempts left")
            print(f"You have ✅ {correct} correct answers, and ❌ {wrong} wrong answers")
            print()

        elif user_choice == "5":
            count = 0
            max_count = 10
            correct = 0
            wrong = 0
            while count < max_count:
                char = random.choice(list(katakana_romaji_na.keys()))
                correct_romaji = katakana_romaji_na[char]
                user_input = input(f"Translate {char} to romaji: ").strip().lower()
                count += 1
                if user_input == correct_romaji:
                    correct +=1
                else:
                    print(f"Wrong. The correct answer is {correct_romaji}")
                    wrong +=1
                print()
                print(f"You have {max_count - count} attempts left")
            print(f"You have ✅ {correct} correct answers, and ❌ {wrong} wrong answers")
            print()

        elif user_choice == "6":
            count = 0
            max_count = 10
            correct = 0
            wrong = 0
            while count < max_count:
                char = random.choice(list(katakana_romaji_ha.keys()))
                correct_romaji = katakana_romaji_ha[char]
                user_input = input(f"Translate {char} to romaji: ").strip().lower()
                count += 1
                if user_input == correct_romaji:
                    correct +=1
                else:
                    print(f"Wrong. The correct answer is {correct_romaji}")
                    wrong +=1
                print()
                print(f"You have {max_count - count} attempts left")
            print(f"You have ✅ {correct} correct answers, and ❌ {wrong} wrong answers")
            print()

        elif user_choice == "7":
            count = 0
            max_count = 10
            correct = 0
            wrong = 0
            while count < max_count:
                char = random.choice(list(katakana_romaji_ma.keys()))
                correct_romaji = katakana_romaji_ma[char]
                user_input = input(f"Translate {char} to romaji: ").strip().lower()
                count += 1
                if user_input == correct_romaji:
                    correct +=1
                else:
                    print(f"Wrong. The correct answer is {correct_romaji}")
                    wrong +=1
                print()
                print(f"You have {max_count - count} attempts left")
            print(f"You have ✅ {correct} correct answers, and ❌ {wrong} wrong answers")
            print()

        elif user_choice == "8":
            count = 0
            max_count = 10
            correct = 0
            wrong = 0
            while count < max_count:
                char = random.choice(list(katakana_romaji_ya.keys()))
                correct_romaji = katakana_romaji_ya[char]
                user_input = input(f"Translate {char} to romaji: ").strip().lower()
                count += 1
                if user_input == correct_romaji:
                    correct +=1
                else:
                    print(f"Wrong. The correct answer is {correct_romaji}")
                    wrong +=1
                print()
                print(f"You have {max_count - count} attempts left")
            print(f"You have ✅ {correct} correct answers, and ❌ {wrong} wrong answers")
            print()

        elif user_choice == "9":
            count = 0
            max_count = 10
            correct = 0
            wrong = 0
            while count < max_count:
                char = random.choice(list(katakana_romaji_ra.keys()))
                correct_romaji = katakana_romaji_ra[char]
                user_input = input(f"Translate {char} to romaji: ").strip().lower()
                count += 1
                if user_input == correct_romaji:
                    correct +=1
                else:
                    print(f"Wrong. The correct answer is {correct_romaji}")
                    wrong +=1
                print()
                print(f"You have {max_count - count} attempts left")
            print(f"You have ✅ {correct} correct answers, and ❌ {wrong} wrong answers")
            print()

        elif user_choice == "10":
            count = 0
            max_count = 10
            correct = 0
            wrong = 0
            while count < max_count:
                char = random.choice(list(katakana_romaji_wa.keys()))
                correct_romaji = katakana_romaji_wa[char]
                user_input = input(f"Translate {char} to romaji: ").strip().lower()
                count += 1
                if user_input == correct_romaji:
                    correct +=1
                else:
                    print(f"Wrong. The correct answer is {correct_romaji}")
                    wrong +=1
                print()
                print(f"You have {max_count - count} attempts left")
            print(f"You have ✅ {correct} correct answers, and ❌ {wrong} wrong answers")
            print()


        elif user_choice == "11":
            count = 0
            max_count = 45
            correct = 0
            wrong = 0
            while count < max_count:
                char = random.choice(list(katakana_romaji_list.keys()))
                correct_romaji = katakana_romaji_list[char]
                user_input = input(f"Translate {char} to romaji: ").strip().lower()
                count += 1
                if user_input == correct_romaji:
                    correct +=1
                else:
                    print(f"Wrong. The answer is {correct_romaji}")
                    wrong +=1
                print()
                print(f"You have {max_count - count} attempts left")
            print(f"You have ✅ {correct} correct answers, and ❌ {wrong} wrong answers")
            print()

        elif user_choice == "12":
            print("Exiting")
            break
