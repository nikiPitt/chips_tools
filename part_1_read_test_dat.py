import cc_dat_utils as ccut

#Part 1
input_dat_file = "data/pfgd_test.dat"

def main():
    data = ccut.make_cc_level_pack_from_dat(input_dat_file)
    print(data)
    #Directly produce terminal result into txt file
    #Python3 part_1_read_test_dat.py > ./output.txt

main()