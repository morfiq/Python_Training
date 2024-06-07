import re
# search/pattern
wordcount = {"BAJAJFINANCELIMITED":0, "CHQ PAID":0}
word1 = "BAJAJFINANCELIMITED"
word2 = "CHQ PAID"
def read_file():
    with open('output_1_AXIS_BANK_CLEANUP_FILE.txt', 'r') as fp:
        for line in fp.readlines():
            # line_words = line.split("\\t")
            # if "432989" in line:
            # print([int(s) for s in re.findall(r'\b\d+\b', line)])
            # print([float(s) for s in re.findall(r'\d+\.\d+', line)])
            #regular expression to extract integer and float numbers from string
            nums = [float(s) for s in re.findall(r'[-+]?(?:\d*\.*\d+)', line)]
            if nums:
                max_num = max(nums)
                # if max_num.is_integer():
                #     max_num = int(max_num)
                print(max_num)
            # print([float(s) for s in line_words if s.isdigit()])
            # print(line_words)
            # if number.is_integer():
            #     number = int(number)
            # print(line)
            if word1 in line:
                wordcount[word1] += 1
            elif word2 in line:
                wordcount[word2] += 1
    print(str(wordcount))
read_file()