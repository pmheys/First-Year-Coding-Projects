##Practice Major 4

data = [["Gender", "Birth Year", "Grad Year", "Sessional Average"],
        ["F", 1989, 2011, [11.32, 10.45, 10.22, 7.81]],
        ["F", 1990, 2013, [7.36, 8.12, 6.33, 9.83, 7.43]],
        ["M", 1987, 2010, [7.25, 8.42, 6.23, 9.26, 9.54, 9.48]]]

def isGraduated(student):
    
    grad = False
    if student[2] <= 2016:
        grad = True

    return grad

def isGender(student, gender):

    output = False
    if student[0] == gender:
        output = True

    return output

def isLastYearAverageAbove(student, grade):

    output = False
    if student[3][len(student[3])-1] > grade:
        output = True

    return output

def query(data, grade, gender):

    numGender = 0
    numGrade = 0

    for i in range(len(data)-1):
        if isGraduated(data[i+1]):
            if isGender(data[i+1], gender):
                numGender += 1
                if isLastYearAverageAbove(data[i+1], grade):
                    numGrade += 1

    output = (float(numGrade)/numGender)*100
    return output

        







            
        
