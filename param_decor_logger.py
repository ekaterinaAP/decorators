from datetime import datetime


def param_decor_logger(path):
    def decor_logger(function_to_decor):
        def get_inf_function(*args, **qwargs):
            with open(path, "a") as file:
                file.seek(0, 2)
                time = datetime.today()
                args_v = args
                qwargs_v = qwargs
                name_function = function_to_decor
                file.write(f'время выполнения: {time} \n')
                file.write(f'аргументы: {args_v} \n')
                file.write(f'ещё аргументы: {qwargs_v} \n')
                file.write(f'имя функции: {name_function} \n')
                file.write('\n')

            function_to_decor(*args, **qwargs)
        return get_inf_function
    return decor_logger


if __name__ == '__main__':
    @param_decor_logger('log.txt')
    def some_function(x, a):
        print(x, a)


    some_function('очень весело', a='Ха-ха-ха')