def main():
    try:
        from collections import OrderedDict
    except ImportError:
        OrderedDict = dict
    global am
    am = chr(254)
    global vm
    vm = chr(253)
    global svm
    svm = chr(252)
    fname = "empmstr"
    fid = "000001"
    displayrec(fname, fid, getrec(fname, fid))
    print "     H A N D L I N G  A R R A Y S"
    print "HERE ARE THE AVAILABLE MENU OPTIONS :"
    option = ""
    dispatch = {'i':[" (I)nsert an attribute, value or sub-value", datains],
                'r':[" (R)eplace an attribute, value or sub-value", datarep],
                'd':[" (D)elete an attribute, value or sub-value", datadel],
                'l':[" (L)ocate an attribute, value or sub-value", dataloc],
                'c':[" (C)lear record", dataclear],
                'x':["e(X)it PROGRAM",""]}
    keys = dispatch.keys()
    for key in keys:
        action = dispatch[key]
        print action[0] 
    while option != "x":
        option = raw_input('ENTER OPTION: ').lower()
        if option != "x":
            if option in keys:
                action[1](option)
            else:
                print "Invalid option entered."
        else:
            print "end of program"

def datains(option):
    print "option entered = " + option
    return

def datarep(option):
    print "option entered = " + option
    return

def datadel(option):
    print "option entered = " + option
    return

def dataloc(option):
    print "option entered = " + option
    return

def dataclear(option):
    print "option entered = " + option
    return

def getrec(fname,fid):
    record = "111-22-3333þJohnsonþLeonardþCharlesþErin E. TullosýAndrew L. JohnsonýRuth D. Irvinþ13322 Hampton Bend Ln.ýþHoustonþTXþ770703483"
    return record


def displayrec(fname, fid, record):
    print 'Here is the data in file "' + fname + '" for Item ID "' + str(fid) + '":'
    thisrecord = record.split(am)
    attrs = len(thisrecord)
    for attr in range(0, attrs):
        thisattr = thisrecord[attr]
        if thisattr.count(vm) == 0:
            print "attr " + str(attr) + ": " + thisattr
        else:
            thisattr = thisattr.split(vm)
            vals = len(thisattr)
            for val in range(0, vals):
                if thisattr.count(svm) == 0:
                    print "attr " + str(attr) + "." + str(val) + ": " + thisattr[val]
                else:
                    thisval = thisattr.split(svm)
                    subvals = len(thisval)
                    for subval in range(0, subvals):
                         print "attr " + str(attr) + "." + str(val) +  "." + str(subval) + ": " + thisval[subval]

if __name__ == '__main__':
    main()
    








"""
attribute marks (^),
value marks (]),
and occasionally, subvalue marks (\) 
"""





"""
Item-id: SS_NO
001 A
002 1
003 SS #
004
005
006
007
008 T3,80
009 T
010 30

Item id: DATE
001 A
002 3
003 DATE
004
005
006
007 D2/
008 T3,8]DI (The "]" character is a value mark.
009 R
010 8

Item-id: AUTHOR
001 A
002 4
003 AUTHOR
004
005
006
007
008 T3,3
009 L
010 3
"""