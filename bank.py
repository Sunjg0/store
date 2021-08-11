import random

print("====================================")
print("|-------中国工商银行账户管理系统-------|")
print("|-------1、开户              -------|")
print("|-------2、存钱              -------|")
print("|-------3、取钱              -------|")
print("|-------4、转账              -------|")
print("|-------5、查询              -------|")
print("|-------6、退出              -------|")
print("====================================")
bank={}
def bank_adduser(account,username,password,country,province,street,door):
    if len(bank) > 100:
        # 超出了银行上限
        return 3
    if username in bank :
        #如果名字  在    bank  执行下面的代码
        return 2
    bank[username]={
        "account":"account",
        #键一个名字       ：值来自传入的参数:account
        "password":"password",
        "country":"country",
        "province":"province",
        "street":"street",
        "door":"door",
        "money":0,
        "brnk_name":bank_name # 直接调用全局参数
    }
    return 1
def py_gmon(x,y,z):
    if len(x) == 8:
        return 0
    elif len(x) > 8 and len(y) > 4:
        return 1
    elif len(y) == 4:
        return 2
    elif z > 10000:
        return 3


def money():   #存款
    moneys = 22
    username = input("请输入您的用户名")
    password = input("请输入您的密码")
    money = int(input("请输入您的存款金额"))
    if username in username:
        print(money+moneys)
    else:
        return False

def gomoney():  #取款
    mm = 10000
    id = input('请输入用户账号')
    password = input('请输入用户密码')
    gmon = int(input('取款金额'))
    num = py_gmon(id,password,gmon)
    if num == 0:
        print('感谢本次交易，剩余余额为',mm-gmon)
    elif num == 1:
        print('帐号不存在')
    elif num == 2:
        print('密码不对')
    elif num == 3:
        print('钱不够')

def zmoney():  #转账
    d = 10000
    a = int(input('请输入转账账号'))
    b = int(input('请输入转账密码'))
    f = input('输入z转出，输入y转入')
    if f == 'z':
        c = int(input('请输入转出金额'))
        print('转出金额为',d-c)
    if f == 'y':
        e = int(input('请输入转入金额'))
        print('转出金额为',d+e)


def select(): #查询账户
    username = input('请输入您的账号')
    password = input('请输入您的密码')
    num = 10000
    if username in username :
        print('当前账号',username)
        print('当前密码','******')
        print('余额',num)
        print('持卡人现居住地址')
        print('开户行',bank_name)


bank_name= "中国工商银行七马路支行"#写死的银行地址
def useradd():
    username=input("请输入您的用户名")
    password=input("请输入您的密码")
    print("请输入您的详细信息")
    country=input("请输入您国家")
    province = input("请输入您省份")
    street = input("请输入您街道")
    door=input("请输入您的门牌号")
    account=random.randint(00000000,99999999) #随机生成8位账号
    status=bank_adduser(account,username,password,country,province,street,door)
    if status == 3:
        print("对不起，改银行的用户已满，请到其他银行办理")
    if status == 2:
        print("对不起，改用户已经开户，不要重复")
    if status == 1:
        print("恭喜你正常开户，以下是您的信息")
        info ='''
          ------------个人信息------------
            用户名:%s
            账号：%s
            密码：*****
            国籍：%s
            省份：%s
            街道：%s
            门牌号：%s
            余额：%s
            开户行名称：%s
        '''
        print(info % (username, account, country, province, street, door, bank[username]["money"], bank_name))


while True:
    num=input("请输入您要办的业务：")
    if num  == "1":
        useradd()
    elif num == "2":
        money()
    elif num == "3":
        gomoney()
    elif num == "4":
        zmoney()
    elif num == "5":
        select()
    elif num == "6":
        print("再见")
        break
    else:
        print("请按照提示输入正确指令")
        break

