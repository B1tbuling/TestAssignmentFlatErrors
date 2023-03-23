from example import ERRORS_EXAMPLE


''' 
    Функция flat проходится рекурсивно по словарю ошибок:
        - если вложенный элемент (в результате рекурсии) - строка, то завершаем рекурсию и добавляем в итоговый
            словарь путь-ключ и текст ошибки;
        - вложенный словарь содержит те же данные, что и словарь ошибок, поэтому рекурсивно вызываем функцию flat,
            передавая список ключей-родителей;
        - вложенный список содержит словари (возможно, что он может просто содержать строки ошибок, данный случай 
            функция не поддерживает. Уточнить по ТЗ, возможен ли такой случай), поэтому итерируемся по нему и 
            рекурсивно вызываем функцию flat, т.к. (см. пункт выше);
    и выводит итоговый словарь, где ключом является путь до ошибки (во вложенном словаре ошибок),
    а значением - текст ошибки.
    
    
    >>> from example import ERRORS_EXAMPLE
    >>> flat(ERRORS_EXAMPLE)
    {'last_name': 'Имя должно состоять из букв','birth_place.address.parts.0.id': 'Неверный идентификатор', 'birth_place.address.parts.1.id': 'Неверный идентификатор', 'groups.1': 'Группа workers не существует'}  
'''


def flat(errors: dict[str, dict | list | str], parent_keys=[], flat_err={}) -> dict[str, str]:
    for err_key, err_value in errors.items():
        match err_value:
            case str():
                flat_err['.'.join(parent_keys + [err_key])] = err_value

            case dict():
                flat(err_value, parent_keys=parent_keys + [err_key], flat_err=flat_err)

            case list():
                for i, dict_err in enumerate(err_value):
                    '''
                        При итерировании по списку, если у вложенного словаря есть дублирующие ключи (т.к в ключе
                        не выводится индекс элемента списка), значение будет перезаписано.
                        Пример решения данной проблемы (но нужно уточнить ТЗ):
                        
                        >>> flat(dict_err, parent_keys=parent_keys + [err_key, f'[{i}]'], flat_err=flat_err)
                    '''
                    flat(dict_err, parent_keys=parent_keys + [err_key], flat_err=flat_err)
    return flat_err


print(flat(ERRORS_EXAMPLE))
