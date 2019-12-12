
# 定义一个学生列表
students = []


def insert():
    """增加学生方法"""
    stuNo = input("请输入学生的学号:")
    stuName = input("请输入学生的姓名:")
    stuSex = input("请输入学生的性别:")
    stuAge = input("请输入学生的年龄:")
    students.append({"id": stuNo, "name": stuName, "sex": stuSex, "age": stuAge})
    print("新增成功！")


def query():
    """查询所有学生信息"""
    print(f"学号：\t姓名：\t性别：\t年龄：")
    for stu in students:
        print(f"{stu.get('id')}\t{stu.get('name')}\t{stu.get('sex')}\t{stu.get('age')}")
    else:
        print(f"\t\t\t共查到{len(students)},条数据")


def delete(args):
    """删除单个学生"""
    for stu in students:
        stNo = stu.get("id")
        if args == stNo:
            flag = input("是否删除该学生？y/n:")
            if 'y' == flag:
                students.remove(stu)
                print("删除成功")
                break
            else:
                print("已取消删除")
                break
    else:
        print("没有您要删除的对象")


def check_one(arg):
    """查询单个的方法"""
    print(f"学号：\t姓名：\t性别：\t年龄：")
    for stu in students:
        if arg == stu.get("id"):
            print(f"{stu.get('id')}\t{stu.get('name')}\t{stu.get('sex')}\t{stu.get('age')}")
            break
    else:
        print("\t\t\t无数据")


def update(arg):
    for stu in students:
        if arg == stu.get("id"):
            stuNo = input(f"请输入修改后的学号（当前学号：{stu.get('id')}）")
            name = input(f"请输入修改后的姓名（当前姓名：{stu.get('name')}）：")
            sex = input(f"请输入修改后的性别（当前性别：{stu.get('sex')}）：")
            age = input(f"请输入修改后的年龄（当前年龄：{stu.get('age')}）：")
            if stuNo != '':
                stu['id'] = stuNo
            if name != '':
                stu['name'] = name
            if sex != '':
                stu['sex'] = sex
            if age != '':
                stu['age'] = age
            print("修改成功")
            print(f"修改后的信息为：{stu.get('id')}\t{stu.get('name')}\t{stu.get('sex')}\t{stu.get('age')}")
            break
    else:
        print("没有您要修改的对象")


if __name__ == '__main__':
    print("**********欢迎来到学生管理系统***********")
    while True:
        print("1、新增学生；2、查询所有学生；3、删除学生；4、查询单个学生；5、修改学生信息；6、退出。")
        select = input("请输入您选择(操作)：")
        if "1" == select:
            print("您选择了（新增学生操作）")
            insert()
        elif "2" == select:
            print("您选择了（查询所有学生操作）")
            query()
        elif "3" == select:
            print("您选择了（删除学生操作）")
            inputId = input("请输入您要删除学生的学号:")
            delete(inputId)
        elif "4" == select:
            print("您选择了（查询单个学生操作）")
            arg = input("请输入您要查询学生的学号：")
            check_one(arg)
        elif "5" == select:
            print("您选择了（修改学生信息操作）")
            arg = input("请输入你要修改学生的学号：")
            update(arg)
        elif "6" == select:
            print("您选择了（退出）")
            print("感谢您的使用....")
            break
        else:
            print("请输入正确的指令！！！")

