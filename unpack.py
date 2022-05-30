import sys, source

#DEAFinitely
#Aviran Gur
def main(argv):
    if '-r' in argv:
        argv.remove('-r')
        for path in argv:
            source.recunpack(path)
    else:
        for path in argv:
            source.unpack(path)

if __name__ == "__main__":
    main(sys.argv[1:])