user@master ~$ echo 'from datetime import datetime
now = datetime.now()
current_time = now.strftime("%H:%M:%S")
print("Current Time is :", current_time)
print("Hello World!")' >hello.py
user@master ~$ . /common/intel/oneAPI_Base_Toolkit/2022.1.2.146/setvars.sh intel64
user@master ~$ srun -N 1 -p gpu -t 10 python hello.py
('Current Time is :', '13:35:57')
Hello World!