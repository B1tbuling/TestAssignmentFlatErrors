from example import ERRORS_EXAMPLE


''' Данная реализация передает рекурсивно ключ-путь строкой, а не списком '''


def flat(errors: dict[str, dict | list | str], parent_key='', flat_err={}) -> dict[str, str]:
    for err_key, err_value in errors.items():
        match err_value:
            case str():
                if parent_key == '':
                    flat_err[err_key] = err_value
                else:
                    flat_err[f'{parent_key}.{err_key}'] = err_value

            case dict():
                parent_err_key = err_key if parent_key == '' else f'{parent_key}.{err_key}'
                flat(err_value, parent_key=parent_err_key, flat_err=flat_err)

            case list():
                for dict_err in err_value:
                    parent_err_key = err_key if parent_key == '' else f'{parent_key}.{err_key}'
                    flat(dict_err, parent_key=parent_err_key, flat_err=flat_err)

    return flat_err


print(flat(ERRORS_EXAMPLE))
