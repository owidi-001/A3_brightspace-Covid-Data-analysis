import csv
import sys
from typing import Counter

# add your name and id
# --------------------

# add all other functions here

# list helper


# Display 2d list
def display_2Dlist(list_param):
    if len(list_param)==0:
        return "No data in list"
    else:
        items='\n'.join(map(str, list_param))
        return items
        
            

# Display dict
def display_dict(dict_param):
    if len(dict_param)==0:
        return "Dictionary is empty"
    else:
        items='\n'.join(map(str, [f'{key}:{value}' for (key, value) in sorted(dict_param.items())]))
        return items


# Return list
def return_list(filename):
    file_items=[]
    database=open(filename,'r')
    database=csv.reader(database)

    database_items=[x for x in database][1:]

    for data in database_items:
        data[1]=data[1].replace('s','')
        file_items.append(data)
    return file_items


# Return dict
def return_dict(filename):
    file_items={}
    database=open(filename,'r')
    database=csv.reader(database)

    database_items=[x for x in database][1:]

    for data in database_items:
        key=data[3]
        data.pop(3)
        file_items[key]=data

    return file_items

#
#  get total cases
def get_total_cases(database,x):
    instances={}
    for row in database:
        if x==0:
            instance=row[0]
            if instance not in instances:
                instances[instance]=0
            else:
                instances[instance]+=1
        elif x==1:
            instance=row[1]
            if instance not in instances:
                instances[instance]=0
            else:
                instances[instance]+=1
        elif x==2:
            instance=row[2]
            if instance not in instances:
                instances[instance]=0
            else:
                instances[instance]+=1

    total_cases=sum([x for x in instances.values()])

    return (display_dict(instances),total_cases)


# display_PHU_summary
def display_PHU_summary(database,dictionary,PHU_ID):
    summary={}
    ids=[x[3] for x in [row for row in database]]
    
    if PHU_ID not in ids:
        return "PHU_ID invalid",exit()
    else:
        summary['PHU id']=PHU_ID
        summary['PHU name']=dictionary[PHU_ID][0]
        summary['PHU city']=f'{dictionary[PHU_ID][1]},{dictionary[PHU_ID][2]}'
        summary['PHU website']=dictionary[PHU_ID][3]
        x,total_cases=get_total_cases(database,0)
        summary['Total cases']=total_cases

    return display_dict(summary)


def get_cases_by_PHU_and_age(database,dictionary):
    cases={}
    ids=[x[3] for x in [row for row in database]]
    for id in ids:
        groups_cases=[]
        for row in database:
            if id==row[3]:
                x,total_cases=get_total_cases(database,1)
                groups_cases.append([row[1],total_cases])
        cases[id]=groups_cases

    return display_dict(cases)


def get_topx_hotspots(database,dictionary,x):
    hotspots={}
    cases={}
    ids=[x[3] for x in [row for row in database]]
    for id in ids:
        groups_cases=[]
        for row in database:
            if id==row[3]:
                x,total_cases=get_total_cases(database,1)
                groups_cases.append([row[1],total_cases])
        cases[id]=groups_cases

    for x in cases:
        name=dictionary[x][0]
        hotspots[x]=[name,f'Total cases{sum([case[1] for case in x])}']

    return display_dict(hotspots)


# --------------------
# the main function, call all other functions inside of this function 
def main():
    # # test list
    # alist = [[1,2],[3,4],[5],[6,7]]
    # print(display_2Dlist(alist))

    # # test dict 
    # adict = {2:6, 7:1, 4:3, 5:'zero'}
    # print(display_dict(adict))

    # # Test return_list
    # database = return_list('data10.csv')
    # print(display_2Dlist(database))

    # Test dict
    # dict = return_dict('data10.csv')
    # print(display_dict(dict))

    # total cases
    # result, total_cases = get_total_cases(database, 0)
    # display_dict(result)

    # display_PHU_summary(database, dict, 2241)

    # result = get_cases_by_PHU_and_age(database, dict)
    # display_dict(result)

    pass



# the main guard, calls the main() function only if you run this program as a stand-alone program
if __name__ == "__main__":
    main()