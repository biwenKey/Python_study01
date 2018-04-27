#enumerate功能是将字符转换成数字
#li = ["电脑","鼠标垫","U盘","游艇"]
#for key,item in enumerate(li):
#    inp_um int(inp)
#    print(key,item)
#
#inp = input("请输入商品:")
#inp_num = int(inp)
#print(li[inp_um])

li = ["电脑","鼠标垫","U盘","游艇"]
for key,item in enumerate(li,1):
#inp_num = int(inp)
    print(key,item)
inp = input("请输入商品:")
inp_num = int(inp)
print(li[inp_num - 1])
4
1



