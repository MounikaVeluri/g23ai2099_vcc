# g23ai2099_vcc
Flask application with Docker implementation

Steps :

1. Create "server.py" file with python codebase to start server

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

2. create "requirements.txt" file for necessary packages 

		Flask==2.0.3
		Werkzeug==2.0.3
		
3. create "Dockerfile" with list of commands to be ran to serve the application

		FROM python:3.9-slim-buster
		WORKDIR /app
		COPY . /app
		RUN pip install --no-cache-dir -r requirements.txt
		EXPOSE 5000
		ENV NAME World
		CMD ["python", "server.py"]

4. Install docker desktop and check if the docker is running in the machine
5. open terminal and run the below command to create an image using the above application

		docker build -t g23ai2099_app:latest .  

6. Once images is created , execute the below command to start container

		docker run -p 5000:5000 g23ai2099_app 

7. Once the application starts running inside the container , we can browse to localhost:5000 in browser
8. check the docker logs <container ID> to check terminal logs of application in case to debug
