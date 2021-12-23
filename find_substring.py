def count_substring(string, sub_string):
    len_string = len(string)
    len_sub_string = len(sub_string)

    count = 0
    for i in range(len_string):
        if len_string - i >= len_sub_string:
            string_check = ''
            for j in range(len_sub_string):
                string_check += string[i+j]

            if string_check == sub_string:
                count += 1
    return count


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)
