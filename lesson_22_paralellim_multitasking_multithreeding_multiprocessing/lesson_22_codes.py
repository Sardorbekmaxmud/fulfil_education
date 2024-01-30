# # CPU - Central Processing Unit
# # CPU --
# # Core - tosh -- asosiy hisob kitob shu yerda bo'ladi
# # Thread - Potok -- Core ni ichida bo'ladi.
# # Vazifasi Core ga ma'lumot olib kelib, yana ma'lumotni qaytarib yuborish hisoblanadi.
# # Multitasking -- Ko'p topshiriqlarni bir vaqtda bajarish deyiladi. Masalan: bizda 4 vazifa bor (4 ta funksiya bor) uni biz 4 thread ga berganmiz,
# u CPU ga olib keladi. CPU ularni ketma-ket hisob kitoblarni bajarib qaytaradi.
# # RAM
# # CPU-bound -- Protsessor ko'p ish qiladi. Bunda protsessor qiynaladi
# # I\O-bound -- I - Input, O - Output -- ma'lumot olib, uni qaytarish. Protsessor qiynalmaydi, lekin ko'p kutib qoladi.


# # coding
import time
import os
from threading import Thread, current_thread
from multiprocessing import Process, current_process

# global variable larni katta harflarda yozish tavsiya qilinadi.
COUNT = 200_000_000  # sanash
SLEEP = 10  # uxlab turishi uchun, to'xtab turadi


def io_bound(sec):
    procession_id = os.getpid()  # prosession id sini olish uchun
    print(
        f"{procession_id} * {current_process().name} * {current_thread().name} --> Kutish boshlandi...")
    time.sleep(sec)
    print(f"{procession_id} * {current_process().name} * {current_thread().name} --> Kutish yakunlandi!")


def cpu_bound(n):
    pid = os.getpid()
    print(f"{pid} * {current_process().name} * {current_thread().name} --> Hisoblash boshlandi...")
    while n > 0:
        n -= 1
    print(f"{pid} * {current_process().name} * {current_thread().name} --> Hisoblash yakunlandi!")


if __name__ == "__main__":
    start = time.time()  # hozirgi, boshlanish vaqti
    # 1-holat: single thread - io bound (1-ta potok va input-output bound)
    # io_bound(SLEEP)                           # 20.001947164535522
    # io_bound(SLEEP)
    # odatiy biz yozayotgan code tezligi.
    # dastur ketma ket 1ta potokda ishlaydi.

    # # 2-holat: multithreeding io-bound        # 10.002147912979126
    # t1_potok_1 = Thread(target=io_bound, args=(SLEEP,))
    # t2_potok_2 = Thread(target=io_bound, args=(SLEEP,))
    #
    # # boshlash
    # t1_potok_1.start()
    # t2_potok_2.start()
    #
    # # jarayonga qo'shish
    # t1_potok_1.join()
    # t2_potok_2.join()
    # # # ikkalasi birdoniga borib birdaniga tugayapti

    # # 3-holat: singlethread - cpu-bound (1ta potokda cpu-bount ishlayapti)
    # cpu_bound(COUNT)                            # 15.451570987701416
    # cpu_bound(COUNT)

    # # 4-holat: multithreed cpu-bound
    # # ikkalasi 1 vaqtda boshlanadi, lekin galma-gal ishlaydi.
    # t1 = Thread(target=cpu_bound, args=(COUNT,))
    # t2 = Thread(target=cpu_bound, args=(COUNT,))
    #
    # t1.start()                                     # 15.652540922164917
    # t2.start()
    #
    # t1.join()
    # t2.join()
    # # 3 va 4 holat bir xil 2 ta potok ishlatsam ham, nega, chunki bari-bir cpu 1ta u ketma-ket bajaryapti vazifani

    # # 5-holat: multiprocessing cpu-bound  -- (2 ta protsessor bilan ishlash cpu-bound da)
    # p1 = Process(target=cpu_bound, args=(COUNT, ))
    # p2 = Process(target=cpu_bound, args=(COUNT, ))   # 7.785441637039185
    #
    # p1.start()
    # p2.start()
    #
    # p1.join()
    # p2.join()

    # # 6-holat: multiprocessing io-bound
    # p1 = Process(target=io_bound, args=(SLEEP, ))
    # p2 = Process(target=io_bound, args=(SLEEP, ))     # 10.141950845718384
    #
    # p1.start()
    # p2.start()
    #
    # p1.join()
    # p2.join()

    end = time.time()  # tugash vaqti
    print("Ketgan vaqt(s)", end - start)

# Xulosa:
# 1. io_bound topshiriqlar uchun ishlatish kerak --> multithreeding --- kutish holatlarida potoklar bilan ishlash yaxshi ekan.
# 2. cpu_bound topshiriqlarda uchun ishlatish kerak --> multiprocessing --- hisoblash holatlarida protsessorlar bilan ishlash dasturni tezlash tirar ekan.

    # 1970 yildan buyog'i ga sanash
    # o'shandan beri o'tgan sekundni oladi
    # print(time.gmtime().tm_yday)
