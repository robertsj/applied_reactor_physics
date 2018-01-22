# Accessing NJOY on Eigendoit

## Remote Login to Eigendoit

Eigendoit is available at `eigendoit.mne.ksu.edu` via port 22222 for SSH. All
students in the course have an account based on their normal KSU credentials.

## Adding NJOY

Immediatel upon getting onto Eigendoit, type the following and enter:

```
nano .bashrc
```

This will load an in-console text editor.  Type the following on the 
first line:

```
export PATH=$PATH:/export/apps/njoy/NJOY2016/bin
```

Then type `Ctl+0` and hit enter when it prompts you for the file name.

Finally, type `Ctl+X` to exit.


## Moving Forward

From there, I recommend creating folders, etc., in which to do your 
work.  Please feel free to use any tools you want in order to access 
Eigendoit and accelerate your work flow.  You may find mounting Eigendoit
as a folder is helpful, and I direct you to Richard Reed for instructions
on doing this and other things.
