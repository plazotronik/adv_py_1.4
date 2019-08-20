import sys


def spliter(string, count):
    start = 0
    end = count
    while start < len(string):
        yield string[start:end]
        start += count
        end += count


def adv_print(*args, **kwargs):
    """
    Advanced print.
    :param args:
    Object for print (string).
    :param kwargs:
    Standard function print. Addon func:
    start - first simbol (def: new line)
    max_line - max simbols in line (def: unlim)
    in_file - print and write to file (def: only print)
    :return:
    """
    params = {
    'sep': ' ',
    'end': '\n',
    'file': sys.stdout,
    'flush': False,
    'start': '\n',
    'max_line': None,
    'in_file': sys.stdout,
    }
    for key in kwargs.keys():
        params[key] = kwargs[key]
    for k, v in params.items():
        globals()[f'_{k}'] = v
    _objects = _sep.join(args)
    if _in_file == sys.stdout or _in_file in [None, False]:
        if _max_line in [None, False]:
            print(_start)
            print(_objects, end=_end, file=_file, flush=_flush)
        else:
            print(_start)
            print('\n'.join(spliter(_objects, _max_line)), end=_end, file=_file, flush=_flush)

    else:
        if _max_line in [None, False]:
            print(_start)
            print(_objects, end=_end, file=_file, flush=_flush)
            with open(_in_file, 'at', encoding='utf8') as file_out:
                file_out.write(_start)
                file_out.write(_objects)
                file_out.write(_end)
        else:
            print(_start)
            print('\n'.join(spliter(_objects, _max_line)), end=_end, file=_file, flush=_flush)
            with open(_in_file, 'at', encoding='utf8') as file_out:
                file_out.write(_start)
                file_out.write('\n'.join(spliter(_objects, _max_line)))
                file_out.write(_end)
