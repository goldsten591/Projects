import pickle
import os
import sys
class pc:
    def __init__(self,class_='Fighter',race='Human',level=1,player='DM',gold=0):
        self.class_=class_
        self.race=race
        self.level=level
        self.player=player
        self.gold=gold
        self.set_max_hp=1
        self.current_hp=1
        self.ac=10
        print(self.race,self.class_,'created')
    def give_gold(self,num):
        try:
            value=int(num)
            self.gold+=value
        except:
            print ('Not in my house!')
    def spend_gold(self,num):
        try:
            value=int(num)
            print ('You try to spend',value,'gold!')
            if self.gold>=value:
                self.gold-=value
                print("You have",self.gold,"gold remaining!")
            else:
                print ("You's a broke hoe!")
        except:
            print ('Not in my house!')
        
    def __repr__(self):
        output=self.class_+', '+str(self.level)+', '+self.player
        return output
    def set_max_hp(self,num):
        try:
            value=int(num)
            self.set_hp=value
        except:
            print ("Not in my house!")
    def healing(self,num):
        try:
            hp=int(num)
            if hp<=0:
                print ("You dont heal negatively, wiener!")
            elif self.current_hp+hp>self.set_max_hp:
                print ('You heal for',hp)
                self.current_hp=self.set_max_hp
                print ("You have",self.set_max_hp,"health!")
            else:
                self.current_hp+=hp
                print ("You have",self.current_hp,"health!")
                if self.current_hp==69:
                    print('Nice')
        except:
            print ("Not today, nerd!")
            #m='continue'
    def damage(self,num):
        try:
            damage=int(num)
            
            if damage<=0:
                print ("Cannot take less than no damage, nerd!")
                m='continue'
            else:
                print('You take',damage,'damage!')
                self.current_hp-=damage
                print(self.current_hp,'Remaining')
                m=1
                if self.current_hp==69:
                    print('Nice')
                if self.current_hp==0:
                    print ("Your vision fades as you fall unconscious.")
                if self.current_hp<0:
                    print ("YOU HAVE DIED!")
        except:
            print ("Why you do?")
            #m='continue'

def quit():
    sys.exit(1)

