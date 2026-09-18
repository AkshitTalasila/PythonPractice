


def unique_list(dupeList):

        newList =[]

        for i in dupeList:
            if(i not in newList):
                 newList.append(i)

        return newList      

print(unique_list([5,5,5,5]))