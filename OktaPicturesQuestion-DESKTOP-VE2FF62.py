<<<<<<< HEAD:OktaPicturesQuestion-DESKTOP-VE2FF62.py
from collections import defaultdict
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
# TEst Case:
test = "photo.jpg, Warsaw, 2013-09-05 14:08:15\njohn.png, London, 2015-06-20 15:13:22\n myFriends.png, Warsaw, 2013-09-05 14:07:13\nEiffel.jpg, Paris, 2015-07-23 08:03:02\npisatower.jpg, Paris, 2015-07-22 23:59:59\nBOB.jpg, London, 2015-08-05 00:02:03\nnotredame.png, Paris, 2015-09-01 12:00:00\nme.jpg, Warsaw, 2013-09-06 15:40:22\na.png, Warsaw, 2016-02-13 13:33:50\nb.jpg, Warsaw, 2016-01-02 15:12:22\nc.jpg, Warsaw, 2016-01-02 14:34:30\nd.jpg, Warsaw, 2016-01-02 15:15:01\ne.png, Warsaw, 2016-01-02 09:49:09\nf.png, Warsaw, 2016-01-02 10:55:32\n g.jpg, Warsaw, 2016-02-29 22:13:11"


def get_significant(num):
    times = 0
    while(num > 0):
        num = num // 10
        times += 1
    return times


def solution(S):
    # write your code in Python 2.7
    pass
    input_list = list(S.split('\n'))

    # print(input_list)
    # split input list by commas
    for i in range(len(input_list)):
        input_list[i] = input_list[i].split(',')  # stores original order
    # print(input_list)

    # split by '.' for extension type and assign it an order #
    order = 1
    for j in range(len(input_list)):
        input_list[j][0] = input_list[j][0].split('.')
        input_list[j].append(order)
        order += 1

    # sort the list based on city name
    new_list = sorted(input_list, key=lambda x: x[1])

    # dict to hold key: city name ; val: list holding all pictures taken in that city
    cities_dict = defaultdict(list)

    # Update the cities_dict by appending to its stored list
    for photo in range(len(new_list)):
        city = new_list[photo][1]
        cities_dict[city].append(new_list[photo])

    # go through the city dict, and for each val (a list of pictures), sort by date taken
    for key, val in cities_dict.items():
        cities_dict[key] = sorted(cities_dict[key], key=lambda x: x[2])
    # print(cities_dict)

    # result list to eventually join as a string
    result_list = [0 for i in range(len(input_list))]

    for key, val in cities_dict.items():
        # print(key,val)
        pic = 1
        for i in range(len(cities_dict[key])):
            # print(cities_dict[key][i])
            tests = len(cities_dict[key])
            figs = get_significant(tests)
            result_list[val[i][3] - 1] = val[i][1] + '0' * \
                (figs - get_significant(pic)) + str(pic) + '.' + val[i][0][1]
            pic += 1
    return_string = "\n".join(list(map(lambda x: x.strip(), result_list)))
    # print(return_string)
    return return_string


print(solution(test))
=======
from collections import defaultdict
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
# TEst Case:
test = "photo.jpg, Warsaw, 2013-09-05 14:08:15\njohn.png, London, 2015-06-20 15:13:22\n myFriends.png, Warsaw, 2013-09-05 14:07:13\nEiffel.jpg, Paris, 2015-07-23 08:03:02\npisatower.jpg, Paris, 2015-07-22 23:59:59\nBOB.jpg, London, 2015-08-05 00:02:03\nnotredame.png, Paris, 2015-09-01 12:00:00\nme.jpg, Warsaw, 2013-09-06 15:40:22\na.png, Warsaw, 2016-02-13 13:33:50\nb.jpg, Warsaw, 2016-01-02 15:12:22\nc.jpg, Warsaw, 2016-01-02 14:34:30\nd.jpg, Warsaw, 2016-01-02 15:15:01\ne.png, Warsaw, 2016-01-02 09:49:09\nf.png, Warsaw, 2016-01-02 10:55:32\n g.jpg, Warsaw, 2016-02-29 22:13:11"


def get_significant(num):
    times = 0
    while(num > 0):
        num = num // 10
        times += 1
    return times


def solution(S):
    # write your code in Python 2.7
    pass
    input_list = list(S.split('\n'))

    # print(input_list)
    # split input list by commas
    for i in range(len(input_list)):
        input_list[i] = input_list[i].split(',')  # stores original order
    # print(input_list)

    # split by '.' for extension type and assign it an order #
    order = 1
    for j in range(len(input_list)):
        input_list[j][0] = input_list[j][0].split('.')
        input_list[j].append(order)
        order += 1

    # sort the list based on city name
    new_list = sorted(input_list, key=lambda x: x[1])

    # dict to hold key: city name ; val: list holding all pictures taken in that city
    cities_dict = defaultdict(list)

    # Update the cities_dict by appending to its stored list
    for photo in range(len(new_list)):
        city = new_list[photo][1]
        cities_dict[city].append(new_list[photo])

    # go through the city dict, and for each val (a list of pictures), sort by date taken
    for key, val in cities_dict.items():
        cities_dict[key] = sorted(cities_dict[key], key=lambda x: x[2])
    # print(cities_dict)

    # result list to eventually join as a string
    result_list = [0 for i in range(len(input_list))]

    for key, val in cities_dict.items():
        # print(key,val)
        pic = 1
        for i in range(len(cities_dict[key])):
            # print(cities_dict[key][i])
            tests = len(cities_dict[key])
            figs = get_significant(tests)
            result_list[val[i][3] - 1] = val[i][1] + '0' * \
                (figs - get_significant(pic)) + str(pic) + '.' + val[i][0][1]
            pic += 1
    return_string = "\n".join(list(map(lambda x: x.strip(), result_list)))
    # print(return_string)
    return return_string


print(solution(test))
>>>>>>> 37ecb04ef3303ff821c407fbe788dc2f07b86a25:OktaPicturesQuestion.py
