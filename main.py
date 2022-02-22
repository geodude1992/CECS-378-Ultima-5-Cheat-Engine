# Memory-mapped file objects behave like both bytearray and like file objects.
import mmap

# File Objects

"""
    The open() function takes two parameters; filename, and mode.
    There are four different methods (modes) for opening a file:
        "r" - Read - Default value. Opens a file for reading, error if the file does not exist
        "a" - Append - Opens a file for appending, creates the file if it does not exist
        "w" - Write - Opens a file for writing, creates the file if it does not exist
        "x" - Create - Creates the specified file, returns an error if the file exists

        "b" - byte - Working with files in binary mode, add 'b' to argument
"""


with open("SAVED.GAM", mode='rb+') as byteReader:

    # If you wish to map an existing Python file object,
    # Use its fileno() method to obtain the correct value for the fileno parameter

    # If length is 0, the maximum length of the map is the current size of the file,
    # except that if the file is empty Windows raises an exception
    # (you cannot create an empty mapping on Windows).

    # class mmap.mmap(fileno, length, tagname=None, access=ACCESS_DEFAULT[,offset])
    memMap = mmap.mmap(byteReader.fileno(), 0)

    print("Drag your SAVED.GAM file into this scripts directory")
    '''
        Gold  0x204 -> 0x205
    '''
    memMap[516] = 231
    memMap[517] = 3

    '''
        Keys  0x206
    '''
    keys = int(input("Set keys: (0-99)\n"))
    memMap[518] = 100

    '''
        Gems  0x207
    '''
    gems = int(input("Set gems: (0-99)\n"))
    memMap[519] = gems

    '''
        Magic Carpet  0x20A
    '''
    magCarpet = int(input("Set Magic Carpet: (0-99)\n"))
    memMap[522] = magCarpet

    '''
        Skull Keys  0x20B
    '''
    skullKeys = int(input("Set Skull Keys: (0-99)\n"))
    memMap[523] = skullKeys

    '''
        Black Badge  0x218
    '''
    blackBadge = int(input("Set Black Badge: (0-99)\n"))
    memMap[536] = blackBadge

    '''
        Magic Axes  0x240
    '''
    magAxes = int(input("Set Magic Axes: (0-99)\n"))
    memMap[576] = magAxes


    # Each Player has 32 bytes
    '''
        Users Player  
    '''
    # 0x0E
    strP1 = int(input("Set Strength for Main Character: (0-99)\n"))
    memMap[14] = strP1

    # 0x0F
    dexP1 = int(input("Set Dextrity for Main Character: (0-99)\n"))
    memMap[15] = dexP1

    # 0x10
    intP1 = int(input("Set Intelligence for Main Character: (0-99)\n"))
    memMap[16] = intP1

    # 0x11
    magicP1 = int(input("Set Magic for Main Character: (0-99)\n"))
    memMap[17] = magicP1

    # 0x12->13  -> 0x03E7 in Little Endian
    memMap[18] = 231    # 0x37
    memMap[19] = 3

    # 0x14->15  -> 0x03E7 in Little Endian
    memMap[20] = 231
    memMap[21] = 3

    # 0x16->17  -> 0x270F in Little Endian
    memMap[22] = 15
    memMap[23] = 39





    '''
        Player 2: Shamino
    '''
    # 0x2E
    strP2 = int(input("Set Strength for Shamino: (0-99)\n"))
    memMap[46] = strP2

    # 0x2F
    dexP2 = int(input("Set Dextrity for Shamino: (0-99)\n"))
    memMap[47] = dexP2

    # 0x30
    intP2 = int(input("Set Intelligence for Shamino: (0-99)\n"))
    memMap[48] = intP2

    # 0x31
    magicP2 = int(input("Set Magic for Shamino: (0-99)\n"))
    memMap[49] = magicP2

    # 0x32->33  -> 0x03E7 in Little Endian
    memMap[50] = 231  # 0x37
    memMap[51] = 3

    # 0x34->35  -> 0x03E7 in Little Endian
    memMap[52] = 231
    memMap[53] = 3

    # 0x36->37  -> 0x270F in Little Endian
    memMap[54] = 15
    memMap[55] = 39





    '''
        Player 3: Iolo
    '''
    # 0x0E
    strP3 = int(input("Set Strength for Iolo: (0-99)\n"))
    memMap[78] = strP3

    # 0x0F
    dexP3 = int(input("Set Dextrity for Iolo: (0-99)\n"))
    memMap[79] = dexP3

    # 0x10
    intP3 = int(input("Set Intelligence for Iolo: (0-99)\n"))
    memMap[80] = intP3

    # 0x11
    magicP3 = int(input("Set Magic for Iolo: (0-99)\n"))
    memMap[81] = magicP3

    # 0x12->13  -> 0x03E7 in Little Endian
    memMap[82] = 231  # 0x37
    memMap[83] = 3

    # 0x14->15  -> 0x03E7 in Little Endian
    memMap[84] = 231
    memMap[85] = 3

    # 0x16->17  -> 0x270F in Little Endian
    memMap[86] = 15
    memMap[87] = 39




    '''
        Player 4: Mariah
    '''
    # 0x0E
    strP4 = int(input("Set Strength for Mariah: (0-99)\n"))
    memMap[110] = strP4

    # 0x0F
    dexP4 = int(input("Set Dextrity for Mariah: (0-99)\n"))
    memMap[111] = dexP4

    # 0x10
    intP4 = int(input("Set Intelligence for Mariah: (0-99)\n"))
    memMap[112] = intP4

    # 0x11
    magicP4 = int(input("Set Magic for Iolo: (0-99)\n"))
    memMap[113] = magicP4

    # 0x12->13  -> 0x03E7 in Little Endian
    memMap[114] = 231  # 0x37
    memMap[115] = 3

    # 0x14->15  -> 0x03E7 in Little Endian
    memMap[116] = 231
    memMap[117] = 3

    # 0x16->17  -> 0x270F in Little Endian
    memMap[118] = 15
    memMap[119] = 39




    '''
        Player 5: Geoffrey
    '''
    # 0x0E
    strP5 = int(input("Set Strength for Geoffrey: (0-99)\n"))
    memMap[142] = strP5

    # 0x0F
    dexP5 = int(input("Set Dextrity for Geoffrey: (0-99)\n"))
    memMap[143] = dexP5

    # 0x10
    intP5 = int(input("Set Intelligence for Geoffrey: (0-99)\n"))
    memMap[144] = intP5

    # 0x11
    magicP5 = int(input("Set Magic for Geoffrey: (0-99)\n"))
    memMap[145] = magicP5

    # 0x12->13  -> 0x03E7 in Little Endian
    memMap[146] = 231  # 0x37
    memMap[147] = 3

    # 0x14->15  -> 0x03E7 in Little Endian
    memMap[148] = 231
    memMap[149] = 3

    # 0x16->17  -> 0x270F in Little Endian
    memMap[150] = 15
    memMap[151] = 39
    
    
    
    
    '''
        Player 6: Janna
    '''

    # 0x0E
    strP6 = int(input("Set Strength for Janna: (0-99)\n"))
    memMap[174] = strP6

    # 0x0F
    dexP6 = int(input("Set Dextrity for Janna: (0-99)\n"))
    memMap[175] = dexP6

    # 0x10
    intP6 = int(input("Set Intelligence for Janna: (0-99)\n"))
    memMap[176] = intP6

    # 0x11
    magicP6 = int(input("Set Magic for Janna: (0-99)\n"))
    memMap[177] = magicP6

    # 0x12->13  -> 0x03E7 in Little Endian
    memMap[178] = 231  # 0x37
    memMap[179] = 3

    # 0x14->15  -> 0x03E7 in Little Endian
    memMap[180] = 231
    memMap[181] = 3

    # 0x16->17  -> 0x270F in Little Endian
    memMap[182] = 15
    memMap[183] = 39
    
    
    
    
    '''
        Player 7: Julia
    '''
    # 0x0E
    strP7 = int(input("Set Strength for Julia: (0-99)\n"))
    memMap[206] = strP7

    # 0x0F
    dexP7 = int(input("Set Dextrity for Julia: (0-99)\n"))
    memMap[207] = dexP7

    # 0x10
    intP7 = int(input("Set Intelligence for Julia: (0-99)\n"))
    memMap[208] = intP7

    # 0x11
    magicP7 = int(input("Set Magic for Janna: (0-99)\n"))
    memMap[209] = magicP7

    # 0x12->13  -> 0x03E7 in Little Endian
    memMap[210] = 231  # 0x37
    memMap[211] = 3

    # 0x14->15  -> 0x03E7 in Little Endian
    memMap[212] = 231
    memMap[213] = 3

    # 0x16->17  -> 0x270F in Little Endian
    memMap[214] = 15
    memMap[215] = 39

    
    
    
    '''
        Player 8: Dupre
    '''
    # 0x0E
    strP8 = int(input("Set Strength for Dupre: (0-99)\n"))
    memMap[238] = strP8

    # 0x0F
    dexP8 = int(input("Set Dextrity for Dupre: (0-99)\n"))
    memMap[239] = dexP8

    # 0x10
    intP8 = int(input("Set Intelligence for Dupre: (0-99)\n"))
    memMap[240] = intP8

    # 0x11
    magicP8 = int(input("Set Magic for Dupre: (0-99)\n"))
    memMap[241] = magicP8

    # 0x12->13  -> 0x03E7 in Little Endian
    memMap[242] = 231  # 0x37
    memMap[243] = 3

    # 0x14->15  -> 0x03E7 in Little Endian
    memMap[244] = 231
    memMap[245] = 3

    # 0x16->17  -> 0x270F in Little Endian
    memMap[246] = 15
    memMap[247] = 39
    
    
    
    
    '''
        Player 9: Katrina
    '''
    # 0x0E
    strP9 = int(input("Set Strength for Katrina: (0-99)\n"))
    memMap[270] = strP9

    # 0x0F
    dexP9 = int(input("Set Dextrity for Katrina: (0-99)\n"))
    memMap[271] = dexP9

    # 0x10
    intP9 = int(input("Set Intelligence for Katrina: (0-99)\n"))
    memMap[272] = intP9

    # 0x11
    magicP9 = int(input("Set Magic for Katrina: (0-99)\n"))
    memMap[273] = magicP9

    # 0x12->13  -> 0x03E7 in Little Endian
    memMap[274] = 231  # 0x37
    memMap[275] = 3

    # 0x14->15  -> 0x03E7 in Little Endian
    memMap[276] = 231
    memMap[277] = 3

    # 0x16->17  -> 0x270F in Little Endian
    memMap[278] = 15
    memMap[279] = 39

    
    
    
    '''
        Player 10: Sentri
    '''
    # 0x0E
    strP10 = int(input("Set Strength for Sentri: (0-99)\n"))
    memMap[302] = strP10

    # 0x0F
    dexP10 = int(input("Set Dextrity for Sentri: (0-99)\n"))
    memMap[303] = dexP10

    # 0x10
    intP10 = int(input("Set Intelligence for Sentri: (0-99)\n"))
    memMap[304] = intP10

    # 0x11
    magicP10 = int(input("Set Magic for Sentri: (0-99)\n"))
    memMap[305] = magicP10

    # 0x12->13  -> 0x03E7 in Little Endian
    memMap[306] = 231  # 0x37
    memMap[307] = 3

    # 0x14->15  -> 0x03E7 in Little Endian
    memMap[308] = 231
    memMap[309] = 3

    # 0x16->17  -> 0x270F in Little Endian
    memMap[310] = 15
    memMap[311] = 39

    
    
    
    '''
        Player 11: Gwenno
    '''
    # 0x0E
    strP11 = int(input("Set Strength for Gwenno: (0-99)\n"))
    memMap[334] = strP11

    # 0x0F
    dexP11 = int(input("Set Dextrity for Gwenno: (0-99)\n"))
    memMap[335] = dexP11

    # 0x10
    intP11 = int(input("Set Intelligence for Gwenno: (0-99)\n"))
    memMap[336] = intP11

    # 0x11
    magicP11 = int(input("Set Magic for Gwenno: (0-99)\n"))
    memMap[337] = magicP11

    # 0x12->13  -> 0x03E7 in Little Endian
    memMap[338] = 231  # 0x37
    memMap[339] = 3

    # 0x14->15  -> 0x03E7 in Little Endian
    memMap[340] = 231
    memMap[341] = 3

    # 0x16->17  -> 0x270F in Little Endian
    memMap[342] = 15
    memMap[343] = 39

    # 0x18
    # lvlP11 = input(int("Set Level for Gwenno: (0-99)\n"))
    #memMap[344] = 99
    
    
    
    
    '''
        Player 12: Johne
    '''
    # 0x0E
    strP12 = int(input("Set Strength for Johne: (0-99)\n"))
    memMap[366] = strP12

    # 0x0F
    dexP12 = int(input("Set Dextrity for Johne: (0-99)\n"))
    memMap[367] = dexP12

    # 0x10
    intP12 = int(input("Set Intelligence for Johne: (0-99)\n"))
    memMap[368] = intP12

    # 0x11
    magicP12 = int(input("Set Magic for Johne: (0-99)\n"))
    memMap[369] = magicP12

    # 0x12->13  -> 0x03E7 in Little Endian
    memMap[370] = 231  # 0x37
    memMap[371] = 3

    # 0x14->15  -> 0x03E7 in Little Endian
    memMap[372] = 231
    memMap[373] = 3

    # 0x16->17  -> 0x270F in Little Endian
    memMap[374] = 15
    memMap[375] = 39

    # 0x18
    # lvlP12 = input(int("Set Level for Johne: (0-99)\n"))
    #memMap[376] = 99
    
    
    
    
    '''
        Player 13: Gorn
    '''
    # 0x0E
    strP13 = int(input("Set Strength for Gorn: (0-99)\n"))
    memMap[398] = strP13

    # 0x0F
    dexP13 = int(input("Set Dextrity for Gorn: (0-99)\n"))
    memMap[399] = dexP13

    # 0x10
    intP13 = int(input("Set Intelligence for Gorn: (0-99)\n"))
    memMap[400] = intP13

    # 0x11
    magicP13 = int(input("Set Magic for Gorn: (0-99)\n"))
    memMap[401] = magicP13

    # 0x12->13  -> 0x03E7 in Little Endian
    memMap[402] = 231  # 0x37
    memMap[403] = 3

    # 0x14->15  -> 0x03E7 in Little Endian
    memMap[404] = 231
    memMap[405] = 3

    # 0x16->17  -> 0x270F in Little Endian
    memMap[406] = 15
    memMap[407] = 39

    # 0x18
    # lvlP13 = input(int("Set Level for Gorn: (0-99)\n"))
    #memMap[408] = 99
    
    
    
    
    '''
        Player 14: Maxwell
    '''
    # 0x0E
    strP14 = int(input("Set Strength for Maxwell: (0-99)\n"))
    memMap[430] = strP14

    # 0x0F
    dexP14 = int(input("Set Dextrity for Maxwell: (0-99)\n"))
    memMap[431] = dexP14

    # 0x10
    intP14 = int(input("Set Intelligence for Maxwell: (0-99)\n"))
    memMap[432] = intP14

    # 0x11
    magicP14 = int(input("Set Magic for Maxwell: (0-99)\n"))
    memMap[433] = magicP14

    # 0x12->13  -> 0x03E7 in Little Endian
    memMap[434] = 231  # 0x37
    memMap[435] = 3

    # 0x14->15  -> 0x03E7 in Little Endian
    memMap[436] = 231
    memMap[437] = 3

    # 0x16->17  -> 0x270F in Little Endian
    memMap[438] = 15
    memMap[439] = 39

    # 0x18
    # lvlP14 = input(int("Set Level for Maxwell: (0-99)\n"))
    #memMap[440] = 99





    '''
        Player 15: Toshi
    '''
    # 0x0E
    strP15 = int(input("Set Strength for Toshi: (0-99)\n"))
    memMap[462] = strP15

    # 0x0F
    dexP15 = int(input("Set Dextrity for Toshi: (0-99)\n"))
    memMap[363] = dexP15

    # 0x10
    intP15 = int(input("Set Intelligence for Toshi: (0-99)\n"))
    memMap[464] = intP15

    # 0x11
    magicP15 = int(input("Set Magic for Toshi: (0-99)\n"))
    memMap[465] = magicP15

    # 0x12->13  -> 0x03E7 in Little Endian
    memMap[466] = 231  # 0x37
    memMap[467] = 3

    # 0x14->15  -> 0x03E7 in Little Endian
    memMap[468] = 231
    memMap[469] = 3

    # 0x16->17  -> 0x270F in Little Endian
    memMap[470] = 15
    memMap[471] = 39

    # 0x18
    # lvlP15 = input(int("Set Level for Toshi: (0-99)\n"))
    #memMap[472] = 99




    '''
        Player 16: Saduj
    '''
    # 0x0E
    strP16 = int(input("Set Strength for Saduj: (0-99)\n"))
    memMap[494] = strP16

    # 0x0F
    dexP16 = int(input("Set Dextrity for Saduj: (0-99)\n"))
    memMap[495] = dexP16

    # 0x10
    intP16 = int(input("Set Intelligence for Saduj: (0-99)\n"))
    memMap[496] = intP16

    # 0x11
    magicP16 = int(input("Set Magic for Saduj: (0-99)\n"))
    memMap[497] = magicP16

    # 0x12->13  -> 0x03E7 in Little Endian
    memMap[498] = 231  # 0x37
    memMap[499] = 3

    # 0x14->15  -> 0x03E7 in Little Endian
    memMap[500] = 231
    memMap[501] = 3

    # 0x16->17  -> 0x270F in Little Endian
    memMap[502] = 15
    memMap[503] = 39

    # 0x18
    # lvlP16 = input(int("Set Level for Saduj: (0-99)\n"))
    #memMap[504] = 99

    print("16 bit values can't be set and are preset to their MAX value")
    print("You file has been Modded!\nNow Drag the SAVED.GAM file back into ULTIMA 5 directory!\nEnjoy your game!")

    memMap.flush()
    memMap.close()
    byteReader.close()


