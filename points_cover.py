import itertools
import argparse

points = list()
U = dict()
S = list()

parser = argparse.ArgumentParser(description= 'Hitting objects problem Solution')
parser.add_argument('-f', '--brute_force', action='store_true')
parser.add_argument('-g', '--parallel_lines', action='store_true')
parser.add_argument('txt_file', type=str)
args = parser.parse_args()
answer = list()

def read_example_txt(example_file):
    with open(example_file, 'r') as txt_file:
        for line in txt_file:
            point = line.split()
            x = int(point[0])
            y = int(point[1])
            points.append((x,y))
    for count, point in enumerate(points):
        U.update({tuple(point) : count+1})

def line_Through_Two_Points_NP(A, B):

    rise = B[1] - A[1]
    run = A[0] - B[0]
    c = rise*(A[0]) + run*(A[1])
    return([rise,run,c])

def point_validates_line(line, point):

    cPoint = line[0] * point[0] + line[1] * point[1]
    if cPoint == line[2]:
        return True
    else:
        return False

def remove_duplicates(ls):
    ls.sort()
    return list(ls for ls,_ in itertools.groupby(ls))

def find_contestant_lines():
    lines = list()
    S_temp = list()
    S = list()
    if args.parallel_lines:
        y_coord = {y[1] for y in points}
        x_coord = {x[0] for x in points}
        for y in y_coord:
            temp_list = list()
            for point in points:
                if point[1] == y:
                    temp_list.append(point)
            lines.append(temp_list)
        for x in x_coord:
            temp_list = list()
            for point in points:
                if point[0] == x:
                    temp_list.append(point)
            lines.append(temp_list)
    else:
        for i, point in enumerate(points[:-1]):
            for next_point in points[i+1:]:
                temp_list = list()
                line = line_Through_Two_Points_NP(point, next_point)

                for each_point in points:
                    if point_validates_line(line, each_point):
                        temp_list.append(each_point)
                lines.append(temp_list)
                lines = remove_duplicates(lines)

    for line in lines:
        temp_list = list()
        for point in line:
            temp_list.append(U[point])
        S_temp.append(temp_list)

    if not args.parallel_lines:
        S_temp = find_lines_combinations(S_temp)
        S = [line for line in S_temp if len(line)!= 1]
    else:
        S = S_temp
    return S
    
def find_lines_combinations(lines):
    S_temp = list()
    for line in lines:
        for i, j in itertools.combinations(range(len(line) + 1), 2):
            S_temp.append(line[i:j])
    S_temp = remove_duplicates(S_temp)
    return S_temp
    
#--------------------------------Functions for brute force algorithm-----------------------------
def find_subsets(S):
    Subsets = list()
    for i in range(1, len(S) + 1):
        for subset in itertools.combinations(S, i):
            Subsets.append(list(subset))
    return Subsets

def subset_covers_U(subset):
    pointCovered = [False] * len(points)
    for line in subset:
        for point in line:
            pointCovered[point-1] = True
    if all(pointCovered):
        return True
    else:
        return False

def brute_force_solution():
    Subsets = find_subsets(S)
    answer = list()
    for subset in Subsets:
        if subset_covers_U(subset):
            answer = subset
            break
    return answer

#--------------------------------Functions for approximative algorithm-----------------------------
def update_coverage_of_S(pointCovered):
    count_list = list()
    for line in S:
        count = 0
        for point in line:
            if pointCovered[point-1] == False:
                count = count + 1
        count_list.append(count)
    return count_list

def get_max_S_coverage(S_coverage):
    index = S_coverage.index(max(S_coverage))
    return index

def approximative_solution():
    pointCovered = [False] * len(points)
    S_coverage = update_coverage_of_S(pointCovered)
    answer = list()

    while not all(pointCovered) == True:
    
        most_cover_index = get_max_S_coverage(S_coverage)
        S_max = S[most_cover_index]
        S_coverage[most_cover_index] = 0
        for point in S_max:
            pointCovered[point-1] = True
        S_coverage = update_coverage_of_S(pointCovered)
        answer.append(S_max)
    
    return answer

#--------------------------------------------------------------------------------------------------
def print_answer(answer):
    answer_XY = list()
    U_rev = {value:key for key, value in U.items()}
    
    for line in answer:
        line_XY = list()
        
        for point in line:
            line_XY.append(U_rev[point])
        answer_XY.append(line_XY)

    for line in answer_XY:
        temp_line = line
        if len(line) == 1:
            next_point = line[0]
            next_point = (next_point[0]+1, next_point[1])
            temp_line.append(next_point)
        temp_line.sort()
        print(*temp_line)

read_example_txt(args.txt_file)
S = find_contestant_lines()
S = [tuple(x) for x in S]

if args.brute_force:
    answer = brute_force_solution()
else:
    answer = approximative_solution()

print_answer(answer)