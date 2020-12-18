# Codificacion_Video_S3


`ffmpeg -i bbb_480.mp4 -i bbb_480_vp8.mkv -i bbb_480_vp9.mkv -i bbb_480_hevc.mkv -filter_complex "[0:v][1:v][2:v][3:v]xstack=inputs=4:layout=0_0|w0_0|0_h0|w0_h0[v]" -map "[v]" mosaico_480.mkv`


# Referencias 
* https://trac.ffmpeg.org/wiki/Create%20a%20mosaic%20out%20of%20several%20input%20videos%20using%20xstack
