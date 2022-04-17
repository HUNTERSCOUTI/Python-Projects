class temps:
    @staticmethod
    def r_w_file(infile, outfile):
        f = open("infile.txt", "r")
        #print(f.read())
        t = open("outfile.txt", "x")
        for x in f:
            



temps.r_w_file("infile.txt", "outfile.txt")
