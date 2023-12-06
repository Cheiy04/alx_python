def best_score(a_dictionary):
    if not a_dictionary:
        return None
    
    max_value = max(a_dictionary.values())
    for key, value in a_dictionary.items():
        if value == max_value:
            return key

if __name__ == '__main__':
    scores = {'Alice': 85, 'Bob': 92, 'Charlie': 78, 'David': 64}
    best_student = best_score(scores)
    print("Student with the best score:", best_student)

