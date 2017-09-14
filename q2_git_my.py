#
# *** To solve this problem _without_ loops or multiplication requires recursion ***
#

def RouterInterfaces (routerNum):                                                   # define the function and pass in the number of routers
    if (routerNum == 0):                                                            # build base case for recursion and return 0 as initial router count can be zero
        print("RouterInterfaces (" + str(routerNum) +  ") = 0 ")                    # print base case RouterInterfaces (0) = 0
        return (0)
    if (routerNum %5 == 0):                                                         # use modulo math to address multiples of 5 cases
        res = 5 + RouterInterfaces(routerNum -1)
        print("RouterInterfaces (" + str(routerNum) + ")" + " = " + str(res))
        return res

    else:
        res = 10 + RouterInterfaces(routerNum -1)                                   # all other router have 10 interfaces
        print("RouterInterfaces (" + str(routerNum) + ")" + " = " + str(res))
        return res

print''                                                                             # line break to make output a little easier to read
RouterInterfaces(17)                                                                # call the function to produce output

