

# Machine_learning_project

### Software and account requirement

1. [Git CLI](https://git-scm.com/download/win)
2. [Git Command/ Documentation](https://git-scm.com/docs/git)


#### TO clone git hub repository in VS and local system

by commands from powershell/command prompt
1.  create new repository in github
2.  #command - git clone "Repository Link"
3.  #comand - ls or dir # to check directory
4.  #comand - cd "to change directory paste directory location"
5.  #comand - code .


#### 2nd way to clone and create repoaitory in local system

1. create new repository in github
2. create fresh folder in any location of Local system
3. click in folder and press shift+ right click and power shell/command prompt
4. in power shell write # comand  -  git clone <"Repository Link">
4. #command - pwd
5. open VScode and select that project fold and in that that clone repository 

6. in Vscode open terminal and then select gitbash terminal 

To check app file 

````
python app.py
````



1. ### *Creating Conda evironment - Commands*



command promt/dit bash/powershell

````
conda --version
````
Create venv in tha same directory
````
conda create -p venv python==3.7 -y  
````
To activate venv 

````
conda activate venv/
````
Or
````
conda activate venv
````

to install requirements file
````
pip install -r requirements.txt

````

Create app.py file and in command prompt type  to rune the file 
````
python app.py
````


2. ### *Push changes to github*

Note: to Add files in git 

````
git add filename "to maintain the version control system"
````
OR
````
git add "file1,file2....filen"
````
OR
````
git add . "to add all the files in one line"
````
To check status
````
git status 
````
````
 > Note : "suppose you have create a file but it not added in git , this command will provide status of which file is not tracked by git"
````

````
git commit  "to comit change"
````

to check log
````
git log
````

Note: to commit changes

````
git commit -m "message"
````

To push changes/to send version

````
git push origin main
````
To check remote URL

````
git remote -v
````
to know branch
````
git branch
````
To roll back

````
````

3. ### *To Connect AWS with Git hub*

to Setup we need 3 things

1. aws email 
2. aws apikey
3. aws app_name

4. ### *Docker*

Create Dockerfile and .dockerignore
````
FROM python:3.7
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE $PORT
CMD gunicorn --workers=4 --bind 0.0.0.0:$PORT app:app
````
dockerignore file is use to enter folder/file name which you don't want to be get into container

````
venv/
.git
.gitignore
````

BUILD DOCKER IMAGE

````
docker --help
````
```` 
docker build -t <image_name>:<tagname> .
````
````
example : docker build -t ml-project:latest .
````
> NOTE: Image name for docker image must be in lowercase

to list docker images

````
docker images
````

Run docker image

````
docker run -p 5000:5000 -e PORT=5000 <image id>
````
To check the running container in docker
````
docker ps
````

To stop the docker the container 
````
docker stop <container_id>or 4digit of <contain_id>
````

5. ### *Setup.py file*
First run
````
python setup.py
````
````
python setup.py install
````
It is use to install all the libraries to execute 
````
pip install -e .
````

6. ### *Create folders under housing*

component,config,entity,exception,pipeline,logger and "__init__.py" file amound each package/folder


7. ### Install ipykernel to run jupiter notebook

````
pip install ipykernel
````
Import PyYAML file to ready YAML file format

````
pip install PyYAML
````

8. To read YAML file 

````
import os
os.getcwd()
## to change directory

os.chdir("d:\\Data Analyst course\\machine learning\\Machine_learning_project")

os.getcwd()
os.listdir(".")
# to read congfig file

"config/config.yaml"
## to join file path with directory

config_file_path = os.path.join("config","config.yaml")
config_file_path
# to check file exists or not
os.path.exists(config_file_path)
````

#### TO read YAML file use below comand

````
import YAML

config_info=None

with open(config_file_path,"rb") as yaml_file:
    config_info = yaml.safe_load(yaml_file)
config_info

````
#### Create function to read YAML file and create util file and dump the code
````

def read_yaml_file(file_path:str)->dict:
    """
    read yaml file and returns the content as dictionary
    file path:str
    """
    try:
        with open(file_path, 'rb') as yaml_file:
            return yaml.safe_load(yaml_file)
        
    except Exception as e:
        raise e
````
````

read_yaml_file(config_file_path)

````


