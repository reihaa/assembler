class Assembler:
    def __init__(self):
        prefix = []
        rex = []
        opcode = []
        d = []
        code_w = []
        Opcode = [opcode,d,code_w]
        mod = []
        reg = []
        r_m = []
        mod_rm = [mod,reg,r_m]
        scale= []
        index = []
        base = []
        sib = [scale,index,base]
        displacement = []
        data = []
        code = [prefix,rex,Opcode,mod_rm,sib,displacement,data]

        return

    def assemble(self, file):
        bin_file = open('bin_code.bin', 'wb')
        for instruction in file:
            machine_code = self.ins_to_mc(instruction)
            bin_file.write(machine_code)
        bin_file.close()
        return

    def ins_to_mc(self, instruction):
        return

    def instuction_classifier(self, instruction):
        return
