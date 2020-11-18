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

```shell
(base) [ec2-user@ip-172-31-9-16 tmp]$ ls
jupyter-tutorials
```

```shell
(base) [ec2-user@ip-172-31-9-16 tmp]$ jupyter notebook --generate-config
Overwrite /home/ec2-user/.jupyter/jupyter_notebook_config.py with default config? [y/N]y
Writing default config to: /home/ec2-user/.jupyter/jupyter_notebook_config.py
```

```shell
(base) [ec2-user@ip-172-31-9-16 tmp]$ ipython
Python 3.8.3 (default, May 19 2020, 18:47:26) 
Type 'copyright', 'credits' or 'license' for more information
IPython 7.19.0 -- An enhanced Interactive Python. Type '?' for help.

In [1]: from IPython.lib import passwd

In [2]: passwd
Out[2]: <function IPython.lib.security.passwd(passphrase=None, algorithm='sha1')>

In [3]: passwd()
Enter password: 
Verify password: 
Out[3]: 'sha1:30b669aae1a3:36f617da4e36a6ac97c1a79e2d0ea6ce7645acc3'

```

Start Jupyter notebook:

```python
jupyter notebook --no-browser
```

```python
http://127.0.0.1:9999/?token=ec9de6a943189498e5cb232a01d84122e4ccfaccb1b23f65
```


