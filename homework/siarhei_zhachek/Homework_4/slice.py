MY_TEXT = 'Mauris fringilla odio sit amet pretium ultricies.' \
          ' Pellentesque habitant morbi tristique'
MY_TEXT_A = MY_TEXT.replace(' ', '')
# print(len(MY_TEXT_A))
MY_TEXT1 = MY_TEXT_A[:8]
MY_TEXT2 = len(MY_TEXT) // 2
MY_TEXT3 = MY_TEXT_A[0::3]
print(MY_TEXT1)
print()
print(MY_TEXT[MY_TEXT2: MY_TEXT2+4])
print()
print(MY_TEXT3)
