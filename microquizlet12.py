import re
import os
import time
fastboot = 'yes'
autocls='yes'
revquiz='yes'
autohelp='yes'
save = 'yes'
kw = []
file_name = ''
def check_progress_file(fw):
    global kw
    if len(fw)==len(kw):
        print('Save file ok')
        time.sleep(1)
    else:
        print('Save file damaged')
        kw = []
        for i in range(len(fw)):
            kw.append(0) # wake table know work, intiger in table remember your progresion in work
        time.sleep(1)
        save_progress()
def save_progress():
    global file_name
    print('saving...')
    save_file_name = file_name + '.progress'
    with open(save_file_name,'w+',encoding='utf-8') as save_progres_to_file:
        for i in range(len(kw)):
            tekst = '.'+str(kw[i])+"\n"
            save_progres_to_file.write(tekst)
def typequiz(word, definition, intiger): # quizlet enginne
    global kw
    n = 0
    while n<=1:
        print(word)
        x = input('>') #word input
        if x =='#exit': # exit from microquizlet
            quit()
        elif x =='#cls':
            os.system('cls') #clean the terminal
            continue
        elif x==definition: # good answer
            kw[intiger] = kw[intiger] + 1
            n = 10
        elif x=='#reboot':
            print('Reboot system')
            main()
        elif x=='#save':
            save_progress()
            continue
        else:
            while True:
                print("Mistake") # if mistake
                print(definition)
                x = input('>')
                if x =='#exit':# exit from microquizlet
                    quit()
                elif x =='#cls': #clean the terminal
                    os.system('cls')
                    continue
                elif x==definition: #good answer after mistake
                    kw[intiger] = kw[intiger] - 2
                    if kw[intiger]<=-3:
                        kw[intiger] = -2
                    n = 10
                    break
                elif x=='#ok': #if you think you know that word you can use it to get a poit and continue
                    kw[intiger] = kw[intiger] + 1
                    n = 10
                    break
                elif x=='#reboot':
                    print('Reboot system')
                    main()
                elif x=='#save':
                    save_progress()
                    continue
                else:
                    continue #loop



def mqconfig(): #def making config file
  global fastboot
  global autocls
  global revquiz
  global autohelp
  global save
  print('Making config file')
  print('Write yes/no')
  while True:
    autocls = input('Auto CLS ')
    if autocls =='yes' or autocls =='no':
        break
    else:
        print('Mistake')
        continue
  while True:
    revquiz = input('Reverse Quiz ')
    if revquiz =='yes' or revquiz =='no':
        break
    else:
        print('Mistake')
        continue
  while True:
    fastboot = input('Fast Boot ')
    if fastboot =='yes' or fastboot =='no':
        break
    else:
        print('Mistake')
        continue
  while True:
    autohelp = input('Auto Help ')
    if autohelp =='yes' or autohelp =='no':
        break
    else:
        print('Mistake')
        continue
  while True:
      save = input('Save progres ')
      if save =='yes' or save =='no':
          break
      else:
          print('Mistake')
          continue
  with open('mq.config','w+',encoding='utf-8') as config:
      text = 'Auto CLS '+autocls+'\n'+'Reverse Quiz '+revquiz+'\n'+'Fast Boot '+fastboot+'\n'+'Auto Help '+autohelp+'\n'+'Save progres '+save+'\n'
      config.write(text)

def up_load(con): #def reading config file
    global fastboot
    global autocls
    global revquiz
    global autohelp
    global save
    pattern = 'Auto CLS (.+)\n'
    autoclsx = re.findall(pattern,con,flags=re.MULTILINE)
    autocls = autoclsx[0]
    #print(autocls)

    if autocls =='yes' or autocls =='no': #first option
        print('ok')
    else:
        print('Config file demaged')
        mqconfig()
    pattern = 'Reverse Quiz (.+)\n'
    revquizx = re.findall(pattern,con,flags=re.MULTILINE)
    revquiz = revquizx[0]

    if revquiz =='yes' or revquiz =='no': #second option
        print('ok')
    else:
        print('Config file demaged')
        mqconfig()
    pattern = 'Fast Boot (.+)\n'
    fastbootx = re.findall(pattern,con,flags=re.MULTILINE)
    fastboot = fastbootx[0]

    if fastboot =='yes' or fastboot =='no': #third option
        print('ok')
    else:
        print('Config file demaged')
        mqconfig()
    pattern = 'Auto Help (.+)\n'
    autohelpx = re.findall(pattern,con,flags=re.MULTILINE)
    autohelp = autohelpx[0]

    if autohelp =='yes' or autohelp =='no': #fourth option
        print('ok')
    else:
        print('Config file demaged')
        mqconfig()
    pattern = 'Save progres (.+)\n'
    savex = re.findall(pattern,con,flags=re.MULTILINE)
    save = savex[0]
    if save =='yes' or save =='no': #third option
        print('ok')
        #print(save)
    else:
        print('Config file demaged')
        mqconfig()
