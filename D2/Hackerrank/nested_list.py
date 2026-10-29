if __name__ == '__main__':
    students = []
    
    # 1. Read input and build the nested list
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])
    
    # 2. Extract all unique scores and sort them ascending
    # Using a set eliminates duplicate scores automatically
    unique_scores = sorted(list(set([student[1] for student in students])))
    
    # 3. Get the second lowest score (index 1 of unique scores)
    second_lowest_score = unique_scores[1]
   
    # 4. Filter out names of students who have this second lowest score
    second_lowest_students = [student[0] for student in students if student[1] == second_lowest_score]
    
    # 5. Sort the filtered names alphabetically
    second_lowest_students.sort()
    # 6. Print each name on a new line
    for name in second_lowest_students:
        print(name)
