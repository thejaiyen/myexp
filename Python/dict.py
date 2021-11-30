thisdict = {}
# OR
thisdict = dict()


# ------------------------------------------------------------------
#  Add to dict
#  way 1
thisdict = {
    "node1" : {
        "sys" : "hi"
    }
}

#  way2
thisdict["node2"]={"sys":"yoo"}

#  way3
thisdict.update({"node3":{"sys":"aloha"}})


print(thisdict)

print (thisdict["node2"]["sys"])
