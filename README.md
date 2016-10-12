cs109-dl-videos
===============

Shell script to scrape Harvard CS109 (Intro to Data Science) lecture videos (both 2013 and 2014 videos!).

Overview
---

This is a basic shell script that downloads all the lecture/section videos associated with the CS109 (Intro to Data Science) course run in 2013 by Harvard University.

Usage
---

## 2015

`hd-2015-video-files.txt` file contains links to both presenter and presentaion
videos. They are HD and without captions. Lectures will have meaningful
filenames after download. To download:

```
cat hd-2015-video-files.txt | ./get-2015.sh
```

If you want SD/Mobile/HD-Captions videos, you need to put the links from
CS109 Data Science videos page into `hg-2015-video-pages.txt` file and
extract video links again:`

```
cat hd-2015-video-pages.txt | ./extract-2015.py > hd-video-files-2015.txt
```
For Ubuntu, I think it needs to install ChromeDriver. I followed this guide and it worked:
https://christopher.su/2015/selenium-chromedriver-ubuntu/

## 2014

```
./get.sh hq-urls.txt # for high quality versions
```

or...

```
./get.sh lq-urls.txt # for lower quality
```

This will download the videos in the same folder as the shell script as `video*.mp4`.

Requires `rtmpdump`, which can be downloaded [here](https://rtmpdump.mplayerhq.hu/). Or if you're on a Debian-based distro, just install it by running `sudo apt-get install rtmpdump`.

Credit goes to [Ketan](http://www.quora.com/Downloads/How-can-I-download-the-videos-for-CS109-Harvards-Data-Science-Course) over at Quora for the `rtmpdump` command that makes this possible.

Other materials
---

* [Lecture slides](https://drive.google.com/folderview?id=0BxYkKyLxfsNVd0xicUVDS1dIS0k&usp=sharing)
* [Homeworks and labs](https://github.com/cs109/content)
