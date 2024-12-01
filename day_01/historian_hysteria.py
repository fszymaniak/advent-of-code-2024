import csv

office, locationId = [], []
def save_distance_file_into_two_separate_list():
    with open("day_01/input_data.txt") as file:
        readfile = csv.reader(file, delimiter=' ')

        for line in readfile:
            line = list(filter(lambda x: len(x), line))
            o = int(line[0])
            l = int(line[1])
            office.append(o)
            locationId.append(l)
        file.close()

    office.sort()
    locationId.sort()

def calculate_distance():
    index = 0
    distance = 0
    while index < len(office):
        distance += abs(office[index] - locationId[index])
        index += 1

    print("Distance: " + str(distance))

def calculate_similarity_score():
    index = 0
    similarity_score = 0
    while index < len(office):
        current_office_value = office[index]
        similarity_score += locationId.count(current_office_value) * current_office_value
        index += 1

    print("Similarity Score: " + str(similarity_score))

save_distance_file_into_two_separate_list()
calculate_distance()
calculate_similarity_score()