def main():
    t=0
    char_dict={}
    def find_spell(spell):
        os.chdir(core_path)
        assets='/Assets'
        path=os.getcwd()
        os.chdir(path+assets)
        lookup=spell+'.txt'
        try:   
            infile=open('spell_direct.txt')
            for line in infile:
                stripped_line=line.strip()
                if spell in stripped_line:
                    (name,type_,lvl,school)=stripped_line.split(',')
                    #print(type_,name,lvl,school,sep='')
            #temp_path=path.strip('/Assets')
            pathway=path+'/spells/'+type_+'/'+lvl+'/'+school
            os.chdir(pathway)
            spell_file=open(lookup,encoding="ISO-8859-1")
            print(spell_file.read())
        except:
            print ('Spell not found. Please check spelling or spell name.')
    def character_creation():
        while True:
            user=input('Name: ')
            class_=input('Class: ')
            race=input('Race: ')
            level=input('Level: ')
            player=input('Player: ')
            gold=input('Gold: ')
            max_hp=input('Max hp: ')
            curr_hp=input('Current hp: ')
            ac=input('ac: ')
            if user=='' or class_=='' or race=='' or level=='' or player=='' or gold=='':
                print("You must input a value. Please adjust accordingly")
                continue
            else:
                try:
                    int_max_hp=int(max_hp)
                    int_curr_hp=int(curr_hp)
                    int_ac=int(ac)
                    int_gold=int(gold)
                    q=len(char_dict)
                    char_dict[q]=user
                    globals()[user]=pc(class_,race,level,player,int_gold)
                    globals()[user].set_max_hp=int_max_hp
                    globals()[user].current_hp=int_curr_hp
                    globals()[user].ac=int_ac
                    print(globals()[user].gold)
                    break
                except:
                    print('Hp/ac values must be positive whole numbers!')
                    continue
    def save():
        os.chdir(core_path)
        path=os.getcwd()
        assets='/Assets'
        os.chdir(path+assets)
        out_pickle=open('pc_dict.pickle','wb')
        for i in range(len(char_dict)):
            query=char_dict[i]+'.pickle'
            pimkle=open(query,'wb')
            char_list=[]
            char_list.append(globals()[char_dict[i]].class_)
            char_list.append(globals()[char_dict[i]].race)
            char_list.append(globals()[char_dict[i]].level)
            char_list.append(globals()[char_dict[i]].player)
            char_list.append(globals()[char_dict[i]].gold)
            char_list.append(globals()[char_dict[i]].set_max_hp)
            char_list.append(globals()[char_dict[i]].current_hp)
            char_list.append(globals()[char_dict[i]].ac)
            pickle.dump(char_list,pimkle)
            pimkle.close()
        pickle.dump(char_dict,out_pickle)
        out_pickle.close()
        print('Save complete!')
    def combat_display():
        print('Name','AC','HP/MAX',sep='\t')
        for i in range(len(char_dict)):
            print(char_dict[i],globals()[char_dict[i]].ac,str(globals()[char_dict[i]].current_hp)+'/'+str(globals()[char_dict[i]].set_max_hp),sep='\t')
    def print_char_dict():
        for i in range(len(char_dict)):
            print(str(i+1)+':',char_dict[i])
    def input_condition(user,length):
        try:
            int_user=int(user)
            int_length=int(length)
            if int_user in range(int_length):
                m=int_user
            else:
                print('Please enter an integer listed above!')
                m='continue'
        except:
            print('Please enter an integer listed above!')
            m='continue'
        return m
    def load():
        os.chdir(core_path)
        assets='/Assets'
        path=os.getcwd()
        os.chdir(path+assets)
        char_dict
        temp_dict=pickle.load(open('pc_dict.pickle','rb'))
        for i in range(len(temp_dict)):
            char_dict[i]=temp_dict[i]
        for i in range(len(char_dict)):
            temp_storage=[]
            name=char_dict[i]+'.pickle'
            temp_storage=pickle.load(open(name,'rb'))
            globals()[char_dict[i]]=pc(temp_storage[0],temp_storage[1],temp_storage[2],temp_storage[3],temp_storage[4])
            globals()[char_dict[i]].set_max_hp=temp_storage[5]
            globals()[char_dict[i]].current_hp=temp_storage[6]
            globals()[char_dict[i]].ac=temp_storage[7]
    #DISPLAY
    true=0
    core_path=os.getcwd()
    os.chdir(core_path)
    print ('WELCOME TO THE DM COMPANION PROGRAM FOR PATHFINDER')
    print('What sould you like to do today?')
    options_dict={0:'Create Character',1:'Take Damage/Heal',2:'Give/Spend Gold',3:'Combat Display',4:'Save',5:'Spell Lookup',6:'Exit'}
    dam_heal={0:'Heal',1:'Damage'}
    while true==0:
        option_dict={1:'New Campaign',2:'Load Campaign'}
        for i in range(1,len(option_dict)+1):
            print (str(i)+':',option_dict[i])
        user=input('>')
        if user.lower()=='exit' or user.lower()=='quit':
            break
        try:
            int_user=int(user)
        except:
            print('Please enter either 1 or 2!')
            continue
        if int_user==1:
            true=1
            #Copy here
            #Menu loop
            while true==1:
                for i in range(len(options_dict)):
                    print(str(i+1)+':',options_dict[i])
                users=input('>')
                #Back function
                if users.lower()=='back' or users.lower()=='b':
                    true=0
                    #break
                    continue
                #Input codition function
                int_users=input_condition(users,len(options_dict)+1)
                if int_users=='continue':
                    continue
                menu_2=int_users-1
                if menu_2!=0 and len(char_dict)==0:
                    print('Create a character first!')
                    character_creation()
                    continue
                #Character creation
                elif menu_2==0:
                    character_creation()
                    continue
                #Damage/Healing
                elif menu_2==1:
                    true=3
                    while true==3:
                        num=len(dam_heal)
                        for i in range(num):
                            print(str(i+1)+':',dam_heal[i])
                        users=input('>')
                        if users.lower()=='back' or users.lower()=='b':
                            true=1
                            break
                        #num+1=len(dam_heal)+1
                        int_user=input_condition(users,num+1)
                        if int_user=='continue':
                            continue
                        new_int_user=int_user-1
                        #Healing
                        if new_int_user==0:
                            num=len(char_dict)
                            print_char_dict()
                            print(str(num+1)+':','All')
                            user=input('Which Character(s)?: ')
                            #Input Condition Function
                            int_user=input_condition(user,len(dam_heal)+1)
                            #Scale down one fro display
                            new_int_user=int_user-1
                            if user.lower()=='back' or user.lower()=='b':
                                true=1
                                break
                            if int_user=='continue':
                                continue
                            #num=len(char_dict)
                            #Heal individual
                            if new_int_user in range(num):
                                health=input('How much healing?: ')
                                try:
                                    int_health=int(health)
                                except:
                                    print('Pick a positive, whole number, you muppet!')
                                    continue
                                globals() [char_dict[new_int_user]].healing(int_health)
                                print(char_dict[new_int_user],'healed for',int_health)
                                true=1
                                break
                            #Heal all function
                            if new_int_user==num:
                                health=input('How much healing?: ')
                                try:
                                    int_health=int(health)
                                except:
                                    print('Pick a positive, whole number, you muppet!')
                                    continue
                                for i in range(len(char_dict)):
                                    globals()[char_dict[i]].healing(int_health)
                                    print(char_dict[i],'healed for',int_health)
                                true=1
                                break
                                
                        #Damage
                        if new_int_user==1:
                            num=len(char_dict)
                            print_char_dict()
