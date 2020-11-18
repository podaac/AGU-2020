# tutorial 8

Go to my EC2 Dashboard:

https://us-west-2.console.aws.amazon.com/ec2/v2/home?region=us-west-2#Home:

Connect to my EC2:

```shell
ssh -i "~/.ssh/key-AGU-2020-ipynb.pem" ec2-user@ec2-34-217-117-190.us-west-2.compute.amazonaws.com
```

Clone this repository:

```shell
(base) [ec2-user@ip-172-31-9-16 tmp]$ git clone https://git.earthdata.nasa.gov/scm/pocumulus/jupyter-tutorials.git
Cloning into 'jupyter-tutorials'...
Username for 'https://git.earthdata.nasa.gov': jmcnelis
Password for 'https://jmcnelis@git.earthdata.nasa.gov': 
remote: Counting objects: 30, done.
remote: Compressing objects: 100% (28/28), done.
remote: Total 30 (delta 13), reused 0 (delta 0)
Unpacking objects: 100% (30/30), done.
```

Start Jupyter notebook:

```python
jupyter notebook --no-browser
```

```python
http://127.0.0.1:9999/?token=ec9de6a943189498e5cb232a01d84122e4ccfaccb1b23f65
```


