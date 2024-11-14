import time
import random
from multiprocessing import Queue

class Stud:
    id=0
    def __init__(self,name:str,sex:str,status='Очередь'):
        self.name=name
        self.sex=sex
        self.status=status
        self.time_start=0
        self.time_work=0
        self.id=Stud.id
        Stud.id+=1


class Examer(Stud):
    id=0
    type='Examer'
    def __init__(self,name:str,sex:str,cur_stud='-',count_stud=0,fail=0,dinner=0):
        super().__init__(name,sex)
        self.cur_stud=cur_stud
        self.count_stud=count_stud
        self.fail=fail
        self.dinner=dinner
        self.id=Examer.id
        self.status=1
        Examer.id+=1


    def session(self,queue:Queue,questions:list,signal_queue:Queue):
        self.time_start=time.time()
        while not queue.empty():
            if (time.time()-self.time_start)>=30 and not self.dinner:
                self.dinner==1
                time.sleep(random.randint(12,18))
            result=0
            correct_answer=0
            incorrect_answer=0
            student=queue.get()
            student.time_start=time.time()
            return_list=[self,student]
            self.cur_stud=student.name
            self.count_stud+=1
            signal_queue.put(return_list)
            for i in range(3):
                number_que=random.randint(0,len(questions)-1)
                question=questions[number_que].que[:]
                answer_stud=Question.answer(question,student.sex)
                answer_examer=[]
                while len(answer_examer)<len(questions[number_que].que):
                    answer=Question.answer(question,self.sex)
                    question.remove(answer)
                    answer_examer.append(answer)
                    if random.choices([0,1],[1/3,2/3])[0]:break
                if answer_stud in answer_examer:
                    questions[number_que].correct+=1
                    correct_answer+=1
                else: incorrect_answer+=1
                signal_queue.put([questions[number_que]])
            mood=random.choices([-1,0,1],[1/8,1/4,5/8])[0]
            time.sleep(random.randint(len(self.name)-1,len(self.name)+1))
            student.time_work=time.time()-student.time_start
            if mood==1:result=1
            elif not mood:
                if correct_answer>incorrect_answer:result=1
            if not result:
                self.fail+=1
                student.status='Провалил'
            else:student.status='Сдал'
            self.cur_stud='-'
            signal_queue.put(return_list)
        self.status=0
        self.time_work=time.time()-self.time_start
        signal_queue.put([self])
            


class Question:
    id=0
    type='Question'
    def __init__(self,que:list):
        self.que=que
        self.id=Question.id
        self.correct=0
        Question.id+=1

    def answer(que:list,sex:str):
        chance=[]
        koef=(1+len(que))*len(que)/2
        for i in range(len(que)):
            if sex=='М':
                chance.append((len(que)-i)/koef)
            else:chance.append((i+1)/koef)
        return random.choices(que,chance)[0]