##                            print(str(num+1)+':','All')
                            user=input('Which Character?: ')
                            #Input Condition Function
                            int_user=input_condition(user,len(dam_heal))
                            #Scale down one from display
                            if int_user=='continue':
                                continue
                            new_int_user=int_user-1
                            if user.lower()=='back' or user.lower()=='b':
                                true=1
                                break
                            if int_user=='continue':
                                continue
                            #num=len(char_dict)
                            #Damage individual
                            if new_int_user in range(num):
                                damage=input('How much damage?: ')
                                try:
                                    int_damage=int(damage)
                                except:
                                    print('Pick a positive, whole number, you muppet!')
                                    continue
                                globals() [char_dict[new_int_user]].damage(int_damage)
                                true=1
                                break
                        else:
                            print('Please enter 1 or 2!')
                            continue
                #Giving/Spending Gold       
                elif menu_2==2:
                    true=4
                    while true==4:
                        #Choosing to spend or give
                        num=len(char_dict)+1
                        gold_options={0:'Give',1:'Spend'}
                        for i in range(len(gold_options)):
                            print(str(i+1)+':',gold_options[i])
                        user=input('>')
                        if user.lower()=='back' or user.lower()=='b':
                            true=1
                            break
                        #Input Condition function
                        int_user=input_condition(user,len(gold_options)+1)
                        if int_user=='continue':
                            continue
                        menu_gold=int_user-1
                        #Giving
                        if menu_gold==0:
                            print_char_dict()
                            print(str(len(char_dict)+1)+':','All')
                            user=input('>')
                            if user.lower()=='back' or user.lower()=='b':
                                continue
                            int_user=input_condition(user,num)
                            if int_user=='continue':
                                continue
                            menu_gold_player=int_user-1
                            if menu_gold_player in range(len(char_dict)):
                                gold=input('How much gold?: ')
                                globals()[char_dict[menu_gold_player]].give_gold(gold)
                            elif menu_gold_player==len(char_dict):
                                gold=input('How much gold?: ')
                                for i in range(len(char_dict)):
                                    globals() [char_dict[i]].give_gold(gold)
                            else:
                                print('Improper input. Try again, nerd!')
                                continue 
                        #Spending    
                        elif menu_gold==1:
                            print_char_dict()
                            print(str(len(char_dict)+1)+':','All')
                            user=input('>')
                            if user.lower()=='back' or user.lower()=='b':
                                continue
                            int_user=input_condition(user,num)
                            if int_user=='continue':
                                continue
                            menu_gold_player=int_user-1
                            if menu_gold_player in range(len(char_dict)):
                                gold=input('How much gold?: ')
                                globals()[char_dict[menu_gold_player]].spend_gold(gold)
                            elif menu_gold_player==len(char_dict):
                                gold=input('How much gold?: ')
                                for i in range(len(char_dict)):
                                    globals() [char_dict[i]].spend_gold(gold)
                            else:
                                print('Improper input. Try again, nerd!')
                                continue 
                        else:
                            print('Please enter the appropriate option!')
                            continue
                #Combat Display
                elif menu_2==3:
                    combat_display()
                    cont=input('\n\nEnter any input to continue.')
                    if cont!='':
                        continue
                    else:
                        continue
                #Save
                elif menu_2==4:
                    save()
                    continue
                #Spell Lookup
                elif menu_2==5:
                    spell=input('What Spell would you like to see?: ')
                    low_spell=spell.lower()
                    find_spell(low_spell)
                    os.chdir(core_path)
                    cont=input('\n\nPress any enter to continue.')
                    if cont!='':
                        continue
                    else:
                        continue
                #Quit
                elif menu_2<len(options_dict)-1:
                    continue
                else:
                    quit()
                #End copy here
        if int_user==2:
            load()
            true=1
            for i in range(len(char_dict)):
                 print(char_dict[i])
            #Paste Here
            while true==1:
                for i in range(len(options_dict)):
                    print(str(i+1)+':',options_dict[i])
                users=input('>')
                #Back function
                if users.lower()=='back' or users.lower()=='b':
                    true=0
                    #break
                    continue
                #Input codition function
                int_users=input_condition(users,len(options_dict)+1)
                if int_users=='continue':
                    continue
                menu_2=int_users-1
                if menu_2!=0 and len(char_dict)==0:
                    print('Create a character first!')
                    character_creation()
                    continue
                #Character creation
                elif menu_2==0:
                    character_creation()
                    continue
                #Damage/Healing
                elif menu_2==1:
                    true=3
                    while true==3:
                        num=len(dam_heal)
                        for i in range(num):
                            print(str(i+1)+':',dam_heal[i])
                        users=input('>')
                        if users.lower()=='back' or users.lower()=='b':
                            true=1
                            break
                        #num+1=len(dam_heal)+1
                        int_user=input_condition(users,num+1)
                        if int_user=='continue':
                            continue
                        new_int_user=int_user-1
                        #Healing
                        if new_int_user==0:
                            num=len(char_dict)
                            print_char_dict()
                            print(str(num+1)+':','All')
                            user=input('Which Character(s)?: ')
                            #Input Condition Function
                            int_user=input_condition(user,len(dam_heal)+1)
                            #Scale down one fro display
                            new_int_user=int_user-1
                            if user.lower()=='back' or user.lower()=='b':
                                true=1
                                break
                            if int_user=='continue':
                                continue
                            #num=len(char_dict)
                            #Heal individual
                            if new_int_user in range(num):
                                health=input('How much healing?: ')
                                try:
                                    int_health=int(health)
                                except:
                                    print('Pick a positive, whole number, you muppet!')
                                    continue
                                globals() [char_dict[new_int_user]].healing(int_health)
                                print(char_dict[new_int_user],'healed for',int_health)
                                true=1
                                break
                            #Heal all function
                            if new_int_user==num:
                                health=input('How much healing?: ')
                                try:
                                    int_health=int(health)
                                except:
                                    print('Pick a positive, whole number, you muppet!')
                                    continue
                                for i in range(len(char_dict)):
                                    globals()[char_dict[i]].healing(int_health)
                                    print(char_dict[i],'healed for',int_health)
                                true=1
                                break
                                
                        #Damage
                        if new_int_user==1:
                            num=len(char_dict)
                            print_char_dict()
