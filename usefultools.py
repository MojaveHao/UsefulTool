from PIL import Image,ImageDraw,ImageFont,ImageSequence
import matplotlib.pyplot as plt
import json
import turtle as t
import webbrowser, os
import platform
import jieba
import jieba.analyse
import jieba.finalseg
import jieba.lac_small
import jieba.posseg
import wordcloud
import os,webbrowser
def old_and_useless_funcs():
    def IDNumber_Tool(idnum):
        lone = len(idnum)
        while len(idnum) != 18:
            return "位数不对"
            #1234567891  2  3  4  5  6   7   8   9  1
            #0123456789[10][11][12][13][14][15][16][17]
        else:
            if int(idnum[16]) % 2 == 0:
                xb = "女"
            else:
                xb = "男"
            year = int(idnum[6:10])
            month = int(idnum[10:12])
            day = int(idnum[12:14])
            return str(xb,"year:",year,"month:",month,"day:",day)
    def hundred_people_name():
        t.speed(0)
        t.ht()
        lista = ['李', '王', '张', '刘', '陈', '杨', '赵', '黄', '周', '吴', '徐', '孙', '胡',
        '朱', '高', '林', '何', '郭', '马', '罗', '梁', '宋', '郑', '谢', '韩', '唐', '冯', '于'
        , '董', '萧', '程', '曹', '袁', '邓', '许', '傅', '沈', '曾', '彭', '吕','苏', '卢', '蒋', '蔡', 
        '贾', '丁', '魏', '薛', '叶', '阎', '余', '潘', '杜', '戴', '夏', '钟', '汪', '田', '任', '姜', '范', '方',
        '石', '姚', '谭', '廖', '邹', '熊', '金', '陆','郝', '孔', '白', '崔', '康', '毛', '邱', '秦', '江', '史', '顾', 
        '侯', '邵', '孟', '龙', '万', '段', '漕', '钱', '汤', '尹', '黎', '易', '常', '武', '乔', '贺', '赖', '龚', '文']
        def draw(info):
            index = 0
            for k in range(10):
                for j in range(10):
                    x = -250 + j * 50
                    y = 250 - 50*k
                    tgt(x, y)
                    for i in range(4):
                        t.fd(50)
                        t.rt(90)
                    tgt(x + 25, -25-15+y)
                    t.write(lista[index], align="center", font=("华文新魏", 20, "normal"))
                    index += 1
            tgt(0,-300)
            t.write(info, align="center", font=("华文新魏", 25, "normal"))
        draw()
    def bqbzz(openimg, size=30, rotate=0, color=(0, 0, 0), ttf=None, text="Your Text"):
        img = Image.open(openimg)
        nimg = Image.new("RGBA",(1000,1000))
        draw = ImageDraw.Draw(nimg)
        if ttf is not None:
            font = ImageFont.truetype(ttf,size)
        draw.text((10, 10), text, font=font, fill=color)
        nimg = nimg.rotate(rotate, expand=True)
        img.paste(nimg,(0,0),nimg)
        plt.imshow(img)
        #plt.show()
    def log(logs: str, mode:str="System", rtn:bool=False,show_printer:bool=False):
        all_logs_sys = []
        all_logs_debug = []
        all_logs_usr = []
        all_logs = []
        if mode == "System":
            all_logs_sys.append(f"System:{logs}")
            if show_printer == True:
                print("System",logs)
            else:
                print(logs)
        elif mode == "Debug":
            all_logs_debug.append(f"Debug:{logs}")
            if show_printer == True:
                print("Debug",logs)
            else:
                print(logs)
        elif mode == "User":
            all_logs_usr.append(f"User:{logs}")
            if show_printer == True:
                print("System",logs)
            else:
                print(logs)
        else:
            all_logs.append(f"{mode}:{logs}")
        all_logs.append([{"User":all_logs_usr}])
        all_logs.append([{"System": all_logs_sys}])
        all_logs.append([{"Debug": all_logs_debug}])
        if rtn == True:
            print(all_logs)
    def get_os_type():
        return platform.uname()[0]
    def finder(lst,wtg,dev=False):#ver1.1.5:append "dev mode" for developers
        n = 0
        found_list = []
        l = len(lst)
        il = int(len(wtg))
        # Warning:There is a problem with this line of code. Please submit a pull request on GitHub(for i in range(0,l,step=il),and this problem is still not slove in version1.1.3 :
        for i in range(0, l, step=il):
            n += 1
            if wtg == lst[i]:
                found_list += lst[i]
        if n != 0 and dev == False:
            if n == 1:
                return str("查询了", n, "次找到了", "是第", i+1, "个")
            elif n >= 2:
                return str("查询到了",n,"个,分别在第",found_list.index(n) + 1,"个")
            else:
                return "没找到"
        if n != 0 and dev == True:
            if n == 1:
                return (n,i+1)
            elif n >= 2:
                return (n, found_list)
            else:
                return None
