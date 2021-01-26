#dictionary = {key:value ,
#             key1: value,
#             key3:value
#              }

schoolDistricts = { "district1" : "High School",
                   "district2" : "Middle School",
                   "district3" : "High School",
                   "FourthDistrict" : "Elementary School"
                   }

print(schoolDistricts)


print(schoolDistricts["district1"])

#add to dictionary

schoolDistricts["district5"] = "test"
print(schoolDistricts)


print(schoolDistricts.keys())

for key in schoolDistricts:
       print(key,schoolDistricts[key])


listofTranslations = ["Hello", "GoodBye",...]

dictionaryOfTranslations = { "Hallo" : "Hello",
                             "Tschuss" : "GoodBye" }
print(dictionaryOfTranslations)
