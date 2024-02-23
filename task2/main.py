# 9. Строки, элементы которых не убывают (т.е. образуют неубывающую
# последовательность чисел) переместить в начало (вверх), сохранив при этом взаимное расположением перемещаемых строк.


def up(row):
    return all(row[i] <= row[i + 1] for i in range(len(row) - 1))


def logic(array2d):
    for i in range(len(array2d)):
        for j in range(i + 1, len(array2d)):
            if up(array2d[j]):
                array2d[i], array2d[j] = array2d[j], array2d[i]
                break


def test_function():
    with open('input2.txt', 'r') as f:
        m = []
        for i in f:
            m.append([int(i) for i in i.strip().split(',')])
    logic(m)
    with open('output2.txt', 'w') as f:
        for i in m:
            f.write(" ".join([str(x) for x in i]))
            f.write('\n')


test_function()
