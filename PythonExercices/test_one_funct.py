import re


def datesBetween(enter_list):
    result_list = []
    regex = r"^\d{4}-\d{2}-\d{2}$"
    for i in enter_list:
        if re.match(regex, i) is None:
            print(f"{i}, no cumple el regex")
        else:
            result_list.append(i)

    return result_list[0], result_list[-1]


fecha_list = ['2023-08-01', '2023-09-01', '2023-10-01']
guardar = datesBetween(fecha_list)
print(guardar)
print(type(guardar))