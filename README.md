# g23ai2099_vcc
Assignment 1: Docker Application Deployment

Name: Mounika V S

Rol.No: G23AI2099

Subject: Virtualization and Cloud Computing


Steps:

1. Create "server.py" file with python codebase to start server.

		from flask import Flask, render_template, request
		
		app = Flask(__name__)
		
		@app.route('/')
		def index():
		    return render_template('index.html')
		
		@app.route('/greet', methods=['POST'])
		def greet():
		    username = request.form.get('username')
		    return f"Hello, {username}!"
		
		if __name__ == '__main__':
		    app.run(host='0.0.0.0', port=5000)

2. Create an index.html file in a template folder to facilitate the html code.

		<!DOCTYPE html>
		<html>
		<head>
		    <title>Flask User Greeting</title>
		</head>
		<body>
		    <h1>Enter your name:</h1>
		    <form method="POST" action="/greet">
		        <input type="text" name="username">
		        <input type="submit" value="Submit">
		    </form>
		</body>
		</html>

3. create "requirements.txt" file for necessary packages.

		Flask==2.0.3
		Werkzeug==2.0.3
		
4. create "Dockerfile" with list of commands to be run to serve the application.

		FROM python:3.9-slim-buster
		WORKDIR /app
		COPY . /app
		RUN pip install --no-cache-dir -r requirements.txt
		EXPOSE 5000
		ENV NAME World
		CMD ["python", "server.py"]

5. Install docker desktop and check if the docker is running in the machine.
6. open terminal and run the below command to create an image using the above application.

		docker build -t g23ai2099_app:latest 

   ![image](https://github.com/user-attachments/assets/811965a5-e694-4914-b35e-3013fe6c014c)
   ![image](https://github.com/user-attachments/assets/d1096ef0-046e-496a-ad11-87efec9d5818)



7. Once images is created, execute the below command to start container

		docker run -p 5000:5000 g23ai2099_app
![image](https://github.com/user-attachments/assets/da85abaa-e99f-41c9-ae84-a8a8480b0b87)


8. Once the application starts running inside the container , we can browse to localhost:5000 in browser
    ![image](https://github.com/user-attachments/assets/55df842f-39bf-4d47-b594-be63444b1582)
   ![image](https://github.com/user-attachments/assets/ce80c51b-d609-46c3-ad21-8878ab67332c)
   ![image](https://github.com/user-attachments/assets/d5b1b80d-b3f5-45eb-af7b-b4d0aee7d358)

9. check the docker logs <container ID> to check terminal logs of application in case to debug

		docker logs <container ID>
