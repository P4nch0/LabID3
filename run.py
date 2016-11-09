import sys
import id3
import numpy as np

if __name__ == '__main__':
    result = id3.ID3()
    attr_end = False
    attrs = []
    data = []
    # Read each input line
    for line in sys.stdin:
        line = line.strip("\n")

        # ignore the comments in the file
        if line.startswith("%"):
            continue

        if not attr_end: # While no "@data" is encountered, it will keep parsing attributes
            if line.startswith("@attribute") or line.startswith("@ATTRIBUTE"):
                # reads the line, removes "@attribute", appends the attr name to the array
                attrs.append(line.split()[1])

            # end attribute cycle if data is encountered
            elif line.startswith("@data") or line.startswith("@DATA"):
                attr_end = True
        else:
            # parse data into array, .arff data is separated by commas
            data.append(line.split(','))
    # print data
    # format the array with NumPy
    data = np.array(data)
    # print data
    # print data.dtype
    params = data[:, 0:-1]
    ans = data[:, -1]

    result.create_tree(params, ans, attrs[0:-1])
    print str(result)