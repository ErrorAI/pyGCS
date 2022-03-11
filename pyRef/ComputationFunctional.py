# This Python file uses the following encoding: utf-8
import os

class ComputationFunctional:
    def __init__(self, name):
        self.name = name
        self.define_s = ["ClearOut"]
        self.use = ["AlphaS"]
        self.l_PDFsname = ["mstw"]
        self.shabMainPath = "/home/user1/proj/pyRef/parts/main.cc"
        self.shabPath = "/home/user1/proj/pyRef/parts/shab"
        self.workDir = "/home/user1/proj/pyRef/computation/" + self.name
        self.includesDir = {}
        pass

    def runComputation(self):
        if not os.path.exists(self.workDir):
            os.makedirs(self.workDir)


        for file in os.listdir(self.shabPath):
            shabFile = open(self.shabPath + "/" + file, "r")
            tempArg = "arg"
            for line in shabFile.readlines():
                if line[0] == "$":
                    arg = line.split("(")[1][:-3]
                    if self.includesDir.get(arg, True):
                        self.includesDir[arg] = []
                    tempArg = arg
                else:
                    self.includesDir[tempArg].append(line)

            shabFile.close

        shabMain = open(self.shabMainPath, "r")
        shabMainLines = shabMain.readlines()


        if os.path.exists(self.workDir + "/main.cc"):
            os.remove(self.workDir + "/main.cc")
        mainFile = open(self.workDir + "/main.cc", "x")
        mainFile.close

        mainFile = open(self.workDir + "/main.cc", "w")

        for shabMain_l in shabMainLines:
            if shabMain_l[0] == "$":
                includeArg = shabMain_l.split("(")[1][:-2]
                try:
                    self.includesDir[includeArg]
                except:
                    print("Error, not exist shabName: ", includeArg)
                    break
                for incarg in self.includesDir[includeArg]:
                    mainFile.write(incarg)
                self.includesDir.pop(includeArg, None)

            else:
                mainFile.write(shabMain_l)
        print("Not use: ", self.includesDir.keys())
        mainFile.close
        shabMain.close

    def getUSEsname(self):
        return ["AlphaS", "AplhaPhysics"]

    def getPDFsname(self):
        return self.l_PDFsname

    def setPDF(self, pdfPath):
        pass
