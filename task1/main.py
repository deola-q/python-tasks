# 9. Необходимо реализовать функцию, которая из списка чисел создаст новый список,
# в котором подряд идущие одинаковые числа будут заменены одним вхождением, например:


def changing_for_array(array):
    new_array = [array[0]]
    for i in range(1, len(array)):
        if array[i - 1] != array[i]:
            new_array.append(array[i])

    return new_array


def test_function():
    with open('input1.txt', 'r') as f:
        array = [int(i) for i in f.readline().split(',')]
        answer = changing_for_array(array)

    with open('output1.txt', 'w') as f:
        f.write(" ".join([str(x) for x in answer]))


test_function()
