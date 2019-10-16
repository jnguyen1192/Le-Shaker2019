from sys import stdin, stdout


def analyse_template(expression):
    return expression


def template(nb_line):
    res = ""
    listres = []
    while nb_line != 0:
        expression = stdin.readline()
        #analyse_template(expression).split(' ')
        listres.append(analyse_template(expression[:-1] + '\n' * 1))
        nb_line -= 1
    res = res.join(listres)
    stdout.write(res)


if __name__ == "__main__":
    # execute only if run as a script
    template(int(stdin.readline()))
