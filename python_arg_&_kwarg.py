# variable length arguments...

def func(normal,*arg,**kwarg):
    print(f"this is normal arguments {normal}")

    print(f"\nthis is *arguments")
    for element in arg:
        print(element,end=" ")

    print(f"\nthis is **keyWordarguments")
    for key,values in kwarg.items():
        print(f"{key}:{values}")

myList=[10,51,48,69,58,43,44,88,100]

mydict={"sanidhya":21,
        "prem":22,
        "tushar":24,
        "tom":22}

func(55,*myList,**mydict)