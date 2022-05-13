# UsefulTool User's Guide
## 安装前准备
1.准备好Python3.7+环境,确保pip已经安装/添加到Path

2.最好准备以下库：

	* pillow

	* matplotlib

	* jieba

	* wordcloud

3.输入命令进行安装:

	* [Widnows][Powershell/cmd]pip install usefultools --upgrade

	* [Linux][Bash]sudo pip install usefultools --upgrade

## 定义/defines:

### 表情包制作/bqbzz(openimg,size=30,rotate=0,color=(0,0,0),ttf=None,text="Your Text")

      - Can:Write something on a photo
      - oepnimg:OpenIMG(PNG,GIF,JPG,JPEG,BMP)
      - size:font size
      - rotate:font rotate
      - color:font color
      - ttf:Using TTF font
      - text:What do you want to write?
### 简单的json读写/json_rw(filename,mode='r'):

      - Can:load a json file
      - filename:Open file
      - mode:How to open the file(r,w,r+,w+,rb,wb,ab,rb+,wb+,ab+)
### [Waste]寻找者/finder(lst):

      - Can:Find a number in a list
      - lst:find a number in what?
### 身份证工具/IDNumber_Tool(idnum):

        - Can:Find info in your IDnumber in China(like:Your Gender,when you was born)
        - idnum:Your IDnumber in China
### 移动海龟/tgt(x=0,y=0):

        -  Let turtle move to(x,y)
### [Waste]百家姓/hundred_people_name():

      - Can:
        - Press your First Name into it
        - Print a list
### 动图生成/summon_gif(gif_dir,sort_reverse=False,ext_file=[".png",".jpg",".jpeg",".bmp"],output_name="Deflut.gif",etc.):

        -Can:Summon a gif by pictures
        - gif_dir:Where are your imgs to summon a gif?
        - sort_reverse:Do you want to invert your gif?If you want,set this True.
        - ext_file:allowed file exts
        - output_name:Your gif's name
        - txt,ttf,size,ttf_color:Please look at [bqbzz]
        - use_own_color_list:If this porgram is using Multi-group-color-list,please set it True.
        -o wn_color_list: Multi-group-color-list
### 动图大爆炸/gif_boom(myDir="renders",open_gif="image.gif")

      -Can:make a gif become pngs
      - myDir:Images will save at here.
      - open_gif:Which gif do you want to boom?
### 初始化海龟init_turtle(x,y,c)

      -Can:init your turtle
      - x,y:go to (x,y)
      - c:set pen_color and fill_color c
### 画星星/os_star(x,y,l,c)

      - Can:Draw a five pointed star at (x,y)
      - long:l
      - color:c
      - Angle adjustment is not supported temporarily
### 日志工具/log(logs: str, mode:str="System", rtn:bool=False,show_printer:bool=False)

      -Can:Print a log
      - logs:Log you want to print
      - mode:Set the name of the log sender. The options are:
          1. System
          2. Debug
          3. User
          4. Your optional name
      - rtn:Return all of the logs
      - show_printer:Select whether to display the sender name (defined in mode)
### 简单读取/ospen(file_name:str)

      -Can:Open a file in the current directory by default
      -file_name:Your file's name
### 获取系统类型/get_os_type()

      -Can:Get your Opering System type(Windows/Mac or Linux)
### 图片转pdf/png_to_pdf(mode: int, lst_of_pngs: list, path: str = ".")

      -Can:Convert png files to pdf files
      -mode:can be 0 or 1
      	0:You must use the "lst_of_pngs" to tell the program names of the png files.
      	1:The program will read all png files in the dir"path"
      -Path:The dir png files saved.Deflut is current directory.
## 更新日志/Update Logs:

    1.2021/10/31 1.1.0 with hotfix 1 
    2.2021/12/20 1.1.1 (Include in Version1.1.2 )
    3.2022/1/17 1.1.2 
    4.2022/1/17 1.1.2 with README.md update
    5.2022/1/21 1.1.3
    6.2022/3/6 1.1.4
    7.2022/3/29 1.1.4 with hotfix 1（1.1.1.4）
