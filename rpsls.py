#coding:gbk
"""
��һ��С��Ŀ��Rock-paper-scissors-lizard-Spock
���ߣ�������
���ڣ�2019/11/21
"""

import random



# 0 - ʯͷ
# 1 - ʷ����
# 2 - ֽ
# 3 - ����
# 4 - ����

# ����Ϊ�����Ϸ����Ҫ�õ����Զ��庯��

def name_to_number(name):
    """
    ����Ϸ�����Ӧ����ͬ������
    """
    if name=='rock':
        return 0
    elif name=='spock':
        return 1
    elif name=='paper':
        return 2
    elif name=='lizard':
        return 3
    elif name=='scissors':
        return 4
    # ʹ��if/elif/else��佫����Ϸ�����Ӧ����ͬ������
    # ��Ҫ���Ƿ��ؽ��
    #��дִ�д���,������ɺ�passɾ��
  
def number_to_name(number):
	if number==0:
		return "rock"
	if number==1:
		return "spock"
	if number==2:
		return "paper"
	if number==3:
		return "lizard"
	if number==4:
		return "scissors"
    # ʹ��if/elif/else��佫��ͬ��������Ӧ����Ϸ�Ĳ�ͬ����
    # ��Ҫ���Ƿ��ؽ��

    #��дִ�д���,������ɺ�passɾ��


def rpsls(player_choice):
    """
    �û�����������һ��ѡ�񣬸���RPSLS��Ϸ��������Ļ�������Ӧ�Ľ��

    """


    # ���"-------- "���зָ�
    player_choice=input("���ѡ����")# ��ʾ�û�������ʾ���û�ͨ�����̽��Լ�����Ϸѡ��������룬�������player_choice

    player_choice_number=name_to_number(player_choice)# ����name_to_number()�������û�����Ϸѡ�����ת��Ϊ��Ӧ���������������player_choice_number

    comp_number=random.randrange(0,4)#�Զ�����0-4֮��������������Ϊ��������ѡ�����Ϸ���󣬴������comp_number

    comp_choice=number_to_name(comp_number)# ����number_to_name()����������������������ת��Ϊ��Ӧ����Ϸ����

    print("���Ե�ѡ����",comp_choice)# ����Ļ����ʾ�����ѡ����������
    result=(comp_number-player_choice_number)%5
    if result==1 or result==2:
        print("������A��")
    if result==3 or result==4:
        print("��Ӯ��")
    if result==0:
        print("���ͼ��������һ����")
    # ����if/elif/else ��䣬����RPSLS������û�ѡ��ͼ����ѡ������жϣ�������Ļ����ʾ�жϽ��

    # ����û��ͼ����ѡ��һ��������ʾ�����ͼ��������һ���ء�������û���ʤ������ʾ����Ӯ�ˡ�����֮����ʾ�������Ӯ�ˡ�

    #����������ʾ��дִ�д��룬������ɺ�ɾ����pass










# �Գ�����в���
print("��ӭʹ��RPSLS��Ϸ")
print("----------------")
rpsls("choice_name")








