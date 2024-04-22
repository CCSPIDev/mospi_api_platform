def Index_agrs():
    import sys
    index_param=['token','Series','Year','Month','State_code','Group_code' ,'Subgroup_code','Sector','Format']
    arg=str(sys.argv).split(",")
    given_p={}
    temp_name=""
    for i in range(1, len(arg)):
        if len(arg[i].split(":"))==2:
            arg_name,arg_val=arg[i].split(":")
            if (i==1):
                arg_name=(arg[1].split(":")[0][2:])
                arg_val=(arg[1].split(":")[1])
            if (i==len(arg)-1):
                arg_name=arg[i].split(":")[0]
                arg_val=arg[i].split(":")[1][:-2]
            arg_name,arg_val=str(arg_name).strip(),str(arg_val).strip()
            if(arg_name in index_param):
                globals() [f'{arg_name}']=arg_val
                given_p[arg_name]=arg_val
                temp_name=arg_name
            # print(arg[1].split(":")[0][2:])
        else:
            if (i==len(arg)-1):
                arg_val=arg[i][:-2]
                globals() [f'{temp_name}']+=f',{arg_val}'
                given_p[temp_name]+=f',{arg_val}'
            else:
                arg_val=arg[i]
                globals() [f'{temp_name}']+=f',{arg_val}'
                given_p[temp_name]+=f',{arg_val}'
    print(given_p)

def CSV_h(string):
    txt=string.split(",")
    request_string=""
    count=0
    if len(txt)==1:
        return string
    for i in txt:
        if(count==len(txt)-1):
            request_string+=f'{i.strip()}'
            return request_string
        request_string+=f'{i.strip()}%2C'
        count+=1
def datafromtoken(url,token):
    import requests
    data = requests.get( url, headers = { "authorization" : token })
    return data

def GetDataIndex(token,Series= "Current_Series_2012",Year="",Month="", State_code="",Group_code="", Subgroup_code='',Sector="",Format="JSON"):
    try:
        if Year!="":
            Year = "Year=" + str(CSV_h(Year)) +"&"
        if Month!="":
            Month = "Month=" + str(CSV_h(Month))+"&"
        if State_code!="":
             State_code = "State_code=" + str(CSV_h(State_code))+"&"
        if Group_code!="":
            Group_code = "Group_code=" + str(CSV_h(Group_code))+"&"
        if Subgroup_code!="":
            Subgroup_code = "Subgroup_code=" + str(CSV_h(Subgroup_code))+"&"
        if Sector!="":
            Sector = "Sector=" + str(CSV_h(Sector))+"&"
        url=(f'http://10.24.89.9/api/cpi/getCPIIndex?Series={Series}&{Year}{Month}{State_code}{Group_code}{Sector}Format={Format}')
        print(f'URL: {url}\n')
        if (Format=="JSON"):
            print(datafromtoken(url,token).json()["data"])
            return datafromtoken(url,token).json()["data"]
        elif(Format=="CSV"):
            print(datafromtoken(url,token).text)
            return datafromtoken(url,token).text
        else:
            print("Format could not be determined")
    except:
        print("Failed")
Series= "Current_Series_2012"
Year= Month= State_code= Group_code= Subgroup_code=Sector=""
Format="JSON"
token=""
Index_agrs()
GetDataIndex(token,Series,Year,Month, State_code,Group_code, Subgroup_code,Sector,Format)
