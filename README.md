# Project-Evaluation-Website
다양한 프로젝트를 평가하고, 평점 및 결과를 확인할 수 있는 웹사이트

프로젝트 클로닝
git clone https://github.com/jangwonii/Project-Evaluation-Website.git

---------------------로컬에서 실행---------------------
1. 의존성 설치
   pip install -r requirements.txt
2. 데이터베이스 마이그레이션
   python manage.py makemigrations
   python manage.py migrate

3.관리자 계정(슈퍼유저) 생성
   python manage.py createsuperuser

4. 개발 서버 실행
   python manage.py runserver


---------------------Docker로 실행---------------------
1. 이미지 빌드
   docker build -t project-evaluation .
   
2. 컨테이너 실행
   docker run -p 8000:8000 project-evaluation
   
3. (최초 1회) 마이그레이션 및 슈퍼유저 생성
   docker exec -it <컨테이너ID> python manage.py migrate
   docker exec -it <컨테이너ID> python manage.py createsuperuser
   
4. 웹사이트 접속
   http://localhost:8000/
   관리자 페이지: http://localhost:8000/admin/
