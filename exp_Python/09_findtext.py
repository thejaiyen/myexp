def textfind(text,find):
    print ("-"*20) 
    print ("text is \"{}\"".format(text))

    contition1 = text.startswith(find)
    print ("startswith {} is \"{}\"".format(find,contition1))
    
    contition2 = find in text
    print ('{} in text is \"{}\"'.format(find,contition2))


textfind ("hi mark","hi")
textfind (" hi mark","hi")
textfind ("sdas hi","hi")