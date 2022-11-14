import sys


def main(input_filename):
    fin = open(input_filename, "r", encoding='utf8')
    fout = open("__" + input_filename, "w", encoding='utf8')

    for line in fin.readlines():
        if len(line) > 0:
            if line[0] == '2' and line[1] == '0' or (line[:4] == "http"):
                pass
            else:
                fout.write(line)


if __name__ == '__main__':
    
    input_filename = '/Users/chenjia/Desktop/danmu.txt'
    main(input_filename)