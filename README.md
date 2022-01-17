# UsefulTool User's Guide
## defines:
### bqbzz(openimg,size=30,rotate=0,color=(0,0,0),ttf=None,text="Your Text"):

      - Can:Write something on a photo
      - oepnimg:OpenIMG(PNG,GIF,JPG,JPEG,BMP)
      - size:font size
      - rotate:font rotate
      - color:font color
      - ttf:Using TTF font
      - text:What do you want to write?
### json_rw(filename,mode='r'):
      - Can:load a json file
      - filename:Oepn file
      - mode:How to open the file(r,w,r+,w+,rb,wb,ab,rb+,wb+,ab+)
### finder(lst):
      - Can:Find a number in a list
      - lst:find a number in what?
### IDNumber_Tool(idnum):
        - Can:Find info in your IDnumber in China(like:Your Gender,when you was born)
        - idnum:Your IDnumber in China
### tgt(x=0,y=0):
        -  Let turtle move to(x,y)
### hundred_people_name():
      - Can:
        - Press your First Name into it
        - Print a list
### summon_gif(gif_dir,sort_reverse=False,ext_file=[".png",".jpg",".jpeg",".bmp"],output_name="Deflut.gif",txt="",ttf="STXINGKA.TTF",text_xy=(80,600),size=80,ttf_color=(0,0,0),use_own_color_list=False,own_color_list=[(0,0,0)]):
        -Can:Summon a gif by pictures
        -  gif_dir:Where are your imgs to summon a gif?
        -  sort_reverse:Do you want to invert your gif?If you want,set this True.
        - ext_file:allowed file exts
        - output_name:Your gif's name
        - txt,ttf,size,ttf_color:Please look at [bqbzz]
        - use_own_color_list:If this porgram is using Multi-group-color-list,please set it True.
        -o wn_color_list: Multi-group-color-list
### gif_boom(myDir="renders",open_gif="image.gif")

      -Can:make a gif become pngs
      - myDir:Images will save at here.
      - open_gif:Which gif do you want to boom?
### init_turtle(x,y,c)
      -Can:init your turtle
      - x,y:go to (x,y)
      - c:set pen_color and fill_color c
### os_star(x,y,l,c)
      - Can:Draw a five pointed star at (x,y)
      - long:l
      - color:c
      - Angle adjustment is not supported temporarily
### log(logs: str, mode:str="System", rtn:bool=False,show_printer:bool=False)
      -Can:Print a log
      - logs:Log you want to print
      - mode:Set the name of the log sender. The options are:
          1. System
          2. Debug
          3. User
          4. Your optional name
      - rtn:Return all of the logs
      - show_printer:Select whether to display the sender name (defined in mode)
### ospen(file_name:str)
      -Can:Open a file in the current directory by default
      -file_name:Your file's name
