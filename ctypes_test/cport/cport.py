import sys, os

dir_path = os.path.dirname(os.path.realpath(__file__))
temp_path = os.path.join(dir_path, "temp.txt")


def main():
    mode = sys.argv[1]

    if mode == "-python":
        port_python()


def port_python():
    file_name = sys.argv[2]

    f = open(temp_path, "w")
    f.write(file_name)
    f.close()

    os.system("swig -python " + file_name + ".i")
    os.system("python3 " + os.path.join(dir_path, "setup.py")+" build_ext --inplace")



if __name__ == "__main__":
    try:
        main()
    except:
        print("error, type 'cport.py -help' for more information.")