# ComputerVisionProject
보행자와 주행자를 위한 도로 알림 프로그램입니다. 🚲⏰
<br><br><br><br>



## Motivation
행정안전부에 따르면 지난 4년간(2019-2022) 평균 자전거 사고 건수는 약 1만 2천 건으로, 자전거 사고를 예방할 대안이 필요했습니다. <br> 또한 시각장애인의 경우 현재 걷고 있는 길이 보행자 도로인지, 자전거 도로인지 구분하기 어렵다는 점을 지적해 도로 안내 프로그램을 기획 및 구현했습니다.<br><br>
<img src="https://github.com/user-attachments/assets/e72eae24-8c01-490d-b7fe-417d6353e831" width=600 height=100/>
<img src="https://github.com/user-attachments/assets/4793374d-ba5c-4c97-af65-97dddde1e3a9" width=400 height=200/>
<img src="https://github.com/user-attachments/assets/77caa9db-3821-4f36-9b71-ed48b03c107d" width=400 height=200/>
<br><br><br><br>



## Functions
1. 자전거 도로를 걷는 보행자가 있을 경우 이동 요청 알람
2. 보행자 도로를 주행하는 bicycle이 있을 경우 이동 요청 알람
<br><br><br><br>



## Approach
1. YOLO 이용해 자전거 도로와 보행자 도로 Detection하기
2. 움직이는 물체 인식하기
3. 물체의 위치(자전거 or 보행자 도로) 파악
4. 부적절한 위치일 경우 메시지 출력 (제자리로 돌아갈 경우 메시지 중단)
<br><br><br><br>



## 실행 화면
<!--<img src="https://github.com/user-attachments/assets/3935e71d-b0db-48f3-9546-36e41765b07d" width=350 height=400/>-->


https://github.com/user-attachments/assets/5da21f29-a3bc-4d49-bedc-23695184a633


https://github.com/user-attachments/assets/ba8bdc68-4072-4572-888c-938598c44c50


<br><br><br><br>



## How to start
- installing Python
  
- installing required Python modules
```bash
pip install inference
pip install python-dotenv
```
File paths and environment variables are managed in ".env"

- setting up API_KEY
```bash
export API_KEY=<your api key>
```

- run the Python script
```bash
python app.py
```
<br><br><br><br>



## Reference
– opensource project: <br>
  https://universe.roboflow.com/engs-89/bikes-ped-scooters <br>
  https://universe.roboflow.com/leo-ueno/people-detection-o4rdr <br>

– articles: <br>
  https://news.mt.co.kr/mtview.php?no=202311171434298126 <br>
  한국소비자원, 시각장애인 보행안전실태조사 <br>
  https://www.kca.go.kr/smartconsumer/sub.do?menukey=7301&mode=view&no=1003080871 <br>
  https://kosis.kr/statHtml/statHtml.do?orgId=110&tblId=DT_110031_101A <br>
  
<br><br><br><br>
