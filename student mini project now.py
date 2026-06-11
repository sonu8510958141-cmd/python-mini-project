students=input("enter your any students name")
marks={
    "math":int(input("enter your any marks ")),
    "science":int(input("enter your any marks ")),
    "english":int(input("enter your nay marks ")),
    "hindi":int(input("enter your nay marks "))
}
marks_dict={}
try:
    marks=int(input(f"enter your any marks{marks}:"))
    if marks < 0 or  marks > 100:
        raise ValueError("marks should be between 0 and 100")
    marks_dict[marks]=marks
    # print("enert valid marks ",marks)
    total=sum(marks_dict.values())
    averange=total/len(marks_dict)
    percentage=(total/500)*100
    print("total =",total)
    print("averange marks :",averange)
    print("percentage marks=",percentage)
except ValueError:
    print("invalid data")

    

    