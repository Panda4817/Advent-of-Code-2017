def create_dancers(num, start):
    letters = []
    letter = ord(start)
    for i in range(num):
        letters.append(chr(letter))
        letter += 1
        if letter > ord("z"):
            letter = ord("a")
    return letters

def spin(lst, num):
    return lst[-num:] + lst[0:-num]


def exchange(lst, p1, p2):
    lst[p1], lst[p2] = lst[p2], lst[p1]
    return lst

def partner(lst, l1, l2):
    tup = tuple(lst)
    p1 = tup.index(l1)
    p2 = tup.index(l2)
    lst[p1],lst[p2] = lst[p2], lst[p1]
    return lst

def parse_move(move, lst):
    type = move[0]
    if type == 's':
        data = int(move[1:])
        lst = spin(lst, data)
    elif type == 'x':
        data = move[1:].split("/")
        lst = exchange(lst, int(data[0]), int(data[1]))
    elif type == 'p':
        data = move[1:].split("/")
        lst = partner(lst, data[0], data[1])
    return lst

def process_data(data):
    dancers = 16
    moves = data.split(",")
    dancers_lst = create_dancers(dancers, "a")
    return moves, dancers_lst

def one_dance_round(lst, moves):
    for m in moves:
        lst = parse_move(m, lst)
    return lst 

def part1(data):
    moves, dancers_lst = process_data(data)
    dancers_lst = one_dance_round(dancers_lst, moves)
    return "".join(dancers_lst)

def part2(data):
    dance_rounds = 1000000000 #too big, find where the dance repeats
    moves, dancers_lst= process_data(data)
    start_seq = "".join(dancers_lst)
    sequences = {}
    for i in range(dance_rounds):
        last_seq = "".join(dancers_lst)
        sequences[i] = last_seq
        if last_seq == start_seq and i != 0:
            break
        dancers_lst = one_dance_round(dancers_lst, moves)
    
    dance_rounds = dance_rounds % i
    
    return sequences[dance_rounds]