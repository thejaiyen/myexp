def textfind(text,find):
    print ("-"*20) 
    print ("text is \"{}\"".format(text))
    print ("startswith {} is \"{}\"".format(find,text.startswith(find)))
    print ('{} in text is \"{}\"'.format(find,find in text))


textfind ("hi mark","hi")
textfind (" hi mark","hi")
textfind ("sdas hi","hi")