def fileio():
    def json_rw(filename,mode='r',enc='utf-8',wrt=""):
            with open(filename,mode,encoding=enc) as f:
                if mode == 'r':
                    conect = json.load(f)
                    return conect
                elif mode == 'w':
                    json.write(wrt)
    def ospen(file_name:str):
        webbrowser.open("file://"+os.path.realpath(file_name))
def turtle_processing():
    def tgt(x=0,y=0):
        t.up()
        t.goto(x,y)
        t.pd()
    def init_turtle(x=0,y=0,c=0):
        t.setheading(0)
        tgt(x,y)
        t.pencolor(c)
        t.fillcolor(c)
        t.setheading(0)
    def os_star(x,y,l,c):
        if platform.uname()[0] == "Windows":
            init_turtle(x,y,c)
            t.begin_fill()
            for i in range(5):
                t.fd(l)
                t.right(144)
            t.end_fill()
        else:
            init_turtle(x,y,c)
            t.begin_fill()
            for i in range(4):
                t.fd(l)
                t.lt(72)
                t.fd(l)
                t.rt(144)
            t.end_fill()
def gif_processing():
    def summon_gif(gif_dir,sort_reverse=False,ext_file=[".png",".jpg",".jpeg",".bmp"],output_name="Deflut.gif",txt="",ttf="STXINGKA.TTF",text_xy=(80,600),size=80,ttf_color=(0,0,0),use_own_color_list=False,own_color_list=[(0,0,0)]):
    #             帧文件路径           反序              允许的扩展名                             输出名         要写入的文字   使用的字体    写入字体的位置     字体大小     字体颜色       使用多组颜色列表            多组颜色列表
        fir = gif_dir#使用fir代替gif_dir
        files = sorted(os.listdir(fir), reverse=sort_reverse)
        frames = []#设置文件列表
        font = ImageFont.truetype(ttf,size)#设置字体
        if use_own_color_list == False:#默认主程序
            for file in files:#遍历文件列表
                name, ext = os.path.splitext(file)#获取文件扩展名
                if ext in ext_file:#如果是图片
                    img = Image.open("{}{}{}".format(fir,os.sep,file))#打开fir文件夹下的file图片
                    print("utop:当前在打开",fir,"下的",file,"文件")
                    draw = ImageDraw.Draw(img)
                    frames.append(draw)
                    print("添加了1张图片到frames")
        else:
            index = len(own_color_list)
            for i in range(len(files)):
                name, ext = os.path.splitext(gif_dir)
                if ext in ext_file:
                    img = Image.open("{}{}{}".format(fir, os.sep, gif_dir))
                    draw = ImageDraw.Draw(img)
                    if txt is not "":
                        draw.text(text_xy,txt,own_color_list[index%i],font=font)
                    frames.append(img)
        print(len(frames))
        frames[0].save(output_name, append_images=frames[1:], save_all=True)
        #webbrowser.open("file://"+os.path.realpath(output_name))
    def gif_boom(myDir="renders",open_gif="image.gif"):
        img = Image.open(open_gif)
        if not os.path.exists(myDir):
            os.mkdir(myDir)
        frames = ImageSequence.Iterator(img)
        i = 0
        for frame in frames:
            frame.save("{}{}render_{}.png".format(myDir, os.sep, i))
            i += 1
'''1.1.0 append things:init_turtle,os_star'''
'''1.1.1 append things:log'''
'''1.1.2  append things:ospen'''
'''1.1.3  append things:get_os_type'''