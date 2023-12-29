# dri_prime1-detection and Steam game setup instructions
Simple script to verify if desired applications are running with discrete graphics

## No Processes using discrete graphics, returns as empty.

## Indicates which processes are using discrete graphics, provides process name and ID.

This was put together rather quickly, I welcome clean up/improvements. 

![Example of this script in use](https://raw.githubusercontent.com/ctsdownloads/dri_prime1-detection/main/PRIME.png)


Step 1: Open a terminal window and download the script to your desired directory.

```
git clone https://github.com/FrameworkComputer/dri_prime1-detection.git
```
Step 2: Change directories to the access the script.

```
cd dri_prime1-detection/ 
```

Step 3: Make it executable.
```
chmod +x amd-prime-dri.sh
```

Step 4: Run this to detect if the discrete card is used for that application.
```
sudo sh amd-prime-dri.sh
```
-------------------------------------------------------

## Steam game setup instructions for Ubuntu 22.04.3 LTS (Long Term Support)

### When to use: 

This is likely only needed for Steam. Seems there is a bug where if you launch Steam normally, it doesn't launch correctly (Ubuntu or Fedora)

**We get past this accordingly.**

- Activities, search for Steam.
- Right click, launch with integrated graphics.
  
![Locate and launch Steam using INTEGRATED graphics](https://raw.githubusercontent.com/ctsdownloads/dri_prime1-detection/main/Steam-1.png)

&nbsp;
&nbsp;
&nbsp;

**With Steam open.**

- Locate your game installed already or install it.
- Right click on the game, goto properties.
  
![Right click on the game, goto properties](https://raw.githubusercontent.com/ctsdownloads/dri_prime1-detection/main/steam-2.png)

&nbsp;
&nbsp;
&nbsp;

**Launch options section**

- Place the following into your launch options, to ensure you are using the discreete GPU and not the integated GPU for your game.

```
DRI_PRIME=1 %command%
```
- Close the General box at the X, there is no save button or anything like that.

----------------------------------------

  ## Steam game setup instructions for Fedora 39

### When to use: 

This is likely only needed for Steam. Seems there is a bug where if you launch Steam normally, it doesn't launch correctly (Ubuntu or Fedora)

**We get past this accordingly.**

- Browse to the horizontal line in the upper left corner, click to open it, search for Steam.
- Right click, *launch Steam normally with a single left click*.
  
![Locate and launch Steam normally](https://raw.githubusercontent.com/FrameworkComputer/dri_prime1-detection/main/f39-steam1.png)

&nbsp;
&nbsp;
&nbsp;

**With Steam open.**

- Locate your game installed already or install it.
- Right click on the game, goto properties.
  
![Right click on the game, goto properties](https://raw.githubusercontent.com/FrameworkComputer/dri_prime1-detection/main/f39-steam2.png)

&nbsp;
&nbsp;
&nbsp;

**Launch options section**

- Place the following into your launch options, to ensure you are using the discreete GPU and not the integated GPU for your game.

```
DRI_PRIME=1 %command%
```
- Close the General box at the X, there is no save button or anything like that.

  

