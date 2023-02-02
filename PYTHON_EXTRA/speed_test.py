import speedtest
from tqdm import tqdm

st = speedtest.Speedtest()

option = int(input('''What speed do you want to test:  
  
1) Download Speed  
  
2) Upload Speed  
  
3) Ping 
  
Your Choice: '''))

match option:
    case 1:
        # with tqdm(total=10) as pbar:
        #     for i in tqdm(range(10)):
        #         pbar.update(10)
        print(st.download())
    case 2:
        print(st.upload())
    case 3:
        servernames = []

        st.get_servers(servernames)

        print(st.results.ping)
    case _:
        print("Please enter the correct choice !")
