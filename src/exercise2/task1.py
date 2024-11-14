import asyncio
import os
import aioconsole
import aiohttp
import aiofiles
import ssl
from prettytable import PrettyTable


#https://images2.pics4learning.com/catalog/s/swamp_15.jpg OK
#https://bad-link-no-website-here.strange/img.png  NO
#https://images2.pics4learning.com/catalog/p/parrot.jpg OK


ssl_context = ssl.create_default_context()
ssl_context.check_hostname = False
ssl_context.verify_mode = ssl.CERT_NONE


def catalog():
    while True:
        path=input()
        if os.path.exists(path):print("Введите другой путь")
        else:
            os.mkdir(path)
            break
    return path


async def manager(queue,input_task,output_task):
    await input_task
    await queue.join()
    output_task.cancel()
    await output_task


async def worker(path,session,ref,i):
    async with session.get(ref) as resp:
        async with aiofiles.open(f"{path}/{i}.jpg","wb") as file:
            async for chunk in resp.content.iter_any():
                await file.write(chunk)
    

async def scan_ref(queue:asyncio.Queue):
    while True:
        ref=await aioconsole.ainput()
        if ref=="":break
        await queue.put(ref)


async def pars_ref(path:str,queue:asyncio.Queue,result:dict):
    i=0 #счетчик файлов
    async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=ssl_context)) as session:
        while True:
                ref=await queue.get()
                try:
                    await worker(path,session,ref,i)
                    result[ref]="Успех"
                    i+=1 
                except: 
                    result[ref]="Ошибка"
                finally:queue.task_done()


def print_result(result:dict):
    table=PrettyTable()
    table.field_names=['Ссылка','Состояние']
    for k, v in result.items():
        table.add_row([k, v])
    os.system('cls' if os.name == 'nt' else 'clear')
    print(table)

        
async def main():
    path=catalog()
    result={}
    queue=asyncio.Queue()
    input_task=asyncio.create_task(scan_ref(queue))
    output_task=asyncio.create_task(pars_ref(path,queue,result))
    manager_task=asyncio.create_task(manager(queue,input_task,output_task))

    try:
        await asyncio.gather(input_task, output_task, manager_task)
    except:
        print_result(result)

if __name__=="__main__":
    asyncio.run(main())