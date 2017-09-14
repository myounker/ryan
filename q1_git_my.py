example_string = '{"totalCount": "1", "ID": "1029", "IP": "10.0.0.1"}'  # set example string
q1_dict = {}                                                            # init question 1 dictionary variable

def j_str_2_dict(funct_string):                         # define function
    json_dict = {}                                      # create dictionary to return

    for kv_pair in funct_string.split(','):             # find key / value pairs in string
        kv_str = str()                                  # init key/value string variable to be used
        key_str = str()                                 # init key string variable to be used
        value_str = str()                               # init value string variable to be used
        for elements in kv_pair:                        # strip out { & } & " & space
            if (elements != '{' and elements != '}' and elements != '"' and elements != ' '):
                kv_str = kv_str + elements              # build key/value string without delimiters
        key = True                                      # use to decide if in key or value part of k/v string
        for chars in kv_str:                            # build individual key & value strings
            if key and (chars != ':'):                  # if you haven't seen : yet you are in key
                key_str = key_str + chars               # build key string
            elif not key and (chars != ':'):            # else sets key to false once it sees : so you must be in value
                value_str = value_str + chars           # build value string
            else:                                       # must be a : so you are moving to value
                key = False                             # set key to false so you start to build value string
        json_dict[key_str] = value_str                  # insert key and value into dictionary
    return (json_dict)                                  # return the dictionary from the function

q1_dict = j_str_2_dict(example_string)                  # main code - call the function and pass in a sample string
print ' '                                               # put in blank line to make code readable
print (type(q1_dict))                                   # print type of q1_dict variable to prove it's a dictionary
print (str(q1_dict))                                    # print out contents of q1_dict