# TODO Напишите функцию find_common_participants

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

def find_common_participants(group1, group2, delimiter=","):
    list1 = group1.split(delimiter)
    list2 = group2.split(delimiter)
    common = []
    for name in list1:
        if name in list2:
            common.append(name)
    common.sort()
    return common

# TODO Провеьте работу функции с разделителем отличным от запятой

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

result = find_common_participants(
    participants_first_group,
    participants_second_group,
    delimiter="|"
)

print(result)