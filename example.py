from PIL import Image,ImageDraw,ImageFont,ImageSequence
import matplotlib.pyplot as plt
import json
import turtle as t
import webbrowser, os
import shutil
def bqbzz(openimg,size=30,rotate=0,color=(0,0,0),ttf=None,text="我\n真\n是\n个\n大\n聪\n明"):
    img = Image.open(openimg)
    nimg = Image.new("RGBA",(1000,1000))
    draw = ImageDraw.Draw(nimg)
    if ttf is not None:
        font = ImageFont.truetype(ttf,size)
    draw.text((10, 10), text, font=font, fill=color)
    nimg = nimg.rotate(rotate, expand=True)
    img.paste(nimg,(0,0),nimg)
    plt.imshow(img)
    plt.show()
def json_rw(filename,mode):
    with open(filename, mode) as f:
        conect = json.load(f)
    return conect
def finder(lst):
    for i in range(len(lst)):
        n += 1
        if wtg == lst[i]:
            return str("查询了",n,"次找到了","是第",i+1,"个")
    else:
        return "没找到"
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
def tgt(x=0,y=0):
    t.up()
    t.goto(x,y)
    t.pd()
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
#   生成动图   帧文件路径           反序              允许的扩展名                             输出名         要写入的文字   使用的字体    写入字体的位置     字体大小     字体颜色       使用多组颜色列表            多组颜色列表
def summon_gif(gif_dir,sort_reverse=False,ext_file=[".png",".jpg",".jpeg",".bmp"],output_name="Deflut.gif",txt="",ttf="STXINGKA.TTF",text_xy=(80,600),size=80,ttf_color=(0,0,0),use_own_color_list=False,own_color_list=[(0,0,0)]):
    fir = gif_dir#使用fir代替gif_dir
    files = sorted(os.listdir(fir), reverse=sort_reverse)
    frames = []#设置文件列表
    font = ImageFont.truetype(ttf,size)#设置字体
    if use_own_color_list == False:#默认主程序
        for file in files:#遍历文件列表
            name, ext = os.path.splitext(file)#获取文件扩展名
            if ext in ext_file:#如果是图片
                img = Image.open("{}{}{}".format(fir+os.sep+file))#打开fir文件夹下的file图片
                print("utop:当前在打开",fir,"下的",file,"文件")
                draw = ImageDraw.Draw(img)
                frames.append(draw)
                print("添加了1张图片到frames")
    else:
        index = len(own_color_list)
        for i in range(len(files)):
            name, ext = os.path.splitext(file)
            if ext in ext_list:
                img = Image.open("{}{}{}".format(fir, os.sep, file))
                draw = ImageDraw.Draw(img)
                if txt is not "":
                    draw.text(textxy,txt,own_color_list[index%i],font=font)
                frames.append(img)
    print(len(frames))
    frames[0].save(output_name, append_images=frames[1:], save_all=True)
    webbrowser.open("file://"+os.path.realpath(output_name))
def gif_boom(myDir="renders",open_gif="bcm.gif"):
    img = Image.open(open_gif)
    if not os.path.exists(myDir):
        os.mkdir(myDir)
    frames = ImageSequence.Iterator(img)
    i = 0
    for frame in frames:
        frame.save("{}{}render_{}.png".format(myDir, os.sep, i))
        i += 1
