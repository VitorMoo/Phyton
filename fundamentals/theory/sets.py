# set is a collection wich is unordered,unidexed and dont allows duplicate values

utensils={"fork","spoon","knife"}
dishes={"plate","cup","bowl","knife"}

#utensils.add("napkin")
#utensils.remove("fork")
#utensils.clear

for i in utensils:
    print(i)

#utensils.update(dishes)
#print(utensils)

#dinner_table=utensils.union(dishes)
#print(dinner_table)

print(utensils.intersection(dishes))
print(utensils.difference(dishes))