from multiprocessing import Process,Queue
from prettytable import PrettyTable
import os
import exam
import time

def table(studetns:list,examers:list,signal_queue:Queue,questions):
    time_start=time.time()
    while len(list(filter(lambda x: x.status==1,examers)))!=0:
        if not signal_queue.empty():
            signal=signal_queue.get()
            if signal[0].type=='Examer':examers[signal[0].id]=signal[0]
            else:questions[signal[0].id]=signal[0]
            if len(signal)>1:studetns[signal[1].id]=signal[1]
        os.system('cls' if os.name == 'nt' else 'clear')
        print(stud_table(studetns))
        print(examer_table(examers))
        print(f"Осталось в очереди: {len(list(filter(lambda x:1 if x.status=='Очередь' else 0,studetns)))} из {len(studetns)}")
        print(f"Время с момента начала экзамена: {time.time()-time_start}")
    result_print(time.time()-time_start,studetns,examers,questions)
    
def result_print(start:float,studetns:list,examers:list,questions:list):
    os.system('cls' if os.name == 'nt' else 'clear')
    print(stud_table(studetns))
    print(examer_table(examers))
    print(f"Время с момента начала экзамена: {start}")
    mvp_students(studetns)
    mvp_examer(examers)
    worse_students(studetns)
    mvp_questions(questions)
    conclusion(studetns)
    

def mvp_students(studetns:list):
    print("Имена лучших студентов:",end=' ')
    data=list(filter(lambda x:x.status=='Сдал',studetns))
    if len(data):
        min_t=data[0].time_work
        for stud in data:
            if stud.time_work<min_t:min_t=stud.time_work
        result=list(filter(lambda x:x.time_work==min_t,data))
        for i in result:print(f"{i.name}",end=' ')
    print()


def mvp_examer(examers:list):
    koef=examers[0].fail/examers[0].count_stud
    for examer in examers:
        kpd=examer.fail/examer.count_stud
        if kpd<koef:koef=kpd
    result=list(filter(lambda x:(x.fail/x.count_stud)==koef,examers))
    print("Имена лучших экзаменаторов:",end=' ')
    for i in result:print(f"{i.name}",end=' ')
    print()

def worse_students(studetns:list):
    print("Имена студентов, которых после экзамена отчислят:",end=' ')
    data=list(filter(lambda x:x.status=='Провалил',studetns))
    if len(data):
        min_t=data[0].time_work
        for stud in data:
            if stud.time_work<min_t:min_t=stud.time_work
        result=list(filter(lambda x:x.time_work==min_t,data))
        for i in result:print(f"{i.name}",end=' ')
    print()


def mvp_questions(questions):
    max_answer=0
    for que in questions:
        if que.correct>max_answer:max_answer=que.correct
    result=list(filter(lambda x:x.correct==max_answer,questions))
    print("Лучшие вопросы:",end=' ')
    for i in range(len(result)):
        res=''
        for string in result[i].que:
            res+=string
            res+=' '
        result[i]=res
        print(result[i])


def conclusion(studetns:list):
    count=0
    result='экзамен не удался'
    for stud in studetns:
        if stud.status=='Сдал':count+=1
    if count/len(studetns)>0.85:result='экзамен удался'
    print(f"Вывод: {''.join(result)}")


def pars_stud(stud_queue:Queue):
    studetns=[]
    with open("students.txt",'r') as file:
        while line:=file.readline():
            stud=exam.Stud(*line.split())
            studetns.append(stud)
            stud_queue.put(stud)
    return studetns

def pars_examer():
    examers=[]
    with open("examiners.txt",'r') as file:
        while line:=file.readline():
            examers.append(exam.Examer(*line.split()))
    return examers

def pars_question():
    questions=[]
    with open('questions.txt','r') as file:
        while line:=file.readline():
            questions.append(exam.Question(line.split()))
    return questions

def stud_table(studetns:list):
    stud_table=PrettyTable()
    stud_table.field_names=["Студент",'Статус']
    for i in range(len(studetns)):
        stud_table.add_row([studetns[i].name,studetns[i].status])
    return stud_table


def examer_table(examers:list):
    examer_table=PrettyTable()
    examer_table.field_names=["Экзаменатор",'Текущий студент','Всего студентов','Завалил','Время работы']
    for i in range(len(examers)):
        examer_table.add_row([examers[i].name, examers[i].cur_stud, examers[i].count_stud, 
        examers[i].fail,time.time()-examers[i].time_start if examers[i].status else examers[i].time_work])
    return examer_table

def main():
    stud_queue=Queue()
    signal_queue=Queue()
    studetns=pars_stud(stud_queue)
    examers=pars_examer()
    questions=pars_question()
    task_list=[]
    for i in range(len(examers)):
        task_list.append(Process(target=examers[i].session,args=(stud_queue,questions,signal_queue,)))
    draw=Process(target=table,args=(studetns,examers,signal_queue,questions,))
    draw.start()
    for task in task_list:task.start()
    draw.join()
    for p in task_list:p.join()

if __name__=='__main__':main()