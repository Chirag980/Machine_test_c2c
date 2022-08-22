

def count_character(File_content):
    vowels =0
    consonant=0
    specialChar = 0
    digit =0
    white_space = 0

    for i in range(0, len(File_content)):
        ch = File_content[i]
        if ((ch>='a' and ch<= 'z') or (ch>='A' and ch<='Z')):
            ch = ch.lower()

            if(ch=='a'or ch=='e'or ch=='i'or ch =='o' or ch=='u'):
                vowels+=1
            else:
                consonant+=1

        elif(ch>='0' and ch<='9'):
            digit +=1

        elif File_content[i]==' ':
            white_space+=1
        else:
            specialChar+=1

    print('No. of Vowels:',vowels)

    print('No. of consonant:',consonant)

    print('No. of special character:',specialChar)

    print('No. of digits:',digit)

    print('No. of White Spaces:', white_space)

File_content  ='Hello India@123'
count_character(File_content)



