##                            print(str(num+1)+':','All')
                            user=input('Which Character?: ')
                            #Input Condition Function
                            int_user=input_condition(user,len(dam_heal))
                            #Scale down one from display
                            if int_user=='continue':
                                continue
                            new_int_user=int_user-1
                            if user.lower()=='back' or user.lower()=='b':
                                true=1
                                break
                            if int_user=='continue':
                                continue
                            #num=len(char_dict)
                            #Damage individual
                            if new_int_user in range(num):
                                damage=input('How much damage?: ')
                                try:
                                    int_damage=int(damage)
                                except:
                                    print('Pick a positive, whole number, you muppet!')
                                    continue
                                globals() [char_dict[new_int_user]].damage(int_damage)
                                true=1
                                break
                        else:
                            print('Please enter 1 or 2!')
                            continue
                #Giving/Spending Gold       
                elif menu_2==2:
                    true=4
                    while true==4:
                        #Choosing to spend or give
                        num=len(char_dict)+1
                        gold_options={0:'Give',1:'Spend'}
                        for i in range(len(gold_options)):
                            print(str(i+1)+':',gold_options[i])
                        user=input('>')
                        if user.lower()=='back' or user.lower()=='b':
                            true=1
                            break
                        #Input Condition function
                        int_user=input_condition(user,len(gold_options)+1)
                        if int_user=='continue':
                            continue
                        menu_gold=int_user-1
                        #Giving
                        if menu_gold==0:
                            print_char_dict()
                            print(str(len(char_dict)+1)+':','All')
                            user=input('>')
                            if user.lower()=='back' or user.lower()=='b':
                                continue
                            int_user=input_condition(user,num)
                            if int_user=='continue':
                                continue
                            menu_gold_player=int_user-1
                            if menu_gold_player in range(len(char_dict)):
                                gold=input('How much gold?: ')
                                globals()[char_dict[menu_gold_player]].give_gold(gold)
                            elif menu_gold_player==len(char_dict):
                                gold=input('How much gold?: ')
                                for i in range(len(char_dict)):
                                    globals() [char_dict[i]].give_gold(gold)
                            else:
                                print('Improper input. Try again, nerd!')
                                continue 
                        #Spending    
                        elif menu_gold==1:
                            print_char_dict()
                            print(str(len(char_dict)+1)+':','All')
                            user=input('>')
                            if user.lower()=='back' or user.lower()=='b':
                                continue
                            int_user=input_condition(user,num)
                            if int_user=='continue':
                                continue
                            menu_gold_player=int_user-1
                            if menu_gold_player in range(len(char_dict)):
                                gold=input('How much gold?: ')
                                globals()[char_dict[menu_gold_player]].spend_gold(gold)
                            elif menu_gold_player==len(char_dict):
                                gold=input('How much gold?: ')
                                for i in range(len(char_dict)):
                                    globals() [char_dict[i]].spend_gold(gold)
                            else:
                                print('Improper input. Try again, nerd!')
                                continue 
                        else:
                            print('Please enter the appropriate option!')
                            continue
                #Combat Display
                elif menu_2==3:
                    combat_display()
                    cont=input('\n\nEnter any input to continue.')
                    if cont!='':
                        continue
                    else:
                        continue
                #Save
                elif menu_2==4:
                    save()
                    continue
                #Spell Lookup
                elif menu_2==5:
                    spell=input('What Spell would you like to see?: ')
                    low_spell=spell.lower()
                    find_spell(low_spell)
                    os.chdir(core_path)
                    cont=input('\n\nPress any enter to continue.')
                    if cont!='':
                        continue
                    else:
                        continue
                #Quit
                elif menu_2<len(options_dict)-1:
                    continue
                else:
                    quit()
        else:
            print('Please enter 1 or 2!')
            continue
    #find_spell('resistance')
main()
