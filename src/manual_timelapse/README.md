Step 1: Run main.py

Step 2: After finishing main.py (which generates a series of JPEGs) run FFMPEG to stitch them into a timelapase:

```
ffmpeg -framerate 25 -loglevel error -i "GENERATED_DIR\%d.jpg" -vcodec mpeg2video -pix_fmt yuv420p -r 25 -y -b 10000k -f vob "OUTPUT_DIR\output.mpg"
```