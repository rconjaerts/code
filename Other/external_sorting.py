import random

def create_random_file(start, end):
    numbers = [i for i in range(start, end)]
    random.shuffle(numbers)

    file = open('random_file.txt', 'w')
    for numb in numbers:
        file.write(str(numb)+'\n')

    file.close

def create_ordered_chunks(memory_size, num_chunks):
    file = open('random_file.txt', 'r')
    for file_number in range(num_chunks):
        chunk = []
        for _ in range(memory_size):
            chunk.append(int(file.readline()))
        chunk.sort()
        file_chunk = open('chunk_'+str(file_number)+'.txt', 'w')
        for numb in chunk:
            file_chunk.write(str(numb)+'\n')
        file_chunk.close
    file.close

def refill_chunk(file):
    return [int(file.readline()) for _ in range(10)]

def find_next_smallest(input):
    all_smallest = [x[0] for x in input]
    return all_smallest.index(min(all_smallest))

def sort_all_chunks(num_chunks, output_size):
    # create an open link to the files so we can read the lines were we stopped
    open_files = [open('chunk_'+str(i)+'.txt', 'r') for i in range(num_chunks)]
    # input files
    input = [[int(file.readline()) for _ in range(output_size)] for file in open_files]
    counter = [1]*output_size
    output = []
    sorted_file = open('sorted_file.txt', 'w')

    # naive k-way merging
    while input:
        smallest = find_next_smallest(input)
        output.append(input[smallest].pop(0))
        # write the output away
        if len(output) == output_size:
            for line in output:
                sorted_file.write(str(line)+'\n')
            output = []
        
        if not input[smallest]:
            if counter[smallest] != output_size:
                input[smallest] = refill_chunk(open_files[smallest])
                counter[smallest] += 1
            else:
                open_files[smallest].close
                del open_files[smallest]
                del input[smallest] 
                del counter[smallest]

    for file in open_files:
        print('still doing this')
        file.close
    sorted_file.close

create_random_file(0, 900)
num_lines = sum(1 for line in open('random_file.txt'))
num_chunks = 9
memory_size = num_lines/num_chunks
create_ordered_chunks(memory_size, num_chunks)
sort_all_chunks(num_chunks, 10)