def mqhelp():
    print('#help   - help in program')
    print('#cls    - clear the cmd')
    print('#exit   - exit from program')
    print('#config - Settings meneger')
    print('#reboot - reopen micro quizlet')
    print('#save - save the progress')
    print('#ok - it will make from the mistake a correct answer')
    wait=input('Press Enter')

def main(): # main definition
    global fastboot
    global autocls
    global revquiz
    global autohelp
    global file_name
    global kw
    kw=[]
    fw=[]
    dw=[]
    print('Micro Quizlet 1.2 Non Pubic Developer Beta') # Micro Hello

    time.sleep(1)
    print('Starting system')
    try:
        with open('mq.config','r',encoding='utf-8') as config:
            print('Uploat config')
            con = config.read()
            up_load(con)

    except:
        print("No config file")
        mqconfig()

    if fastboot=='no':
        time.sleep(2)

    if autohelp=='yes':
        mqhelp()
    os.system('cls')
    #cli = 'quiz.txt'
    while True:
        cli = input('Enter name of file ') # type file name
        if cli=='#exit':
            quit()
        elif cli=='#help':
            mqhelp()
            continue
        elif cli=="#config":
            mqconfig()
            continue
        elif cli=='#cls' or cli=='#clear':
            os.system('cls')
            continue
        else:
            try:
                with open(cli,'r',encoding='utf-8') as f: # open quizlet file to read only with encoding as utf-8
                    data = f.read()
                    file_name = cli
                break
            except:
                print('No file ',cli)
                continue
    pattern = '(.+),'
    dw = re.findall(pattern, data,flags=re.MULTILINE) # write to table definition word
    pattern = ',(.+)\n'
    fw = re.findall(pattern, data,flags=re.MULTILINE) # write to table forein word
    #global kw
    #fw = ['jabłko','gruszka','styczeń'] # test table
    #dw = ['apple','pearl','January']
    if save=='yes':
        try:
            a = file_name+'.progress'
            with open(a,'r',encoding='utf-8') as h: #upload progress file
                progres_data = h.read()
                pattern = '.(.+)\n'
                nkw=re.findall(pattern, progres_data,flags=re.MULTILINE)
                for i in range(len(nkw)):
                    kw.append(int(nkw[i]))
        except:
            print('Can not load progress file')
            if fastboot=='no':
                time.sleep(2)
            for i in range(len(fw)):
                kw.append(0) # wake table know work, intiger in table remember your progresion in work
    else:
        for i in range(len(fw)):
            kw.append(0)
    #print(fw)
    #fw = ['jabłko','gruszka','styczeń'] # test table
    #dw = ['apple','pearl','January']
    #kw = [0,0,0]
    if save=='yes':
        check_progress_file(fw) #check progres file
    n = 0
    while True:
        n+=1
        if n>=10: # safety pin break the loop when work is finished
            break
        for i in range(len(fw)): # main work loop
            if kw[i]>=3:
                continue # continue when you know that word
            else: 
                n == 0
                if kw[i]%2 == 0 or revquiz=='no': # noramal quizlet
                    if autocls =='yes':
                        os.system('cls') #clear cmd
                    typequiz(fw[i],dw[i],i)
                else: # rewerse quizlet
                    if autocls=='yes':
                        os.system('cls') #clear cmd
                    typequiz(dw[i],fw[i],i)


    print('You did it!')
    main()
main()
