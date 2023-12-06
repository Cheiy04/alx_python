def common_elements(set_1, set_2):
    duplicate = set()

    for item in set_1:
        if item in set_2 :
            duplicate.add(item)

    return duplicate

if __name__ == '__main__':

    set_1 = { "Python", "C", "Javascript" }
    set_2 = { "Bash", "C", "Ruby", "Perl" }
    c_set = common_elements(set_1, set_2)
    print(list(c_set))