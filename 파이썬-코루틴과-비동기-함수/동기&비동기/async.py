import time
import asyncio

async def delivery(name,mealtime):
    print(f"{name}에게 배달 완료")
    await asyncio.sleep(mealtime)
    print(f"{name} 식사 완료, {mealtime} 만큼 시간 소요")
    print(f"{name} 그릇 수거 완료")
    return 
    
async def main():
    await asyncio.gather( # 동시성으로 작동하는 코드
        delivery("A",4),
        delivery("B",3),
        delivery("C",1)
    )
    
if __name__ == "__main__":
    start = time.time()
    asyncio.run(main()) 
    end = time.time()
    print(end - start)