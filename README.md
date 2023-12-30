# dri_prime1-detection and Steam game setup instructions

A simple application to verify if desired applications are running with discrete graphics

## Indicates which processes are using discrete graphics, provides process name and ID.

Step 1: Open a terminal window and download the AppImage to your desired directory.

- Ubuntu, Activities, search terminal. Fedora, horizonal line in the upper right, search terminal.
- Copy and paste in the following depending on your specific distro listed below, followed by the enter key.

*Ubuntu 22.04 users*:

```
sudo apt install libfuse2 python3-pyqt5 && wget https://github.com/FrameworkComputer/dri_prime1-detection/releases/download/AppImage/dGPU-detect.AppImage
```

*Fedora 39 users*:

```
sudo dnf install python3-qt5 && wget https://github.com/FrameworkComputer/dri_prime1-detection/releases/download/AppImage/dGPU-detect.AppImage
```

Step 2: Make it executable.
```
chmod +x dGPU-detect.AppImage
```

Step 4: Run this to detect if the discrete card is used for that application.

`./dGPU-detect.AppImage` or simply double click the downloaded AppImage file.

**If the dGPU is not running applications:**

![No dGPU running any applications](https://raw.githubusercontent.com/FrameworkComputer/dri_prime1-detection/main/no-dgpu.png)


**If the dGPU is running applications:**

![dGPU running running applications](https://raw.githubusercontent.com/FrameworkComputer/dri_prime1-detection/main/yes-dgpu.png)

-------------------------------------------------------

## Steam game setup instructions for Ubuntu 22.04.3 LTS (Long Term Support)

### When to use: 

This is likely only needed for Steam. Seems there is a bug where if you launch Steam normally, it doesn't launch correctly (Ubuntu or Fedora)

**We get past this accordingly.**

- Activities, search for Steam.
- Right click, *launch with integrated graphics*.
  
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

  

