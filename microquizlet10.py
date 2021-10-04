import re
import os
import time
fastboot = 'yes'
autocls='yes'
revquiz='yes'
autohelp='yes'

def mqconfig(): #def making config file
  global fastboot
  global autocls
  global revquiz
  global autohelp
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
  with open('mq.config','w+',encoding='utf-8') as config:
      text = 'Auto CLS '+autocls+'\n'+'Reverse Quiz '+revquiz+'\n'+'Fast Boot '+fastboot+'\n'+'Auto Help '+autohelp+'\n'
      config.write(text)

def up_load(con): #def reading config file
    global fastboot
    global autocls
    global revquiz
    global autohelp
    pattern = 'Auto CLS (.+)\n'
    autoclsx = re.findall(pattern,con,flags=re.MULTILINE)
    autocls = autoclsx[0]
    print(autocls)

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

def mqhelp():
    print('#help   - help in program')
    print('#cls    - clear the cmd')
    print('#exit   - exit from program')
    print('#config - Settings meneger')
    wait=input('Press Enter')
print('Micro Quizlet 1.0') # Micro Hello

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
            break
        except:
            print('No file ',cli)
            continue
pattern = '(.+),'
dw = re.findall(pattern, data,flags=re.MULTILINE) # write to table definition word
pattern = ',(.+)\n'
fw = re.findall(pattern, data,flags=re.MULTILINE) # write to table forein word
kw = []
for i in range(len(fw)):
    kw.append(0) # wake table know work, intiger in table remember your progresion in work

#print(fw)
#fw = ['jabłko','gruszka','styczeń'] # test table
#dw = ['apple','pearl','January']
#kw = [0,0,0]
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
                print(fw[i])
                x = input('>')
                if x =='#exit':
                    quit()
                #elif x=='#cls': # it does not work
                #    os.system('cls')
                #    i = i - 1
                #    continue
                else:
                    if x == dw[i]:
                        kw[i]+=1
                        continue
                    else:
                        while True:
                            print('Mistake')
                            print(dw[i])
                            x = input('-')
                            if x =='#exit': #exit from mirco quizlet
                                quit()
                            elif x =='#cls':
                                os.system('cls')
                                continue
                            elif x == dw[i]:
                                kw[i]-=2
                                if kw[i]<=-3:
                                    kw[i]=-2
                                break
                            else:
                                continue
            else: # rewerse quizlet
                if autocls=='yes':
                    os.system('cls') #clear cmd
                print(dw[i])
                x = input('>')
                if x =='#exit':
                    quit()
                #elif x=='#cls': # it does not work
                #    os.system('cls')
                #    i = i - 1
                #    continue
                else:
                    if x == fw[i]:
                        kw[i]+=1
                        continue
                    else:
                        while True:
                            print('Mistake')
                            print(fw[i])
                            x = input('-')
                            if x =='#exit': #exit from mirco quizlet
                                quit()
                            elif x=='#cls':
                                os.system('cls')
                                continue
                            elif x == fw[i]:
                                kw[i]-=2
                                if kw[i]<=-3:
                                    kw[i]=-2
                                break
                            else:
                                continue


print('You did it!')
