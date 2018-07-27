#filelist of images names in a file
with open("../augmented_DATA/testdata3/filelist_N_test.txt", "rt") as fin:
    # filelist of images path and names and label
    with open("../augmented_DATA/testdata3/filenames_test.txt", "wt") as fout:
        for line in fin:
                line = '../augmented_DATA/testdata3/N_test/'+ line.replace('\n',' ') + '0\n'
                fout.write(line)
